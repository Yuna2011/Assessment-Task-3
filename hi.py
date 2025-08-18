import matplotlib.pyplot as plt
import pandas as pd
dataset_df = pd.read_csv('dataset.csv')


def display_visualisation(dataset_df):
    # Sort by Total Score so the chart looks cleaner (optional)
    dataset_df = dataset_df.sort_values("Total Score", ascending=False)

    # Plot grouped bar chart
    dataset_df.plot(
        kind='bar',
        x='Country',
        y=['Talent', 'Total Score'],  # multiple columns = grouped bars
        figsize=(14, 8),
        title='Talent vs Total Score by Country'
    )

    plt.ylabel("Scores")
    plt.xticks(rotation=90)  # rotate country names for readability
    plt.legend(title="Metrics")
    plt.tight_layout()
    plt.show()