import pandas as pd

# Load your CSV data into a Pandas DataFrame
df = pd.read_csv('D1.csv')

# Define a list of betting providers you want to analyze
providers = ['B365', 'BW', 'IW', 'PS', 'WH', 'VC']

# Create a dictionary to store the accuracy for each provider
accuracy_results = {}

# Iterate through each provider
for provider in providers:
  correct_predictions = 0

  # Iterate through each match
  for index, row in df.iterrows():
    # Extract odds for Home, Draw, and Away
    home_odd = row[f'{provider}H']
    draw_odd = row[f'{provider}D']
    away_odd = row[f'{provider}A']

    # Find the lowest odd (highest probability)
    lowest_odd = min(home_odd, draw_odd, away_odd)

    # Determine the predicted outcome based on the lowest odd
    if lowest_odd == home_odd:
      predicted_outcome = 'H'
    elif lowest_odd == draw_odd:
      predicted_outcome = 'D'
    else:
      predicted_outcome = 'A'

    # Compare the predicted outcome to the actual result
    if predicted_outcome == row['FTR']:
      correct_predictions += 1

  # Calculate accuracy
  accuracy = (correct_predictions / len(df)) * 100
  accuracy_results[f'{provider} Accuracy'] = accuracy

# Print the accuracy results
for provider, accuracy in accuracy_results.items():
  print(f'{provider}: {accuracy:.2f}%')