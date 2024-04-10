from SMA_crossover import SMACrossOverFromBelow
from result_logger import ResultLogger
from run_backtest import BacktestRunner
from sma_strategy import SMAStrategy

# Define the strategies and their parameters
strategies = [
    (SMAStrategy, {'sma_period': 21}),
    (SMAStrategy, {'sma_period': 34}),
    (SMAStrategy, {'sma_period': 55}),
    (SMAStrategy, {'sma_period': 89}),
    (SMAStrategy, {'sma_period': 144}),
    (SMAStrategy, {'sma_period': 233}),
    (SMACrossOverFromBelow, {'sma1_period': 21, 'sma2_period': 34}),
    (SMACrossOverFromBelow, {'sma1_period': 34, 'sma2_period': 55}),
    (SMACrossOverFromBelow, {'sma1_period': 55, 'sma2_period': 89}),
    (SMACrossOverFromBelow, {'sma1_period': 89, 'sma2_period': 144}),
    (SMACrossOverFromBelow, {'sma1_period': 144, 'sma2_period': 233}),
    #(SMAStrategy, {'sma_period': 377}),
    #(SMAStrategy, {'sma_period': 610}),
    #(SMAStrategy, {'sma_period': 987}),
   # (SMAStrategy, {'sma_period': 1597}),
   # (SMAStrategy, {'sma_period': 2584}),
]

# Create an instance of BacktestRunner
runner = BacktestRunner(strategies, 'META')

# Run the backtests
results = runner.run_backtests()

# Compare the results
ResultLogger.print_results(results)
ResultLogger.plot_results(results, filename='results.png', horizontal_line=10000)