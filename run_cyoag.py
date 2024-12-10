import subprocess
import sys
import os
import requests

# Create a flag file to prevent recursive installs
INSTALL_FLAG_FILE = "installing_flag.txt"
REPO_URL = 'https://github.com/Nathaniel-Stokes35/cyoag_git.git'  # GitHub repository URL
LOCAL_REPO_DIR = 'cyoag_git'  # Local directory to clone the repo

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
        with open(os.path.join('cyoag_git', 'requirements.txt'), 'r') as f:
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
    except Exception as e:
        print(f"Error while checking/installing dependencies: {e}")
    finally:
        # Remove the flag file after installation is complete
        if os.path.exists(INSTALL_FLAG_FILE):
            os.remove(INSTALL_FLAG_FILE)
        run_game()

def is_git_installed():
    """Check if Git is installed by running 'git --version'."""
    try:
        subprocess.check_call(['git', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except FileNotFoundError:
        print("Git is not installed or not available in PATH.")
        return False
    except subprocess.CalledProcessError:
        print("Git is installed but encountered an error.")
        return False

def clone_repository():
    """Clone the repository from GitHub if it isn't already cloned."""
    if not is_git_installed():
        print("Git is not installed. Please install Git to continue. You can get it from https://git-scm.com/download.")

    if not os.path.exists(LOCAL_REPO_DIR):
        print(f"Repository not found locally. Cloning from GitHub...")
        try:
            subprocess.check_call(['git', 'clone', REPO_URL])
            print(f"Repository cloned successfully to {LOCAL_REPO_DIR}.")
        except subprocess.CalledProcessError as e:
            print(f"Error cloning repository: {e}")
    else:
        print(f"Repository already exists locally at {LOCAL_REPO_DIR}.")

def run_game():
    """Launch the game based on the operating system."""
    if sys.platform.startswith('linux'):
        # Linux: Try using gnome-terminal or fallback to xterm if gnome-terminal isn't found
        try:
            subprocess.run(['gnome-terminal', '--geometry=300x50', '--', 'python3', {os.path.join('cyoag_git', 'cyoag.py')}])
        except FileNotFoundError:
            print("gnome-terminal not found, trying xterm.")
            subprocess.run(['xterm', '-geometry', '300x50', '-e', f'python3 {os.path.join('cyoag_git', 'cyoag.py')}'])
    elif sys.platform.startswith('win'):
        # Windows: Open Command Prompt, set window size, and run the Python script
        subprocess.run('mode con: cols=300 lines=50', shell=True)  # Set terminal window size
        subprocess.run(['start', 'cmd', '/k', f'python {os.path.join('cyoag_git', 'cyoag.py')}'], shell=True)
    else:
        print("Unsupported platform.")

def check_and_download_file():
    """Check if cyoag.py exists locally, and if not, download it."""
    if not os.path.exists('cyoag.py'):
        print(f"cyoag.py not found. Downloading from GitHub...")
        try:
            response = requests.get('https://raw.githubusercontent.com/Nathaniel-Stokes35/cyoag_git/main/cyoag.py')
            response.raise_for_status()  # Check if the request was successful
            with open('cyoag.py', 'wb') as file:
                file.write(response.content)
            print(f"cyoag.py successfully downloaded from GitHub.")
        except requests.exceptions.RequestException as e:
            print(f"Failed to download file: {e}")
    else:
        print("cyoag.py already exists locally.")

if __name__ == "__main__":
    # First, Clone the repository from GitHub if needed
    clone_repository()

    # Next, install dependancies
    install_requirements()  # Install missing packages from requirements.txt  

    # Check and download cyoag.py if missing
    check_and_download_file()