# Changelog

All notable changes to this cookbook are documented here.

## [1.1.0] — 2026-05-06

### Fixed
- `docs/CREDIT_COSTS.md`: corrected `backtest_custom_strategy` and `backtest_custom_strategy` min tier from FREE to PRO — FREE tier does not include backtesting
- `research/oos-validation-results.md`: corrected AVAX/1h failure reason — was "mean-reversion strategy" (fabricated), now "CFO Line strategy overfit on 1h intraday noise"
- `examples/02-market-intelligence/fear-greed-context.md`: removed "coming soon" language, replaced with factual note about pattern library data requirements
- `README.md`: added leverage disclosure on 6.24% avg monthly return figure
- `README.md`: corrected paid tools table to show PRO as minimum tier for backtesting

### Added
- `QUICKSTART.md`: zero-to-first-backtest guide in 7 steps
- `CHANGELOG.md`: this file
- `setup/cursor.md`: Cursor-specific MCP setup guide
- `README.md`: "Is It Free?" section, closing Get Started CTA, CFO Anny Line definition, inbound link to `docs/LITMUS_TEST.md`

### Improved
- `README.md`: research hook in opening paragraph, guest-first Quick Connect ordering, leverage disclosure, keyword density (Bitcoin, Ethereum, MCP server, algorithmic trading, trading strategy)
- `README.md`: example gallery descriptions reference use cases more concretely

## [1.0.0] — 2026-05-05

### Added
- Initial release: 52 files across setup/, examples/ (01–09), research/, scripts/, litmus/, docs/, .github/
- 9 example folders with 48 example files
- 8 research files from 2026-04-26 overnight strategy session (702 combinations, 12 assets)
- 8 Python scripts covering auth, market monitoring, backtesting, and portfolio management
- Litmus test suite with 4 JSON schemas and 2 check files
