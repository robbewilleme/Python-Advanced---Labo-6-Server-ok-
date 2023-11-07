import json

def read_servers(filepath: str):
    with open(filepath, "r") as serverfile:
        servers = json.load(serverfile)
    return servers

def write_results(results, filepath: str):
    with open(filepath, "w") as resultfile:
        json.dump(results, resultfile, indent=4)