from flask import Flask, jsonify

app = Flask(__name__) #-> Create a Flask application instance

@app.route('/scores')
def get_scores():
    data = [
        {"name": "Ankit Sharma", "score": 78},
        {"name": "Shourya Sharma", "score": 88},
        {"name": "Rohan Mehta", "score": 62},
        {"name": "Kavita Joshi", "score": 91},
        {"name": "Aryan Saini", "score": 70},
        {"name": "Pooja Choudhary", "score": 84},
        {"name": "Manish Mishra", "score": 55},
        {"name": "Rohit Sharma", "score": 76},
        {"name": "Charvi Koolwal", "score": 93}
    ]
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)