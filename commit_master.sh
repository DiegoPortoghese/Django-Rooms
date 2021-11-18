#!/bin/sh
git checkout sviluppo
git add .
git commit -a -m "Auto Commit for merge master"
git push
echo "Merge Commit on master"
git checkout master
git merge sviluppo
git push
echo "Set current brash on sviluppo"
git checkout sviluppo
