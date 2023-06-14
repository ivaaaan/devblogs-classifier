import json

# Open file for reading
with open('other.txt', 'r') as f:
    lines = f.readlines()

# Transform lines into a list of dictionaries
data = [{"title": line.strip(), "category": "other"} for line in lines]

# Write data to JSON file
with open('other.json', 'w') as f:
    json.dump(data, f)
