import backtrader as bt

class SMAStrategy(bt.Strategy):
    params = (('sma_period', 20),)

    def __init__(self):
        self.sma = bt.indicators.SimpleMovingAverage(self.data0, period=self.params.sma_period)
        self.trade_counter = 0
        self.win_counter = 0
        self.buy_price = None
        self.win_rate = 0

    def next(self):
        if self.sma[-1] < self.data0.close[-1] and self.sma[0] > self.data0.close[0]:
            self.buy(data=self.data0)
            self.buy_price = self.data0.close[0]
            #self.log('BUY EXECUTED, %.2f' % self.data0.close[0])

        if self.sma[-1] > self.data0.close[-1] and self.sma[0] < self.data0.close[0]:
            if self.position.size != 0:
                self.sell(data=self.data0)
                if self.buy_price is not None and self.data0.close[0] > self.buy_price:
                    self.win_counter += 1
                #self.log('SELL EXECUTED, %.2f' % self.data0.close[0])
                self.trade_counter += 1

    def log(self, txt, dt=None):
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, SMA Period: %d, %s' % (dt.isoformat(), self.params.sma_period, txt))

    def stop(self):
        if self.trade_counter > 0:  # Avoid division by zero
            self.win_rate = self.win_counter / self.trade_counter * 100
            #print(f"Win rate: {self.win_rate}%")
        #else:
            #print("No trades were made.")