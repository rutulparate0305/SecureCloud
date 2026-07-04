from datetime import datetime 
LOG_FILE = "logs/activity.log"

def log_activity(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE,"a") as file:
        file.write(f"{timestamp} - {message}\n")