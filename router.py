import os.path
from logging.handlers import TimedRotatingFileHandler
from threading import Event

from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QStackedWidget
from PyQt6 import QtGui
import configparser
from settings import MEDIA_ROOT, CONFIG_FILE, LOG_FOLDER
from views.kafka_thread import StartKafkaThread
from views.login import LoginPage
from views.dashboard import DashboardPage
from views.mouse_tracking import MouseTrackingThread
from views.screenshot import ScreenshotThread

import logging as logging

from evdev import InputDevice, categorize, ecodes, list_devices

class Router(QStackedWidget):
    valueChanged = pyqtSignal(object)

    def __init__(self):
        super().__init__()

        # Create the stop event for the screenshot thread
        self.stop_event = Event()

        try:
            config = configparser.ConfigParser()
            config_file_path = CONFIG_FILE
            config.read(f'{config_file_path}')
            if 'surveillance' in config and config['surveillance'].get('is_surveillance_active'):
                self.consumer = {
                    'is_surveillance_active': config.getboolean('surveillance', 'is_surveillance_active')
                }
                print(self.consumer)
            else:
                self.consumer = {
                    'is_surveillance_active': True
                }
        except:
            self.consumer = {
                'is_surveillance_active': True
            }

        # Initialize the screenshot thread but do not start it yet
        self.screenshot_thread = None
        self.mouse_tracking_thread = None
        self.kafka_thread = None
        # Create instances of the pages
        self.setWindowIcon(QtGui.QIcon(f"{MEDIA_ROOT}/icon/admin.png"))
        self.setWindowTitle('QB')
        self.resize(397, 434)
        self.setFixedSize(397, 434)

        self.logger = None
        self.logger_setup()
        self.login_page = LoginPage(self.consumer, self.logger)
        self.dashboard_page = None

        # Add login page to the stacked widget
        self.addWidget(self.login_page)

        # Assign router to login page for navigation
        # self.login_page.consumer = self.consumer
        self.login_page.router = self

        # Load configuration and decide the initial page
        self.load_initial_page()


    def load_initial_page(self):
        config = configparser.ConfigParser()
        config_file_path = f'{CONFIG_FILE}'
        if os.path.exists(config_file_path):
            config.read(f'{CONFIG_FILE}')
        else:
            self.navigate_to(page_name='login')

        # Check if user data exists in config.ini
        if 'info' in config and config['info'].get('token'):
            # Start the screenshot thread only if the token exists
            self.start_screenshot_thread()
            self.start_mouse_tracking_thread()
            self.start_qb_kafka()
            # Create the dashboard page only after the thread is started
            self.dashboard_page = DashboardPage(self.consumer, self.screenshot_thread)
            self.addWidget(self.dashboard_page)
            self.dashboard_page.consumer = self.consumer

            # Show the dashboard
            first_name = config['info'].get('first_name')
            # last_name = config['info'].get('last_name')
            self.dashboard_page.update_welcome_message(f'{first_name}')
            self.setCurrentWidget(self.dashboard_page)
        else:
            # Show the login page if no user data is found
            self.setCurrentWidget(self.login_page)
            print('Login Page here')

    def logger_setup(self):
        log_folder = LOG_FOLDER
        if not os.path.exists(log_folder):
            os.makedirs(log_folder)
        log_file = os.path.join(log_folder, 'error.log')

        log_handler = TimedRotatingFileHandler(log_file, when="midnight", interval=1, backupCount=30)
        log_handler.setLevel(logging.DEBUG)
        log_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.logger.addHandler(log_handler)

        # logging.getLogger('kafka').setLevel(logging.CRITICAL)

        kafka_loggers = ['kafka', 'kafka.conn', 'kafka.consumer', 'kafka.producer', 'kafka.admin']

        for kafka_logger in kafka_loggers:
            logging.getLogger(kafka_logger).setLevel(logging.CRITICAL)
            logging.getLogger(kafka_logger).propagate = False

    def start_screenshot_thread(self):
        # Only start the screenshot thread if it hasn't been started yet
        if self.screenshot_thread is None or not self.screenshot_thread.is_alive():
            self.stop_event.clear()
            self.screenshot_thread = ScreenshotThread(self.stop_event, self.consumer, self.logger)
            self.screenshot_thread.start()
            self.screenshot_thread.router = self

    def start_mouse_tracking_thread(self):
        if self.mouse_tracking_thread is None or not self.mouse_tracking_thread.is_alive():
            self.stop_event.clear()
            self.mouse_tracking_thread = MouseTrackingThread(self.stop_event, self.consumer, self.logger)
            # self.mouse_tracking_thread = MouseTrackingThread(self.stop_event, self.consumer)
            self.mouse_tracking_thread.start()
            self.mouse_tracking_thread.router = self

    def start_qb_kafka(self):
        if self.kafka_thread is None or not self.kafka_thread.is_alive():
            self.kafka_thread = StartKafkaThread(self.consumer)
            self.kafka_thread.start()

    def navigate_to(self, page_name):
        if page_name == 'dashboard':
            self.start_screenshot_thread()
            self.start_mouse_tracking_thread()
            self.dashboard_page = DashboardPage(self.consumer, self.screenshot_thread)
            self.addWidget(self.dashboard_page)
            self.setCurrentWidget(self.dashboard_page)
            self.start_qb_kafka()

        elif page_name == 'login':
            self.setCurrentWidget(self.login_page)
