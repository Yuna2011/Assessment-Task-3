# data_module.py
import matplotlib.pyplot as plt
import pandas as pd
dataset_df = pd.read_csv('dataset.csv')


def display_dataset_preview():
    # pd.set_option('display.max_rows', 1000)
    print(dataset_df)
    pass

def display_visualisation():
    dataset_df.plot(
               kind='Bar',
               x='Country',
               y='Talent''Total Score',
               color='black',
               alpha=0.3,
               title='Talent and Total Score'
              )
    plt.show()
    pass

def search_data():
    # Use pandas here
    pass

