from ping3 import ping
import requests

def check_server(server: str) -> bool:
    response = ping(server)
    if response is not None:
        return True
    else:
        return False

def check_webserver(server: str) -> bool:
    url = f'http://{server}'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return True
    except requests.exceptions.ConnectionError:
        return False

def main():
    server = input("IP or hostname: ")
    response = check_server(server)
    if response:
        print(f"Server ({server}) is online")
    else:
        print(f"Server ({server}) is offline")

if __name__ == "__main__":
    main()
