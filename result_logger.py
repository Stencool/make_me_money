import matplotlib.pyplot as plt
import numpy as np
class ResultLogger:

        def print_results(results):
            print("\nFinal comparison of all strategies:")
            for (strategy_name, sma_period), (final_value, num_trades, win_rate, gain_percentage) in results.items():
                print(f'Strategy: {strategy_name}, SMA Period: {sma_period}, Final Portfolio Value: {final_value:.2f}, Number of Trades: {num_trades}, Win rate: {win_rate}, Gain percentage: {gain_percentage}')

        def plot_results(results, filename='results.png',  horizontal_line=None):
            # Create a new figure and a subplot for the bar plot
            # Create a new figure with a specific size
            plt.figure(figsize=(800, 600))
            fig, ax1 = plt.subplots()
            final_values = []
            strategy_names = []
            win_rates = []
            gain_percentages = []
            for (strategy_name, sma_period), (final_value, num_trades, win_rate, gain_percentage) in results.items():
                final_values.append(final_value)
                strategy_names.append(f"{strategy_name}_{sma_period}")
                win_rates.append(win_rate)  
                gain_percentages.append(gain_percentage)   
            # Get the strategy names and final portfolio values
            #strategy_names = [f"{strategy_name}_{sma_period}" for (strategy_name, sma_period), (final_value, num_trades, win_Rate) in results.items()]
            #final_values = [final_value for (strategy_name, params), (final_value, num_trades, win_rate) in results.items()]
            #win_rates = [win_rate for (strategy_name, params), (final_value, num_trades, win_rate) in results.items()]

            # Create an array for the x values
            x = np.arange(len(strategy_names))

            # Create a bar plot
            ax1.bar(x, final_values)
            ax1.set_xticks(x)
            ax1.set_xticklabels(strategy_names, rotation='vertical')
            ax1.set_yticks(range(0, round(max(final_values))+500, 100))  # Set the ticks on the y-axis
            ax1.set_ylim(max(final_values)-1000, max(final_values)+1000)  # Set the limits of the y-axis


             # Create a second y-axis for the win rates
            ax2 = ax1.twinx()
            ax2.plot(x, win_rates, color='y', marker='o', label='Win Rates')
            ax2.set_xticklabels([])
            
            
            # Set the ticks and limits for the right y-axis
            ax2.set_yticks(range(0, round(max(win_rates))+1, 10))  # Set the ticks on the right y-axis
            ax2.set_ylim(min(win_rates)-5, max(win_rates)+5)  # Set the limits of the right y-axis

            # Create a third y-axis for the gain percentages
            ax3 = ax1.twinx()
            ax3.spines['right'].set_position(('outward', 30))  # Move the third y-axis to the right
            ax3.plot(x, gain_percentages, color='b', marker='o', label='Gain Percentages')
            ax3.set_xticklabels([])
            # Add a legend to the plot
           # ax1.legend(loc='upper left')
            ax2.legend(loc='upper right')
            ax3.legend(loc='upper right')

            # Set the ticks and limits for the third y-axis
            ax3.set_yticks(range(0, round(max(gain_percentages))+1, 1))  # Set the ticks on the third y-axis
            ax3.set_ylim(min(gain_percentages)-5, max(gain_percentages)+5)  # Set the limits of the third y-axis

            if horizontal_line is not None:
                ax1.axhline(y=horizontal_line, color='r', linestyle='-')

            # Save the plot as a PNG file
            plt.tight_layout()
            plt.savefig(filename, bbox_inches='tight')