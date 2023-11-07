from jsonhandler import write_server, read_servers, write_servers


def add_server(name: str, ip: str):
    server = {"name": name, "ip": ip}
    write_server(server, "servers.json")

def list_all_servers():
    return read_servers("servers.json")

def delete_server(name: str):
    servers = read_servers("servers.json")
    for server in servers:
        if server["name"] == name:
            servers.remove(server)
    
    write_servers(servers, "servers.json")
    