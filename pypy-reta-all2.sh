#!/bin/bash
cd ~
function ctrl_c() {
    cat ~/myRepos/reta/head1.alx
    cat ~/myRepos/reta/religionen.js
    cat ~/myRepos/reta/head2.alx
    cat ~/middle.alx
    cat ~/myRepos/reta/footer.alx
}
trap ctrl_c INT
if [ "$1" == 'reta' ]; then
	pypy3 ~/myRepos/reta/reta -spalten --alles --breite=0 -ausgabe --art=html --onetable --nocolor >  ~/middle1.alx
fi
chown -R alex:alex ~/myRepos/reta
ctrl_c
cd -
