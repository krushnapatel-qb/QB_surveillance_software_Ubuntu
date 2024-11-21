#!/bin/bash

SERVICE_NAME="qb.service"
SERVICE_PATH="/etc/systemd/system/$SERVICE_NAME"
SOURCE_PATH="/home/tipl-qb/Desktop/SS_21Nov/$SERVICE_NAME"

#DESKTOP_FILE_NAME="qb.desktop"
#DESKTOP_SOURCE_PATH="/home/tipl-qb/Desktop/SS_21Nov/$DESKTOP_FILE_NAME"
#DESKTOP_INSTALL_PATH="$HOME/.local/share/applications/$DESKTOP_FILE_NAME"

if [ "$EUID" -ne 0 ]; then
  echo "This script must be run as root. Use sudo."
  exit 1
fi

if [ -f "$SOURCE_PATH" ]; then
  echo "Copying $SERVICE_NAME to $SERVICE_PATH..."
  cp "$SOURCE_PATH" "$SERVICE_PATH"
else
  echo "Service file $SOURCE_PATH not found."
  exit 1
fi

chmod 644 "$SERVICE_PATH"
echo "Permissions set to 644 for $SERVICE_NAME."

systemctl enable "$SERVICE_NAME"
echo "$SERVICE_NAME enabled to start on boot."

systemctl start "$SERVICE_NAME"
echo "Service installation complete."

systemctl daemon-reload
echo "systemd daemon reloaded."

#if [ -f "$DESKTOP_SOURCE_PATH" ]; then
#  echo "Copying $DESKTOP_FILE_NAME to $DESKTOP_INSTALL_PATH..."
#  cp "$DESKTOP_SOURCE_PATH" "$DESKTOP_INSTALL_PATH"
#  chmod +x "$DESKTOP_INSTALL_PATH"
#  echo "Permissions set to executable for $DESKTOP_FILE_NAME."
#else
#  echo ".desktop file $DESKTOP_SOURCE_PATH not found."
#  exit 1
#fi
#chmod 644 "$DESKTOP_FILE_PATH"

#/opt/qb_files/qb &
#echo "Application started immediately."