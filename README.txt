Choose Your Own Adventure Novel Game (CYOAG)
Welcome to the Choose Your Own Adventure Game (CYOAG)! This is a Python-based interactive game where you create and explore a personalized character and journey, influenced by your responses and choices.

Features:
Cross-platform Support: Now available as standalone executables for Linux, Windows, and macOS.
Character Creation: Design your character based on the MBTI personality types and test your decisions in various story settings.
Multiple Settings: Explore different genres such as Space, Pirate, and Fantasy (currently, only the Space setting is available).
How to Play:
Download the Executable:

Choose your platform (Linux, Windows, or macOS) from the Releases section of this GitHub repository.
Download the appropriate .tar.gz, .zip, or .app file for your operating system.
Run the Executable:

Linux: Extract the .tar.gz and run the cyoag-linux executable.
Windows: Extract the .zip and run the cyoag-windows.exe file.
macOS: Extract the .tar.gz and open the .app bundle to start the game.
Enjoy the Game: Make choices that define your character's personality, starting class, and path in a space-themed adventure (more settings and features will be added in the future).

How to Run (For Developers):
If you'd like to run the game from source, follow the steps below:

Clone the repository:

bash
Copy code
git clone https://github.com/Nathaniel-Stokes35/cyoag.git
cd cyoag
Install dependencies:

Make sure you have Python 3.x installed.
Install the required dependencies by running:
bash
Copy code
pip install -r requirements.txt
Run the game:

bash
Copy code
python run_cyoag.py
Dependencies:
Pillow: For image handling.
tkinter: For the graphical user interface (GUI).
Python 3.x: Required for running the game.

Contributing:
Feel free to fork this repository, contribute improvements, or suggest new features. I plan to add more settings, classes, and options as development continues. If you’d like to contribute to the project, please open an issue or submit a pull request.

GitHub Actions:
This project uses GitHub Actions to automatically build platform-specific executables. Every time a change is pushed to the main branch, the system automatically packages the game for Linux, Windows, and macOS, which can be downloaded from the Releases section.
Contributing
This is a personal project, but if you're interested in contributing or adding new features, feel free to submit a pull request! Contributions are always welcome, and feel free to open issues for any bugs you encounter or features you think would improve the game.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
The MBTI personality system used in the game is based on the Myers-Briggs Type Indicator, a well-known personality typing system.
This project uses Python and Tkinter to create an interactive text-based adventure.
Notes:
If you have any issues with the setup or need help running the game, feel free to open an issue on the GitHub repository.
The automated setup should handle everything, but if you prefer to install dependencies manually, you can find more details in the requirements.txt file.
