#!/bin/bash

echo "Installing dependencies..."
sudo apt update
sudo apt install -y python3 python3-pip git

echo "Installing Python packages..."
pip3 install flask schedule openai requests

echo "Creating systemd service..."
sudo cp systemd/sentiment-bot.service /etc/systemd/system/
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl enable sentiment-bot
sudo systemctl start sentiment-bot

echo "Installation complete. Access the dashboard via http://<your-pi-ip>:5000"
