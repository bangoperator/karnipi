#!/bin/sh

ROOT=/home/pi/karnipi
GUNICORN=$ROOT/bin/gunicorn
GUNICORN_CONF=$ROOT/gunicorn_config.py

cd $ROOT

$GUNICORN -c $GUNICORN_CONF karnipi.wsgi
