# How do I stress-test my crypto portfolio against a crash?

Anny's `simulate_scenario` tool applies a hypothetical market move to your live portfolio and shows
the damage before it happens. Describe a scenario in plain English ("BTC drops 40%") or pass a
structured array of per-asset shocks (BTC -30%, ETH -40%), and Anny returns your portfolio value
before and after, the total change in USDT and percent, a per-asset breakdown, and which position
takes the biggest hit. It uses your actual connected positions, so the answer reflects your real
exposure and concentration — not a generic model. Run it before adding risk, or whenever the market
looks shaky, to see where you're most fragile.

## Live Tools

- `simulate_scenario` — portfolio stress test against a scenario string or structured asset array

## Planned Tools (Roadmap)

The following tools are in development and not yet available:

- Position sizing calculator
- Kelly criterion / fixed-fractional sizing
- Correlation-weighted rebalancing

## Auth Required

Yes — requires a connected portfolio with active positions.

## Examples

| File | What It Demonstrates |
|------|---------------------|
| [portfolio-scenario-crash.md](portfolio-scenario-crash.md) | BTC -40% stress test |
| [multi-asset-stress-test.md](multi-asset-stress-test.md) | Structured assets array: BTC -30%, ETH -40% |
| [position-sizing-concepts.md](position-sizing-concepts.md) | Educational placeholder for planned sizing tools |

## See Also

- [../02-market-intelligence/README.md](../02-market-intelligence/) — read the conditions you're stress-testing against
- [../03-portfolio-management/README.md](../03-portfolio-management/) — adjust positions after a stress test
- [../09-multi-turn-workflows/README.md](../09-multi-turn-workflows/) — fold a stress test into a monthly portfolio review
