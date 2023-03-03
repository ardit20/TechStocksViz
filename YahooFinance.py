import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
import mplcursors
sns.set_style('darkgrid')

# Define a list of ticker symbols for tech stocks
tickers = ['AAPL', 'AMZN', 'GOOGL', 'MSFT', 'FB']

# Download historical stock prices for the tickers using yfinance
tech_stocks = yf.download(tickers, start='2016-01-01', end='2023-03-03')

# Plot the adjusted close prices for the tech stocks
fig, ax = plt.subplots(figsize=(12, 8))
lines = []
for ticker in tickers:
    line, = ax.plot(tech_stocks['Adj Close'][ticker], label=ticker)
    lines.append(line)

# Format plot
ax.set_title('Tech Stocks Adjusted Close Prices', fontsize=18)
ax.set_xlabel('Date', fontsize=14)
ax.set_ylabel('Price ($)', fontsize=14)
ax.tick_params(axis='both', labelsize=12)
ax.legend(fontsize=12)

# Add tooltip
mplcursors.cursor(lines, hover=True)

# Show plot
plt.show()
