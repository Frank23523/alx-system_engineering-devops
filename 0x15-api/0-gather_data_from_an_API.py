#!/usr/bin/python3
""" Gather data from an API """

import requests
import sys


if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"

    employee_id = sys.argv[1]
    user = requests.get(api_url + "users/{}".format(employee_id)).json()

    parameters = {"userId": employee_id}
    todos = requests.get(api_url + "todos", parameters).json()

    completed_tasks = [todo for todo in todos if todo["completed"]]
    total_tasks = len(todos)
    completed_count = len(completed_tasks)
    employee_name = todos[0]["userId"]

    print(f"Employee {employee_name} is done with tasks"
          "({completed_count}/{total_tasks}):")

    for task in completed_tasks:
        print("\t {}".format(task['title']))
