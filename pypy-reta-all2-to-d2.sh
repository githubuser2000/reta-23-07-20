#!/bin/bash
if [ "$1" == 'reta' ] || [ "$2" == 'reta' ]  || [ "$3" == 'reta' ] || [ "$4" == 'reta' ]; then
	bla=reta
fi 
if [ "$1" == 'snapshot' ] || [ "$2" == 'snapshot' ]  || [ "$3" == 'snapshot' ] || [ "$4" == 'snapshot' ]; then
	reta-all2-snapshot.sh $bla > ~/religionen.html
else
	geschafft=false
	pypy-reta-all2.sh $bla > ~/religionen_.html
	[ `cat ~/religionen_.html | grep -e '^</table>$' | grep -v table2 | wc -l` -eq 1 ] && geschafft=true
	$geschafft && cp -av ~/religionen_.html ~/religionen.html
fi 
#$geschafft && cp ~/religionen.html ~/myRepos/reta/religionen.html 
if [ "$1" == 'htmld2' ] || [ "$2" == 'htmld2' ] || [ "$3" == 'htmld2' ] || [ "$4" == 'htmld2' ]; then
	if $geschafft; then
		cd ~;tar -c religionen.html | plzip -1 - | ssh root@d2 'plzip -d - | tar --overwrite -xf - -C /media/2TB/data/www/forum/' && echo html zu d2 gesendet || echo html konnte nicht zu d2 gesendet werden
		tar -c religionen.html | ssh root@ppp 'tar --overwrite -xf - -C /srv/http/forum' && echo html zu ppp gesendet || echo html konnte nicht zu ppp gesendet werden
		cd -
	fi
fi
if [ "$1" == 'tar' ] || [ "$2" == 'tar' ] || [ "$3" == 'tar' ] || [ "$4" == 'tar' ]; then
	echo sende auch tar
	cd /home/alex/myRepos/reta
	cp -ax {*.{csv,txt,py,js,bbcode},reta} /home/alex/myRepos/religions-tabelle-releasses/31
	cp -ax pypy-reta-all2-to-d2.sh /home/alex/myRepos/religions-tabelle-releasses/31
	cp -ax pypy-reta-all2.sh /home/alex/myRepos/religions-tabelle-releasses/31
	cd -
	cd /home/alex/myRepos/religions-tabelle-releasses/31
	tar -c {*.{csv,txt,py,js,bbcode},reta,pypy-reta-all2-to-d2.sh,pypy-reta-all2.sh} > /home/alex/myRepos/religions-tabelle-releasses/reta.tar
	cd -
	cd /home/alex/myRepos/religions-tabelle-releasses/; tar -c reta.tar | plzip -1 - | ssh root@d2 'plzip -d - | tar --overwrite -xf - -C /media/2TB/data/www/forum/'
	cd /home/alex/myRepos/religions-tabelle-releasses/; tar -c reta.tar | ssh root@ppp 'tar --overwrite -xf - -C /srv/http/forum'
	git add -A;git commit -m "$(date)";git push
	cd -
fi
