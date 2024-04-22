#!/usr/bin/python3

"""
Module: employee_todo.py
Fetches and displays TODO list progress for a given
employee ID using a REST API.
"""

import requests
import sys


def fetch_todo_progress(employee_id):
    """
    Function: fetch_todo_progress
    Fetches TODO list progress for a given employee ID.
    Parameters:
        - employee_id: Integer, employee ID
    Returns: None
    """

    # URL of the API endpoint
    response = requests.get(user_url)
    data = response.json()
    employee_name = data.get('name')

    # Fetch TODO list for the employee
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Display progress
    print("Employee {} is done with tasks ({}/{}):".format(
        employee_name, completed_tasks, total_tasks), end='\n')

    # Display titles of completed tasks
    for task in todos_data:
        if task.get('completed', False):
            print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 employee_todo.py <employee_id>")
        sys.exit(1)
    employee_id = int(sys.argv[1])
    fetch_todo_progress(employee_id)
