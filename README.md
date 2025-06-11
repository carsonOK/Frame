# 🔷 Frame 

Frame is a lightweight Windows app that automatically takes a screenshot every 30 seconds — like Microsoft Recall, but without all the heavy requirements or complicated setup.

## Features

- Automatically captures your screen every 30 seconds  
- Runs silently in the background with minimal resource use  
- Simple, no-frills design focused on ease of use  
- No heavy dependencies or complex permissions needed  
- Ideal for productivity tracking, troubleshooting, or quick screen logging

## Installation

### 1. Install Python

- Download and install the latest Python from [python.org](https://www.python.org/downloads/).  
- **Important:** During installation, check **Add Python to PATH** before clicking **Install Now**.

### 2. Download Frame

- Go to the [Releases](https://github.com/carsonOK/Frame/releases) tab.  
- Download the latest `.zip` file and unzip it anywhere you want.

### 3. Install dependencies

- Open **Command Prompt** and navigate to the unzipped Frame folder, e.g.:  `cd C:\Users\admin\downloads\Frame`, and run the following command: `pip install Pillow pystray pywin32 requests`.

### 4. Run frame!
- Open another **Command Prompt** window in the directory you downloaded Frame and run `python.exe Frame.py`! Frame should start taking screenshots every 30 seconds and saving them to the /screenshots folder.

## Usage

- Once running, Frame works quietly in the background.  
- Screenshots are saved in the default `Screenshots` folder.
- To stop capturing, simply exit the app from the system tray.

## Coming Soon

- Customizable screenshot intervals  
- Option to start minimized or on system startup  
- More user-friendly GUI and animations  

## Contributing

Contributions and feedback are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License.
