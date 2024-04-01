BUY = "1"
SELL = "0"

# FIAT
FIAT = "FIAT"
RUB = "RUB"
UAH = "UAH"
ALL_FIAT = [RUB, UAH]

# CRYPTO
CRYPTO = "CRYPTO"
USDT = "USDT"
BTC = "BTC"
ETH = "ETH"
USDC = "USDC"
ALL_CRYPTO = [USDT, BTC, ETH, USDC]

VARIATOR = {}
for i in ALL_CRYPTO:
    VARIATOR[i] = CRYPTO
for i in ALL_FIAT:
    VARIATOR[i] = FIAT

# RUS
TINKOFF = "75"
ROSBANK = "185"
ROSSELKHOZBANK = "66"
RUSSIANSTANDARTBANK = "533"
SBERBANK = "377"
ADVCASH = "5"
SBP = "382"

# UKR
PRIVATBANK = "60"
MONOBANK = "43"

# MOVES
BINANCE_SPOT = 'BINANCE_SPOT'
BYBIT_SPOT = 'BYBIT_SPOT'
BYBIT_P2P = 'BYBIT_P2P'
BINANCE_P2P = 'BINANCE_P2P'
'''ALSO FIAT'''

ALL_MOVES = [FIAT, BINANCE_SPOT, BYBIT_SPOT, BYBIT_P2P, BINANCE_P2P]
AVALIABLE_MOVES = {
    FIAT: [BYBIT_P2P, BINANCE_P2P],
    BYBIT_P2P: [FIAT, BYBIT_SPOT],
    BINANCE_P2P: [FIAT, BINANCE_SPOT],
}

AVALIABLE_UNITS = {
    FIAT: [RUB, UAH],
    BINANCE_SPOT: [USDC, USDT, BTC, ETH],
    BINANCE_P2P: [USDC, USDT, BTC, ETH],
    BYBIT_SPOT: [USDC, USDT, BTC, ETH],
    BYBIT_P2P: [USDC, USDT, BTC, ETH]
}