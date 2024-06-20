import os
import json


def add_titles_and_filter(obj, parent_key=None):
    if isinstance(obj, dict):
        new_dict = {}
        required_found = False
        for key, value in obj.items():
            if required_found:
                # Skip any key that comes after "required"
                continue
            if key == "required":
                required_found = True
                # You can include "required" in the new_dict if you don't want to remove it entirely
                new_dict[key] = value
            elif key == "type" and parent_key:
                # Insert "title" after "type"
                new_dict[key] = value
                formatted_title = parent_key.replace("_", " ").capitalize()
                new_dict["title"] = formatted_title
            else:
                new_dict[key] = add_titles_and_filter(value, key)
        return new_dict
    elif isinstance(obj, list):
        return [add_titles_and_filter(item, parent_key) for item in obj]
    else:
        return obj


# Example JSON
json_data = {
    "insert your data":"here"
}
transformed_data = add_titles_and_filter(json_data)


directory = "C:\\jsonCleaner"
if not os.path.exists(directory):
    os.makedirs(directory)

with open(os.path.join(directory, "temp.txt"), "w") as file:
    json.dump(transformed_data, file, indent=2)
with open("temp.txt", "w") as file:
    json.dump(transformed_data, file, indent=2)

print(f"Transformed data has `been written to temp.txt")
