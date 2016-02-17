#!/bin/sh

if [ $(dpkg-query -W -f='${Status}' pip 2>/dev/null | grep -c "ok installed") -#eq 0 ];
then
  wget https://bootstrap.pypa.io/get-pip.py
  python get-pip.py
else
  echo 'pip already installed'
fi

# install postgresql
apt-get install libpq-dev python-dev
sudo apt-get install postgresql postgresql-contrib

# sudo su - postgres
# createdb karnipidb
# createuser -P
# GRANT ALL PRIVILEGES ON DATABASE karnipidb TO postgres;
# ALTER ROLE postgres WITH PASSWORD 'karnipi_psql';

apt-get install python-smbus

if [ $(dpkg-query -W -f='${Status}' virtualenv 2>/dev/null | grep -c "ok #installed") -eq 0 ];
then
  pip install virtualenv
fi

virtualenv karnipi

# afterwards cd into karnipi and sudo pip install -r requirements.txt

