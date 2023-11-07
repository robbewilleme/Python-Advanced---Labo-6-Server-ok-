import json

def read_servers(filepath: str):
    with open(filepath, "r") as serverfile:
        servers = json.load(serverfile)
    return servers

def write_results(results, filepath: str):
    existing_results = {}
    try:
        with open(filepath, "r") as existingfile:
            existing_results = json.load(existingfile)
    except FileNotFoundError:
        pass
    
    timestamp, new_results = results
    existing_results[f"pingresults_{timestamp}"] = new_results

    with open(filepath, "w") as resultfile:
        json.dump(existing_results, resultfile, indent=4)