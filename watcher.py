import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import subprocess
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

class ChangeHandler(FileSystemEventHandler):
    def __init__(self, command):
        self.command = command
        self.process = subprocess.Popen(self.command, shell=True)
        logging.info(f"Started process: {self.process.pid}")

    def on_modified(self, event):
        if not event.is_directory and 'database/database.db' not in event.src_path and '__pycache__/' not in event.src_path:
            logging.info(f"File modified: {event.src_path}")
            self.restart_process()

    def restart_process(self):
        logging.info("Restarting process...")
        self.process.terminate()
        self.process.wait()  # Wait for the process to terminate
        self.process = subprocess.Popen(self.command, shell=True)
        logging.info(f"Started process: {self.process.pid}")

if __name__ == "__main__":
    path = os.getcwd()  # Loyihaning asosiy katalogini kiriting
    command = f"python3 {path}/main.py"  # Asosiy skriptingizning to'liq yo'lini kiriting

    event_handler = ChangeHandler(command)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    logging.info(f"Started monitoring {path}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
