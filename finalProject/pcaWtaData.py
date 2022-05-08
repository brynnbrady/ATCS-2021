import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.decomposition import PCA

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

    def get_features(self):
        features = ["height", "starting_age","age_turned_pro", "training_city_avg_income",
                  "tennis_academy", "coach_age_fifteen", "birth_city_avg_income", "parental_marital_status",
                  "sibling_number", "which_child_quant"]
        x = self.data.loc[:, features].values
        x = StandardScaler().fit_transform(x)
        return x

    def get_pca_df_n_components(self, x, n):
        pca = PCA(n_components=n)
        principalComponents = pca.fit_transform(x)

        principalDf = pd.DataFrame(data=principalComponents)
        print(pca.singular_values_)
        return principalDf

    def visualize_2d_pca(self, pca_df):
        print(pca_df)
        sns.scatterplot(data=pca_df, x=pca_df[0], y = pca_df[1])\
            .set(title = "PC1 vs. PC2", xlabel = "PC1", ylabel = "PC2")
        plt.show()

    def visualize_2d_pca_with_target(self, pca_df, target):
        print(pca_df)
        sns.scatterplot( x=pca_df[0], y = pca_df[1], hue = self.data[target])\
            .set(title = "PC1 vs. PC2", xlabel = "PC1", ylabel = "PC2")
        plt.show()

''' Main '''
if __name__ == '__main__':
    # Create model variable and get data
    pca_model = PCAModel()
    pca_model.load_data("updated_wta_data.csv")
    x = pca_model.get_features()
    pca_df = pca_model.get_pca_df_n_components(x, 2)
    pca_model.visualize_2d_pca_with_target(pca_df, "career_wins")