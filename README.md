# Python-Advanced Opdracht 6 - Server Management and Monitoring Tool

This Python script is a server management and monitoring tool designed to help you check the status of servers, add new servers, delete existing servers, and generate a report of the server check results. It offers both command-line and interactive modes for user interaction.

## Prerequisites

Before using this tool, make sure you have the requirements installed in a virtual environment:

- `pip install requirements.txt`

## Usage

### Interactive Mode

You can run the script without any command-line arguments to enter interactive mode. In this mode, you will be prompted to choose between "check" and "manage" modes.

- **Check Mode**:
  - This mode allows you to check the status of servers listed in a JSON configuration file.
  - The results are displayed in a tabular format and saved to a JSON file.
  - A report is generated in HTML format based on the results.

- **Manage Mode**:
  - This mode allows you to perform server management actions:
    - **add**: Add a new server to the configuration.
    - **delete**: Delete an existing server from the configuration.
    - **list**: List all servers in the configuration.

### Command-Line Mode

You can also use the script in command-line mode by providing specific arguments:

- `python main.py check`:
  - Performs a server check, saves the results to a JSON file, and generates an HTML report.

- `python main.py add server_name ip_address`:
  - Adds a new server to the configuration with the given name and IP address.

- `python main.py delete server_name`:
  - Deletes the server with the specified name from the configuration.

- `python main.py list`:
  - Lists all servers in the configuration.


