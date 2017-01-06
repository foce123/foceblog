#!/bin/bash


#vim ~/.git-credentials
#https://{username}:{password}@github.com
#git config --global credential.helper store

#username='foce123@gmail.com'
#password='focefoce'

if [ "$1" = "" ];then
  echo "plz input one git commit message"
  exit
else
\cp -rf /data/pyweb/foce/foceblog/ /data/git/blog/
echo "copy files to git/blog done!"
cd /data/git/blog/foceblog/
echo "change directory to foceblog"
echo "git pushing..."
git add .
git commit -m "$1"
#git remote add origin https://github.com/foce123/foceblog.git
git push -u origin master

#/usr/bin/expect <<EOF
#set timeout 1000
#spawn git push -u origin master
#expect {
#"Username" {send "${username}\r";exp_continue}
#"Password" {send "${password}\r"}
#}
#set timeout 2000
#interact
#EOF
#echo "gitpush done!"
fi
