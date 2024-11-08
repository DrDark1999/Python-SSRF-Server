# Python-SSRF-Server
Your own SSRF Server
# SSRF Server

This project implements a simple SSRF (Server-Side Request Forgery) server using Flask. The server logs incoming HTTP requests and sends notifications to a Discord webhook whenever a request is made, excluding DNS requests. This can be useful for testing SSRF vulnerabilities and monitoring suspicious activities.

## Features

- Logs incoming HTTP requests (method, URL, headers, body).
- Sends a notification to a Discord webhook on each SSRF hit.
- Includes client IP address in the webhook notification.
- Stores logs in `~/.ssrf-server/ssrf-server.log`.
- Simple SSRF test page displayed for requests.

## Prerequisites

To run this SSRF server, you need to have Python 3 and the following Python libraries installed:

- `Flask` (for the web server)
- `discord-webhook` (for sending Discord notifications)

You can install these dependencies using the following command:

```bash
pip install flask discord-webhook
```
## Setup

1. Clone or download this repository to your local machine.
2. Create a directory for the log file if it doesn't exist. The log file will be stored in `~/.ssrf-server/ssrf-server.log`.
3. Replace the `webhook_url` , `public_ip` and `open_port`  in the script with your own Discord webhook URL, Public IP Address and Open Port.

## Usage

1. Open a terminal and navigate to the folder containing the `ssrf_server.py` script.
2. Run the SSRF server using the following command:

```bash
python3 ssrf_server.py
```
The server will start listening on IP `public_ip` and port `open_port`. You can change the host and port in the script if needed.

3. When an SSRF request is made to this server, the following actions will occur:
  * The request details will be logged in the file `~/.ssrf-server/ssrf-server.log`.
  * A notification will be sent to the specified Discord webhook with the request details, including the client's IP address.

## Example Discord Notification
Here is an example of what the Discord notification might look like:
```
SSRF Hit Alert: GET http://example.com/path | Client IP: 192.168.1.100
```

## The Way I'm Using It in VPS

1. **Setting Up the Tool**:  
   After setting up the SSRF server and confirming that it's working correctly, proceed to the next step.

2. **Creating an Alias and Using `nohup` for Background Execution**:  
   To ensure that the SSRF server runs continuously in the background, even after disconnecting from the VPS, use `nohup` (No Hang Up) and create an alias for easy management. 

   - Run the following command to add an alias that will start the SSRF server using `nohup` and save logs to a file:

     ```bash
     echo "alias ssrf-server='nohup python3 /path/to/ssrf_server.py > /tmp/ssrf-server.log 2>&1 &'" >> ~/.bashrc
     source ~/.bashrc
     ```

   - This will:
     - Run the SSRF server in the background using `nohup`.
     - Save both standard output and error messages to `/tmp/ssrf-server.log`.
     - The `&` ensures the process runs in the background.

   - Now you can start the SSRF server anytime by simply running:

     ```bash
     ssrf-server
     ```

3. **Viewing the SSRF Server Logs**:  
   To make it easier to view the SSRF server logs, you can create another alias to quickly display the contents of the log file.

   - Run the following command to add an alias for viewing the SSRF server logs:

     ```bash
     echo "alias ssrf-server-log='cat ~/.ssrf-server/ssrf-server.log'" >> ~/.bashrc
     source ~/.bashrc
     ```

   - This will allow you to view the logs anytime by simply running:

     ```bash
     ssrf-server-log
     ```

   - The command will display the contents of the log file where the SSRF server output is saved (`~/.ssrf-server/ssrf-server.log`).

4. **Verifying the Server**:  
   - To check the logs and verify that the server is running, use the following command:

     ```bash
     tail -f /tmp/ssrf-server.log
     ```

     This will show real-time updates from the SSRF server log.

5. **Stopping the Server**:  
   - To stop the SSRF server, find its process ID (PID) and kill it. Use the following command to find the PID:

     ```bash
     ps aux | grep ssrf-server
     ```

   - Once you have the PID, you can stop the server by running:

     ```bash
     kill <PID>
     ```

6. **Log Directory**:  
   - The log file is saved at `/tmp/ssrf-server.log` and the backup file will be saved at `~/.ssrf-server/ssrf-server.log`. If needed, you can change the log file path in the alias command to save the logs elsewhere.
