from ping3 import ping


def check_server(server: str) -> bool:
    response = ping(server)
    if response:
        return True
    else:
        return False
