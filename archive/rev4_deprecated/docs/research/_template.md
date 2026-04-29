# Research Dispatch Template

Use this shape for every Rev-4.2 contract research return. Researchers find evidence and flag overlap candidates; they do not adjudicate final tiers or headline dedupe.

```yaml
counterparty: <name>
contract_overview:
  type: take-or-pay | option | ground lease | colo | JV | cloud capacity | chip procurement | unknown
  term_years: <number or null>
  announced_capex_usd_b: <number or null>
  delivery_window: {earliest: <YYYY-MM-DD or null>, central: <YYYY-MM-DD or null>, latest: <YYYY-MM-DD or null>}
  exclusivity_or_optionality: <text>
atoms:
  - id: atom:<stable_id>
    site: <name + location, or "unspecified">
    operator: <name>
    user_or_anchor: <name>
    gw_facility: <number or [low, central, high]>
    gw_it: <number or null>
    basis: facility_MW | IT_MW | ambiguous_compute
    pue_assumed: <number or null>
    energization_window: {earliest: <YYYY-MM-DD or null>, central: <YYYY-MM-DD or null>, latest: <YYYY-MM-DD or null>}
    operational_status: T1 | T2 | T3 | T4 | T5 | T6 | unknown
    exact_quote: "<short verbatim quote supporting size/status/timing>"
    source_url: <url>
    source_publisher: <name>
    source_publication_date: <YYYY-MM-DD>
    accessed_date: <YYYY-MM-DD>
    epoch_site_overlap_candidates:
      - epoch_site: <name>
        epoch_attributed_to: <hyperscaler>
        overlap_gw_facility: <number or null>
        overlap_evidence: <quote or rationale>
    risks:
      counterparty: <text>
      regulatory: <text>
      power_interconnect: <text>
      supply_chain: <text>
      technology: <text>
      financing: <text>
      structural_optionality: <text>
contradictions:
  - <source X says A; source Y says B>
gaps:
  - <what would resolve the open question>
```

## Source Discipline

- Prefer primary sources: SEC filings, company releases, utility filings, planning documents, government records, investor presentations, and contracts.
- Use credible secondary sources only when primary evidence is unavailable; label them as secondary.
- Keep quotes short and load-bearing.
- Every capacity number needs basis, date, publisher, URL, and uncertainty notes.
- Every possible Epoch overlap gets listed as a candidate, not silently resolved.
