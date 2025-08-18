import matplotlib.pyplot as plt
import pandas as pd
dataset_df = pd.read_csv('dataset.csv')


def search_data():
    # Ask user for country name
    country_name = input("Enter the country you want to search for: ").strip()
    
    # Filter the dataset
    filtered_df = dataset_df[dataset_df['Country'].str.lower() == country_name.lower()]
    
    # Check if the country exists
    if filtered_df.empty:
        print(f"No data found for '{country_name}'")
        return
    
    # Get Talent and Total Score
    talent = filtered_df['Talent'].values[0]
    total_score = filtered_df['Total Score'].values[0]
    
    # Print the results in one line
    print(f"{country_name}: Talent = {talent}, Total Score = {total_score}")

# Example usage
search_data()
