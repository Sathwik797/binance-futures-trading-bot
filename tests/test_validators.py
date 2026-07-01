from bot.validators import *

print(validate_symbol("btcusdt"))
print(validate_side("buy"))
print(validate_order_type("market"))
print(validate_quantity(0.001))
print(validate_price(100000, "LIMIT"))

print("\nAll validations passed successfully!")