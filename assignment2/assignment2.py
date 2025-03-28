# Task 2
import csv
import traceback

def read_employees():
    employees_data = {"fields" : [], "rows" : []}

    try:
        with open("../csv/employees.csv", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader):
                if index == 0:
                    employees_data["fields"] = row
                else:
                    employees_data["rows"].append(row)

        return employees_data
    
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = [f'File: {trace[0]}, Line: {trace[1]}, Func: {trace[2]}, Message: {trace[3]}'
            for trace in trace_back
        ]

        print(f"An exception occurred: {type(e).__name__}")
        print(f"Exception message: {str(e)}")
        print(f"Stack trace: {stack_trace}")
        return None 
    
employees = read_employees()

print(employees)

# Task 3

def column_index(column_name):
    try:
        return employees["fields"].index(column_name)
    except ValueError:
        print(f"Column '{column_name}' not found.")
        return None
    
employee_id_column = column_index("employee_id")
print(f"Index of 'employee_id': {employee_id_column}")

# Task 4

def first_name(row_number):
    first_name_col = column_index("first_name")
    if first_name_col is not None:
        return employees['rows'][row_number][first_name_col]
    else:
        return None
    
print(first_name(0))

# Task 5

def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    matches = list(filter(employee_match, employees["rows"]))
    return matches

print(employee_find())

# Task 6

def employee_find2(employee_id):
    matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))
    return matches


#Task 7

def sort_by_last_name():

    last_name_col = column_index("last name")
    employees['rows'].sort(key=lambda row: row[last_name_column])
    return employees['rows']

sort_by_last_name()
print(employees)

#Task 8

def employee_dict(row):
    headers = employees['fields']
    employee_id_column = column_index('employee_id')

    employee_data = {key: value for key, value in zip(headers, row) if key != "employee_id"}

    return employee_data

#Task 9

def all_employees_dict():
    employee_id_column = column_index('employee_id')

    employees_dict = {row[employee_id_column]: employee_dict(row) for row in employees["rows"]}

    return employees_dict

#task 10

import os

def get_this_value():
    return os.getenv('THISVALUE')

#Task 11

import custom_module

def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

set_that_secret("MySuperSecret")
print(custom_module.secret)

#Task 12

def read_minutes():

    files = ["../csv/minutes1.csv", "../csv/minutes2.csv"]
    minutes_dicts = {
        f"minutes{i+1}": {"fields": None, "rows": []}
        for i in range(len(files))
    }
    try:
        for i, file_path in enumerate(files):
            with open(file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                fields = next(reader)
                rows = [tuple(row) for row in reader]
                minutes_dicts[f'minutes{i+1}'] = {'fields': fields, 'rows':rows}

    except Exception as e: 
        print(f'An error occurred: {e}')
    
    return minutes_dicts['minutes1'], minutes_dicts['minutes2']

minutes1, minutes2 = read_minutes()

# Task 13

def create_minutes_set():

    set1 = set(minutes1['rows'])
    set2 = set(minutes2['rows'])


    return set1.union(set2)

minutes_set = create_minutes_set()

#Task 14

from datetime import datetime

def create_minutes_list():
    minutes_list = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_set))
    return minutes_list

minutes_list = create_minutes_list()

#Task 15

def write_sorted_list():
    global minutes_list

    minutes_list.sort(key=lambda x: x[1])
    formatted_list = list(map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), minutes_list))

    with open("./minutes.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(minutes1['fields'])
        writer.writerows(formatted_list)

    return formatted_list

sorted_minutes = write_sorted_list()

