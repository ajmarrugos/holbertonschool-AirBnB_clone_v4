#!/usr/bin/env bash
# Bash scrip to setup the web server for the deployment of web_static
# Deployment process: Stage 0

# Updates, upgrades on board packages and installs Nginx
sudo apt update -y
sudo apt upgrade -y
sudo apt install -y nginx 

# Create the folders
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# Create a fake HTML file
sudo echo "Holberton" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link
sudo ln -fs /data/web_static/releases/test/ /data/web_static/current

# Give ownership to directory
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to server
sudo sed -i '/listen 80 default_server;/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-available/default
sudo service nginx restart
