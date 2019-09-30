#!/bin/bash
PYTHON=python





echo "starting backend socket daemon"
$PYTHON predict.py conf/train.json & PRED=$!
echo "backend socket daemon started, pid is $PRED"
echo "starting flask wrapper"

$PYTHON server.py & FLASK=$!

echo "flask wrapper started , pid is $FLASK"

function wasted ()
{
    kill -15 $FLASK
    kill -15 $PRED
    exit 0
}

trap "wasted" 2

while :
do
    kill -0 $FLASK
    kill -0 $PRED
    sleep 30
done

