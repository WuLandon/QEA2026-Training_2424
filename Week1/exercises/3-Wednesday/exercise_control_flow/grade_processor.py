scores = [88, 92, 75, -1, 63, 95, 81, 70, -5, 55, 100, 78, -999, 90, 85]

valid_scores = []
grade_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

print("Student Grades:")

for index, score in enumerate(scores):
    # Stop processing if sentinel value is found
    if score == -999:
        print("\nSentinel value encountered. Stopping processing.")
        break

    # Skip invalid negative scores
    if score < 0:
        continue

    # Assign letter grade
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    print(f"Student {index}: Score = {score}, Grade = {grade}")

    valid_scores.append(score)
    grade_counts[grade] += 1

# Summary statistics
if valid_scores:
    average = sum(valid_scores) / len(valid_scores)
    highest = max(valid_scores)
    lowest = min(valid_scores)

    print("\nClass Summary")
    print("-" * 30)
    print(f"Average Score: {average:.2f}")
    print(f"Highest Score: {highest}")
    print(f"Lowest Score: {lowest}")

    print("\nGrade Distribution:")
    for grade in ["A", "B", "C", "D", "F"]:
        print(f"{grade}: {grade_counts[grade]}")
else:
    print("No valid scores found.")
