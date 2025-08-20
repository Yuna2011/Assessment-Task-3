import matplotlib.pyplot as plt
import pandas as pd
Dataset1_df = pd.read_csv('Dataset1.csv')




def display_dataset_preview():
   total_rows = len(Dataset1_df)
   print(f"The dataset has {total_rows} rows.")
  
   # Ask how many rows they want to see (default: 5)
   n_input = input(f"Enter the number of rows to display (1-{total_rows}, default 5 (press enter)): ").strip()
  
   if n_input == "":
       n = 5
   else:
       try:
           n = int(n_input)
           if n < 1 or n > total_rows:
               print(f"Number out of range. Showing first 5 rows instead.")
               n = 5
       except ValueError:
           print("Invalid input. Showing first 5 rows instead.")
           n = 5
  
   # Display the chosen number of rows
   print(Dataset1_df.head(n))




def display_visualisation(Dataset1_df):
   # Sort by Total Score so the chart looks cleaner (optional)
   Dataset1_df = Dataset1_df.sort_values("Total Score", ascending=False)


   # Plot grouped bar chart
   Dataset1_df.plot(
       kind='bar',
       x='Country',
       y=['Talent', 'Total Score'],  # multiple columns = grouped bars
       figsize=(14, 8),
       title='Talent vs Total Score by Country'
   )


   plt.ylabel("Scores")
   plt.xticks(rotation=90)  # rotate country names for readability
   plt.legend(title="Key")
   plt.tight_layout()
   plt.show()






def search_data():
   # Ask user for country name
   country_name = input("Enter the country you want to search for: ").strip()
  
   # Filter the dataset
   filtered_df = Dataset1_df[Dataset1_df['Country'].str.lower() == country_name.lower()]
  
   # Check if the country exists
   if filtered_df.empty:
       print(f"No data found for '{country_name}'")
       return
  
   # Get Talent and Total Score
   talent = filtered_df['Talent'].values[0]   
   total_score = filtered_df['Total Score'].values[0]
  
   # Print the results in one line
   print(f"Talent = {talent}")
   print(f"Total Score = {total_score}")

# search_data()


