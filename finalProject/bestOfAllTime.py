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

''' Load and Process Data '''
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

# Standardize Data
scaler = StandardScaler().fit(x)
x = scaler.transform(x)

# Split into train and test data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

''' Create Model '''
model = LogisticRegression().fit(x_train, y_train)

# Print the weights for the logistic regression equation
coef = model.coef_[0]
print("Weights for model:")
print(coef)
print()

''' Test Model '''
# Get predictions from x_test - Returns a 2D array
y_pred = model.predict(x_test)

# Get confusion matrix
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Get accuracy
print("Accuracy: ", model.score(x_test, y_test))

''' Make a new prediction '''
# quantitative data
height = int(input("How tall is the player in inches?\n"))
starting_age = int(input("At what age did the player start playing?\n"))
turned_pro = int(input("At what age did the player turn pro?\n"))
training_city_income = int(input("What is the average annual income in the city the player trains in?\n"))
birth_city_income = int(input("What is the average annual income in the city the player was born in?\n"))
siblings = int(input("How many siblings does the player have?\n"))

# qualitative data, turn into quantitative values
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
sibling_order = which_child_transformer.transform([sibling_order])[0]

# Scale the inputs
x_pred = [[height, starting_age, turned_pro,training_city_income, academy, coach,
           birth_city_income, marital_status,siblings, sibling_order]]
x_pred = scaler.transform(x_pred)

# Make and print the prediction
if model.predict(x_pred)[0] == "no":
    print("This player will likely not make the best of all time list")
else:
    print("This player will likely make the best of all time list")