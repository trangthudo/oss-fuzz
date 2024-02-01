import os
import csv
import shutil

# Function to read the first column values from csv file
def read_csv_file(file_path):
    values = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header row
        for row in csv_reader:
            values.append(row[0])
    return values

# Function to extract string after last "/"
def extract_name(url):
    return url.split('/')[-1].lower()

# Function to create dictionary from csv values
def create_dictionary(csv_values):
    dictionary = {}
    for value in csv_values:
        name = extract_name(value)
        dictionary[name] = 1
    return dictionary

# Function to match and delete folders in projects directory
def delete_unmatched_folders(projects_dir, dictionary, log_file):
    with open(log_file, 'a') as log:
        for folder in os.listdir(projects_dir):
            folder_path = os.path.join(projects_dir, folder)
            if os.path.isdir(folder_path):
                if folder.lower() not in dictionary:
                    shutil.rmtree(folder_path)
                    log.write(f"Deleted folder: {folder_path}\n")
                else:
                    log.write(f"Folder '{folder}' matched, keeping it.\n")
            else:
                log.write(f"Skipping file: {folder_path}\n")

def main():
    # Path to csv file
    csv_file_path = "cpp.csv"

    # Path to projects directory
    projects_dir = "projects"

    # Log file path
    log_file = "log.txt"

    # Read values from csv file
    csv_values = read_csv_file(csv_file_path)

    # Create dictionary from csv values
    dictionary = create_dictionary(csv_values)

    # Delete unmatched folders in projects directory and log the actions
    delete_unmatched_folders(projects_dir, dictionary, log_file)

if __name__ == "__main__":
    main()
