scores = [2, 5, 7, 9, 3, 5, 8, 4, 6]

# Remove duplicates and sort the scores in descending order
unique_scores = sorted(set(scores), reverse=True)

# Check if there is a runner-up score
if len(unique_scores) > 1:
    runner_up_score = unique_scores[1]
    print("The runner-up score is:", runner_up_score)
else:
    print("There is no runner-up score.")

print(unique_scores)