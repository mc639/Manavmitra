# Manavmitra
Manavmitra is a News Based Web Application Created using  Python's Django Framework

Setting up Django :

sudo apt-get update
sudo apt-get install python-pip python-dev mysql-server libmysqlclient-dev
sudo mysql_secure_installation

mysql -u root -p
CREATE DATABASE myproject CHARACTER SET UTF8;
CREATE USER myprojectuser@localhost IDENTIFIED BY 'password';
CREATE USER wizzy@localhost IDENTIFIED BY 'mammu@19';
GRANT ALL PRIVILEGES ON myproject.* TO myprojectuser@localhost;
GRANT ALL PRIVILEGES ON manmitra.* TO wizzy@localhost;
FLUSH PRIVILEGES;
exit


Import Database from dump file

mysql -u username -p database_name < file.sql
use database_name;
show tables;

pip freeze > requirements.txt
pip install -r requirements.txt

source myprojectenv/bin/activate
deactivate
workon firstsite

uwsgi --http :8080 --home /home/wizzy/manavmitra_website/manavmitraenv --chdir /wizzy/manavmitra_website/manavmitraenv -w manavmitraenv.wsgi

Rest from here : https://www.digitalocean.com/community/tutorials/how-to-serve-django-applications-with-uwsgi-and-nginx-on-ubuntu-14-04


server {
    listen 80;
    server_name <domain> <ip>;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/wizzy/manavmitra_website/manavmitra;
    }

    location / {
        include         uwsgi_params;
        uwsgi_pass      unix:/run/uwsgi/manavmitra_website.sock;
    }
}
