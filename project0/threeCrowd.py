names = ["abc", "def", "ghi", "jkl"]

def crowd_test(list):
    if len(list) > 3:
        print("Your room is crowded")
        list.pop(0)
    if len(list) > 3:
        print("Perfect amount of people")

crowd_test(names)
