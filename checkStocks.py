import yfinance as yf

from currency_converter import CurrencyConverter


class StockCheck:

    def __init__(self, owned: dict = {}):
       # self.abb = yf.Ticker("ABB.AX")
       # self.aapl = yf.Ticker("AAPL")
       # self.ryt = yf.Ticker("RYT")
       # self.ibm = yf.Ticker("IBM")
        self.c = CurrencyConverter()
        self.owned = owned

    def outputStocks(self):
        from pprint import pprint
        pprint(dir(self.abb.actions))

    def percentageChange(self):
        pass

    def _convert_to_aud(self, amount: dict) -> dict:
        aud_amount = {}
        for k, v in amount.items():
            # We can just append ASX stock values without converting
            if '.AX' in k:
                aud_amount[k] = v
                continue
            aud_amount[k] = round(self.c.convert(v, 'USD', 'AUD'), 2)

        return aud_amount

    def totals(self, owned: dict) -> dict:
        amount = {}
        sumTotal = 0
        for k, _ in owned.items():
            stock = yf.Ticker(k)
            if 'ETF' in stock.info['quoteType']:
                amount[k] = round(
                    stock.info['regularMarketPrice'] * owned[k], 2)
                continue 
            amount[k] = round(stock.info['currentPrice'] * owned[k], 2)

        aud_amount = self._convert_to_aud(amount)
        for _, v in aud_amount.items():
            sumTotal += v

        new_line = '\n'
        msg = (f"Total portfolio: ${round(sumTotal, 2)}, {new_line}" 
               f"Breakdown: {aud_amount}")

        return(msg)


owned = {"RYT": 1, "AAPL": 1, "IBM": 1, "ABB.AX": 1}

print(StockCheck().totals(owned))