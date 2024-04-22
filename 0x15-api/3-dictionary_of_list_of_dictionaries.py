#!/usr/bin/python3
""" Script to retrieve and export TODO list progress for all employees
using a REST API.

Requirements:
- Use urllib or requests module
- Display progress information in the specified format
- Export data in JSON format
"""

import json
import requests
import sys


def fetch_todo_progress():
    """ Fetches and exports TODO list progress for all employees

    Returns:
    - None
    """
    # JSONPlaceholder API base URL
    api_url = 'https://jsonplaceholder.typicode.com/'

    # Fetch all users
    users_url = '{}users'.format(api_url)
    users_response = requests.get(users_url)
    users_data = users_response.json()

    # Dictionary to store tasks for all employees
    all_employees_tasks = {}

    # Iterate over each user to fetch TODO list
    for user in users_data:
        name = user.get('username')
        userid = user.get('id')

        # Fetch TODO list for the employee
        todos_url = '{}todos?userId={}'.format(api_url, userid)
        todos_response = requests.get(todos_url)
        tasks_data = todos_response.json()

        # List to store tasks for the current employee
        tasks_list = []

        # Prepare tasks data for the employee
        for task in tasks_data:
            dict_task = {
                "username": name,
                "task": task.get('title'),
                "completed": task.get('completed')
            }
            tasks_list.append(dict_task)

        # Add tasks data to the dictionary
        all_employees_tasks[str(userid)] = tasks_list

    # Export data to JSON file
    filename = 'todo_all_employees.json'
    with open(filename, mode='w') as json_file:
        json.dump(all_employees_tasks, json_file)


if __name__ == "__main__":
    # Call the function to get information about all employees
    fetch_todo_progress()
