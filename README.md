# Binance Futures Testnet Trading Bot

A modular command-line Python application for placing **MARKET** and **LIMIT** orders on the **Binance USDT-M Futures Testnet**.

> ⚠️ **Testnet only:** This project is intended for Binance Futures Testnet use. Do not use real funds or production credentials.

## ✨ Features

- MARKET and LIMIT orders
- BUY and SELL support
- CLI built with `argparse`
- Input validation
- API error handling
- Structured logging
- Environment-based credential management

## 🏗️ Architecture

```text
CLI
 ↓
Validation
 ↓
Order Logic
 ↓
Binance Client
 ↓
Futures Testnet
```

The code separates API communication, order handling, validation, logging, and CLI interaction.

## 🛠️ Tech Stack

- Python 3.10+
- python-binance
- python-dotenv
- argparse
- logging

## 📂 Project Structure

```text
trading_bot/
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
├── tests/
│   ├── __init__.py
│   ├── test_client.py
│   ├── test_market_order.py
│   └── test_validators.py
├── logs/
│   └── trading.log
├── cli.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/Sathwik797/binance-futures-trading-bot.git
cd binance-futures-trading-bot
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## 🔐 Environment Variables

Create a `.env` file in the project root:

```env
API_KEY=YOUR_BINANCE_TESTNET_API_KEY
SECRET_KEY=YOUR_BINANCE_TESTNET_SECRET_KEY
```

Never commit `.env` or API credentials to GitHub.

## ▶️ Usage

### MARKET order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### LIMIT order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 200000
```

Orders are submitted to the **Binance Futures Testnet**.

## 🧪 Validation & Error Handling

The application validates:

- Trading symbol
- Order side (`BUY` / `SELL`)
- Order type (`MARKET` / `LIMIT`)
- Positive quantity
- Required price for LIMIT orders

It also handles missing credentials, Binance API errors, invalid input, and unexpected runtime failures.

## 📝 Logging

The application records API activity, order requests/responses, and errors in:

```text
logs/trading.log
```

## 🔮 Future Improvements

- Additional order types
- Order cancellation
- Position management
- More comprehensive automated tests
- Optional web interface

## 👨‍💻 Author

**Sathwik Reddy**

Built as a Python developer internship project using the Binance Futures Testnet.
