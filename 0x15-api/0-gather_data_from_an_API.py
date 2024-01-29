#!/usr/bin/python3
"""
Gather fake data from an API testing mock site
https://jsonplaceholder.typicode.com
Gets the completed tasks list for userId

Usage:
    ./0-gather_data_from_an_API.py <userId>
Output:
    Employee <EMPLOYEE_NAME> is done with
    tasks(<NUMBER_OF_DONE_TASKS>/<TOTAL_NUMBER_OF_TASKS>):
    /t <List of completed tasks>
"""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    completed = [t.get("title") for t in todos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    [print("\t {}".format(c)) for c in completed]
