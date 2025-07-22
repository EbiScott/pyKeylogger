# pyKeylogger

This is a basic keylogger written in Python using the `pynput` library. It captures keystrokes and saves them to a log file.

## Features

*   Logs keystrokes to `logFile.txt`.
*   Writes to the log file in batches of 15 keystrokes.
*   Stops logging when the Esc key is pressed.

## Prerequisites

*   Python 3.x
*   `pynput` library

## Installation

1.  **Clone the repository (or download the script):**

```
    git clone https://github.com/EbiScott/pyKeylogger
    cd pyKeylogger
```


2.  **Install the pynput library:**

```
    pip install pynput
```


## Usage

1.  **Run the script:**

```
    python main.py
```


2.  **The keylogger will start capturing keystrokes.**  The keystrokes will be stored in the logFile.txt file in the same directory as the script.

3.  **To stop the keylogger, press the Esc key.**



## Important Considerations

*   **Legality and Ethics:** Using a keylogger without explicit consent is illegal and unethical. This tool should only be used for legitimate purposes, such as security testing or personal use on your own devices.
*   **Security:** This is a very basic keylogger and is not intended for use in high-security environments. It may be vulnerable to detection and circumvention.
*   **File Handling:** The script appends to logFile.txt. You might want to add a mechanism to clear the log file periodically or when the script starts.
*   **Key Formatting:** The current formatting of the log file is quite basic. You could improve it by adding timestamps, separating key presses with spaces or other delimiters, or using a more structured format (e.g., JSON).

## Disclaimer

This project is for educational purposes only. The author is not responsible for any misuse or damage caused by this software.  Use this responsibly and ethically.  Do not use this code to violate anyone's privacy or break the law.
