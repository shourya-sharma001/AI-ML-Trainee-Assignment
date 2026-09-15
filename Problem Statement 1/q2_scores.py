import requests
import matplotlib.pyplot as plt

# fetching data from our local Flask API instead of hardcoding it
response = requests.get("http://127.0.0.1:5000/scores")
students = response.json()

scores = []
for student in students:
    scores.append(student["score"])

# calculate the average
avg_score = sum(scores) / len(scores)
print("Average Score:", avg_score)

names = []
for student in students:
    names.append(student["name"])

# make the bar chart
plt.figure(figsize=(10, 6))
plt.bar(names, scores, color='skyblue')
plt.xlabel("Student Name")
plt.ylabel("Score")
plt.title("Student Test Scores")
plt.xticks(rotation=30)
plt.axhline(y=avg_score, color='red', linestyle='--', label=f'Average: {avg_score:.1f}')
plt.legend()
plt.tight_layout()
plt.show()