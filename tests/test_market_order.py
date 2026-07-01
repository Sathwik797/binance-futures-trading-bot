from bot.orders import OrderManager

manager = OrderManager()

order = manager.place_market_order(
    symbol="BTCUSDT",
    side="BUY",
    quantity=0.001
)

print(order)