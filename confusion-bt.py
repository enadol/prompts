import pandas as pd
from sklearn.metrics import confusion_matrix

# Load your CSV data into a Pandas DataFrame
df = pd.read_csv('D1.csv')

# Define a list of betting providers you want to analyze
providers = ['B365', 'BW', 'IW', 'PS', 'WH', 'VC']

# Iterate through each provider
for provider in providers:
  # Extract predicted outcomes
  predicted_outcomes = []
  for index, row in df.iterrows():
    home_odd = row[f'{provider}H']
    draw_odd = row[f'{provider}D']
    away_odd = row[f'{provider}A']
    lowest_odd = min(home_odd, draw_odd, away_odd)

    if lowest_odd == home_odd:
      predicted_outcomes.append('H')
    elif lowest_odd == draw_odd:
      predicted_outcomes.append('D')
    else:
      predicted_outcomes.append('A')

  # Create the confusion matrix
  cm = confusion_matrix(df['FTR'], predicted_outcomes, labels=['H', 'D', 'A'])

  # Print the confusion matrix
  print(f"Confusion Matrix for {provider}:")
  print(cm)
  print("\n")