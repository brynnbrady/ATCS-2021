games = ["bridge", "hearts", "queen of spades"]
print("My games: ", games)

new_game = ""
keepAsking = True

while keepAsking == True:
    new_game = input("Add a game or type 'stop' to quit: ")
    if new_game == 'stop':
        keepAsking = False
    else:
        games.append(new_game)

print("Our games: ", games)
