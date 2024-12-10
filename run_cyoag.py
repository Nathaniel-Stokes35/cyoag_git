import subprocess
import sys
import os

# Create a flag file to prevent recursive installs
INSTALL_FLAG_FILE = "installing_flag.txt"

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
            subprocess.run(['gnome-terminal', '--geometry=300x50', '--', 'python3', 'cyoag.py'])
        except FileNotFoundError:
            print("gnome-terminal not found, trying xterm.")
            subprocess.run(['xterm', '-geometry', '300x50', '-e', 'python3 cyoag.py'])
    elif sys.platform.startswith('win'):
        # Windows: Open Command Prompt, set window size, and run the Python script
        subprocess.run('mode con: cols=300 lines=50', shell=True)  # Set terminal window size
        subprocess.run(['start', 'cmd', '/k', 'python cyoag.py'], shell=True)
    else:
        print("Unsupported platform.")

if __name__ == "__main__":
    install_requirements()  # Install missing packages from requirements.txt
    run_game()  # Launch the game