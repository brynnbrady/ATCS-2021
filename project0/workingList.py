careers = ["doctor", "scientist", "teacher", "lawyer"]
print("Teacher is at index", careers.index("teacher"))
print("Teacher is in the list:", "teacher" in careers)
careers.append("musician")
careers.insert(0, "athlete")
for career in careers:
    print(career)