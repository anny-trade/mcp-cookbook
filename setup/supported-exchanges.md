# Supported Exchanges

Anny connects to exchanges via CCXT. Two modes are available depending on the exchange's
API capabilities.

## Trading Modes

| Mode | What It Supports |
|------|-----------------|
| **Full** | Balance, open orders, market buy/sell, cancel orders, live bot trading |
| **Portfolio** | Balance and open orders only — read-only view, no order placement |

An exchange qualifies for Full mode only if it passes all 5 criteria: liquidity, order
lifecycle reliability, API rate limits and uptime, required order types, and settlement
edge cases. Failing any category = Portfolio mode only.

## Confirmed Full-Mode Exchanges (order placement supported)

These exchanges are confirmed to support live trading through Anny:

| Exchange | Notes |
|---|---|
| **Binance** | Primary exchange; widest asset coverage |
| **Bybit** | Spot trading; strong API reliability |
| **OKX** | Spot trading supported |
| **Kraken** | Lower volume, solid reliability |
| **KuCoin** | Supported; confirm symbol availability before ordering |
| **Gate.io** | Supported |
| **MEXC** | Supported |

## Portfolio-Mode Exchanges (balance/orders view only)

Exchanges connected in portfolio mode show balances and open orders but **do not accept
order placement through Anny**. This includes most smaller exchanges and any exchange
where the API order lifecycle fails the reliability criteria.

## Checking Exchange Availability for a Symbol

Before placing an order, always run:

```
Is DOTUSDT available for trading on my exchange?
```

Uses `check_symbol_availability`. Returns whether the symbol is tradeable, the minimum
order size, and any restrictions.

## Connecting Your Exchange

```
How do I connect my Binance account to Anny?
```

Uses `get_exchange_setup_guide` with `exchange: "binance"`. Returns step-by-step API key
creation instructions specific to that exchange, including required permissions and
IP whitelist recommendations.

Supported `exchange` values include: `binance`, `bybit`, `okx`, `kraken`, `kucoin`,
`gateio`, `mexc`, and others. Use `check_symbol_availability` first to confirm your
exchange is in Full mode.

## SPOT Only

All order execution through Anny MCP is **SPOT market only**. Futures, margin, and
leveraged tokens are not supported through the MCP trading tools.

## See Also

- [examples/03-portfolio-management/check-symbol-availability.md](../examples/03-portfolio-management/check-symbol-availability.md)
- [examples/03-portfolio-management/check-exchange-balance.md](../examples/03-portfolio-management/check-exchange-balance.md)
- [docs.anny.trade](https://docs.anny.trade) — full exchange compatibility list
