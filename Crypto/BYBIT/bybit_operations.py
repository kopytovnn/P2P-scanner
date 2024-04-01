import requests
from bybit_constants import *
from Block import *


paymentRU = [
  "75",
  "14",
  "377",
  "64",
  "584",
  "585",
  "582",
  "583",
  "581",
  "63",
  "185",
  "533"
]
paymentRU_Alt = [ADVCASH]
paymentUA = []
payment = paymentRU


def p2p_buy(block, token):
    assert type(block) == Block_start
    currency = block.units
    amount = block.amount

    data = {
        "amount": "",
        "authMaker": "false",
        "canTrade": "false",
        "currencyId": currency,
        "page": "1",
        "payment": payment,
        "side": BUY,
        "size": "10",
        "tokenId": token,
        "userId": 64807169
    }

    data1 = {
        "amount": "",
        "authMaker": "false",
        "canTrade": "false",
        "currencyId": "RUB",
        "page": "1",
        "payment": ["185", "75"],
        "side": "1",
        "size": "10",
        "tokenId": "USDT",
        "userId": 64807169
    }
    result = requests.post("https://api2.bybit.com/fiat/otc/item/online", json=data).json()
    if result['result']['items']:
        bo = result['result']['items'][0]
    else:
        return Block_buy(crush=True)

    userId = bo['userId']
    price = float(bo['price'])
    minAmount, maxAmount = float(bo['minAmount']), float(bo['maxAmount'])

    newBlock = Block_buy(tradeInfo=(amount / price, token),
                         history=[block],
                         linkToBuy=f'https://www.bybit.com/fiat/trade/otc/profile/{userId}/{token}/{currency}/item',
                         limit=(minAmount, maxAmount))

    return newBlock


def spot(block, token):
    currency = block.units
    old_amount = block.amount
    history = block.history

    base_url_bybit = 'https://api.bybit.com'
    r_bybit = requests.get(f"{base_url_bybit}/spot/v3/public/quote/ticker/24hr")
    # print(r_bybit.json())

    try:
        answer_bybit = \
            [(float(i['ap']), float(i['bp'])) for i in r_bybit.json()['result']['list'] if i['s'] == currency + token]
        buy_bybit, sell_bybit = answer_bybit[0]
        amount = old_amount * buy_bybit
    except BaseException:
        answer_bybit = \
            [(float(i['ap']), float(i['bp'])) for i in r_bybit.json()['result']['list'] if i['s'] == token + currency]
        buy_bybit, sell_bybit = answer_bybit[0]
        amount = old_amount / buy_bybit

    newBlock = Block_change(tradeInfo=(amount, token),
                            history=history + [block],
                            linkToChange='NOT AVALIABLE RIGHT NOW')
    return newBlock


def p2p_sell(block, currency):
    # assert type(block) in [Block_buy, Block_change]

    token = block.units
    amount = block.amount
    history = block.history

    data = {
        "amount": "40000",
        "authMaker": "false",
        "canTrade": "false",
        "currencyId": currency,
        "page": "1",
        "payment": payment,
        "side": SELL,
        "size": "10",
        "tokenId": token,
        "userId": 64807169
    }
    result = requests.post("https://api2.bybit.com/fiat/otc/item/online", json=data).json()
    if result['result']['items']:
        bo = result['result']['items'][0]
    else:
        return Block_buy(crush=True)

    userId = bo['userId']
    price = float(bo['price'])
    minAmount, maxAmount = float(bo['minAmount']), float(bo['maxAmount'])

    newBlock = Block_sell(tradeInfo=(amount * price, token),
                          history=history + [block],
                          linkToSell=f'https://www.bybit.com/fiat/trade/otc/profile/{userId}/{token}/{currency}/item',
                          limit=(minAmount, maxAmount))

    return newBlock
