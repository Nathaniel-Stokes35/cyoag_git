import subprocess
import sys

def install_package(package):
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
    except subprocess.CalledProcessError:
        print(f"Error installing {package}. Please try installing manually.")

def check_and_install_package():
    try:
        # Attempt to import Pillow
        import PIL
    except ImportError:
        # Install if not present
        print("Pillow is not installed. Installing now...")
        install_package('Pillow==11.0.0')

def run_game():
    # Determine the operating system
    if sys.platform.startswith('linux'):
        # Linux: Use gnome-terminal (or adjust for your preferred terminal emulator)
        subprocess.run(['gnome-terminal', '--geometry=300x50', '--', 'bash', '-c', 'python3 cyoag.py; exec bash'])
    elif sys.platform.startswith('win'):
        # Windows: Open Command Prompt, set window size, and run the Python script
        subprocess.run('mode con: cols=300 lines=50', shell=True)  # Set terminal window size
        subprocess.run(['start', 'cmd', '/k', 'python cyoag.py'], shell=True)
    else:
        print("Unsupported platform.")

if __name__ == "__main__":
    check_and_install_package()
    run_game()