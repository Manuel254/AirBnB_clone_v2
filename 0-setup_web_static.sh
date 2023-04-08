#!/usr/bin/env bash
# Sets up web servers for deployment of static files

sudo apt -y update
sudo apt install -y nginx
sudo service nginx start
CONF=/etc/nginx/sites-available/default

sudo mkdir -p "/data/web_static/releases/test"
sudo mkdir -p "/data/web_static/shared"

sudo touch "/data/web_static/releases/test/index.html"

if [ ! -s "$html" ]
then
cat > "$html" << EOF
  <html>
    <head>
    </head>
    <body>
      Holberton School
    </body>
  </html>
EOF
fi

ln -sf "/data/web_static/releases/test/" "/data/web_static/current"

sudo chown -R ubuntu:ubuntu "/data/"

if ! grep -q "location /hbnb_static {" $CONF
then
        sudo sed -i '/server_name _;/a\\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current\/;\n\t}\n' $CONF
fi
sudo service nginx restart
