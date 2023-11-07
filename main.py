from datetime import datetime
from checker import check_server
from jsonhandler import read_json, write_results
from manageservers import add_server, list_all_servers, delete_server
from report import generate_html_report
import sys

def check():
    print("program started in check mode")
    print("checking server...")
    results = []
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    servers = read_json("servers.json")
    for server in servers:
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
    print("program started in management mode, options:")
    print(" \"add\": add servers")
    print(" \"delete\": delete servers")
    print(" \"list\": list servers")
    while True:
        command = input("type one of the command above: ")
        if command == "add":
            print("add server")
            name = input("name: ")
            ip = input("ip: ")
            add_server(name, ip)
        elif command == "delete":
            print("delete server")
            del_name = input("geef de naam van de server die je wilt verwijderen: ")
            delete_server(del_name)
        elif command == "list":
            print("list servers")
            print(list_all_servers())

def main():
    if len(sys.argv) < 2:
        mode = input("Typ 'check' om het programma in check modus te starten, typ 'manage' om het programma in management modus te starten: " )
        if mode == "check":
            timestamp, results = check()
            write_results(timestamp, results, "results.json")
            generate_html_report("report_template.html")
        elif mode == "manage":
            manage()
    else:
        if sys.argv[1] == "check":
            timestamp, results = check()
            write_results(timestamp, results, "results.json")
            generate_html_report("report_template.html")
        elif sys.argv[1] == "manage":
            manage()
        else:
            print("Invalid argument. Use 'check' or 'manage' as arguments.")



if __name__ == "__main__":
    main()
