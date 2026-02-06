# ActualPrice — Gemini 3 Multi-Agent Demo Suite

**Live Demo:** [ssp-staging.vercel.app/demo](https://ssp-staging.vercel.app/demo)

## What It Does

ActualPrice is an AI-powered dynamic pricing engine for e-commerce. This demo showcases four multi-agent pipelines — each orchestrating three specialized Gemini 3 agents that stream their reasoning in real time.

## Gemini 3 Features Used

- **Gemini 3 Flash (`gemini-3-flash-preview`)** — powers all four agent pipelines with fast streaming
- **Native Thinking Levels** — configurable reasoning depth (`minimal` / `low` / `high`) via `ThinkingConfig`, letting agents trade speed for deeper analysis
- **Thought Signatures** — extracts native `part.thought` flags from Gemini 3 responses, displayed as real-time "agent thinking" in the UI
- **Multimodal Vision** — Visual Pricing and Launch Detector accept product screenshots for Gemini image analysis
- **1M Token Context** — Crisis Detector feeds comprehensive sentiment history for full-context analysis

## The Four Demos

| Demo | Agents | What It Does |
|------|--------|-------------|
| **Visual Pricing Intelligence** | Scout → Analyst → Strategist | Upload a product screenshot → get AI pricing recommendations |
| **Crisis Detector** | Monitor → Analyzer → Response | Paste brand mentions → detect PR crises in real time |
| **Launch Detector** | Scanner → Validator → Assessor | Feed competitor signals → detect product launches + threat level |
| **Market Trends** | Collector → Analyzer → Forecaster | Enter a product category → get trend analysis + price forecasts |

## Architecture
```
User Input (text / image)
    │
    ▼
┌─────────────────────────────────────────┐
│         SSE Streaming Endpoint          │
│         (FastAPI + EventSource)         │
└─────────┬───────────────────────────────┘
          │
          ▼
┌─────────────────────────────────────────┐
│  Agent 1: Observe & Scan                │
│  ├─ Gemini 3 Flash (thinking: low)      │
│  ├─ Multimodal input (text + vision)    │
│  └─ Streams thoughts → SSE → UI        │
│                                         │
│  Agent 2: Validate & Analyze            │
│  ├─ Receives Agent 1 output             │
│  ├─ Gemini 3 Flash (thinking: low)      │
│  └─ Extracts structured data (JSON)     │
│                                         │
│  Agent 3: Decide & Recommend            │
│  ├─ Receives Agent 1 + 2 output         │
│  ├─ Gemini 3 Flash (thinking: low)      │
│  └─ Final recommendation + confidence   │
└─────────────────────────────────────────┘
          │
          ▼
┌─────────────────────────────────────────┐
│  Frontend (Next.js + TypeScript)        │
│  ├─ Real-time agent thought display     │
│  ├─ Pulsing status indicators           │
│  └─ Structured result cards             │
└─────────────────────────────────────────┘
```

## Code Structure
```
├── backend/services/ai_trend_analysis/
│   ├── ai_clients.py            # Gemini 3 client — streaming, thinking levels, thought extraction
│   ├── visual_analyzer.py       # Visual Pricing: Scout → Analyst → Strategist
│   ├── crisis_detector.py       # Crisis Detector: Monitor → Analyzer → Response
│   ├── launch_detector.py       # Launch Detector: Scanner → Validator → Assessor
│   └── market_trends_visual.py  # Market Trends: Collector → Analyzer → Forecaster
│
├── frontend/app/demo/
│   ├── visual-pricing/          # Screenshot upload + agent stream + pricing card
│   ├── crisis-detector/         # Brand monitoring + severity assessment
│   ├── launch-detector/         # Competitor signal analysis + threat level
│   └── market-trends/           # Category trends + price forecasting
```

## Third-Party Integrations

- **Google Gemini 3 API** (`google-genai` Python SDK) — core AI engine
- **Next.js 14** — frontend framework
- **FastAPI** — backend API + SSE streaming
- **Tailwind CSS** — styling

## Links

- **Live Demo:** [ssp-staging.vercel.app/demo](https://ssp-staging.vercel.app/demo)
- **Full Platform:** [getactualprice.com](https://getactualprice.com)
- **Video:** [YouTube link TBD]

Built for the [Google DeepMind Gemini 3 Hackathon](https://gemini3.devpost.com/) — February 2026
