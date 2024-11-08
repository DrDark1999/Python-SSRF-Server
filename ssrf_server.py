import logging
from flask import Flask, request
from discord_webhook import DiscordWebhook

# Flask App for SSRF Server
app = Flask(__name__)

# Discord Webhook configuration
webhook_url = "DISCORD_WEBHOOK_URL"  # Provided Discord webhook URL

import os
import logging

# Get the HOME directory dynamically
home_dir = os.getenv("HOME")

# Define the log file path
log_file = os.path.join(home_dir, ".ssrf-server", "ssrf-server.log")

# Create the directory if it doesn't exist
os.makedirs(os.path.dirname(log_file), exist_ok=True)

# Log configuration
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(message)s')


class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=["GET", "POST"])
def log_request(path):
    try:
        # Log incoming request details to the log file
        log_message = f"Received request: {request.method} {request.url}\nHeaders: {request.headers}\nBody: {request.data.decode()}\n"
        print(log_message)  # Print to console for interactive mode
        logging.info(log_message)  # Save to log file

        # Send notification to Discord if it's not a DNS request
        if 'dns' not in path.lower():
            webhook = DiscordWebhook(url=webhook_url, content=f"SSRF Hit Alert: {request.method} {request.url}\nBody: {request.data.decode()}\n")
            webhook.execute()

        # HTML response
        html_response = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>SSRF Test Server</title>
            <style>
                body { font-family: Arial, sans-serif; text-align: center; color: #333; }
                .message { margin-top: 20%; color: #4CAF50; }
            </style>
        </head>
        <body>
            <div class="message">
                <h1>SSRF Test Server</h1>
                <p>from Bhargav Hede (<a href="https://bhargavhede.in" target="_blank">bhargavhede.in</a>)</p>
            </div>
        </body>
        </html>
        """
        return html_response, 200
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        return "Internal Server Error", 500

if __name__ == "__main__":
    # Run the Flask app
    app.run(host="public_ip", port=open_port)
