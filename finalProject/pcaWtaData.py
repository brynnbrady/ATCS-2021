import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.decomposition import PCA

''' 
Name: Principal Component Analysis model
Description: reduces multidimensional data into a chosen number of components (eigenvectors that maximize variation
             in the data set) - allows for visualization of the data in 2D is two components chosen, graphs data projected
             onto the vectors
Note: PCA is used to increase the power of finding relationships between multiple variables (e.g. personal features) and
      a target variable (e.g. measures of success)
'''
class PCAModel:
    """ Constructor """
    def __init__(self):
        self.data = None
        self.which_child_transformer = None
        self.model = None

    def load_data(self, filepath):
        """
        Load in the data and replace all qualitative variables with numerical values
        :param filepath: the csv file being loaded in
        :return: nothing
        """
        self.data = pd.read_csv(filepath)
        self.qual_to_quant_data()
        self.update_prize_money()

    def qual_to_quant_data(self):
        """
        Replace qualitative variables with numerical/quantitative values
        :return: nothing
        """
        # Replace qualitative measures with numerical values
        self.data["tennis_academy"].replace(["no", "yes"], [0, 1], inplace=True)
        self.data["coach_age_fifteen"].replace(["coach", "parent"], [0, 1], inplace=True)
        self.data["parental_marital_status"].replace(["not married", "married"], [0, 1], inplace=True)

        which_child = self.data["which_child"].values
        self.which_child_transformer = LabelEncoder().fit(which_child)
        which_child = self.which_child_transformer.transform(which_child)
        self.data["which_child_quant"] = which_child

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
            desired_row = year - 1968
            old_prize_money = self.data["prize_money"][index]
            inflation_rate = inflation["inflation"][desired_row]
            new_prize_money.append(old_prize_money*inflation_rate)
        self.data["new_prize_money"] = new_prize_money

    def get_features(self):
        """
        Get the personal features about a player and scale them
        :return: the scaled features
        """
        features = ["height", "starting_age","age_turned_pro", "training_city_avg_income",
                  "tennis_academy", "coach_age_fifteen", "birth_city_avg_income", "parental_marital_status",
                  "sibling_number", "which_child_quant"]
        x = self.data.loc[:, features].values
        x = StandardScaler().fit_transform(x)
        return x

    def get_pca_df_n_components(self, x, n):
        """
        Perform pca on the personal features about tennis players
        :param x: personal features being dimensionally reduced
        :param n: number of desired components
        :return: values of the mutlidimensional data points projected onto the different components
        """
        pca = PCA(n_components=n)
        principalComponents = pca.fit_transform(x)

        principalDf = pd.DataFrame(data=principalComponents)
        print(principalDf)
        return principalDf

    def visualize_2d_pca(self, pca_df):
        """
        If the pca returned 2 components, visualize those data points projected onto a plot of the first component (x-axis)
        and the second component (y-axis)
        :param pca_df: dataframe of the data points projected onto the principal components
        :return: nothing
        """
        sns.scatterplot(data=pca_df, x=pca_df[0], y = pca_df[1])\
            .set(title = "PC1 vs. PC2", xlabel = "PC1", ylabel = "PC2")
        plt.show()

    def visualize_2d_pca_with_target(self, pca_df, target):
        """
        If the pca returned 2 components, visualize those data points projected onto a plot of the first component (x-axis)
        and the second component (y-axis) with a hue that represents a measure of career success (i.e. looking to see if
        the principal components show any correlation with different measures of success)
        :param pca_df: dataframe of the data points projected onto the principal components
        :param target: measure of success being examined
        :return: nothing
        """
        sns.scatterplot( x=pca_df[0], y = pca_df[1], hue = self.data[target])\
            .set(title = "PC1 vs. PC2", xlabel = "PC1", ylabel = "PC2")
        plt.show()

''' Main - perform pca on tennis player data to see if there is any relation between the summarize, reduced data
            and any measures of success'''
if __name__ == '__main__':
    # Create model variable and get data
    pca_model = PCAModel()
    pca_model.load_data("updated_wta_data.csv")
    x = pca_model.get_features()
    pca_df = pca_model.get_pca_df_n_components(x, 2)
    pca_model.visualize_2d_pca_with_target(pca_df, "new_prize_money")
    pca_model.visualize_2d_pca_with_target(pca_df, "career_wins")
    pca_model.visualize_2d_pca_with_target(pca_df, "career_length")