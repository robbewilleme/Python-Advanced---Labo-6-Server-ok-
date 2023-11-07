from datetime import datetime
from checker import check_server
from jsonhandler import read_servers, write_results
import sys

def check():
    print("program started in check mode")
    print("checking server...")
    results = []
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    servers = read_servers("servers.json")
    for server in servers["servers"]:
        name = server["name"]
        ip = server["ip"]
        print(f"Pinging {name} at IP address: {ip}")
        try:
            pingresult = check_server(ip)
            results.append({"name": name, "pingresult": pingresult})
        except:
            pass
    return timestamp, results

def manage():
    print("program started in management mode")

def main():
    if len(sys.argv) < 2:
        mode = input("Typ 'check' om het programma in check modus te starten, typ 'manage' om het programma in management modus te starten: " )
        if mode == "check":
            results = check()
            write_results(results, "results.json")
        elif mode == "manage":
            manage()


        # print("Program started in interactive mode, input options:")
        # print(" \"check\": check mode")
        # print(" \"add\": add servers")
        # print(" \"delete\": delete servers")
        # print(" \"list\": list servers")

        # if check_server("192.168.80.45"):
        #     print("server online")
        # else:
        #     print("server offline")
    else:
        print(sys.argv[1])


if __name__ == "__main__":
    main()
