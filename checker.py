from ping3 import ping


def check_server(server: str) -> bool:
    response = ping(server)
    if response:
        return True
    else:
        return False

def main():
    server = input("Ip or hostname: ")
    response = check_server(server)
    if response:
        print(f"Server({server}) is online")
    else:
        print(f"Server({server}) is offline")

if __name__ == "__main__":
    main()