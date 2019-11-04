#!/bin/bash
PYTHON=python
UWSGI=uwsgi

echo "starting all-in-one flask server"

nohup $UWSGI uwsgi1.ini &>log & FLASK=$!

echo "flask wrapper started , pid is $FLASK"


