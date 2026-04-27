# ACCELERATOR + SERVER BOM — Anatomy of One AI Facility Gigawatt
*Source: accelerator-bom-research subagent, 2026-04-27. Primary-source research note.*

## Headline (CRITICAL FINDING)

The paper's **$13-17B/GW** accelerator capex is **too tight for 2026**. It fits 2024 H100 vintage cleanly, or 2026 if restricted to "GPU silicon only."

**Defensible 2026 ranges**:
- Accelerator silicon (chip + HBM only, no Grace/NVSwitch): **$13-18M/MW**
- Rack-complete server BOM (in-rack only): **$16-23M/MW** ($19.5M central)
- **Total IT BOM at the customer (incl. networking + storage outside rack): $19-28B/GW** ($23.5B/GW central)

For comparison, **Bernstein's headline $35B/GW total facility capex** = ~$23-24B IT + ~$10-12B mech/elec/civil/land. The paper's $1.2-1.5T / 51.4 GW ≈ $23-30B/GW total — sits in the lower-middle of Bernstein's range.

**Recommendation**: either restate the $13-17B/GW assumption to specify "chip-silicon only," or widen to **$15-22B/GW** to cover both definitional bookends.

## Chips per facility-MW falls with each generation

This is the single biggest counterintuitive finding for the section: **chips per MW *decreases* with each generation as power per chip rises faster than performance per watt**.

| Vintage | Platform | Chips/facility-MW (PUE 1.15, +10% net/storage) |
|---|---|---|
| 2024 | HGX H100 (8-GPU air-cooled) | ~570 H100/MW |
| 2025 | HGX B200 8-GPU air-cooled | ~470-530 B200/MW |
| 2025-26 | GB200 NVL72 (liquid) | **~430-460 B200/MW** |
| 2026 | GB300 NVL72 | ~400-430 B300/MW |
| 2H'2026 | Vera Rubin NVL144 | ~800-900 Rubin dies/MW |
| 2027 | Rubin Ultra NVL576 (Kyber, 600kW racks) | ~650-750 Rubin Ultra dies/MW |

(SemiAnalysis 100k H100 cluster benchmark: 20,480 GPUs in 28.4 MW = 1,389 W/GPU system-allocated = ~720 H100/MW critical IT, ~600/facility-MW. Reconciles.)

## H100e per facility-MW (the right scaling unit)

| Chip | Peak FP8 (H100=1.0) |
|---|---|
| H100/H200 | 1.0 (3,958 TFLOPS sparse FP8) |
| B200 | ~2.5× |
| GB200 (per B200 die) | ~2.5× |
| B300 / GB300 | ~3.75× |
| Rubin (R200) | ~7.5-8× |
| Rubin Ultra | ~10-12× |
| AMD MI300X | ~0.8× |
| AMD MI355X | ~2.5× |
| AMD MI400 | ~5-6× |
| TPU v5p / Ironwood (v7p) | ~0.45× / ~1.2× |
| Trainium 2 / 3 | ~0.3× / ~0.65× |
| Maia 200 | ~1.3× |

**H100e per facility-MW by vintage**:

| Vintage | Dominant platform | Chips/MW | H100e/chip | **H100e per facility-MW** |
|---|---|---|---|---|
| 2024 | HGX H100 | ~570 | 1.0 | **~0.57M** ✓ matches Epoch |
| 2026 base | GB200 NVL72 | ~440 | 2.5 | **~1.10M** |
| 2026 stretch | GB300 NVL72 | ~415 | 3.75 | **~1.55M** |
| 2H'2026-2027 | Vera Rubin NVL144 (theoretical pure) | ~850 | 7.5 | ~6.4M (theoretical) |
| 2028 realistic deployed mix | Rubin/Rubin-Ultra blend on Blackwell-Ultra installed base | 700-800 | 8-10 | **~1.5-2.5M** (installed-base weighted) |

The paper's 0.5M / 1.0-1.3M / 1.5-2.0M is **consistent with this** if 2028 is treated as installed-base-weighted (which it should be).

## Accelerator unit cost (volume / hyperscaler-negotiated, 2024-2026)

| Accelerator | Vintage | Volume $/chip | Power |
|---|---|---|---|
| NVIDIA H100 SXM | 2023-24 | $25-30k vol; $27-40k street | 700 W |
| NVIDIA H200 SXM | 2024 | $30-40k | 700 W |
| NVIDIA B200 (HGX) | 2025 | $30-40k chip; ~$500k 8-GPU server | 1000-1200 W |
| NVIDIA GB200 superchip | 2025 | ~$60-70k per superchip; **NVL72 rack ~$3.0-3.4M** | 2,700 W |
| NVIDIA GB300 (Blackwell Ultra) | 2H'25-2026 | NVL72 rack ~$3.7-4.0M; inference variant up to ~$6M | 1,400 W/GPU; rack 120 kW |
| NVIDIA Vera Rubin (R200, NVL144) | 2H'2026 | NVL72/144 rack **~$8.8M** (sell-side) | rack 120-130 kW |
| NVIDIA Rubin Ultra (Kyber, NVL576) | 2H'2027 | TBD; analysts $15-20M+ | **600 kW per rack** |
| AMD MI300X | 2024 | ~$10k to Microsoft, $15k street | 750 W |
| AMD MI325X | Q3'2025 | est $15-18k (256GB HBM3e) | ~1,000 W |
| AMD MI355X (CDNA4) | 2H'2025 | est $20-25k (288GB HBM3e) | 1,400 W liquid |
| AMD MI400 | 2026 | est $25-35k (432GB HBM4) | ~1,500-1,600 W |
| Google TPU v5p | 2024 | est ~$8-10k all-in | ~700 W |
| Google Trillium (v6e) | 2024 | est $5-8k (inference) | ~300-500 W |
| Google Ironwood (v7p) | 2025-26 | est $10-15k (192GB HBM3e, 4.6 PF FP8) | ~600-700 W |
| AWS Trainium 2 | 2024-25 | est $6-10k | ~500-650 W |
| AWS Trainium 3 | Dec 2025 | est $10-15k (3nm, 2.52 PF FP8, 144GB HBM3e) | ~750 W |
| Microsoft Maia 100 | 2024 | est ~$5-7k | ~700 W |
| Microsoft Maia 200 | 2026 | est ~$10-14k (3nm, 216GB HBM3e) | 750 W |
| Meta MTIA v2 | 2024 | est ~$2-4k (5nm, inference) | 90 W |
| Meta MTIA v3 ("Iris") + v4 ("Santa Barbara") | 2025-26 | est $6-12k (Broadcom co-design) | up to 180 kW/rack |

## Per-rack BOM splits (Bernstein/SemiAnalysis)

GB200 NVL72 ($5.9M Bernstein per-rack BOM with infra allocation):
- Compute: 57%
- Infra: 43%
- Networking ~13% of total facility
- Mech/elec ~30%
- Storage ~1-1.5%

HGX H100 server (~$190k vol):
- 8× H100 SXM modules: ~70-75% (~$140-150k)
- SXM baseboard + NVSwitch: ~5%
- 2× host CPU: ~3-4%
- Host DRAM (1-2 TB DDR5): ~3%
- 8× ConnectX-7/BlueField-3: ~3-4%
- Local NVMe (~30TB): ~1%
- PSU/fans/chassis/BMC: ~3%

GB200 NVL72 (~$3.1M rack BOM): non-accelerator silicon ≈ **30-35% of rack cost** (Grace ~$108k, NVLink Switch trays ~$500k, ConnectX-8/BlueField ~$300k, rest cooling/copper/mech).

## Hyperscaler refresh cycles (10-K disclosures, primary)

- **Microsoft (FY23 10-K, Q4'22 call)**: server life 4→6 years, ~$3.7B FY23 P&L benefit. Post-2024: re-shortened a *subset* of GPU servers back toward 4 years.
- **Meta (FY24 10-K / Q4'24 earnings, Jan 2025)**: extended useful life of certain servers/networking 4-5→5.5 years, ~$2.9B FY25 depreciation reduction.
- **Amazon (Q4'23 10-K, Feb 2024)**: extended servers 5→6 years, ~$900M Q1'24 net-income benefit. **(Q4'24 10-K, Feb 2025)**: partial reversal — "a subset of servers and networking equipment" reverted **6→5 years effective Jan 1 2025** due to "increased pace of technology development, particularly in AI/ML"; ~$700M FY25 hit.
- **Google/Alphabet (FY23 10-K)**: extended servers 4→6 years.
- **Oracle**: continues 4-5 year server life.

**Takeaway**: accounting useful lives stretched to 5.5-6 years just as the *economic* obsolescence cycle for frontier AI accelerators compressed to 2-3 years (H100→B200 in 18 mo, B200→B300 in 9-12 mo, B300→Rubin in another 12 mo). **A 4-year effective AI accelerator refresh cycle is the right modelling assumption**, with Amazon's 2025 reversal as primary-source evidence.

## Custom-silicon offset

The Maia 200, Trainium 3, Ironwood, and MI355X/MI400 ramps materially reduce blended $/H100e for hyperscalers operating their own fleets (Google, AWS, Meta), perhaps **25-40% on like-for-like H100e basis**. This is the strongest reason the paper's $13-17B/GW band can survive: a hyperscaler-mix buildout with 40-50% custom silicon gets there.

## Bottom line for the paper

1. **Use $19-22B/GW as central 2026-vintage all-NVIDIA accelerator + server BOM.** $13-17B/GW too tight for 2026; restate as chip-silicon-only or widen to $15-22B/GW.
2. **Chips per facility-MW decreases with each generation** (570 H100 → 440 GB200 → 415 GB300 → 850 Rubin) — counterintuitive but power per chip rises faster than performance per watt.
3. **H100e per facility-MW**: 0.57M (2024) → 1.1M GB200 / 1.55M GB300 (2026) → 1.5-2.5M (2028 realistic deployed) → 6M+ pure-Rubin ceiling (unlikely before 2029). Paper consistent.
4. **4-year AI refresh cycle** best supported by Amazon Q4'24 10-K reversal.
5. **Custom-silicon mix** (40-50% non-NVIDIA) is what would let the paper's $13-17B/GW survive intact.
