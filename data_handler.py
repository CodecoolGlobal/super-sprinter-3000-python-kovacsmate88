import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story():
    with open(DATA_FILE_PATH, newline='') as user_stories:
        user_stories = list(csv.DictReader(user_stories))
    return user_stories


def add_user_story(user_story: dict):
    with open(DATA_FILE_PATH, 'a', newline='') as user_stories:
        writer = csv.DictWriter(user_stories, DATA_HEADER)
        writer.writerow(user_story)


def update_user_story(stories):
    with open(DATA_FILE_PATH, 'w', newline='') as u_stories:
        writer = csv.DictWriter(u_stories, DATA_HEADER)
        writer.writeheader()
        writer.writerows(stories)



def generate_id():
    user_stories = get_all_user_story()
    id = max([int(user_story['id']) for user_story in user_stories]) + 1
    return len(get_all_user_story()) + 1
