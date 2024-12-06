import platform
import subprocess
import sys

def install_dependencies():
    """Detect the OS and run the appropriate setup script to install dependencies."""
    os_type = platform.system()

    if os_type == "Linux" or os_type == "Darwin":  # Linux or macOS
        print("Detected Linux or macOS. Running setup.sh...")
        subprocess.run(["bash", "setup.sh"], check=True)
    elif os_type == "Windows":
        print("Detected Windows. Running setup.bat...")
        subprocess.run(["setup.bat"], check=True)
    else:
        print("Unsupported OS. Please manually install dependencies.")
        sys.exit(1)

def run_game():
    """Run the main game script."""
    print("Launching the game...")
    subprocess.run(["python3", "cyoag.py"], check=True)

if __name__ == "__main__":
    try:
        # Step 1: Install dependencies based on OS
        install_dependencies()
        
        # Step 2: Run the game
        run_game()
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")
        sys.exit(1)