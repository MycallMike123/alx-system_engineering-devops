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
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    try:
        # Fetch data from the API
        response = requests.get(url)
        data = response.json()

        # Extract employee name
        employee_name = data[0]['name'].split()[0]

        # Calculate progress
        total_tasks = len(data)
        done_tasks = sum(1 for task in data if task['completed'])

        # Display progress
        status = 'OK' if done_tasks == total_tasks
        print(f"Employee {employee_name}: {status}")
        for task in data:
            if task['completed']:
                print(f"\t{task['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 employee_todo.py <employee_id>")
        sys.exit(1)
    employee_id = int(sys.argv[1])
    fetch_todo_progress(employee_id)
