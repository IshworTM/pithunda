scores = map(int, input("Enter a list:\n>> ").split())
unique_scores = list(scores)
print(f'Before sorting\n-> {unique_scores}')
unique_scores.sort(reverse= True)
print(f'After sorting\n-> {unique_scores}')

if len(unique_scores) >= 1:
    print(f"The runner-up score is {unique_scores[1]}.")  # The second element is the runner-up
else:
    print("Error 698: Scores can't be less than 1.")
