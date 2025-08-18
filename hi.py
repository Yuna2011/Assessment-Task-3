import matplotlib.pyplot as plt
import pandas as pd
dataset_df = pd.read_csv('dataset.csv')


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
    

