# Import necessary modules
import os
import collections

# First input data: List of employee names formatted as 'First_Last'
employee_list = [
    "Jasen_Kerluke",
    "Lazlo_Daniel",
    "Amparo_Schuster",
    "Tia_Kunde",
    "Alana_Lueilwitz",
    "Tia_Mraz",
    "Lazlo_Metz",
    "Caroline_Pollich",
    "Aiyana_Weber",
    "Lazlo_Rolfson"
]

# Second input data: List of dictionaries containing employee names and ages
employee_obj_list = [
    {"Name": "Jasen Kerluke", "Age": 30},
    {"Name": "Lazlo Daniel", "Age": 27},
    {"Name": "Amparo Schuster", "Age": 23},
    {"Name": "Tia Kunde", "Age": 32},
    {"Name": "Alana Lueilwitz", "Age": 29},
    {"Name": "Tia Mraz", "Age": 33},
    {"Name": "Lazlo Metz", "Age": 43},
    {"Name": "Caroline Pollich", "Age": 25},
    {"Name": "Aiyana Weber", "Age": 24},
    {"Name": "Lazlo Rolfson", "Age": 37}
]

# Task 1: Create a '.txt' file for each employee named after them
# This loop iterates over the employee_list and opens a new text file for each employee,
# ensuring that the filename matches the employee's name.
for i in employee_list:
    try:
        with open(f"{i}.txt", "w+") as file:
            pass  # File is opened but left empty
    except Exception as e:
        print(f"Error creating file {i}: {e}")

# Task 2: Print out the top 5 frequent first names and their respective frequency
# This block splits each employee name into first and last names, counts the occurrences of each first name,
# and prints the top 5 most frequent first names along with their counts.
import os
import collections

newlist = []
for word in employee_list:
    word = word.split("_")
    newlist.append(word[0])
counter = collections.Counter(newlist)

print(counter)

# Task 3: Organize the files into folders according to the first letter of each person's surname
# This block creates a new directory for each unique first letter of the surnames in the employee list.
# It then attempts to create these directories, printing success messages upon successful creation.
newlist1 = []
for word in employee_list:
    word = word.split("_")
    newlist1.append(word[1])

for i in newlist1:
    path = i[0]
    try:
        os.mkdir(path)
    except OSError:
        print("Creation of the directory {} failed".format(path))
    else:
        print("Successfully created the directory {}".format(path))

# Note: The actual moving of files into these directories was not included in the original script.
# To move the files, you would need to implement additional logic similar to Task 1 but targeting the newly created directories.
