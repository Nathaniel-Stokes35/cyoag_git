import subprocess
import sys
import os
import requests

# Define constants
FILE_NAME = 'cyoag.py'  # Name of the game file
GITHUB_URL = 'https://raw.githubusercontent.com/Nathaniel-Stokes35/cyoag_git/main/cyoag.py'  # URL for the game file
REPO_URL = 'https://github.com/Nathaniel-Stokes35/cyoag_git.git'  # URL for the GitHub repository
LOCAL_REPO_DIR = 'cyoag_git'  # Directory to store the cloned repo
INSTALL_FLAG_FILE = "installing_flag.txt"  # Flag to prevent recursive installs

def download_file():
    """Download the cyoag.py file from GitHub if it's missing."""
    try:
        print(f"{FILE_NAME} not found. Downloading from GitHub...")
        response = requests.get(GITHUB_URL)
        response.raise_for_status()  # Check if the request was successful
        with open(FILE_NAME, 'wb') as file:
            file.write(response.content)
        print(f"{FILE_NAME} successfully downloaded from GitHub.")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download file: {e}")
        sys.exit(1)

def clone_repository():
    """Clone the repository from GitHub if it isn't already cloned."""
    if not os.path.exists(LOCAL_REPO_DIR):
        print(f"Repository not found locally. Cloning from GitHub...")
        try:
            subprocess.check_call(['git', 'clone', REPO_URL])
            print(f"Repository cloned successfully to {LOCAL_REPO_DIR}.")
        except subprocess.CalledProcessError as e:
            print(f"Error cloning repository: {e}")
            sys.exit(1)
    else:
        print(f"Repository already exists locally at {LOCAL_REPO_DIR}.")

def install_package(package):
    """Installs the given package using pip."""
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
    except subprocess.CalledProcessError:
        print(f"Error installing {package}. Please try installing manually.")

def install_requirements():
    """Check if all required packages in requirements.txt are installed."""
    if os.path.exists(INSTALL_FLAG_FILE):
        print("Installation already in progress. Skipping installation step.")
        return
    
    try:
        # Create a flag to indicate installation is in progress
        with open(INSTALL_FLAG_FILE, 'w') as f:
            f.write("Installation in progress...\n")

        # Read the requirements.txt file
        with open('requirements.txt', 'r') as f:
            required_packages = f.readlines()

        # Clean up any extra spaces or newlines from each package name
        required_packages = [pkg.strip() for pkg in required_packages if pkg.strip()]

        for package in required_packages:
            try:
                # Try importing the package to check if it's installed
                __import__(package.split('==')[0])  # Handle versions like 'package==version'
            except ImportError:
                # If the package is missing, install it
                print(f"{package} is not installed. Installing...")
                install_package(package)

    except FileNotFoundError:
        print("requirements.txt file not found. Please ensure it is in the same directory as the script.")
        sys.exit(1)
    except Exception as e:
        print(f"Error while checking/installing dependencies: {e}")
        sys.exit(1)
    finally:
        # Remove the flag file after installation is complete
        if os.path.exists(INSTALL_FLAG_FILE):
            os.remove(INSTALL_FLAG_FILE)

def run_game():
    """Launch the game based on the operating system."""
    if sys.platform.startswith('linux'):
        # Linux: Try using gnome-terminal or fallback to xterm if gnome-terminal isn't found
        try:
            subprocess.run(['gnome-terminal', '--geometry=300x50', '--', 'python3', FILE_NAME])
        except FileNotFoundError:
            print("gnome-terminal not found, trying xterm.")
            subprocess.run(['xterm', '-geometry=300x50', '-e', f'python3 {FILE_NAME}'])
    elif sys.platform.startswith('win'):
        # Windows: Open Command Prompt, set window size, and run the Python script
        subprocess.run('mode con: cols=300 lines=50', shell=True)  # Set terminal window size
        subprocess.run(['start', 'cmd', '/k', f'python {FILE_NAME}'], shell=True)
    else:
        print("Unsupported platform.")

def check_and_download_file():
    """Check if cyoag.py exists locally, and if not, download it."""
    # Check for the game file in the current directory (or the parent directory if you prefer)
    if not os.path.exists(FILE_NAME):
        download_file()  # Download if the file is missing
    else:
        print(f"{FILE_NAME} found locally. Proceeding with installation and execution.")

if __name__ == "__main__":
    clone_repository()         # Clone the repository if not already present
    check_and_download_file()  # Check for the file in the parent directory, and download if missing
    install_requirements()     # Install missing packages from requirements.txt
    run_game()                 # Launch the game