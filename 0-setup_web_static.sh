#!/usr/bin/env bash
# Sets up web servers for deployment of static files

sudo apt -y update
sudo apt install -y nginx
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
sudo chown -R ubuntu:ubuntu "/data/"

if [ ! -s "$html" ]
then
        echo -e "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html" > "$html"
fi

if [ -e "$symlink" ]
then
        sudo rm "$symlink"
fi
ln -s "$dir5" "$symlink"

if ! grep -q "location /hbnb_static {" $CONF
then
        sudo sed -i '/server_name _;/a\\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current\/;\n\t}\n' $CONF
fi
sudo nginx -s reload
