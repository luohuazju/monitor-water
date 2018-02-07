#!/bin/sh -ex

#start the service
cd /share/water-monitor/restful_api
gunicorn -c gunicorn.py.ini restful_api.wsgi