import csv
from datetime import datetime

def log_to_csv(data, filename="telemetry_log.csv"):
    try:
        with open(filename, "r"):
            file_exists = True
    except FileNotFoundError:
        file_exists = False

    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["timestamp"] + list(data.keys()))

        writer.writerow([datetime.now().isoformat()] + list(data.values()))
