# Enter your code here. Read input from STDIN. Print output to STDOUT


num_students, num_subjects = map(int, input().split())


student_scores = []


for _ in range(num_subjects):
    
    subject_marks = list(map(float, input().split()))

    
    student_scores.append(subject_marks)


transposed_scores = zip(*student_scores)

# Iterate through each student's marks
for student_marks in transposed_scores:
    # Calculate the average score for the current student
    average_score = sum(student_marks) / num_subjects

    # Print the average score with one decimal place
    print("{:.1f}".format(average_score))
