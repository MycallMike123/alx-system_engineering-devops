#!/usr/bin/python3

""" Script to retrieve and display TODO list progress for a given employee
using a REST API.

Requirements:
- Use urllib or requests module
- Accept an integer as a parameter (employee ID)
- Display progress information in the specified format
- Export data in CSV format
"""

import csv
import requests
import sys


def fetch_todo_progress(employee_id):
    """ Fetches and displays TODO list progress for a given employee.

    Args:
    - employee_id (int): ID of the employee to retrieve TODO list for.

    Returns:
    - None
    """

    # The JSONPlaceholder API base URL
    api_url = 'https://jsonplaceholder.typicode.com/'

    # Construct URLs for the user
    user_url = '{}users/{}'.format(api_url, employee_id)
    todos_url = '{}todos?userId={}'.format(api_url, employee_id)

    # Fetch user information
    user_response = requests.get(user_url)
    user_data = user_response.json()

    username = user_data.get('username')

    # Fetch tasks for the employee
    todos_response = requests.get(todos_url)
    tasks_data = todos_response.json()

    # Create a list of tasks with relevant information
    tasks_list = []
    for task in tasks_data:
        tasks_list.append(
            [employee_id, username, task.get('completed'), task.get('title')])

    # Create a CSV file
    filename = '{}.csv'.format(employee_id)
    with open(filename, mode='w') as employee_file:
        employee_writer = csv.writer(
            employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

        # Write the task data
        for task in tasks_list:
            employee_writer.writerow(task)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    # Extract employee ID from command-line arguments
    employee_id = sys.argv[1]
    fetch_todo_progress(employee_id)
