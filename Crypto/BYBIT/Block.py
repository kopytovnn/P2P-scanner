class Block_start:
    def __init__(self, tradeInfo=-1):
        self.amount, self.units = tradeInfo

    def __str__(self):
        answer = f'<b>{self.amount}</b> {self.units} | Старт\n'
        return answer


class Block_buy:
    def __init__(self, crush=False, tradeInfo=-1, history=-1, linkToBuy=-1, limit=-1):
        self.crush = crush
        if not self.crush:
            self.amount, self.units = tradeInfo
            self.linkToBuy = linkToBuy
            self.minAmount, self.maxAmount = limit
            self.history = history

    def __str__(self):
        if self.crush:
            return 'Block "BUY" has been crushed.'
        answer = f'<b>{self.amount}</b> {self.units} | <a href="{self.linkToBuy}">Покупка</a>\n'
                 # f'from {self.minAmount} to {self.maxAmount}\n\n'
        return answer


class Block_change:
    def __init__(self, crush=False, tradeInfo=-1, history=-1, linkToChange=-1):
        self.crush = crush
        if not self.crush:
            self.amount, self.units = tradeInfo
            self.linkToChange = linkToChange
            self.history = history

    def __str__(self):
        if self.crush:
            return 'Block "CHANGE" has been crushed.'
        answer = f'<b>{self.amount}</b> {self.units} | Обмен на споте\n'
        return answer


class Block_sell:
    def __init__(self, crush=False, tradeInfo=-1, history=-1, linkToSell=-1, limit=-1):
        self.crush = crush
        if not self.crush:
            self.amount, self.units = tradeInfo
            self.linkToSell = linkToSell
            self.minAmount, self.maxAmount = limit
            self.history = history

    def __str__(self):
        if self.crush:
            return 'Block "SELL" has been crushed.'
        answer = ''
        iterator = 1
        for i in self.history:
            answer += f'{iterator}. ' + str(i)
            iterator += 1
        answer += f'{iterator}. <b>{self.amount}</b> RUB | <a href="{self.linkToSell}">Продажа</a>\n\n'
                 # f'Лимиты {self.minAmount} - {self.maxAmount}\n\n'
        return answer
        # return '\n'.join(answer)

