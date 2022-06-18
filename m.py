import requests
from bs4 import BeautifulSoup
import json

with open("data.json", "w") as f:
    json.dump([], f)

# function to add to JSON


def write_json(new_data, filename='data.json'):
    with open(filename, 'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data.append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent=4)


# Make a request to https://annapurnapost.com
r = requests.get(
    "https://annapurnapost.com/news/workers-do-not-even-get-to-work-206572")
soup = BeautifulSoup(r.content, 'html.parser')

# Extract title of page
r = soup.body.text

# print the result
print(r)

write_json({
    "r": r,
})
