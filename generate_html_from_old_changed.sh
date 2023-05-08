#!/bin/bash
function ctrl_c() {
    cat head1.alx
    cat religionen.before23-0429.changed.js
    cat head2.alx
    cat middle.alx
    ./grundStrukHtml.py blank
    cat footer.alx
}
trap ctrl_c INT
./reta -spalten --alles --breite=0 -ausgabe --art=html --onetable --nocolor > middle.alx
ctrl_c
