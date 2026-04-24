# AI Compute Commitment Surface — Rundown

**Data cutoff:** Epoch AI 2026-04-16  |  Overlay closed 2026-04-22
**Scope:** Western AI program (primary) + Sovereign-AI sidebar (UAE, Saudi, India, UK)

---

## 1. Headline — what each layer contributes

| Layer | Operational today (2026-Q2) | Full buildout (2027-2030) |
|---|---:|---:|
| Epoch evidenced floor | 6.67 GW | 33.05 GW |
| Our Class A overlay (Western) | — | +8.17 GW  [3.30, 11.04] |
| Our neocloud ex-Epoch overlay | +1.49 GW | +9.39 GW |
| **Western total** | **8.16 GW** | **50.61 GW  [45.74, 53.48]** |
| Sovereign-AI sidebar | — | +1.95 GW  [0.72, 4.40] |
| Global reference | 8.16 GW | 52.56 GW  [46.46, 57.88] |

Epoch captures **65% of the Western horizon on its own** (33.05 / 50.61). Our overlay adds the remaining 35% — 17.56 GW — split between announced-but-unphotographed Class A commitments (8.17 GW) and neocloud fleets Epoch barely touches (9.39 GW).

---

## 2. The dedup audit — headline vs. incremental per commitment

This is where the "we avoided double-counting" claim actually lives. **Announced** = what the press release says. **Incremental** = what we added after subtracting Epoch's existing coverage.

### Western commitments

| # | Commitment | Announced | Epoch already had | We add (point) | Range |
|---|---|---:|---:|---:|---|
| 1 | Anthropic–AWS (Apr 20, 2026) | 5.00 GW | 1.83 GW | **3.17 GW** | [2.50, 5.00] |
| 2 | Anthropic–Fluidstack (Nov 2025) | — | 0.44 GW | 0 | — |
| 3 | Anthropic–Azure (Nov 18, 2025) | 1.00 GW | 0.00 GW | **1.00 GW** | [0.00, 1.00] |
| 4 | **OpenAI Stargate (8 sites, $500B)** | **10.00 GW** | **10.63 GW** | **0** | [0.00, 0.00] |
| 5 | OpenAI–Microsoft Fairwater | — | 4.45 GW | 0.70 GW | [0.40, 1.50] |
| 6 | Meta Hyperion + Prometheus | 6.00 GW | 3.61 GW | **2.74 GW** | [0.00, 2.74] |
| 7 | Meta–Nebius $27B (Class C) | — | 0.00 | — | — |
| 8 | xAI–HUMAIN Saudi | 0.50 GW | 0.00 GW | 0.50 GW | [0.40, 0.60] |
| 9 | xAI Colossus 2 (full target) | 2.00 GW | 1.94 GW | 0.06 GW | [0.00, 0.20] |
|   | **Western Class A subtotal** |   |   | **8.17 GW** | **[3.30, 11.04]** |

### Sovereign-AI (sidebar — NOT in Western denominator)

| # | Commitment | Announced | Epoch had | We add | Range |
|---|---|---:|---:|---:|---|
| 10 | Microsoft–G42 UAE (Khazna) | 0.20 GW | 0 | 0.20 GW | [0.20, 0.20] |
| 11 | HUMAIN–AMD Saudi | 0.50 GW | 0 | 0.50 GW | [0.30, 0.70] |
| 12 | Reliance Jio Jamnagar | 1.00 GW | 0 | 1.00 GW | [0.12, 3.00] |
| 13 | UK Culham AI Growth Zone | 0.50 GW | 0 | 0.25 GW | [0.10, 0.50] |
|   | **Sovereign subtotal** |   |   | **1.95 GW** | **[0.72, 4.40]** |

---

## 3. The big cancellations — where headline ≠ reality

Three rows where the headline number shrinks the most under dedup:

| Commitment | Press release | Reality after dedup | Why |
|---|---|---|---|
| OpenAI Stargate ($500B / 10 GW) | 10.00 GW | **0** | All 8 sites already in Epoch at aggregate 10.63 GW. Announcement describes sites Epoch has photographed. |
| Anthropic–AWS 5 GW "new" | 5.00 GW | 3.17 GW | Epoch had 1.83 GW at Madison + Ridgeland + New Carlisle. Only ~3 GW is genuinely net-new site capacity. |
| Meta Hyperion 6 GW | 6.00 GW | 2.74 GW (stretch) / 0 (floor) | Meta's own newsroom says "over 2 GW" — matches Epoch. Zuckerberg's 5 GW earnings-call figure is a stretch target. |

**If we had summed announcements naively, we'd have reported 34.2 GW of Class A incremental. Actual incremental after dedup: 8.17 GW. The overlay kills 76% of the headline noise.**

---

## 4. Parallel surfaces — do NOT add to physical GW

| Class | What it is | Size | Why it's excluded |
|---|---|---|---|
| B — chip procurement | AMD 6 GW + Broadcom 10 GW + NVIDIA 10 GW commitments | 26 GW / $138B | Chips deploy INTO the Class A shells above. Adding would triple-count. |
| C — dollar-only | Altman's $1.4T aggregate remark, Alphabet UK £5B + Germany €5.5B, MSFT UK £2.5B, Groq Saudi $1.5B | $1,417B | Envelopes that overlap Class A capex. Not a physical commitment. |

---

## 5. Horizon distribution — when does Epoch's 33 GW actually land?

| Year of full buildout | Sites | MW | Share |
|---|---:|---:|---:|
| 2025 | 1 | 263 | 0.8% |
| 2026 | 14 | 9,776 | 29.6% |
| 2027 | 8 | 9,114 | 27.6% |
| 2028 | 9 | 12,829 | 38.8% |
| 2029 | 1 | 800 | 2.4% |
| 2030 | 1 | 267 | 0.8% |

**Only 30% of Epoch's "buildout" number lands in 2026.** The 38.8% that lands in 2028 is where the "will they actually build it" risk concentrates.

---

## 6. The framing number that matters most

```
Operational today:       8.16 GW
Western horizon target: 50.61 GW
─────────────────────────────────
Gap (not yet built):    42.45 GW    (83.9% of target)
Built:                   8.16 GW    (16.1% of target)
```

**84% of the Western capex-revenue story lives in capacity that doesn't exist yet.** The entire flywheel / coverage-ratio thesis rides on whether this 2028-2030 pipeline materializes on announced timelines. That's the number to put a falsification date on.

---

## 7. Wider-canvas exclusions — what we explicitly did NOT add

We canvassed these and documented each rejection with a primary-source check:

| Candidate | Why excluded |
|---|---|
| Apple Private Cloud Compute | No MW disclosure |
| Oracle ex-Stargate | No named sites outside Stargate envelope |
| Tesla Cortex | No primary MW disclosure (Musk tweet figures only) |
| Cohere / DeepMind | No owned sites (compute purchased from hyperscalers) |
| Digital Realty / Equinix merchant | Structural double-count risk — shells for already-counted hyperscalers |
| EuroHPC 6 new AI Factories | No MW-per-site disclosed yet |
| Mistral Bruyères-le-Châtel | Below 100 MW Class A threshold |

Seven exclusions, each logged in `compute_commitments_overlay.yaml#excluded_with_reason` with the primary source we checked and the reason.

---

## 8. Methodology in one paragraph

Epoch AI's Frontier Data Centers dataset is the evidenced floor — ~200 sites worldwide identified via satellite imagery, permit filings, and public disclosures, each tagged #confident, #likely, or #speculative by Epoch. We treat this as ground truth for physical capacity.

On top of this we layer **announced commitments** that Epoch either hasn't captured yet or has captured only partially. Every commitment row records (a) the verbatim announcement language, (b) which Epoch sites overlap and why, (c) the incremental GW after subtraction, (d) a low/high range reflecting interpretation uncertainty, and (e) the primary sources.

Commitments are classified:
- **Class A** — physical capacity at named (or named-program) sites. Contributes to the physical GW surface.
- **Class B** — chip procurement (AMD MI-series, Broadcom ASIC, NVIDIA GB200 LOIs). Does NOT contribute — chips deploy into Class A shells.
- **Class C** — dollar/equity commitments without site or GW disclosure. Tracked for financial reconciliation only.

Neocloud fleets (CoreWeave, Nebius, Nscale, Crusoe, Lambda, Applied Digital, Fluidstack, Voltage Park, Together, Fermi) are tracked in `neocloud_overlay.yaml` with per-operator dedup against Epoch.

**Sovereign-AI** (UAE, Saudi, India, UK) is reported as a sidebar — not combined with the Western total — because the capex-revenue denominator in our Western AI program analysis should not be diluted by state-backed programs with different funding and timeline dynamics.
