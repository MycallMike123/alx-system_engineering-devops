#!/usr/bin/python3
"""Module: employee_todo.py
Fetches and displays TODO list progress for a given employee
ID using a REST API
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
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = "{}/users/{}".format(base_url, employee_id)
    todos_url = "{}/todos?userId={}".format(base_url, employee_id)

    # Fetch user information
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Fetch TODO list for the employee
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Calculate progress
    total_tasks = len(todos_data)
    completed_tasks = sum(task.get("completed", False) for task in todos_data)

    # Display progress
    print("Employee {} is done with tasks ({}/{}):".format(
        employee_name, completed_tasks, total_tasks), end='\n')

    # Display titles of completed tasks
    for task in todos_data:
        if task.get('completed', False):
            print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    # Extract employee ID from command-line arguments
    employee_id = int(sys.argv[1])
    fetch_todo_progress(employee_id)
