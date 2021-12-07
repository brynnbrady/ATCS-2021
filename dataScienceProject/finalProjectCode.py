#######################################################################################################################
# Brynn Brady - Final Project Code
# Ms. Namasivayam
# AT CompSci - 12/7/2021
#
# Quick note about styling: the waa (wins above average) variables are written in the form position_waa, but every
# other variable uses camel case
#######################################################################################################################

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv("mlbLastTenYears.csv")

## Creating additional columns that combine statistics

# 1 fielding WAA is the sum of the WAA of all the fielding postions (not including pitching) WAA
df["fielding_waa"] = df["LF_waa"] + df["RF_waa"] + df["CF_waa"] + df["SS_waa"] + df["1B_waa"] + df["2B_waa"] \
                     + df["3B_waa"] + df["C_waa"]
# 2 outfielding WAA is the sum of the WAA of left field, right field, and center field positions
df["outfielding_waa"] = df["LF_waa"] + df["RF_waa"] + df["CF_waa"]
# 3 infielding WAA is the sum of the WAA of catcher, 1st baseman, 2nd baseman, 3rd baseman, and shortstop positions
df["infielding_waa"] = df["SS_waa"] + df["1B_waa"] + df["2B_waa"] + df["3B_waa"] + df["C_waa"]
# 4 pitching WAA is the sum of the WAA of starting and relief pitching
df["pitching_waa"] = df["SP_waa"] + df["RP_waa"]
# 5 total WAA is the sum of the WAA for all postions
df["total_waa"] = df["pitching_waa"] + df["fielding_waa"]
# 6 tealing attempts includes successful and unsuccessful stealing attempts
df["stealingAttempts"] = df["totalSteals"] + df["totalCaughtStealing"]
# 7 stealing percentage is the percent of stealing attempts that were successful
df["stealingPercentage"] = df["totalSteals"] / df["stealingAttempts"]

pd.set_option("display.max_columns", None)

## Graph 1 - scatterplot showing correlation between teams' starting pitching WAA (strength of starting pitching)
# and the number of games they won during the season — whether or not the team made the playoffs is shown in color

sns.scatterplot(data=df, x = "SP_waa", y = "wins", hue = "wentToPlayoffs", palette = "Blues")\
    .set(title = "Relationship Between the Strength of a Team's Starting Pitching and the Team's Success",
         xlabel = "Team's Starting Pitching WAA", ylabel = "Season Wins")

# calculating correlation coefficient and line of best fit
print("graph 1 correlation and line of best fit:")
x = df["SP_waa"]
y = df["wins"]
correlation = y.corr(x)
print(correlation)
model = np.polyfit(x, y, 1)
predict = np.poly1d(model)
print(model)

plt.show()

## Graph 2 - scatterplot showing correlation between teams' relief pitching WAA (strength of relief pitching)
# and the number of games they won during the season — whether or not the team made the playoffs is shown in color

sns.scatterplot(data=df, x = "RP_waa", y = "wins", hue = "wentToPlayoffs", palette = "Blues").\
    set(title = "Relationship Between the Strength of a Team's Relief Pitching and the Team's Success",
        xlabel = "Team's Relief Pitching WAA", ylabel = "Season Wins")

# calculating correlation coefficient and line of best fit
print("graph 2 correlation and line of best fit:")
x = df["RP_waa"]
y = df["wins"]
correlation = y.corr(x)
print(correlation)
model = np.polyfit(x, y, 1)
predict = np.poly1d(model)
print(model)

plt.show()

## Graph 3 - pie chart showing breakdown of how far teams got in the playoffs if they made the playoffs last year

# make new dataframe of the teams that made the playoffs last year
playoffTeams = df.loc[df["playoffsPreviousYear"] == "yes"]

# get values for pie chart
madeBothYrs = playoffTeams.loc[playoffTeams["wentToPlayoffs"] == "yes"]
madeBothYrsCount = len(madeBothYrs.index)
onlyMadePrev = playoffTeams.loc[playoffTeams["wentToPlayoffs"] == "no"]
onlyMadePrevCount = len(onlyMadePrev.index)

# set labels, colors, and title of pie chart
lbls = ["Did Not Make Playoffs the Following Year", "Made Playoffs the Following Year"]
size_of_groups=[madeBothYrsCount, onlyMadePrevCount,]
clrs = sns.color_palette('pastel')
plt.pie(size_of_groups, labels = lbls, colors = clrs)
plt.title("Breakdown of How Many Playoff Teams Made the Playoffs the Following Year")

plt.show()

## Graph 4 - pie chart showing breakdown of how far all teams got in the playoffs

# get values for pie chart
madePlayoffs = df.loc[df["wentToPlayoffs"] == "yes"]
madePlayoffsCount = len(madePlayoffs.index)
noPlayoffs = df.loc[df["wentToPlayoffs"] == "no"]
noPlayoffsCount = len(noPlayoffs.index)

# set labels, colors, and title of pie chart
lbls = ["Did Not Make the Playoffs", "Made the Playoffs"]
size_of_groups=[noPlayoffsCount, madePlayoffsCount]
clrs = sns.color_palette('pastel')
plt.pie(size_of_groups, labels = lbls, colors = clrs)
plt.title("Breakdown of How Many Teams Made the Playoffs")

plt.show()

## Graph 5 - scatterplot showing correlation between successful stealing percentage and wins, playoffs status in color

sns.scatterplot(data=df, x = "stealingPercentage", y = "wins", hue = "wentToPlayoffs", palette = "Blues")\
    .set(title = "Relationship Between a Team's Successful Stealing Percentage and the Team's Success",
        xlabel = "Team's Successful Stealing Percentage", ylabel = "Season Wins")

# calculating correlation coefficient and line of best fit
print("graph 5 correlation and line of best fit:")
x = df["stealingPercentage"]
y = df["wins"]
correlation = y.corr(x)
print(correlation)
model = np.polyfit(x, y, 1)
predict = np.poly1d(model)
print(model)

plt.show()

## Graph 6 - scatterplot showing correlation between teams' combined infield WAA and wins, playoffs status in color

sns.scatterplot(data=df, x = "infielding_waa", y = "wins", hue = "wentToPlayoffs", palette = "Blues")\
    .set(title = "Relationship Between the Strength of a Team's Infielding and the Team's Success",
         xlabel = "Team's Combined Infielding WAA", ylabel = "Season Wins")

# calculating correlation coefficient and line of best fit
print("graph 6 correlation and line of best fit:")
x = df["infielding_waa"]
y = df["wins"]
correlation = y.corr(x)
print(correlation)
model = np.polyfit(x, y, 1)
predict = np.poly1d(model)
print(model)

plt.show()

## Graph 7 - scatterplot showing correlation between teams' combined outfield WAA and wins, playoffs status in color

sns.scatterplot(data=df, x = "outfielding_waa", y = "wins", hue = "wentToPlayoffs", palette = "Blues")\
    .set(title = "Relationship Between the Strength of a Team's Outfielding and the Team's Success",
         xlabel = "Team's Combined Outfielding WAA", ylabel = "Season Wins")

# calculating correlation coefficient and line of best fit
print("graph 7 correlation and line of best fit:")
x = df["outfielding_waa"]
y = df["wins"]
correlation = y.corr(x)
print(correlation)
model = np.polyfit(x, y, 1)
predict = np.poly1d(model)
print(model)

plt.show()

## Graph 8 - scatterplot showing relationship between average age of batters on a team and team's wins/playoff status

sns.scatterplot(data=df, x = "battersAvgAge", y = "wins", hue = "wentToPlayoffs", palette = "Blues")\
    .set(title = "Relationship Between the Average Age of Batters on a Team and the Team's Success",
         xlabel = "Team's Average Batter Age", ylabel = " Season Wins")

# calculating correlation coefficient and line of best fit
print("graph 8 correlation and line of best fit:")
x = df["battersAvgAge"]
y = df["wins"]
correlation = y.corr(x)
print(correlation)
model = np.polyfit(x, y, 1)
predict = np.poly1d(model)
print(model)

plt.show()

## Graph 9 - histogram showing the distribution of home run counts of teams that went to the playoffs

# get teams that went to playoffs
playoffTeams = df.loc[df["wentToPlayoffs"] == "yes"]

sns.histplot(data=playoffTeams, x="totalHRs", binwidth = 25)\
    .set(title = "Distribution of Home Run Counts of Teams that Made the Playoffs", xlabel = "Home Run Count")
print("mean home runs for teams that made the playoffs:")
print(playoffTeams["totalHRs"].mean())
plt.xticks(np.arange(75,350,25))

plt.show()

## Graph 10 - boxplot showing distribution of the double plays count for teams that made the playoffs

sns.boxplot(data=df, x = "wentToPlayoffs", y="doublePlays", palette = "Blues")\
    .set(title = "Distribution of the Number of Double Plays Made by Teams that Did and Did Not Make the Playoffs",
         xlabel = "Whether or Not a Team Went to the Playoffs", ylabel = "Number of Double Plays Made")

plt.show()

## Graph 11 - boxplot showing distribution of the errors count for teams that made the playoffs

sns.boxplot(data=df, x = "wentToPlayoffs", y="errors", palette = "Blues")\
    .set(title = "Distribution of the Number of Errors Made by Teams that Did and Did Not Make the Playoffs",
         xlabel = "Whether or Not a Team Went to the Playoffs", ylabel = "Number of Errors Made")

plt.show()

## Graph 12 - scatterplot showing the correlation between average number of runs scored by a team in a game
# and their season wins - playoff status is shown in color

sns.scatterplot(data=df, x = "avgRunsPerGame", y = "wins", hue = "wentToPlayoffs", palette = "Blues")\
    .set(title = "Relationship Between a Team's Average Number of Runs Scored per Game and the Team's Success",
         xlabel = "Average Number of of Runs Scored per Game by Team", ylabel = " Season Wins")

# calculating correlation coefficient and line of best fit
print("graph 12 correlation and line of best fit:")
x = df["avgRunsPerGame"]
y = df["wins"]
correlation = y.corr(x)
print(correlation)
model = np.polyfit(x, y, 1)
predict = np.poly1d(model)
print(model)

plt.show()

## Graph 13 - scatterplot showing correlation between teams' pitching WAA (strength of starting and relief pitching
# combined) and the number of games they won during the season — whether or not the team made the playoffs is in color

sns.scatterplot(data=df, x = "pitching_waa", y = "wins", hue = "wentToPlayoffs", palette = "Blues")\
    .set(title = "Relationship Between a Team's Pitching Strength and the Team's Success",
         xlabel = "Team's Combined Starting and Relief Pitching WAA", ylabel = " Season Wins")

# calculating correlation coefficient and line of best fit
print("graph 13 correlation and line of best fit:")
x = df["pitching_waa"]
y = df["wins"]
correlation = y.corr(x)
print(correlation)
model = np.polyfit(x, y, 1)
predict = np.poly1d(model)
print(model)

plt.show()