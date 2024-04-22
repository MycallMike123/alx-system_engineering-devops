#!/usr/bin/python3

"""Script to retrieve and display TODO list progress for a given employee
using a REST API.

Requirements:
- Use urllib or requests module
- Accept an integer as a parameter (employee ID)
- Display progress information in the specified format
- Export data in JSON format
"""

import json
import requests
import sys


def fetch_todo_progress(employee_id):
    """ Fetches and displays TODO list progress for a given employee

    Args:
    - employee_id (int): ID of the employee to retrieve TODO list for.

    Returns:
    - None
    """

    # JSONPlaceholder API base URL
    api_url = 'https://jsonplaceholder.typicode.com/'

    # Construct URLs for user
    user_url = '{}users/{}'.format(api_url, employee_id)
    todos_url = '{}todos?userId={}'.format(api_url, employee_id)

    # Fetch user information
    user_response = requests.get(user_url)
    user_data = user_response.json()

    username = user_data.get('username')

    # Fetch TODO list for the employee
    todos_response = requests.get(todos_url)
    tasks_data = todos_response.json()

    # display titles of completed tasks
    tasks_list = []
    for task in tasks_data:
        dict_task = {
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        }
        tasks_list.append(dict_task)

    # Create a dictionary with the employee's tasks
    employee_tasks = {str(employee_id): tasks_list}

    # Export data to JSON file
    filename = '{}.json'.format(employee_id)
    with open(filename, mode='w') as json_file:
        json.dump(employee_tasks, json_file)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    # Extract employee ID from command-line arguments
    employee_id = sys.argv[1]

    fetch_todo_progress(employee_id)
