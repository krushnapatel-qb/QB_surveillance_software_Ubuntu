# # from pynput import keyboard
# #
# # def on_press(key):
# #     try:
# #         print('alphanumeric key {0} pressed'.format(key.char))
# #     except AttributeError:
# #         print('special key {0} pressed'.format(key))
# #
# # def on_release(key):
# #     print('{0} released'.format(key))
# #     if key == keyboard.Key.esc:
# #         # Stop listener
# #         return False
# #
# # # Collect events until released
# # with keyboard.Listener(
# #         on_press=on_press,
# #         on_release=on_release) as listener:
# #     listener.join()
#
#
#
# # import evdev
# # from evdev import InputDevice, categorize, ecodes
# #
# # # List all input devices to find the correct keyboard device
# # devices = [InputDevice(path) for path in evdev.list_devices()]
# # for device in devices:
# #     print(device.path, device.name, device.phys)
# #
# # # Select the correct device (for example, /dev/input/event2 might be your keyboard)
# # keyboard = InputDevice('/dev/input/event2')
# #
# # # Read keypress events from the keyboard
# # for event in keyboard.read_loop():
# #     if event.type == ecodes.EV_KEY:
# #         key_event = categorize(event)
# #         print(key_event)
# #         if key_event.keystate == key_event.key_down:
# #             print(f"Key {key_event.keycode} pressed")
#
#
# # import subprocess
# # import time
# # time.sleep(5)
# # process_name='systemd'
# # # callall='TASKLIST'
# # callall = ['ps', '-A']
# # outputall=subprocess.check_output(callall)
# # outputstringall=str(outputall)
# # # print(outputstringall)
# # if process_name in outputstringall:
# #     print("Locked.")
# # else:
# #     print("Unlocked.")
#
# # import dbus
# # sessionBus = dbus.SessionBus()
# # screenSaver = sessionBus.get_object("org.gnome.ScreenSaver", "/org/gnome/ScreenSaver")
# # screenSaverIface = dbus.Interface(screenSaver, 'org.gnome.ScreenSaver')
# # screenSaverSetActive = screenSaverIface.get_dbus_method("SetActive")
# # screenSaverSetActive(False)
#
# import os
# # import subprocess
# #
# # subprocess.Popen(['loginctl unlock-session 2'],shell=True) #2 is my session id
#
# import subprocess
# import time
# def is_screen_locked():
#     try:
#         # Execute the command to check the screensaver status
#         output = subprocess.check_output(['gnome-screensaver-command', '-q']).decode('utf-8')
#         # Check if the output contains 'active' indicating the screen is locked
#         return 'inactive' in output
#     except subprocess.CalledProcessError as e:
#         print(f"Error checking screen lock status: {e}")
#         return False
#
# if __name__ == "__main__":
#     print(is_screen_locked())
#     for i in range(15):
#         if is_screen_locked():
#             print(i, "Screen is unlocked")
#         else:
#             print(i, "Screen is locked")
#
#         time.sleep(3)

from PIL import ImageGrab
from functools import partial

screenshot = partial(ImageGrab.grab, all_screens=True)

image = screenshot()

image.save("screenshot.png")


