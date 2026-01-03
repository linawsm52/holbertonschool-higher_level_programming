#!/usr/bin/python3
"""
Task 2: Consuming and processing data from an API using Python
"""

import csv
import requests


URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """Fetch posts from JSONPlaceholder and print status code + titles."""
    try:
        response = requests.get(URL, timeout=10)
    except requests.RequestException:
        print("Status Code: 0")
        return

    print(f"Status Code: {response.status_code}")

    if response.status_code != 200:
        return

    posts = response.json()
    for post in posts:
        print(post.get("title", ""))


def fetch_and_save_posts():
    """Fetch posts and save selected fields (id, title, body) to posts.csv."""
    try:
        response = requests.get(URL, timeout=10)
    except requests.RequestException:
        return

    if response.status_code != 200:
        return

    posts = response.json()

    data = []
    for post in posts:
        data.append({
            "id": post.get("id"),
            "title": post.get("title"),
            "body": post.get("body"),
        })

    with open("posts.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
        writer.writeheader()
        writer.writerows(data)

