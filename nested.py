score_list = {}

# Input the total number of students
total_students = int(input("Enter the total number of students:\n>> "))

# Input names and scores for each student
for x in range(total_students):
    name = input(f"Enter the name of student {x + 1}:\n>> ")
    score = float(input(f"Enter the score of student {x + 1}:\n>> "))

    if score in score_list:
        score_list[score].append(name)
    else:
        score_list[score] = [name]

# Sort the scores and names
sorted_scores = sorted(score_list.keys())
second_lowest_score = sorted_scores[1]

# Get the names of students with the second lowest score
result = score_list[second_lowest_score]
result.sort()

# Print the names
print("\n".join(result))