#!/bin/bash
# Custom script for Azure VM
apt-get update
apt-get install -y nginx
systemctl start nginx
systemctl enable nginx
echo "<h1>Hello from Azure VM!</h1>" > /var/www/html/index.html
