'''
Creates a Logistic Regression Model to determine
if someone will survive a battle against breast cancer
considering their age and number of nodes
'''

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import confusion_matrix

''' Load Data '''
data = pd.read_csv("wta_data.csv")

data["tennis_academy"].replace(["no", "yes"], [0, 1], inplace=True)
data["coach_age_fifteen"].replace(["coach", "parent"], [0, 1], inplace=True)
data["parental_marital_status"].replace(["not married", "married"], [0, 1], inplace=True)

# Read in features and classes
which_child = data["which_child"].values

# Transform qualitative data to quantitative
which_child_transformer = LabelEncoder().fit(which_child)
which_child = which_child_transformer.transform(which_child)

data["which_child_quant"] = which_child

x = data[["height", "starting_age", "age_turned_pro", "training_city_avg_income",
          "tennis_academy", "coach_age_fifteen", "birth_city_avg_income", "parental_marital_status",
          "sibling_number", "which_child_quant"]].values
y = data["best_of_all_time"].values

print(x)


# Standardize Data

# Split into train and test data

''' Create Model '''

# Print the weights for the logistic regression equation

''' Test Model '''
# Get predictions from x_test - Returns a 2D array

# Get confusion matrix

# Get accuracy

''' Make a new prediction '''

# Scale the inputs

# Make and print the prediction