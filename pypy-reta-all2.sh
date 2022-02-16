#!/bin/bash
cd /home/alex/myRepos/reta
cat ~/myRepos/reta/head1.alx
cat ~/myRepos/reta/religionen.js
cat ~/myRepos/reta/head2.alx
if [ "$1" == 'reta' ]; then
	pypy3 reta -spalten --alles --breite=0 -ausgabe --art=html --onetable --nocolor >  ~/middle.alx && ja=true || ja=false
fi
cat ~/middle.alx
cat ~/myRepos/reta/footer.alx
cd - > /dev/null
