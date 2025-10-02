# Simple Python Keylogger

A simple keylogger script written in Python for educational purposes. It demonstrates how to listen to keyboard events and log them to a file.

## Disclaimer

This script is intended for educational purposes only. Do not use it on any computer without the owner's explicit permission. Misuse of this software is illegal and unethical.

## Features

* Logs keystrokes to `keylog.txt`.
* Formats special keys (Space, Enter) for readability.
* Writes logs in batches to improve performance.
* Adds a startup timestamp to the log file.
* Stops execution when the `ESC` key is pressed.

## Usage

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/AhmetGultekin0/simple-keylogger.git](https://github.com/AhmetGultekin0/simple-keylogger.git)
    ```

2.  **Navigate to the directory:**
    ```bash
    cd simple-keylogger
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the script:**
    You may need to run this script with administrator/sudo privileges for it to work correctly.
    ```bash
    python keylogger.py
    ```

5.  **Stop the script:**
    To stop the logger, click on another window (not the terminal) and press the `ESC` key.
