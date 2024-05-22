#!/usr/bin/python3
""" Gather data from an API and export to CSV """

import csv
import requests
import sys


if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"

    employee_id = sys.argv[1]
    user = requests.get(api_url + "users/{}".format(employee_id)).json()
    username = user.get("username")

    parameters = {"userId": employee_id}
    todos = requests.get(api_url + "todos", parameters).json()

    csv_filename = "{}.csv".format(employee_id)

    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([employee_id, username,
                             todo["completed"], todo["title"]])
