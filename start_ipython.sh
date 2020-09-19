#!/usr/bin/env bash
python main.py $@
git add sessions
git commit -m "`date`"
git pull -X theirs origin master
git push origin master