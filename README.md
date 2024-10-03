# ETL Assignment

This repository contains the code and files needed to generate a report from an SQLite database using both SQL and pandas.

## Part 1: SQL Query

### Files
- `part1_sql_query.sql`: Contains the SQL query used to generate the report.

### Instructions
1. **Download and Install SQLite DB Browser**:
   - You can download it from SQLite DB Browser.
2. **Open the SQLite Database**:
   - Open SQLite DB Browser and load the `S30 ETL Assignment.db` file.
3. **Execute the SQL Query**:
   - Go to the "Execute SQL" tab.
   - Copy and paste the contents of `part1_sql_query.sql` into the query editor.
   - Click "Execute" to run the query and view the results.

## Part 2: Pandas Script

### Files
- `part2_pandas_script.py`: Contains the Python script that uses pandas to generate the report.
- `requirements.txt`: List of the Python packages needed to run the script.

### Instructions
1. **Set Up the Environment**:
   - Ensure you have Python installed. You can download it from Python.org.
2. **Create and Activate Virtual Environment**: (Optional - if you do not want to change anything with your globally installed packages)
   - Open a terminal or command prompt.
   - Navigate to the directory containing the repository files.
   - Run the following command to create Virtual Environment:
     ```bash
     python -m venv myenv
     ```
     - Run the following command to activate Virtual Environment:
     ```bash
     source myenv/Scripts/Activate
     ```
3. **Install Required Packages**:
   - Open a terminal or command prompt.
   - Navigate to the directory containing the repository files.
   - Run the following command to install the required packages:
     ```bash
     pip install -r requirements.txt
     ```
4. **Run the Script**:
   - Execute the script by running:
     ```bash
     python part2_pandas_script.py
     ```
   - This will generate the `report.csv` file with the results.

## Output
- `report.csv`: The generated report, delimited by semicolons.

## Repository Structure
my-etl-assignment/
│
├── .gitignore
├── part1_sql_query.sql
├── part2_pandas_script.py
├── README.md
├── report.csv (This will be overwritten every time you execute `part2_pandas_script.py` assuming the path indicated is the same)
├── requirements.txt
└── S30 ETL Assignment.db
