"""All prompt templates in one place, easy to iterate.

The analysis contract (risk taxonomy, persona fields, section names) lives in
constants here and in schema.py so the prompt text, the JSON schema sent for
native structured outputs, and the eval scorer can never drift apart.

Note: ANALYZE_PROMPT uses doubled braces ({{ }}) for the literal JSON so that
str.format() leaves them intact.
"""

# ── Contract constants ──
# The eleven-type risk taxonomy, plus Healthy and Unknown. Order matters only
# for display; the scorer matches by exact string.
RISK_TYPES = [
    "Champion loss",
    "Silent decay",
    "Power user concentration",
    "Frustrated not gone",
    "Stalled expansion",
    "Adoption failure",
    "Sentiment mismatch",
    "Relationship gap",
    "Reduced footprint",
    "Vibe risk",
    "Healthy",
    "Unknown",
]
SEVERITIES = ["high", "medium", "low", "unknown"]
CONFIDENCES = ["high", "medium", "low"]
PERSONA_FIELDS = [
    "primary_contact",
    "comm_style",
    "decision_style",
    "what_they_say_vs_mean",
    "approach_recommendation",
]
SECTIONS = ["situation", "contact_read", "where_to_press", "do_this_today"]

# Analysis focus modes, mirrored from the browser app. `full` fills every
# section; the other three trim what the model has to write.
FOCUS_INSTRUCTIONS = {
    "full": "FULL BRIEF: fill every section.",
    "revenue": (
        "REVENUE RISK SCAN: fill situation, leverage_points (Priority 1 ONLY — "
        "return a single-item array), and do_this_today. Leave contact_persona "
        "fields and secondary_contacts as empty strings and an empty array."
    ),
    "relationship": (
        "RELATIONSHIP READ: fill contact_persona deeply and include up to 3 "
        "secondary_contacts (each note covering comm style, decision style, "
        "says-vs-means). Keep situation to one sentence and leverage_points to "
        "one relationship-focused item."
    ),
    "precall": (
        "PRE-CALL PREP: expand do_this_today into 3-4 specific action items (use "
        "\\n between them) with exact suggested language where relevant, and "
        "return one leverage point. Keep situation to two sentences."
    ),
}
# Output budgets per mode, mirrored from the browser app. The full brief
# with section_sources, secondary_contacts, and data_gaps runs 2,000-3,000
# tokens of JSON; 1,500 truncates it mid-object on every account.
FOCUS_MAX_TOKENS = {"full": 4000, "revenue": 2200, "relationship": 2600, "precall": 2000}

# ── Prompt 1: per-doc summarization ──
SUMMARIZE_PROMPT = """You are analyzing one document from a customer account file.
Extract only what matters for account health assessment:
- Key signals (positive or negative sentiment shifts)
- Anything the customer said about value, risk, competitors, budget, or renewal
- Action items or commitments made
- Tone/relationship signals (enthusiasm, frustration, disengagement)
- Any red flags or green flags

Document type: {doc_type}
Document name: {doc_name}

Return a tight 3-5 sentence summary. No filler. Signal over noise.

DOCUMENT:
{content}
"""

# ── Prompt 2: main analysis (JSON output) ──
# The source-weighting block is the part the ablation removes. Everything else
# in the prompt is identical between arms.
SOURCE_WEIGHTING = """SOURCE WEIGHTING:
Treat all-hands decks, kick-off/annual review decks, MBR/QBR notes, and CRM notes as PRIMARY sources: they record what the customer committed to and what leadership said. Treat Slack/Teams chat logs, transcripts, and internal notes as SECONDARY: useful for tone and day-to-day texture, but they over-represent whoever talks the most. When a primary and a secondary source disagree, say so and weight the primary.

CONTACT READ:
Identify the PRIMARY CONTACT as the most senior stakeholder who has budget authority or vendor decision-making power — NOT the person most frequently mentioned in chat logs. Look for titles like Director, Senior Director, VP, Head of, or Chief. An admin or day-to-day user who appears constantly is a secondary contact, however engaged they are.
"""

ANALYZE_PROMPT = """You are Signal, an expert CS strategist. Analyze this account and return ONLY valid JSON.
No markdown, no backticks, nothing outside the JSON object.

The data may include all-hands decks, kick-off decks, MBR/QBR notes, CSV/CRM exports, Slack/Teams chat logs, SWOT docs, internal notes, transcripts, or email threads, or any mix. Read everything holistically and name the pattern, not just the metrics.

{weighting}SOURCE ATTRIBUTION (required): populate "section_sources" with the document types that actually contributed to each section, using the type labels shown in brackets in the summaries.

FOCUS: {focus}

ACCOUNT: {account_name}
CONTACTS: {contacts}
RENEWAL: {renewal_days} days
ARR: {arr}

DOCUMENT SUMMARIES:
{summaries}

Return exactly this JSON (respect the FOCUS instruction):
{{
  "situation": "2-4 sentences: what is actually happening across ALL sources",
  "risk_type": "one of: {risk_types}",
  "risk_severity": "high | medium | low | unknown",
  "data_sources_detected": ["list each content type you found and used"],
  "leverage_points": [
    {{"rank": 1, "what": "specific action grounded in this account's data", "why": "reason from the actual signals", "timeline": "this week"}},
    {{"rank": 2, "what": "specific action", "why": "reason", "timeline": "this month"}},
    {{"rank": 3, "what": "specific action", "why": "reason", "timeline": "this quarter"}}
  ],
  "do_this_today": "one concrete 24-hour action — specific, not generic",
  "contact_persona": {{
    "primary_contact": "Name and title, or Unknown",
    "comm_style": "evidence-based read on how they communicate",
    "decision_style": "how they make decisions",
    "what_they_say_vs_mean": "surface vs subtext read",
    "approach_recommendation": "exactly how to engage given the current situation"
  }},
  "secondary_contacts": [
    {{"name_title": "name and title", "note": "their role and why they are secondary"}}
  ],
  "section_sources": {{
    "situation": ["doc types that informed this section"],
    "contact_read": ["doc types"],
    "where_to_press": ["doc types"],
    "do_this_today": ["doc types"]
  }},
  "data_gaps": ["specific information that would sharpen the read", "gap 2"],
  "confidence": "high | medium | low",
  "confidence_note": "what data would sharpen this read",
  "suggested_questions": ["follow-up question 1", "question 2", "question 3"]
}}
"""

# ── Prompt 3: chat follow-up (system prompt) ──
CHAT_SYSTEM_PROMPT = """You are Signal, an expert CS strategist. You have full context on this account.
Answer questions directly and specifically — never generically.
If the user gives you new information, revise your read explicitly and say what changed.

ACCOUNT BRIEF:
{brief_json}

SOURCE SUMMARIES:
{summaries}
"""
