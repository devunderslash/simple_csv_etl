import csv
import os
from datetime import datetime


def get_user_input():
    print("Please enter the pathway to the folder containing the csv files you would like to deduplicate.")
    print("Example: /Users/username/Documents/csv_files")
    folder_path = input()
    os.chdir(folder_path)

    print("Please enter the main name of the output file.")
    print("Example: charlie_bell")
    main_name = input()

    return main_name


def combine_csv_files():
    header_saved = False
    with open('combine.csv', 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        for filename in os.listdir('.'):
            if filename.endswith('.csv'):
                with open(filename, 'r') as readfile:
                    reader = csv.reader(readfile)
                    try:
                        header = next(reader)
                        if not header_saved:
                            writer.writerow(header)
                            header_saved = True
                        writer.writerows(reader)
                    except StopIteration:
                        continue

def remove_duplicates():
    rows = set()
    with open('combine.csv', 'r') as infile, open('combine_without_dups.csv', 'w') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        for row in reader:
            row_tuple = tuple(row)
            if row_tuple not in rows:
                writer.writerow(row)
                rows.add(row_tuple)

def update_currentAmt():
    with open('combine_without_dups.csv', 'r') as infile, open('temp.csv', 'w') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        headers = next(reader)
        writer.writerow(headers)
        currentAmt_index = headers.index('CurrentAmt')
        for row in reader:
            if row[currentAmt_index] in {'0', '00.00', '0.00'}:
                row[currentAmt_index] = '0.01'
            writer.writerow(row)

def rename_file(file_name):
    today = datetime.now().strftime("%Y-%m-%d")
    new_file_name = f"{file_name}_{today}.csv"
    os.rename('combine_without_dups.csv', new_file_name)

def main():
    new_file_name = get_user_input()
    combine_csv_files()
    remove_duplicates()
    update_currentAmt()
    os.remove('combine_without_dups.csv')
    os.rename('temp.csv', 'combine_without_dups.csv')
    rename_file(new_file_name)

if __name__ == "__main__":
    main()
