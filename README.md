# Signal v0.0.1

**Paste the mess --> get the read.**  
AI-powered account intelligence for CS teams.

---

## Architecture

```
Browser (index.html on GitHub Pages)
    ↓ POST request (account data + prompt)
Cloudflare Worker (worker.js)
    ↓ forwards with API key in header
Anthropic API
    ↓ returns analysis JSON
Cloudflare Worker
    ↓ strips headers, adds CORS
Browser renders brief + chat
```

The API key never touches the browser. 

---

## What's in v0.0.1

- Portfolio view — 4 demo accounts + add your own
- File upload — .txt, .csv, .vtt, .srt, .md, .json, .html, .log, .tsv
- Paste input — raw text, Teams chat, MBR notes, etc.
- Auto content-type detection (transcript, MBR/QBR, CSV, chat log, email, SWOT)
- AI synthesis — situation read, contact persona, ranked leverage points, "do this today"
- Chat interface — interrogate Signal about this specific account
- Privacy — nothing stored, session only, cleared on close

---

## What's next (v0.1+)

- [ ] Longitudinal memory — compare this call to the last one
- [ ] Feedback loop — "here's what happened after you suggested that"
- [ ] Multi-contact persona — different reads for champion vs economic buyer
- [ ] Revenue trend visualization from CSV input
- [ ] Export brief as PDF / shareable link
