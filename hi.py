import matplotlib.pyplot as plt
import pandas as pd
dataset_df = pd.read_csv('dataset.csv')


<<<<<<< HEAD
#def display_visualisation():
        #bars = plt.bar()
        #plt.xlabel("Country") #Labelling the x axis 
        #plt.ylabel("Score") #Labelling the y axis
        #plt.title("Correlation of each countries Talent and Total Score") 


#plt.show() 

dataset_df.plot(
               kind='bar',
               x='Country',
               y='Total Score'
               color='blue',
               alpha=0.3,
               title='Correlation of arrival and distance'
              )
plt.show()
    

=======
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
>>>>>>> 0d23af467d28505bd1a5de6247b42eda06c12e6f
