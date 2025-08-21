import matplotlib.pyplot as plt  # Importing matplotlib 
import pandas as pd  # Importing pandas
dataset_df = pd.read_csv('dataset.csv')  # Reading the dataset from a CSV file

from data_module import (  # Importing functions from data_module.py
    display_dataset_preview, 
    display_visualisation,
    search_data,
)

def main_menu():  # Main menu function to display options to the user
    while True: 
        print("\n=== Data Viewer Interface ===")  
        print("1. View dataset")  
        print("2. View visualisation")  
        print("3. Search or filter data") 
        print("4. Exit")  

        choice = input("Select an option (1-4): ").strip()  # Taking user input for menu selection

        if choice == '1':  # If user chooses to view dataset
            display_dataset_preview()  # Call function to display dataset preview
        elif choice == '2':  # If user chooses to view visualisation
            display_visualisation(dataset_df)  # Call function to display visualisation
        elif choice == '3':  # If user chooses to search or filter data
            search_data()  # Call function to search or filter data
        elif choice == '4':  # If user chooses to exit
            print("Exiting program.")  # Display exit message
            break  # Break the loop to exit the program
        else:  # If user enters an invalid option
            print("Invalid selection. Please choose a number between 1 and 4.")  # Display error message for invalid selection

if __name__ == "__main__":  # If this script is run directly
    main_menu()  # Call the main menu function to start the program