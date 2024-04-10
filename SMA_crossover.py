import backtrader as bt

class SMACrossOverFromBelow(bt.Strategy):
    params = (('sma1_period', 20), ('sma2_period', 50))

    def __init__(self):
        self.sma_short = bt.indicators.SimpleMovingAverage(self.data0, period=self.params.sma1_period)
        self.sma_long = bt.indicators.SimpleMovingAverage(self.data0, period=self.params.sma2_period)
        self.trade_counter = 0
        self.win_counter = 0
        self.buy_price = None
        self.win_rate = 0

    def next(self):
        if self.sma_short[0] > self.sma_long[0] and self.sma_short[-1] < self.sma_long[-1]:
            self.buy(data=self.data0)
            self.buy_price = self.data0.close[0]

        if self.sma_short[0] < self.sma_long[0] and self.sma_short[-1] > self.sma_long[-1]:
            if self.position.size != 0:
                self.sell(data=self.data0)
                if self.buy_price is not None and self.data0.close[0] > self.buy_price:
                    self.win_counter += 1
                self.trade_counter += 1
    def stop(self):
        if self.trade_counter > 0:  # Avoid division by zero
            self.win_rate = self.win_counter / self.trade_counter * 100