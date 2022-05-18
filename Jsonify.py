import json
from os import makedirs, path,mkdir
"""This file turns a dictionary into json"""

def create_directories(directory_path):
    # check for valid directory
    if directory_path:
        if not path.exists(directory_path):
            try:
                makedirs(directory_path)
            except Exception as e:
                print(
                    f"Something went wrong creating the directory{directory_path}")
                print(f"Error: {e}")
        if directory_path[-1] != '/':
            directory_path += '/'
    
    return directory_path


def dict_to_json(post: dict) -> json:
    """
        Input:
            post: dict
        Return
            json object

        Convert dictionary to json string
    """
    json_object = json.dumps(post, indent=4)
    return json_object


def write_to_json_file(post: dict, directory_path: str = "") -> None:
    """
        Input:
            post: dictionary
            directory_path: str
        Return
            json object

        Convert dictionary to json and writes it to a file
    """
    #add directory path to dictionary for future use
    post = add_filepath_to_json(post,directory_path)

    # check for valid directory and create if needed
    post_directory_path = create_directories(directory_path)

    filename = post_directory_path  + post["post_name"].replace(" ", "_") + ".json"
    with open(filename, 'w') as outfile:
        json.dump(post, outfile)

    print(f"Dumped json into: {filename}")


def add_filepath_to_json(json_file, directory_path) -> json:
    new_json_file = json_file
    new_json_file["filepath"]= f'{directory_path}'


    return new_json_file

