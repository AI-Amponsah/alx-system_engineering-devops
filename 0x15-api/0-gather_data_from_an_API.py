#!/usr/bin/python3
import requests
from sys import argv

"""Python script that, using this REST API"""
if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    employee_id = int(argv[1])
    employee_endp = "{}/users/{}".format(base_url, employee_id)
    name = requests.get(employee_endp).json().get("name")
    task_endp = "{}/todos".format(base_url)
    tasks = requests.get(task_endp).json()
    user_tasks = [task for task in tasks if task.get("userId") == employee_id]
    tasks_completed = [task for task in user_tasks if task.get("completed")]
    print("Employee {} is done with tasks({}/{}):".format(name,
          len(tasks_completed), len(user_tasks)))

    for task in tasks_completed:
        print("\t {}".format(task.get("title")))
