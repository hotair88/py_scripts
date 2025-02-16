from dotenv import load_dotenv
import os
import subprocess
import time

load_dotenv()
os.startfile(os.getenv("SHEET_PATH"))

firefox_path = os.getenv("FIREFOX_PATH")


urls = [
    os.getenv("URL1"),
    os.getenv("URL2"),
    os.getenv("URL3"),
]

# Open a new window and the first URL
subprocess.Popen([firefox_path, "-new-window", urls[0]])

time.sleep(1)

for url in urls[1:]:
    subprocess.Popen([firefox_path, "-new-tab", url])