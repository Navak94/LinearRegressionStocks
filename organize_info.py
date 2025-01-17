import pandas as pd

# File paths
stock_analysis_file = "stock_analysis.csv"
linear_regression_file = "stock_analysis_linear_regression.csv"
lstm_trends_file = "lstm_stock_trends.csv"

# Load the main stock analysis CSV
stock_df = pd.read_csv(stock_analysis_file)
stock_df.set_index("Company", inplace=True)

# Load Linear Regression CSV & check for duplicates
linear_df = pd.read_csv(linear_regression_file)
linear_last_column = linear_df.columns[-1]
linear_data = linear_df.set_index("Company")[linear_last_column]
linear_data = linear_data[~linear_data.index.duplicated(keep='first')]

# Load LSTM Trends CSV & check for duplicates
lstm_df = pd.read_csv(lstm_trends_file)
lstm_last_column = lstm_df.columns[-1]
lstm_data = lstm_df.set_index("Company")[lstm_last_column]
lstm_data = lstm_data[~lstm_data.index.duplicated(keep='first')]

# Align indices to stock_df
linear_data = linear_data.reindex(stock_df.index, fill_value="No Data")
lstm_data = lstm_data.reindex(stock_df.index, fill_value="No Data")

# Update stock_analysis.csv
stock_df["Linear Regression"] = linear_data
stock_df["Neural Network"] = lstm_data

# Save the updated CSV
stock_df.reset_index().to_csv(stock_analysis_file, index=False)

print("✅ stock_analysis.csv has been updated successfully!")
