import os
import sys
from pathlib import Path

Base_url = "http://192.168.1.106:8000"
LoginAPI = f"{Base_url}/api/login_view/"
ScreenShotApi = f"{Base_url}/tracking/screenshot/"
ConfigurationApi = f"{Base_url}/configuration/software_configuration/"
MouseDurationApi = f'{Base_url}/tracking/user_mouse_tracking/'
AppVersionUrl = f'{Base_url}/configuration/app_version/'
LogsUrl = f'{Base_url}/tracking/restartlogs/'
# LogsUrl = f'{Base_url}/tracking/create_log/'

BASE_DIR = Path(__file__).resolve().parent

MEDIA_URL = '/media/'

quantumbot_folder = r'/home/tipl-qb/Desktop/Quantumbot'

if not os.path.exists(quantumbot_folder):
    os.makedirs(quantumbot_folder)

LOG_FOLDER = r'/home/tipl-qb/Desktop/Quantumbot/Log'
ORIGINAL_FILE_PATH = r'/home/tipl-qb/Desktop/Quantumbot/Quantumbot.exe'

TASKLOGPATH = '/home/tipl-qb/Desktop/Quantumbot/taskmanager.log'

CONFIG_FILE = r'/home/tipl-qb/Desktop/Quantumbot/config.ini'
CONFIG_FILE_PATH = r'/home/tipl-qb/Desktop/Quantumbot'

if getattr(sys, 'frozen', False):  # Check if the application is running as a PyInstaller bundle
    MEDIA_ROOT = os.path.join(sys._MEIPASS, 'media')
    print(MEDIA_ROOT)
else:
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    print(MEDIA_ROOT)


def is_dark_theme(app):
    palette = app.palette()
    window_color = palette.color(palette.ColorRole.Window)
    brightness = window_color.red() * 0.299 + window_color.green() * 0.587 + window_color.blue() * 0.114
    return brightness < 128
