/**
 * Signal — Cloudflare Worker API proxy
 * Paste this entire file into the Cloudflare Workers editor and click Deploy.
 * Then go to Settings > Variables > add ANTHROPIC_API_KEY (encrypted).
 *
 * This proxy enforces the model and request limits server-side, so a caller
 * who finds the Worker URL can't run arbitrary models or unbounded requests
 * on your API key.
 */

// ── Server-side policy ──
// Only these models are allowed. Reject anything else.
const ALLOWED_MODELS = [
  'claude-sonnet-4-6',
  'claude-opus-4-8',
  'claude-haiku-4-5',
]
const DEFAULT_MODEL = 'claude-sonnet-4-6'
// Hard cap on output tokens, regardless of what the client asks for.
const MAX_TOKENS_CAP = 2048

addEventListener('fetch', event => {
  event.respondWith(handleRequest(event.request))
})

async function handleRequest(request) {
  const ALLOWED_ORIGIN = '*'

  const corsHeaders = {
    'Access-Control-Allow-Origin': ALLOWED_ORIGIN,
    'Access-Control-Allow-Methods': 'POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
  }

  const json = (obj, status) =>
    new Response(JSON.stringify(obj), {
      status,
      headers: { 'Content-Type': 'application/json', ...corsHeaders },
    })

  // CORS preflight
  if (request.method === 'OPTIONS') {
    return new Response(null, { headers: corsHeaders })
  }

  if (request.method !== 'POST') {
    return json({ error: 'Method not allowed' }, 405)
  }

  let body
  try {
    body = await request.json()
  } catch (e) {
    return json({ error: 'Invalid JSON' }, 400)
  }

  // ── Validate + sanitize the request server-side ──
  if (!Array.isArray(body.messages) || body.messages.length === 0) {
    return json({ error: 'messages must be a non-empty array' }, 400)
  }

  const model = body.model || DEFAULT_MODEL
  if (!ALLOWED_MODELS.includes(model)) {
    return json(
      { error: `model not allowed. Allowed: ${ALLOWED_MODELS.join(', ')}` },
      400
    )
  }

  // Clamp max_tokens to the cap (and require a sane positive value).
  const requested = Number(body.max_tokens) || MAX_TOKENS_CAP
  const max_tokens = Math.min(Math.max(1, requested), MAX_TOKENS_CAP)

  // Build the outbound payload from a strict whitelist — drop everything else.
  const payload = { model, max_tokens, messages: body.messages }
  if (typeof body.system === 'string') {
    payload.system = body.system
  }

  // Forward to Anthropic
  const anthropicResp = await fetch('https://api.anthropic.com/v1/messages', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'x-api-key': ANTHROPIC_API_KEY,
      'anthropic-version': '2023-06-01',
    },
    body: JSON.stringify(payload),
  })

  const data = await anthropicResp.json()

  return new Response(JSON.stringify(data), {
    status: anthropicResp.status,
    headers: {
      'Content-Type': 'application/json',
      ...corsHeaders,
    },
  })
}
