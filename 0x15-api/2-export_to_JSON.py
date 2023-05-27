#!/usr/bin/python3
"""Exports to-do list data for an employee to JSON format"""

import json
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get("{}users/{}".format(url, employee_id)).json()
    tasks = requests.get("{}users/{}/todos".format(url, employee_id)).json()
    data_dict = {
                employee_id: [{"task": task.get("title"),
                           "completed": task.get("completed"),
                           "username": user.get("username")} for task in tasks]
            }
    # open a new JSON file in write mode
    with open("{}.json".format(employee_id), "w", newline="") as file:
        json.dump(data_dict, file)
