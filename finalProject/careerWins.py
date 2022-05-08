"""
A Linear Regression Model for predicting the number of career wins a
tennis player will have given personal features about them
"""

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

''' 
Name: Career wins linear regression class
Description: machine learning, linear regression model that makes predictions about how many wins a tennis player
             will have during their career considering their personal statistics
'''
class CareerWinsLinRes:
    """ Constructor """
    def __init__(self):
        self.data = None
        self.which_child_transformer = None
        self.model = None
        self.scaler = None

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

    def get_x_and_y(self):
        """
        Get the values of the independent and dependent variables for the linear regression model
        :return: tuple of array of independent variables and array of dependent variable
        """
        x = self.data[["height", "starting_age","age_turned_pro", "training_city_avg_income",
                  "tennis_academy", "coach_age_fifteen", "birth_city_avg_income", "parental_marital_status",
                  "sibling_number", "which_child_quant"]].values
        self.scaler = StandardScaler().fit(x)
        x = self.scaler.transform(x)
        y = self.data["career_wins"].values
        return x, y

    def create_model(self, x, y):
        """
        Create a linear regression model that predicts the number of career wins a player has based on their
        personal statistics
        Prints out weights (coefficients) for each personal stat and the model's intercept
        :param x: personal features about a player
        :param y: number of career wins that player has
        :return: tuple of an array of x testing data and an array of y testing data, used for predictions
        """

        # Separate data into training and testing sets
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

        # Create the Model
        self.model = LinearRegression().fit(x_train, y_train)

        # Print model coefficients and slope
        print("Model Information, Weights and Intercept: ")
        print("Height: ", self.model.coef_[0])
        print("Starting Age: ", self.model.coef_[1])
        print("Age Turned Pro: ", self.model.coef_[2])
        print("Training City Average Income: ", self.model.coef_[3])
        print("Tennis Academy: ", self.model.coef_[4])
        print("Coach at Age 15: ", self.model.coef_[5])
        print("Birth City Average Income: ", self.model.coef_[6])
        print("Parental Marital Status: ", self.model.coef_[7])
        print("Number of Siblings: ", self.model.coef_[8])
        print("Which Child Order: ", self.model.coef_[9])
        print("Intercept: ", self.model.intercept_)
        print()
        return x_test, y_test

    def test_model(self, x_test, y_test):
        """
        Make and print out the model's predictions of the designated testing data
        :param x_test: personal statistics testing data
        :param y_test: corresponding career wins testing data
        :return: nothing
        """

        # Get the predicted y values for the x_test values - return an array
        predictions = self.model.predict(x_test)

        # Compare the actual and predicted values
        print("Testing Linear Model with Test Data:")
        for index in range(len(x_test)):
            # Acutal y value
            actual = y_test[index]

            # Predicted y value
            y_pred = predictions[index]

            # Test x values
            x_height = x_test[index][0]
            x_start_age = x_test[index][1]
            x_pro_age = x_test[index][2]
            x_train_inc = x_test[index][3]
            x_academy = x_test[index][4]
            x_coach = x_test[index][5]
            x_birth_inc = x_test[index][6]
            x_marital = x_test[index][7]
            x_num_sibs = x_test[index][8]
            x_which_child = x_test[index][9]

            print("Height: ", x_height, " Starting Age: ", x_start_age, " Age Turned Pro: ", x_pro_age,
                  " Training City Average Income: ", x_train_inc, " Tennis Academy: ", x_academy, " Coach at Age 15: ",
                  x_coach, " Birth City Average Income: ", x_birth_inc, " Parental Marital Status: ", x_marital,
                  " Number of Siblings: ", x_num_sibs, " Which Child Order: ", x_which_child,
                  " Predicted career wins: ", y_pred, " Actual career wins: ", actual)

''' Main - create a linear regression model that predicts a player's career wins based on personal statistics '''
if __name__ == '__main__':
    # Create model variable and get data
    lin_res_model = CareerWinsLinRes()
    lin_res_model.load_data("updated_wta_data.csv")

    # Make prediction
    x, y = lin_res_model.get_x_and_y()
    x_test, y_test = lin_res_model.create_model(x, y)
    lin_res_model.test_model(x_test, y_test)
