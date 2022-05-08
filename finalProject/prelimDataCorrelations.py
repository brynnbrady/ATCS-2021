"""
Create a class for visualizing and analyzing historical relationship between
personal statistics about a tennis player and their success
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


class GraphicsAndStats:
    """ Constructor """
    def __init__(self):
        self.data = None

    def load_data(self, filepath):
        """
        Load in the data and replace all qualitative variables with numerical values
        :param filepath: the csv file being loaded in
        :return: nothing
        """
        self.data = pd.read_csv(filepath)

    def print_summary_stats(self, stat):
        print("Distribution statistics for players'", stat)
        quartiles = np.percentile(self.data[stat],[0, 25, 50, 75, 100])
        print("Min: ", self.data[stat].min())
        print("Q1: ", quartiles[0])
        print("Median: ", quartiles[1])
        print("Q3: ", quartiles[2])
        print("Max: ", self.data[stat].max())
        print()

        range = self.data[stat].max() - self.data[stat].min()
        iqr = quartiles[2] - quartiles[0]
        print("Range: ", range)
        print("IQR: ", iqr)

        print("Mean: ", round(np.mean(self.data[stat]), 3))
        print("Standard Deviation: ", round(np.std(self.data[stat]), 3))

    def create_histogram(self, stat):
        sns.histplot(data=self.data, x=stat).set(title = "Distribution of players' " + stat,
        xlabel = stat, ylabel = "count")
        plt.show()

    def create_scatterplot(self, x_stat, y_stat):
        sns.scatterplot(data=self.data, x=x_stat, y=y_stat). \
            set(title="Relationship Between players' " + x_stat + " and players' " + y_stat,
                xlabel=x_stat, ylabel=y_stat)
        plt.show()

    def create_scatterplot_with_hue(self, x_stat, y_stat, hue_stat):
        sns.scatterplot(data=self.data, x=x_stat, y=y_stat, hue = hue_stat)\
            .set(title="Relationship Between players' " + x_stat + " and players' " + y_stat,
            xlabel=x_stat, ylabel=y_stat)
        plt.show()

    def create_two_var_barplot(self, category, count):
        sns.barplot(x=category, y=count, data=self.data)
        plt.show()

    def create_three_var_barplot(self, category, count, hue):
        sns.barplot(x=category, y=count, hue = hue, data=self.data)
        plt.show()

    def create_comparative_boxplots(self, category, y_stat):
        sns.boxplot(x=category, y=y_stat, data=self.data)
        plt.show()

    def create_comparative_histograms(self, x_category, hue_var):
        sns.histplot(data=self.data, x=x_category, hue=hue_var, multiple="dodge", shrink=.8)
        plt.show()

''' Main - analyzing the historical relationships between tennis players' personal statistics and success '''
if __name__ == '__main__':
    # Make graphs and statistical summaries to analyze tennis player data
    gs = GraphicsAndStats()
    gs.load_data("updated_wta_data.csv")
    # Insert graphs here