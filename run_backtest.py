import backtrader as bt
import yfinance as yf

class BacktestRunner:
    def __init__(self, strategies, stock_symbol='AAPL'):
        self.strategies = strategies
        self.stock_symbol = stock_symbol

    def run_backtests(self):
        results = {}
        # Create a cerebro engine
        cerebro = bt.Cerebro()

        for Strategy, params in self.strategies:
             # Log the creation of the strategy
            print(f'Creating strategy {Strategy.__name__} with parameters {params}')
           
            # Download historical market data
            data_df = yf.download(self.stock_symbol, start='2010-01-01', end='2022-12-31')
           
            # Add the strategy
            cerebro.addstrategy(Strategy, **params)

             # Create a Data Feed
            data = bt.feeds.PandasData(dataname=data_df)

            # Add the data feed to the cerebro engine
            cerebro.adddata(data)

            # Run the backtest
            result = cerebro.run()

            # Check if the result list is not empty
            if result:
                # Get the final portfolio value
                final_value = result[0].broker.get_value()
                num_trades = result[0].trade_counter
                win_rate = result[0].win_rate

                # Store the result
                results[(Strategy.__class__.__name__, params['sma_period'])] = (final_value, num_trades, win_rate)

                # Print out the final result
                print(f'Final Portfolio Value for {Strategy.__class__.__name__}: {final_value:.2f}, Number of Trades: {num_trades}, Win rate: {win_rate}')
            else:
                print(f'No results for {Strategy.__name__}')
        return results


