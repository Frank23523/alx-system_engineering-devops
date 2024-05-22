#!/usr/bin/python3
""" Gather data from an API and export to JSON """

import json
import requests
import sys


if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"

    employee_id = sys.argv[1]
    user = requests.get(api_url + "users/{}".format(employee_id)).json()
    username = user.get("username")

    parameters = {"userId": employee_id}
    todos = requests.get(api_url + "todos", parameters).json()

    # Prepare the data in the required format
    tasks = []
    for todo in todos:
        task_dict = {
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": username
        }
        tasks.append(task_dict)

    data = {employee_id: tasks}

    # Write to JSON file
    json_filename = "{}.json".format(employee_id)
    with open(json_filename, 'w') as json_file:
        json.dump(data, json_file)
