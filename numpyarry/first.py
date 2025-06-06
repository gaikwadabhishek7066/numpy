import numpy as np

# Sample students and marks in [Math, Science, English]
students = np.array(["Alice", "Bob", "Charlie", "David"])
marks = np.array([
    [85, 78, 92],  # Alice
    [72, 88, 80],  # Bob
    [90, 95, 94],  # Charlie
    [65, 70, 60]   # David
])

# Calculations
total = np.sum(marks, axis=1)
average = np.mean(marks, axis=1)
highest = np.max(marks, axis=0)
lowest = np.min(marks, axis=0)
top_scorer_index = np.argmax(total)

# Report
print("\n📋 Student Report")
for i in range(len(students)):
    print(f"{students[i]} - Total: {total[i]}, Avg: {average[i]:.2f}")

print("\n📈 Subject-wise Stats:")
subjects = ["Math", "Science", "English"]
for i in range(3):
    print(f"{subjects[i]} - Highest: {highest[i]}, Lowest: {lowest[i]}")

print(f"\n🏆 Top Scorer: {students[top_scorer_index]} with {total[top_scorer_index]} marks")
