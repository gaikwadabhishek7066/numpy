import numpy as np

marks = np.array([
    [85, 92, 78],
    [88, 76, 90],
    [90, 91, 89],
    [70, 60, 65],
    [95, 100, 98]
])

# 2. Calculate total and average marks per student
total_per_stud = np.sum(marks,axis=1)
avg_per_stud = np.mean(marks,axis=1)

# 3. Find the top scorer
top_scorer_index = np.argmax(total_per_stud)
top_scorer_marks = marks[top_scorer_index]

# 3. Find the top scorer
avg_per_sub = np.mean(marks,axis=0)

# Output results
for i, (total,avg) in enumerate(zip(total_per_stud,avg_per_stud)):
    print(f"Student {i + 1}: Total = {total},average = {avg:.2f}")

print(f"\nTop Scorer: Student {top_scorer_index + 1} with total marks = {total_per_stud[top_scorer_index]}")

print("\nAverage marks per subject:")
subjects = ['Subject 1', 'Subject 2', 'Subject 3']
for i, avg in enumerate(avg_per_sub):
    print(f"{subjects[i]}: {avg:.2f}")