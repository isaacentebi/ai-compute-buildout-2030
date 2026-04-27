# NETWORKING FABRIC — Anatomy of One AI Facility Gigawatt
*Source: networking-research subagent, 2026-04-27. Primary-source research note.*

## Headline

For a 2026-vintage frontier AI training campus on GB200/GB300 NVL72 (or comparable Trainium2/TPUv7/MI355 systems), networking fabric (NVLink + back-end fabric + front-end + inter-DC) is **13-18% of total cluster capex = $3.0-5.5M/MW** of incremental networking, **above legacy cloud's <$1M/MW** — i.e. AI clusters spend **3-6× more on networking per MW** than legacy cloud.

[SemiAnalysis CPO research](https://newsletter.semianalysis.com/p/co-packaged-optics-cpo-book-scaling): on GB300 NVL72, transceivers are **60% of networking cost and 45% of networking power**. Networking is 15% of total cluster cost — so transceivers alone are ~9% of total cluster TCO before scale-up optics.

## Sub-component decomposition ($/MW, 2026)

| Sub-component | Low | High | Primary source / anchor |
|---|---|---|---|
| NVLink/NVSwitch (intra-rack scale-up, if costed separately) | $1.0M | $1.7M | SemiAnalysis GB200 BOM; Amphenol/Fibermall |
| Back-end fabric — switches | $0.8M | $1.4M | Dell'Oro AI back-end; Broadcom T5/T6 ASP |
| Back-end fabric — optics + DACs/AOCs | $1.2M | $2.4M | SemiAnalysis CPO (60% of fabric); LightCounting |
| Back-end fabric — NICs/DPUs | $0.4M | $0.8M | NVIDIA ConnectX-7 list; AMD Pollara |
| Front-end network (storage + management) | $0.2M | $0.4M | Crehan; analyst rule-of-thumb |
| Inter-DC: ZR/ZR+ pluggables + DWDM line system | $0.1M | $0.4M | Ciena; Cignal AI |
| Inter-DC: amortized owned fiber (per MW supported) | $0.1M | $0.4M | Lumen/Zayo industry indices; Microsoft AI WAN |
| **Total networking capex / MW (2026)** | **$3.8M** | **$7.5M** | Aggregate |

Lean RoCE/UEC + 2:1 oversub + merchant optics: ~$3.0M/MW. NVIDIA-IB + 4-layer + LinkX: $7M+/MW. **Central case**: $4-6M/MW incremental above legacy cloud.

## Intra-rack: NVLink/NVSwitch

NVL72 = 72 Blackwell GPUs in a single NVLink domain over 9 NVSwitch trays (28.8 Tb/s each, 18 1.6T twin-port OSFP cages per tray). Connectivity via **5,184 copper twinax pairs** through Amphenol Paladin HD 224G blind-mate cartridges = ~2 miles of cable inside 4 vertical NVLink spine cartridges.

- Copper NVLink BOM: ~$220k per NVL72 rack ≈ $3,000/GPU
- All-optical counterfactual would cost **$2.2M/rack at NVIDIA 75% GM** vs $220k copper — copper saves ~$1.5-2M per rack inside scale-up
- Hyperscaler NVL72 all-in: **~$3.1M base / ~$3.9M loaded** with networking, storage, tax
- Vera Rubin NVL72: **$7.2-8.8M/rack**

NVLink fabric (switches + spine + DensiLink): **$300-500k per NVL72 rack = ~10-15% of rack BOM = $2,500-4,000 per GB200 GPU**.

## Back-end fabric: the IB → Ethernet transition

[Dell'Oro Sep 2025](https://www.delloro.com/news/ai-back-end-networks-continue-their-shift-to-ethernet-now-accounting-for-over-two-thirds-of-3q-2025-switch-sales-in-ai-clusters/): **Ethernet surpassed InfiniBand in 2025**, accounting for **>two-thirds of AI back-end switch sales by 3Q25** and "more than doubling" InfiniBand for the full year. [>$100B cumulative AI back-end switch sales 2025-2029](https://www.delloro.com/news/data-center-switch-sales-in-ai-back-end-networks-to-exceed-100-b-over-the-next-five-years/).

650 Group: AI networking TAM ~$20B in 2025, >$50B by 2026, AI scale-out Ethernet >$100B by 2030.

NVIDIA networking ran ~$11B annualized late FY25; **Spectrum-X alone exceeded $10B annualized** by 2Q FY26. InfiniBand revenue "nearly doubled" sequentially on XDR adoption.

**UEC 1.0 closes the protocol gap** (released June 11, 2025; 562-page spec). AMD/Pensando shipped first UEC-compliant 400GbE NIC (Pollara) into OCI. Founding members: AMD, Broadcom, Cisco, Arista, Meta, Microsoft, Intel — everyone except NVIDIA.

## Optics — the dominant fabric line item

- **Transceivers = 60% of networking cost** (SemiAnalysis CPO)
- 800G transceiver TAM: ~$14B (2025) → $24B (2029)
- CPO (Broadcom Bailly 51.2T): 5.4W/port vs ~15W discrete = 65% power savings; saves ~31% networking cost / 86% transceiver cost / ~3% total cluster cost when deployed
- Switch silicon: Broadcom Tomahawk 5 (51.2T, 64×800G) at ~$70-120k per pizza-box switch

## Inter-DC fabric — now real

Three reference deployments establish that frontier training has crossed single-site:

1. **Microsoft Fairwater Wisconsin ↔ Atlanta** (Oct/Nov 2025): **120,000 miles of dedicated fiber**, custom Multi-Path Reliable Connected (MRC) protocol co-developed with NVIDIA + OpenAI. ([Microsoft Source](https://news.microsoft.com/source/features/ai/from-wisconsin-to-atlanta-microsoft-connects-datacenters-to-build-its-first-ai-superfactory/))

2. **AWS Project Rainier (Indiana) for Anthropic**: $11B, ~500k Trainium2 chips, 2.2 GW. Multi-site, scaled-out via EFA over 10p10u fabric (10 PB capacity, <10 µs latency) and SIDR routing protocol.

3. **Google Jupiter / Apollo OCS**: deployed across all TPUv4/v5/v6. Google: 30% capex reduction, 41% power reduction, 5× speed, 50× downtime reduction vs pre-OCS Jupiter.

400G ZR/ZR+ pluggables: ~$8-15k/unit (third-party clones), 2-3× higher OEM. 800G ZR/ZR+ launched 2024-25: ~$20-35k/unit OEM. Cignal AI: 800ZR market crosses $1B in 2026.

## Vendor concentration

- **Switch silicon (back-end Ethernet)**: Broadcom T5/T6/Ultra dominant; Cisco Silicon One G200 second; Marvell/NVIDIA Spectrum tertiary
- **Switch systems**: Arista (7800R4), Celestica, Accton, Cisco, H3C/Huawei (China)
- **InfiniBand**: NVIDIA-only
- **NICs/DPUs**: NVIDIA ConnectX-7/8 + BlueField-3/4 dominant; AMD Pensando Pollara (UEC) and Intel IPU second-source
- **NVLink scale-up**: NVIDIA-only. Connectors: Amphenol lead, Molex/TE secondary
- **Coherent optics**: Ciena, Marvell, Coherent Corp, Lumentum, Acacia (Cisco), Nokia/Infinera

Net: BOM compression as Ethernet wins. SemiAnalysis estimates merchant Ethernet fabric is **20-35% cheaper than NVIDIA-IB** at the fabric-cost line.
