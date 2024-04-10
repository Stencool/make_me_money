import backtrader as bt

class GainObserver(bt.Observer):
    lines = ('gain',)

    def next(self):
        self.lines.gain[0] = (self._owner.broker.getvalue() / self._owner.broker.startingcash - 1) * 100