from bot.client import BinanceClient

client = BinanceClient().get_client()

try:
    account = client.futures_account()

    print("✅ Client Connected Successfully")

except Exception as e:
    print(e)