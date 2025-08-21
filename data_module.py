import matplotlib.pyplot as plt  # Importing matplotlib
import pandas as pd  # Importing pandas
dataset_df = pd.read_csv('dataset.csv')  # Reading the dataset from a CSV file




def display_dataset_preview():  # Function to display a preview of the dataset
   total_rows = len(dataset_df)  # Get the total number of rows in the dataset
   print(f"The dataset has 62 rows.")  # Display the total number of rows in the dataset
  
   n_input = input(f"Enter the number of rows to display (1-62, default 5 (press enter)): ").strip()  # Ask how many rows they want to see (default: 5)
  
   if n_input == "":  # If user presses enter without inputting a number
       n = 5  # Default to 5 rows
   else:
       try:
           n = int(n_input)  # Convert input to integer
           if n < 1 or n > total_rows:  # Check if the number is out of range
               print(f"Number out of range. Showing first 5 rows instead.")  # Display error message for out of range input 
               n = 5   #Default to 5 rows
       except ValueError:  # If input is not a valid integer
           print("Invalid input. Showing first 5 rows instead.")  # Display error message for invalid input
           n = 5  # Default to 5 rows
  
   selected_columns = ['Country', 'Talent', 'Total score']  # Display the chosen number of rows
   print(dataset_df[selected_columns].head(n))  # Display the first n rows of the selected columns




def display_visualisation(dataset_df):

   dataset_df.plot(  # Plot grouped bar chart
       kind='bar',  # Specify the kind of plot
       x='Country',  # x-axis is Country
       y=['Talent', 'Total score'],  # Rultiple columns = grouped bars, y-axis is Talent and Total score
       figsize=(14, 8),  # Set figure size
       title='Talent vs Total Score by Country'  # Set title of the plot
   )


   plt.ylabel("Scores")  # Set y-axis label
   plt.xticks(rotation=90)  # Rotate country names for readability
   plt.legend(title="Key")  # Set legend title
   plt.tight_layout()  # Adjust layout to prevent overlap
   plt.show()  # Show the plot






def search_data():  # Function to search or filter data by country
   country_name = input("Enter the country you want to search for: ").strip()  # Ask user for country name
  
   filtered_df = dataset_df[dataset_df['Country'].str.lower() == country_name.lower()]  # Filter the dataset
  
   # Check if the country exists
   if filtered_df.empty:
       print(f"No data found for '{country_name}'")
       return
  
   # Get Talent and Total Score
   talent = filtered_df['Talent'].values[0]   
   total_score = filtered_df['Total score'].values[0]
  
   # Print the results in one line
   print(f"Talent = {talent}")
   print(f"Total Score = {total_score}")