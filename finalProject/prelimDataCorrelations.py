"""
Create a class for visualizing and analyzing the relationships between
personal statistics about a tennis player and their success
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

''' 
Name: Graphical and Distribution Statistics Class
Description: allows users to make different types of graphs to visualize data sets - useful for analyzing
             the relationship between sucess and characteristics in sports
'''
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
        self.update_prize_money()
        self.make_junior_training()

    def update_prize_money(self):
        """
        Update players' prize money using the inflation dataset that takes into consideration the year
        Make players' "new prize money" equal to what their prize money would be today (2022) considering inflation
        :return: nothing
        """
        inflation = pd.read_csv("inflation_data.csv")
        new_prize_money = []
        for index in range(len(self.data)):
            year = self.data["year_turned_pro"][index]
            desired_row = year - 1968 # Inflation data starts in the year 1968
            old_prize_money = self.data["prize_money"][index]
            inflation_rate = inflation["inflation"][desired_row]
            new_prize_money.append(old_prize_money*inflation_rate)
        self.data["new_prize_money"] = new_prize_money # New column in dataframe for re-inflated prize money

    def make_junior_training(self):
        """
        Make a new column that measures how long that player trained as a junior
        :return: nothing
        """
        self.data["junior_training_length"] = self.data["age_turned_pro"] - self.data["starting_age"]

    def print_summary_stats(self, stat):
        """
        Print summary statistics about the distribution of variable
        :param stat: the variable distribution being analyzed
        :return: nothing
        """
        print("Distribution statistics for players'", stat)
        quartiles = np.percentile(self.data[stat],[0, 25, 50, 75, 100])
        print("Min: ", self.data[stat].min())
        print("Median: ", quartiles[1])
        print("Mean: ", round(np.mean(self.data[stat]), 3))
        print("Max: ", self.data[stat].max())
        iqr = quartiles[2] - quartiles[0]
        print("IQR: ", iqr)
        print("Standard Deviation: ", round(np.std(self.data[stat]), 3))
        print()

    ''' Graphical Options Below '''
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


''' Main - analyzing the historical relationships between tennis players' personal statistics and success '''
if __name__ == '__main__':
    # Make graphs and statistical summaries to analyze tennis player data
    gs = GraphicsAndStats()
    gs.load_data("updated_wta_data.csv")

    # Look at effect from the r-inflation calculation
    gs.create_scatterplot_with_hue("prize_money", "new_prize_money", "year_turned_pro")
    gs.create_scatterplot("year_turned_pro", "new_prize_money")
    gs.create_scatterplot("year_turned_pro", "prize_money")

    # Analyze relationships between different measures of success
    gs.create_comparative_boxplots("best_of_all_time", "career_length")
    gs.create_comparative_boxplots("best_of_all_time", "career_wins")
    gs.create_comparative_boxplots("best_of_all_time", "prize_money")
    gs.create_comparative_boxplots("best_of_all_time", "new_prize_money")
    gs.create_scatterplot_with_hue("career_length", "career_wins", "new_prize_money")

    # Analyze relationships between siblings and success
    gs.create_comparative_boxplots("which_child", "career_length")
    gs.create_comparative_boxplots("which_child", "career_wins")
    gs.create_comparative_boxplots("which_child", "new_prize_money")
    gs.create_comparative_boxplots("sibling_number", "career_length")
    gs.create_comparative_boxplots("sibling_number", "career_wins")
    gs.create_comparative_boxplots("sibling_number", "new_prize_money")

    # Analyze relationships between type of coaching received and success
    gs.create_comparative_boxplots("coach_age_fifteen", "career_length")
    gs.create_comparative_boxplots("coach_age_fifteen", "career_wins")
    gs.create_comparative_boxplots("coach_age_fifteen", "new_prize_money")
    gs.create_comparative_boxplots("tennis_academy", "career_length")
    gs.create_comparative_boxplots("tennis_academy", "career_wins")
    gs.create_comparative_boxplots("tennis_academy", "new_prize_money")

    # Analyze relationships between career timeline and success
    gs.create_scatterplot("starting_age", "career_length")
    gs.create_scatterplot("starting_age", "career_wins")
    gs.create_scatterplot("starting_age", "new_prize_money")
    gs.create_scatterplot("age_turned_pro", "career_length")
    gs.create_scatterplot("age_turned_pro", "career_wins")
    gs.create_scatterplot("age_turned_pro", "new_prize_money")
    gs.create_scatterplot("junior_training_length", "career_length")
    gs.create_scatterplot("junior_training_length", "career_wins")
    gs.create_scatterplot("junior_training_length", "new_prize_money")

    # Analyze relationships between socioeconomic status and success
    gs.create_scatterplot("training_city_avg_income", "career_length")
    gs.create_scatterplot("training_city_avg_income", "career_wins")
    gs.create_scatterplot("training_city_avg_income", "new_prize_money")
    gs.create_scatterplot("birth_city_avg_income", "career_length")
    gs.create_scatterplot("birth_city_avg_income", "career_wins")
    gs.create_scatterplot("birth_city_avg_income", "new_prize_money")

    # Analyze relationships between height and success
    gs.create_scatterplot("height", "career_length")
    gs.create_scatterplot("height", "career_wins")
    gs.create_scatterplot("height", "new_prize_money")

    # Look at distribution of personal stats
    gs.print_summary_stats("height")
    gs.print_summary_stats("starting_age")
    gs.print_summary_stats("age_turned_pro")
    gs.print_summary_stats("training_city_avg_income")
    gs.print_summary_stats("birth_city_avg_income")
    gs.print_summary_stats("sibling_number")

    # Look at distribution of success measures
    gs.print_summary_stats("career_wins")
    gs.print_summary_stats("career_length")
    gs.print_summary_stats("new_prize_money")
    gs.print_summary_stats("highest_pro_ranking")