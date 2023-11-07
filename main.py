from datetime import datetime
from checker import check_server, check_webserver
from jsonhandler import read_json, write_results
from manageservers import add_server, list_all_servers, delete_server
from report import generate_html_report
import sys
from rich.console import Console
from rich.table import Table

console = Console()
def check():
    console.print("program started in check mode", style="bold blue")
    console.print("checking server...", style="bold blue")
    
    results = []
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    servers = read_json("servers.json")
    
    table = Table(title="Server Check Results")
    table.add_column("Server Name", style="bold")
    table.add_column("IP Address")
    table.add_column("Ping Result")
    table.add_column("Web Server Status")
    
    for server in servers:
        name = server["name"]
        ip = server["ip"]
        console.print(f"Checking {name} at IP address: {ip}", style="bold")
        
        try:
            pingresult = check_server(ip)
            webserver = check_webserver(ip)
            results.append({"name": name, "pingresult": pingresult, "webserver": webserver})
            
            table.add_row(name, ip, str(pingresult), str(webserver))
        except Exception as e:
            console.print(f"Error checking {name}: {e}", style="red")
    
    console.print(table)
    return timestamp, results


def manage():
    console = Console()

    console.print("program started in management mode, options:", style="bold blue")
    console.print(" [bold]add[/bold]: add servers")
    console.print(" [bold]delete[/bold]: delete servers")
    console.print(" [bold]list[/bold]: list servers")

    while True:
        command = input("type one of the commands above: ")
        if command == "add":
            console.print("add server", style="bold blue")
            name = input("name: ")
            ip = input("ip: ")
            add_server(name, ip)
        elif command == "delete":
            console.print("delete server", style="bold blue")
            del_name = input("geef de naam van de server die je wilt verwijderen: ")
            delete_server(del_name)
        elif command == "list":
            console.print("list servers", style="bold blue")
            server_list = list_all_servers()
            if server_list:
                for server in server_list:
                    console.print(server, style="bold green")
            else:
                console.print("No servers found.", style="bold red")

def main():
    if len(sys.argv) < 2:
        mode = input("Typ 'check' om het programma in check modus te starten, typ 'manage' om het programma in management modus te starten: " )
        if mode == "check":
            timestamp, results = check()
            write_results(timestamp, results, "results.json")
            console.print("generating report...", style="bold blue")
            generate_html_report("report_template.html")
            console.print("report.html succesfully generated", style="bold")
        elif mode == "manage":
            manage()
    else:
        if sys.argv[1] == "check":
            timestamp, results = check()
            write_results(timestamp, results, "results.json")
            console.print("generating report...", style="bold blue")
            generate_html_report("report_template.html")
            console.print("report.html succesfully generated", style="bold green")
        elif sys.argv[1] == "manage":
            manage()
        else:
            print("Invalid argument. Use 'check' or 'manage' as arguments.")



if __name__ == "__main__":
    main()
