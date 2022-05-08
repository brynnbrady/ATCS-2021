'''
A Logistic Regression Model to determine if a tennis player will
ultimately make the "best of all time" list
'''

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import confusion_matrix

''' 
Name: Best of all time logistic regression class
Description: machine learning, classification model that uses logistic regression to make predictions about 
             whether a tennis player will make the 'best of all time' list given their personal statistics
'''
class BestOfAllTimeLogRes:
    """ Constructor """
    def __init__(self):
        self.data = None
        self.which_child_transformer = None
        self.scaler = None
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
        """
        Get personal aspects about a tennis player (features) and scale them
        :return: scaled features
        """
        x = self.data[["height", "starting_age", "age_turned_pro", "training_city_avg_income",
                  "tennis_academy", "coach_age_fifteen", "birth_city_avg_income", "parental_marital_status",
                  "sibling_number", "which_child_quant"]].values
        # Standardize Data
        self.scaler = StandardScaler().fit(x)
        x = self.scaler.transform(x)
        return x

    def get_target(self):
        """
        Get the best of all time values for each player
        :return: best of all time values
        """
        y = self.data["best_of_all_time"].values
        return y

    def create_model(self, x, y):
        """
        Create a logistic regression model that predicts whether player will make the best of all time list
        Prints the weights for the model, the confusion matrix, and accuracy
        :param x: personal features about players, already scaled
        :param y: whether players made the best of all time list
        :return: nothing
        """

        # Create the model
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
        self.model = LogisticRegression().fit(x_train, y_train)

        # Print the weights for the logistic regression equation
        weights = self.model.coef_[0]
        self.print_weights(weights)

        print("Confusion Matrix:")
        y_pred = self.model.predict(x_test)
        print(confusion_matrix(y_test, y_pred))

        # Get accuracy
        print("Accuracy: ", self.model.score(x_test, y_test))

    def print_weights(self, weights):
        """
        Print the weight of each feature in the logistic regression model
        :param weights: the weights of the features
        :return: nothing
        """
        print("Weights for model:")
        print("Height: ", weights[0])
        print("Starting Age: ", weights[1])
        print("Age Turned Pro: ", weights[2])
        print("Training City Average Income: ", weights[3])
        print("Tennis Academy: ", weights[4])
        print("Coach at Age 15: ", weights[5])
        print("Birth City Average Income: ", weights[6])
        print("Parental Marital Status: ", weights[7])
        print("Number of Siblings: ", weights[8])
        print("Which Child Order: ", weights[9])
        print()

    def get_prediction_input(self):
        """
        Get the personal features about a new player that the user wants to make a prediction about
        :return: the scaled inputted features
        """
        height = int(input("How tall is the player in inches?\n"))
        starting_age = int(input("At what age did the player start playing?\n"))
        turned_pro = int(input("At what age did the player turn pro?\n"))
        training_city_income = int(input("What is the average annual income in the city the player trains in?\n"))
        birth_city_income = int(input("What is the average annual income in the city the player was born in?\n"))
        siblings = int(input("How many siblings does the player have?\n"))

        academy = str(input("Did the player train at a reputable academy?\n"))
        if academy == "no":
            academy = 0
        else:
            academy = 1

        coach = str(input("Was this player's coach a professional coach or a parent?\n"))
        if coach == "coach":
            coach = 0
        else:
            coach = 1

        marital_status = str(input("Are the player's parents married?\n"))
        if marital_status == "no":
            marital_status = 0
        else:
            marital_status = 1

        sibling_order = str(input("Is the player the oldest, youngest, middle, or only child?\n"))
        sibling_order = self.which_child_transformer.transform([sibling_order])[0]

        # Scale the inputs
        x_pred = [[height, starting_age, turned_pro, training_city_income, academy, coach,
                   birth_city_income, marital_status, siblings, sibling_order]]
        x_pred = self.scaler.transform(x_pred)
        return x_pred

    def make_prediction(self):
        """
        Using user input about a new player, make a prediction about whether the player will make the best of all time
        list using the logistic regression model
        Print prediction
        :return: nothing
        """
        # Make and print the prediction
        x_pred = self.get_prediction_input()
        if self.model.predict(x_pred)[0] == "no":
            print("This player will likely not make the best of all time list")
        else:
            print("This player will likely make the best of all time list")

''' Main - create a logistic regression model that predicts whether a player will make the best of all time list'''
if __name__ == '__main__':
    # Create model variable and get data
    log_res_model = BestOfAllTimeLogRes()
    log_res_model.load_data("wta_data_updated.csv")
    x = log_res_model.get_features()
    y = log_res_model.get_target()

    # Create model and make prediction
    log_res_model.create_model(x, y)
    log_res_model.make_prediction()
