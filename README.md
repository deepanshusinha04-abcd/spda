# University Student Performance Analytics Dashboard

A VS Code-ready Flask + HTML/CSS/JavaScript interactive dashboard for the Data Analytics course.

## Features

- Interactive Department, Semester, Gender and Performance filters
- KPI cards
- Average GPA by Department bar chart
- Attendance vs Final Exam scatter chart
- Study Hours vs GPA scatter chart
- Academic metrics bar chart
- At-risk student table
- Data-driven improvement recommendations
- CSV-based data source that can later be replaced by a Kaggle dataset

## Run in VS Code

1. Open this folder in VS Code.
2. Open the VS Code terminal.
3. Create a virtual environment:

   Windows:
   `python -m venv venv`

4. Activate it:

   PowerShell:
   `venv\Scripts\Activate.ps1`

   Command Prompt:
   `venv\Scripts\activate`

5. Install packages:

   `pip install -r requirements.txt`

6. Start:

   `python app.py`

7. Open the local URL shown in the terminal, normally:
   `http://127.0.0.1:5000`

## Replace with Kaggle data

After selecting a suitable Kaggle dataset, replace `data/students.csv` and update the column names in `static/script.js` if necessary.

## Important

The included dataset is DEMO data, not real student data. Do not present it as measured university data.
