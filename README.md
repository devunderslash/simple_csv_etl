# CSV Extract Transform Load

## Description
This project is a simple ETL pipeline that reads a collective csv files from a directory, extracts the data, transforms it, and loads it into a new CSV file.

## Installation
1. Clone the repository - `git clone https://github.com/devunderslash/simple_csv_etl.git`
2. Create a virtual environment - `python3 -m venv venv`
3. Activate the virtual environment - `source venv/bin/activate`
4. Install the dependencies if there are any (currently not) - `pip install -r requirements.txt`

## Usage
1. Run the script - `python3 deduplicate_csv.py`
2. You will be prompted to enter the path to the directory containing the csv files and a name for the output file.
3. The script will then read the csv files, extract the data, transform it, and load it into a new CSV file.
