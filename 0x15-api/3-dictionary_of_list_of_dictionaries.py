#!/usr/bin/python3
""" Dictionary of list of dictionaries """

import json
import requests

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"

    users = requests.get(api_url + "users").json()
    todos = requests.get(api_url + "todos").json()

    # Prepare the data in the required format
    data = {}
    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        user_tasks = [
            {
                "username": username,
                "task": todo.get("title"),
                "completed": todo.get("completed")
            }
            for todo in todos if todo.get("userId") == user_id
        ]
        data[user_id] = user_tasks

    # Write to JSON file
    json_filename = "todo_all_employees.json"
    with open(json_filename, 'w') as json_file:
        json.dump(data, json_file)
