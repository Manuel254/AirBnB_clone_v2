#!/usr/bin/env bash
# Sets up web servers for deployment of static files

sudo apt -y update
sudo apt install -y nginx
sudo service nginx start
dir1=/data/
dir2=/data/web_static/
dir3=/data/web_static/releases/
dir4=/data/web_static/shared/
dir5=/data/web_static/releases/test/
html="$dir5""index.html"
symlink="$dir2""current"
CONF=/etc/nginx/sites-available/default

for dir in "$dir1" "$dir2" "$dir3" "$dir4" "$dir5"
do
        if [ ! -d "$dir" ]
        then
                sudo mkdir "$dir"
        fi
done

sudo touch "$html"

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

ln -sf "$dir5" "$symlink"

sudo chown -R ubuntu:ubuntu "/data/"

if ! grep -q "location /hbnb_static {" $CONF
then
        sudo sed -i '/server_name _;/a\\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current\/;\n\t}\n' $CONF
fi
sudo service nginx restart
