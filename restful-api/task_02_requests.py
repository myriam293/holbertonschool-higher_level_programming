#!/usr/bin/python3
"""Module for fetching and processing posts using requests"""
import requests
import csv

url = 'https://jsonplaceholder.typicode.com/posts'


def fetch_and_print_posts():
    """Fetch posts and print status code and titles"""

    response = requests.get(url)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get("title"))
    else:
        print("Request was not successful.")


def fetch_and_save_posts():
    """Fetch posts and save to CSV with id, title, body"""

    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
        filename = 'posts.csv'

        with open(filename, 'w', encoding='UTF-8') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()

            for post in posts:
                writer.writerow({
                    'id': post.get('id'),
                    'title': post.get('title'),
                    'body': post.get('body')
                })
    else:
        print("Request was not successful.")
