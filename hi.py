import matplotlib.pyplot as plt
import pandas as pd
dataset_df = pd.read_csv('dataset.csv')

def display_visualisation():
    dataset_df.plot(
               kind='line',
               x='country',
               y='percentage',
               color='black',
               alpha=0.3,
               title='Correlation of talent and e'
              )
    plt.show()
    pass