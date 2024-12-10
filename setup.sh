import subprocess
import sys
import os

def run_game():
    # Determine the operating system
    if sys.platform.startswith('linux'):
        # Linux: Use gnome-terminal (or adjust for your preferred terminal emulator)
        subprocess.run(['gnome-terminal', '--', 'bash', '-c', 'python3 cyoag.py; exec bash'])
    elif sys.platform.startswith('win'):
        # Windows: Open Command Prompt and run the Python script
        subprocess.run(['start', 'cmd', '/k', 'python cyoag.py'], shell=True)
    else:
        print("Unsupported platform.")

if __name__ == "__main__":
    run_game()