import json

def read_json(filepath: str):
    with open(filepath, "r") as file:
        content = json.load(file)
    return content

def write_results(timestamp, results, filepath: str):
    existing_results = {}
    try:
        with open(filepath, "r") as existingfile:
            existing_results = json.load(existingfile)
    except FileNotFoundError:
        pass
    
    new_results = results
    existing_results[f"Scan Results ({timestamp})"] = new_results

    with open(filepath, "w") as resultfile:
        json.dump(existing_results, resultfile, indent=4)
    

def write_server(server, filepath: str):
    existing_servers = []
    servers = []
    try:
        existing_servers = read_json(filepath)
    except FileNotFoundError:
        pass
    
    if not existing_servers:
        servers.append(server)
        with open(filepath, "w") as f:
            json.dump(servers, f, indent=4)
    else:
        existing_servers.append(server)

        with open(filepath, "w") as serverfile:
            json.dump(existing_servers, serverfile, indent=4)

def write_servers(servers, filepath: str):
    with open(filepath, "w") as serverfile:
        json.dump(servers, serverfile, indent=4)
