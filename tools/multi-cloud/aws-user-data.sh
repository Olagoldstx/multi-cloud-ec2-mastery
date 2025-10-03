#!/bin/bash
# User data script for AWS EC2 instance
apt-get update
apt-get install -y nginx
systemctl start nginx
systemctl enable nginx
echo "<h1>Hello from AWS EC2!</h1>" > /var/www/html/index.html
