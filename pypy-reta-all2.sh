#!/bin/bash
trap ctrl_c INT
if [ "$1" == 'reta' ]; then
	pypy3 ~/myRepos/reta/reta -spalten --alles --breite=0 -ausgabe --art=html --onetable --nocolor >  ~/myRepos/reta/middle1.alx
    git mv ~/myRepos/reta/middle1.alx ~/myRepos/reta/middle.alx
fi

function ctrl_c() {
    cat ~/myRepos/reta/head1.alx
    cat ~/myRepos/reta/religionen.js
    cat ~/myRepos/reta/head2.alx
    cat ~/myRepos/reta/middle.alx
    cat ~/myRepos/reta/footer.alx
}

ctrl_c
