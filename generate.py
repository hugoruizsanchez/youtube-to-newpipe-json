# The purpose of the program is to import a plain text file (copy and paste from the YouTube subscriptions feed),
# with some channels starting with "@". We need to collect the names of these channels along with their corresponding
# URLs and export them in a JSON file with the Newpipe format.

# Dependencies

import json

# Import file

f = open('subscriptions.txt', 'r')

subscriptions_content = f.readlines()

# Export format
# Each channel should have the format: {service_id:"", url:"", name:""}
export = {
    "app_version": "0.19.8",
    "app_version_int": 953,
    "subscriptions": []
}

# Keywords for scraping

keywords = ["© 2024 Google LLC YouTube, a Google company", "Subscribed"]

# Function that finds keywords in a string

def has_keyword(block, keywords):
    for word in keywords:
        if word in block:
            return True
    return False

# Scraping the file and inserting the information into channels.

buffer = 0

for block in subscriptions_content:
    if block != "\n":
        if buffer == 2:
            index_channel = {"service_id": 0}
            index_channel["name"] = block.replace("\n", "")
            buffer = buffer - 1
        elif buffer == 1:
            if "@" in block:
                index_channel["url"] = "https://youtube.com/" + block.split("•")[0]
                export["subscriptions"].append(index_channel)
            buffer = buffer - 1

        if has_keyword(block, keywords):
            buffer = 2

# Convert the file to JSON and export it.

print(export)

with open("result.json", "w") as outfile:
    json.dump(export, outfile)
