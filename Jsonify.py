import json
"""This file turns a dictionary into json"""

def dict_to_json(self, post: dict) -> json:
    """
        Input: 
            post: dict
        Return 
            json object

        Convert dictionary to json string
    """
    json_object = json.dumps(post, indent=4)
    return json_object

def write_to_json_file(self, post: dict, directory_path: str = "") -> None:
    """
        Input: 
            post: dictionary
            directory_path: str
        Return 
            json object

        Convert dictionary to json and writes it to a file
    """

    #check for valid directory
    if directory_path:
        if not path.exists(directory_path):
            try:
                mkdir(directory_path)
            except:
                print(f"Something went wrong creating the directory{directory_path}")
        if directory_path[-1] != '/':
            directory_path += '/'


    filename = directory_path + post["title"].replace(" ", "_")[0:45] + ".json"
    with open(filename, 'w') as outfile:
        json.dump(post, outfile)

    print(f"Dumped json into: {filename}")