import os
import time
import threading
import logging
from datetime import datetime
from PIL import ImageGrab, Image
import pystray
from pystray import MenuItem as item
from PIL import ImageDraw
import win32com.client
import requests

APP_NAME = "Frame"
SCREENSHOT_INTERVAL = 30
ASSETS_DIR = os.path.join(os.getcwd(), "assets")
SCREENSHOT_DIR = os.path.join(os.getcwd(), "screenshots")
ICON_PATH = os.path.join(ASSETS_DIR, "icon.ico")
ICON_URL = "https://raw.githubusercontent.com/carsonOK/Frame/refs/heads/main/icon.ico"
STARTUP_NAME = f"{APP_NAME}.lnk"
LOG_FILE = os.path.join(os.getcwd(), f"{APP_NAME}.log")

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def log_info(msg):
    print(msg)
    logging.info(msg)

def log_error(msg):
    print("ERROR:", msg)
    logging.error(msg)

os.makedirs(SCREENSHOT_DIR, exist_ok=True)
os.makedirs(ASSETS_DIR, exist_ok=True)

def download_icon():
    if not os.path.exists(ICON_PATH):
        try:
            log_info(f"Downloading icon from {ICON_URL} ...")
            r = requests.get(ICON_URL, timeout=10)
            r.raise_for_status()
            with open(ICON_PATH, "wb") as f:
                f.write(r.content)
            log_info("Icon downloaded successfully.")
        except Exception as e:
            log_error(f"Failed to download icon: {e}")

def enable_autostart():
    try:
        startup_path = os.path.join(
            os.getenv('APPDATA'),
            'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup', STARTUP_NAME
        )
        target = os.path.realpath(__file__)
        shell = win32com.client.Dispatch("WScript.Shell")
        shortcut = shell.CreateShortCut(startup_path)
        shortcut.Targetpath = target
        shortcut.WorkingDirectory = os.getcwd()
        shortcut.IconLocation = ICON_PATH if os.path.exists(ICON_PATH) else target
        shortcut.save()
        log_info("Auto-start shortcut created.")
    except Exception as e:
        log_error(f"Failed to create auto-start shortcut: {e}")

def take_screenshot():
    log_info("Screenshot thread started.")
    while True:
        try:
            now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filepath = os.path.join(SCREENSHOT_DIR, f"screenshot_{now}.png")
            img = ImageGrab.grab()
            img.save(filepath)
            log_info(f"Saved screenshot: {filepath}")
        except Exception as e:
            log_error(f"Failed to take screenshot: {e}")
        time.sleep(SCREENSHOT_INTERVAL)

def create_default_icon():
    image = Image.new('RGB', (64, 64), color='black')
    draw = ImageDraw.Draw(image)
    draw.rectangle((10, 10, 54, 54), outline="white", width=4)
    return image

def create_tray():
    try:
        def on_quit():
            log_info("Quit clicked. Exiting.")
            icon.stop()
            os._exit(0)

        if os.path.exists(ICON_PATH):
            image = Image.open(ICON_PATH)
        else:
            image = create_default_icon()

        menu = (item('Quit', on_quit),)
        global icon
        icon = pystray.Icon(APP_NAME, image, APP_NAME, menu)
        log_info("Tray icon started.")
        icon.run()
    except Exception as e:
        log_error(f"Tray icon error: {e}")

if __name__ == "__main__":
    log_info("App started.")
    download_icon()
    enable_autostart()
    threading.Thread(target=take_screenshot, daemon=True).start()
    create_tray()
    log_info("App exited.")
