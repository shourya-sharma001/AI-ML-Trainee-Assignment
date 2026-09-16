import requests
import matplotlib.pyplot as plt


def fetch_scores(url="http://127.0.0.1:5000/scores"):
    # this needs mock_scores_api.py running in another terminal first
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.ConnectionError:
        print("Couldn't connect to the mock API.")
        print("Start it first in another terminal: python mock_scores_api.py")
        return []
    except requests.exceptions.RequestException as e:
        print("Request to the mock API failed:", e)
        return []


def plot_scores(students):
    if not students:
        print("No score data to plot.")
        return

    names = [s["name"] for s in students]
    scores = [s["score"] for s in students]

    avg_score = sum(scores) / len(scores)
    print("Average Score:", avg_score)

    plt.figure(figsize=(10, 6))
    plt.bar(names, scores, color='skyblue')
    plt.xlabel("Student Name")
    plt.ylabel("Score")
    plt.title("Student Test Scores")
    plt.xticks(rotation=30)
    plt.axhline(y=avg_score, color='red', linestyle='--', label=f'Average: {avg_score:.1f}')
    plt.legend()
    plt.tight_layout()

    plt.savefig("scores_chart.png")
    print("Saved chart as scores_chart.png")
    plt.show()


def main():
    students = fetch_scores()
    plot_scores(students)


if __name__ == "__main__":
    main()