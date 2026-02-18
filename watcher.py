import os
import time
import shutil

INBOX = "Inbox"
NEEDS_ACTION = "Needs_Action"

def start_watching():
    print("Atlas (AI Employee) active...")
    if not os.path.exists(INBOX):
        os.makedirs(INBOX)
    if not os.path.exists(NEEDS_ACTION):
        os.makedirs(NEEDS_ACTION)

    while True:
        files = os.listdir(INBOX)
        for filename in files:
            old_path = os.path.join(INBOX, filename)
            new_path = os.path.join(NEEDS_ACTION, filename)
            if os.path.isfile(old_path):
                print(f"Naya task mila: {filename}. Moving to Needs_Action...")
                shutil.move(old_path, new_path)
        time.sleep(2)

if __name__ == "__main__":
    start_watching()
