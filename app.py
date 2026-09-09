from flask import Flask, render_template, jsonify
import pandas as pd
from pathlib import Path

app = Flask(__name__)
DATA_FILE = Path("data/students.csv")

def load_data():
    df = pd.read_csv(DATA_FILE)
    return df

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/students")
def students():
    df = load_data()
    return jsonify(df.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)
