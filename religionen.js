var col =  document.getElementsByClassName('RowNumber 1');
var selectedSpaltenMany1 = {};
var selectedSpaltenMany2 = {};
window.onload = function() {
let div = document.createElement('div');
let div2 = document.createElement('div');
div.className = "headingsDiv";
document.body.insertBefore(div, document.getElementsByTagName("table")[0]);
    chk_spalten = "<fieldset style=\"font-size: medium;\"><input type=\"radio\" id=\"spaltenWahl\" name=\"spaltOrZeilWahl\" onchange=\"toggleChkSpalten(this);\" checked=\"true\"><label>Spalten Checkboxen</label><input type=\"radio\" id=\"zeilenWahl\" name=\"spaltOrZeilWahl\" onchange=\"toggleChkSpalten(this);\"><label>Zeilen Eingabefelder</label><input type=\"radio\" id=\"keinsWahl\" name=\"spaltOrZeilWahl\" onchange=\"toggleChkSpalten(this);\"><label>frei machen zur Tabellenansicht</label></fieldset>"
div.innerHTML = chk_spalten;
tdClasses = document.getElementsByClassName("z_0");
/*tdClasses = []
for (i = 0; i < tdClasses1.length; i++) 
	if (tdClasses1[i].className.includes("z_0"))
		tdClasses.push(tdClasses1[i]);*/
p1map = {},p2map = {},mapMapMap = {}, str = "", p1Bmap = {};
str3 = ""
for (i = 0; i < tdClasses.length; i++) {
	name = tdClasses[i].className;
	var num = name.match(/r_(\d+)/)
	if (num != null) {
		//num = num.substring(2,0);
		num = parseInt(num[1]);
		str = num[1];
		//num = i
		var p1a = name.match(/p1_([^\s])+/g);
		var p2a = name.match(/p2_([^\s])+/g);
		if (p1a != null) {
			for (p1i = 0; p1i < p1a.length; p1i++) {
				if (p1a[p1i].includes("p1_"))
					p1a[p1i] = p1a[p1i].substring(3);
				p1b = p1a[p1i].match(/[^,]+/g);
				if (p1b != null) {
				for (p1k = 0; p1k < p1b.length; p1k++) {
						p1 = p1b[p1k];
						if (typeof mapMapMap[p1] === 'undefined')
							mapMapMap[p1]= {};
						if (p2a != null) {
							for (p2i = 0; p2i < p2a.length; p2i++) {
								if (p2a[p2i].includes("p2_"))
									p2a[p2i] = p2a[p2i].substring(3);
								p2b = p2a[p2i].match(/[^,]+/g);
								if (p2b != null) {
									for (p2k = 0; p2k < p2b.length; p2k++) {
										p2 = p2b[p2k];
										if (p2 != null) {
											var p3a = p2.match(/p3_(\d+)_/);
											if (p3a != null) {
												p3b = parseInt(p3a[1], 10);
												p2 = p2.substring(p3a[1].length + 4);
												if (p3b == p1k) {
													if (p2.length > 0) {
														if (typeof mapMapMap[p1][p2] === 'undefined')
															mapMapMap[p1][p2]= new Set();
														mapMapMap[p1][p2].add(num);
													} else {
														if (typeof mapMapMap[p1][null] === 'undefined')
															mapMapMap[p1][null]= new Set();
														mapMapMap[p1][null].add(num);
													}
												}
											}
										} else {
											if (typeof mapMapMap[p1][null] === 'undefined')
												mapMapMap[p1][null]= new Set();
											mapMapMap[p1][null].add(num);
										}
									}
								}
							}
						} else{
							if (typeof mapMapMap[p1][null] === 'undefined')
								mapMapMap[p1][null]= new Set();
							mapMapMap[p1][null].add(num);
						}
					}
				}
			}
		}
	}
}

	var p1keys = Object.keys(mapMapMap);
	var p1Bkeys = Object.keys(p1Bmap);
	//checkboxes = "<span style=\"white-space: nowrap;\"><input type=\"checkbox\" onchange=\"toggleSpalten(\'r_0\');\"><label>Nummererierung</label>";
checkboxes = "<div id=\"chk_spalten\" style=\"display:none;\"><span style=\"\">";
	for (i = 0; i < p1keys.length; i++) {
		var chk2s = "";
		var p2keys = Object.keys(mapMapMap[p1keys[i]]);
		for (k = 0; k < p2keys.length; k++) {
			numbers = Array.from(mapMapMap[p1keys[i]][p2keys[k]]);
			if (p2keys[k] != null && p2keys[k] != 'null') {
				chk2 = '<label style=\"white-space: nowrap;font-size: medium;\"><input type="checkbox" value="'+p2keys[k]+'" onchange="toggleP2(this,\''+numbers+'\',\''+[p1keys[i],p2keys[k]]+'\');">'+makeSpacesOutOf_(p2keys[k])+'</label><label style=\"white-space: normal;\">&nbsp; </label>';
				chk2s += chk2;
			}
			
		}
		if ( mapMapMap[p1keys[i]][null] !== undefined ) {
			numbers = Array.from(mapMapMap[p1keys[i]][null]);
			insertnull = 'toggleP2(this,\''+numbers+'\',\''+[p1keys[i],null]+'\');'
		} else {
			insertnull = '';
		}
        checkbox = '<br><input type="checkbox" value="'+p1keys[i]+'" onchange="toggleP1(\''+p1keys[i]+'\');'+insertnull+'"><label style=\"white-space: normal;font-size: medium;\">'+makeSpacesOutOf_(p1keys[i])+'</label><div id="'+p1keys[i]+'" style="display:none;white-space: normal; border-left: 40px solid rgba(0, 0, 0, .0);">'+chk2s+'</div>';
		checkboxes += checkbox;
	}
	str2 = checkboxes + "</span></div>";
	div.innerHTML += str2;
    str4 = "<div id=\"inputZeilen\" style=\"display:none\"><table borders=\"0\" id=\"table2\">";
    str5 = "<tr><td><label>von bis und Einzelnes: </label></td><td><input typ=\"text\" id=\"zeilenErlaubtText\" value=\"1-10,12\"></input></td><td><input type=\"radio\" class=\"neuErlauben\" name=\"zeilenDazuOrWeg1\" onchange=\"\" checked=\"true\"><label>neu sichtbar</label><input type=\"radio\" class=\"neuHinfort\" name=\"zeilenDazuOrWeg1\" onchange=\"\"><label>neu unsichtbar</label><input type=\"radio\" class=\"dazuErlauben\" name=\"zeilenDazuOrWeg1\" onchange=\"\"><label>zusätzlich sichtbar</label><input type=\"radio\" class=\"dazuHinfort\" name=\"zeilenDazuOrWeg1\" onchange=\"\"><label>zusätzlich unsichtbar</label><input onclick=\"clickZeilenErlaubenUsw();\" type=\"submit\" value=\"auswählen\"></td></tr>";
    str6 = "<tr><td><label>Vielfacher und Nachbarn: </label></td><td><input typ=\"text\" id=\"VielfacheErlaubtText\" value=\"10+0+1,7+0\"></td><td></input><input type=\"radio\" class=\"neuErlauben\" name=\"zeilenDazuOrWeg2\" onchange=\"\" checked=\"true\"><label>neu sichtbar</label><input type=\"radio\" class=\"neuHinfort\" name=\"zeilenDazuOrWeg2\" onchange=\"\"><label>neu unsichtbar</label><input type=\"radio\" class=\"dazuErlauben\" name=\"zeilenDazuOrWeg2\" onchange=\"\"><label>zusätzlich sichtbar</label><input type=\"radio\" class=\"dazuHinfort\" name=\"zeilenDazuOrWeg2\" onchange=\"\"><label>zusätzlich unsichtbar</label><input onclick=\"clickVielfacheErlaubenUsw();\" type=\"submit\" value=\"auswählen\"></td></tr>";
    str8 = "<tr><td><label>Potenzen: </label></td><td><input typ=\"text\" id=\"potenzenErlaubtText\" value=\"3,5\"></input></td><td><input type=\"radio\" class=\"neuErlauben\" name=\"zeilenDazuOrWeg3\" onchange=\"\" checked=\"true\"><label>neu sichtbar</label><input type=\"radio\" class=\"neuHinfort\" name=\"zeilenDazuOrWeg3\" onchange=\"\"><label>neu unsichtbar</label><input type=\"radio\" class=\"dazuErlauben\" name=\"zeilenDazuOrWeg3\" onchange=\"\"><label>zusätzlich sichtbar</label><input type=\"radio\" class=\"dazuHinfort\" name=\"zeilenDazuOrWeg3\" onchange=\"\"><label>zusätzlich unsichtbar</label><input onclick=\"clickPotenzenErlaubenUsw();\" type=\"submit\" value=\"auswählen\"></td></tr>";
    str9 = "<tr><td colspan=\"2\"><input type=\"radio\" id=\"sonneWahl\" name=\"sunmoonplanetblackhole\" onchange=\"\" checked=\"true\"><label>Sonne</label><input type=\"radio\" id=\"mondWahl\" name=\"sunmoonplanetblackhole\" onchange=\"\"><label>Mond</label><input type=\"radio\" id=\"planetWahl\" name=\"sunmoonplanetblackhole\" onchange=\"\"><label>Planet</label><input type=\"radio\" id=\"schwarzeSonneWahl\" name=\"sunmoonplanetblackhole\" onchange=\"\" onclick=\"window.alert('Schwarze Sonnen kehren die Orginalbedeutung ins Gegenteil.');\"><label>schwarze Sonne</label></td><td><input type=\"radio\" class=\"neuErlauben\" name=\"zeilenDazuOrWeg4\" onchange=\"\" checked=\"true\"><label>neu sichtbar</label><input type=\"radio\" class=\"neuHinfort\" name=\"zeilenDazuOrWeg4\" onchange=\"\"><label>neu unsichtbar</label><input type=\"radio\" class=\"dazuErlauben\" name=\"zeilenDazuOrWeg4\" onchange=\"\"><label>zusätzlich sichtbar</label><input type=\"radio\" class=\"dazuHinfort\" name=\"zeilenDazuOrWeg4\" onchange=\"\"><label>zusätzlich unsichtbar</label><input onclick=\"clickHimmelskoerperErlaubenUsw();\" type=\"submit\" value=\"auswählen\"></td></tr>";
    str10 = "<tr><td><label>Zählung: </label></td><td><input typ=\"text\" id=\"zaehlungErlaubtText\" value=\"1,3-4\"></input></td><td><input type=\"radio\" class=\"neuErlauben\" name=\"zeilenDazuOrWeg5\" onchange=\"\" checked=\"true\"><label>neu sichtbar</label><input type=\"radio\" class=\"neuHinfort\" name=\"zeilenDazuOrWeg5\" onchange=\"\"><label>neu unsichtbar</label><input type=\"radio\" class=\"dazuErlauben\" name=\"zeilenDazuOrWeg5\" onchange=\"\"><label>zusätzlich sichtbar</label><input type=\"radio\" class=\"dazuHinfort\" name=\"zeilenDazuOrWeg5\" onchange=\"\"><label>zusätzlich unsichtbar</label><input onclick=\"clickZaehlungenErlaubenUsw();\" type=\"submit\" value=\"auswählen\"></td></tr>";
    str11 = "<tr><td><label>Primzahlvielfacher: </label></td><td><input typ=\"text\" id=\"primVielfache\" value=\"1\"></input></td><td><input type=\"radio\" class=\"neuErlauben\" name=\"zeilenDazuOrWeg6\" onchange=\"\" checked=\"true\"><label>neu sichtbar</label><input type=\"radio\" class=\"neuHinfort\" name=\"zeilenDazuOrWeg6\" onchange=\"\"><label>neu unsichtbar</label><input type=\"radio\" class=\"dazuErlauben\" name=\"zeilenDazuOrWeg6\" onchange=\"\"><label>zusätzlich sichtbar</label><input type=\"radio\" class=\"dazuHinfort\" name=\"zeilenDazuOrWeg6\" onchange=\"\"><label>zusätzlich unsichtbar</label><input onclick=\"clickPrimVielfacheErlaubenUsw();\" type=\"submit\" value=\"auswählen\"></td></tr>";
    str12 = "<tr><td colspan=\"2\"><input type=\"radio\" id=\"proInnen\" name=\"proContra4Richtungen\" onchange=\"\" checked=\"true\"><label>pro innen</label><input type=\"radio\" id=\"proAussen\" name=\"proContra4Richtungen\" onchange=\"\"><label>pro Außen</label><input type=\"radio\" id=\"gegenDritte\" name=\"proContra4Richtungen\" onchange=\"\"><label>gegen Dritte</label><input type=\"radio\" id=\"proDritte\" name=\"proContra4Richtungen\" onchange=\"\" onclick=\"\"><label>pro Dritte</label></td><td><input type=\"radio\" class=\"neuErlauben\" name=\"zeilenDazuOrWeg7\" onchange=\"\" checked=\"true\"><label>neu sichtbar</label><input type=\"radio\" class=\"neuHinfort\" name=\"zeilenDazuOrWeg7\" onchange=\"\"><label>neu unsichtbar</label><input type=\"radio\" class=\"dazuErlauben\" name=\"zeilenDazuOrWeg7\" onchange=\"\"><label>zusätzlich sichtbar</label><input type=\"radio\" class=\"dazuHinfort\" name=\"zeilenDazuOrWeg7\" onchange=\"\"><label>zusätzlich unsichtbar</label><input onclick=\"clickPrimRichtungenErlaubenUsw();\" type=\"submit\" value=\"auswählen\"></td></tr>";
    str7 = "</table></div>";
	div.innerHTML += str4 + str5 + str6 + str8 + str9 + str10 + str11 + str12 + str7;
    // Spaltenreihenfolge
	tableHeadline = document.getElementsByTagName("table")[1].getElementsByTagName('tr')[0].getElementsByTagName('td');
    for (var u=0; u<tableHeadline.length; u++) {
        tableHeadline[u].innerHTML += '<select id="hselec_'+u+'" value="'+u+'" onchange="headingSelected(this, '+u+');"></select>'
    }
    toggleChkSpalten();
}

alleMonde = [4,8,9,16,25,27,32,36,49,64,81,100,121,125,128,144,169,196,216,225,243,256,289,324,343,361,400,441,484,512,529,576,625,676,729,784,841,900,961,1000,1024]
primZahlen = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013, 1019, 1021]


function makeSpacesOutOf_(text) {
    if (text.length == 25)
        if (text == 'primzahlvielfachesgalaxie')
            return 'Primzahlvielfache Galaxie'
    if (text.length == 8)
        if (text == 'zaehlung')
            return 'Zählung'
    if (text.length == 12)
        if (text == 'nummerierung')
            return 'Nummerierung'
    if (text.length == 11)
        if (text == 'kombination')
            return 'Kombinationen'
    var forNewString = [];
    for (var i=0; i<text.length; i++)
        if (text[i] == '_')
            forNewString.push(' ');
        else
            forNewString.push(text[i]);
    return forNewString.join("");
}


function toggleP2(dasTag, spaltenNummern, para1u2) {
    //window.alert('bla: '+dasTag.checked);
	spaltenNummern = spaltenNummern.split(',');
	existingParameterNamesArrayIndex = MatrixHasCouple(para1u2, selectedSpaltenMany2);
	if (existingParameterNamesArrayIndex.size > 0) {
		existingParameterNamesKeys = Array.from(existingParameterNamesArrayIndex);
		for (i=0; i<existingParameterNamesKeys.length; i++){
			for (k=0; k<selectedSpaltenMany2[existingParameterNamesKeys[i]].length; k++) {
				if (selectedSpaltenMany2[existingParameterNamesKeys[i]][k] == para1u2 ) {
					selectedSpaltenMany2[existingParameterNamesKeys[i]].splice(k,1);
				} else {
				}
			}
		}
		toggleForNums(spaltenNummern);
	} else {
		for (i=0; i<spaltenNummern.length; i++)
			if (typeof(selectedSpaltenMany2[spaltenNummern[i]]) !== "undefined")
				selectedSpaltenMany2[spaltenNummern[i]].push(para1u2);
			else
				selectedSpaltenMany2[spaltenNummern[i]]=[para1u2];
		toggleForNums(spaltenNummern);
	}
}

function MatrixHasCouple(couple, SpaltenNumberToParameters) {
	existing = new Set();
	for (var key in SpaltenNumberToParameters) {
		for (i=0; i<SpaltenNumberToParameters[key].length; i++) {
			for (k=0; k<SpaltenNumberToParameters[key].length; k++) {
				if (SpaltenNumberToParameters[key][k] != couple) {
				} else {
					existing.add(key);
				}
			}
		}
	}
	return existing;
}

function toggleForNums(colNums) {
	for (n = 0; n < colNums.length; n++) {
		/*if (typeof(selectedSpaltenMany2[colNums]) === 'undefined')
			toggleSpalten(colNums[n]);
		else {
			toggleSpalten(colNums[n]);
		}*/
		toggleSpalten(colNums[n]);
	}
    //window.alert("colNums 0:"+colNums[0])
    refresh();
}

function refresh() {
    sortedKeysOfHeadingNumbersByVisibility();
    setAllListsInHeadings();
    updateVisibleHeadingsNumbersAndItsKeysList();
}

function updateVisibleHeadingsNumbersAndItsKeysList() {
    keys = Object.keys(visibleHeadingsSelectUnsorted);
    for (var i=0; i<keys.length; i++) {
        visibleHeadingsNumbers[keys[i]] = visibleHeadingsSelectUnsorted[keys[i]].value;
    }
    keys2 = Object.keys(visibleHeadingsNumbers);
    //window.alert("vis num"+ keys2.length)
    //window.alert("vis num 0: "+ visibleHeadingsNumbers[keys2[0]])
}

function toggleName(p2) {
	if (p2.style.display != 'none') 
		p2.style.display = 'none';
    else
        if (p2.getElementsByTagName("input").length > 0)
        { 
		    p2.style.display = 'block';
		    p2.style.fontSize = 'medium';
        }
}

function toggleP1(p1) {
	p2 = document.getElementById(p1);
	if (typeof(p2.style) != "undefined") {
		var num = p2.className.match(/r_(\d+)/)
        if (num != null && num.length > 1)
			num = num[1]
		if ( (selectedSpaltenMany1[num] === 'undefined') === (p2.style.display != 'none')) {
			selectedSpaltenMany1[num] = p2
			toggleName(p2)
		} else {
			toggleName(p2)
			delete selectedSpaltenMany1[num]
		}
	} else 
		window.alert(p2.innerHTML + ' ! ');
}

function toggleSpalten(colNumber) {
	ZeileIhreZellen = document.getElementsByClassName('r_'+colNumber);
	if (typeof(selectedSpaltenMany2[colNumber]) === 'undefined') { 
		away = true;
		//window.alert("undefined "+colNumber);
	} else
		away = selectedSpaltenMany2[colNumber].length==0;
	//window.alert("Stelle "+colNumber+"hat Länge "+selectedSpaltenMany2[colNumber].length);
	if (typeof(ZeileIhreZellen[0].style) != "undefined") {
		if (ZeileIhreZellen[0].style.display == 'none')
            changeHeadline(ZeileIhreZellen[0], true);
        else
            if (away)
                changeHeadline(ZeileIhreZellen[0], false);

        if (ZeileIhreZellen[0].getElementsByTagName("option").length == 0)
            spalteEinzelnDeaktiviertWorden = false;
        else 
            if (ZeileIhreZellen[0].getElementsByTagName("option")[0].selected)
                spalteEinzelnDeaktiviertWorden = true;
            else
                spalteEinzelnDeaktiviertWorden = false;

		for (i=0; i < ZeileIhreZellen.length; i++) { 
			if (ZeileIhreZellen[i].style.display == 'none' && ! spalteEinzelnDeaktiviertWorden) {
				ZeileIhreZellen[i].style.display = 'table-cell';
		        ZeileIhreZellen[i].style.fontSize = 'medium';
            } else 
				if (away || spalteEinzelnDeaktiviertWorden) {
					ZeileIhreZellen[i].style.display = 'none';
		    }
        }
		if (spalteEinzelnDeaktiviertWorden) {
                //window.alert('B '+ZeileIhreZellen[0].className.match(/r_(\d+)/g)[0]);
                //window.alert('B '+ZeileIhreZellen[0].className.match(/r_(\d+)/g)[0].substring(2));
                delete visibleHeadingsSelectUnsorted[parseInt(ZeileIhreZellen[0].className.match(/r_(\d+)/g)[0].substring(2))];
                // sie wieder zu aktivieren, auf 1 statt 0 setzen (wobei hier die richtige zahl eigentlich besser wäre)
                // auf 1 setzen ist aber okay, weil die durch refresh usw. sowieso wieder umgesetzt wird 
                ZeileIhreZellen[0].getElementsByTagName("option")[1].selected = 'selected';
        }
    }
	else 
		window.alert(ZeileIhreZellen[0].innerHTML + ' ! '+colNumber);

}

var tableHeadline;
var visibleHeadingsSelectUnsorted = {};
var visibleHeadingsNumbers = {};

function changeHeadline(oneColHeading, addTrueRemoveFalse) {
    sel = oneColHeading.getElementsByTagName('select')[0];
	var num = oneColHeading.className.match(/r_(\d+)/g);
    if (num.length>0)
        num = parseInt(num[0].substring(2));
    else
        num = 0;
	//window.alert(num);

    if (addTrueRemoveFalse)
        visibleHeadingsSelectUnsorted[num]=sel;
    else
        if (num in visibleHeadingsSelectUnsorted)
            delete visibleHeadingsSelectUnsorted[num];
	//window.alert(Object.keys(visibleHeadingsSelectUnsorted).length);
    //
}

function makeSpalteUnsichtbar(spalteToUnsichtbar, momentaneSpalte_als_r_ , hiddenTrueVisibleFalse) {
    //spalteToUnsichtbar = document.getElementsByClassName("r_"+momentaneSpalte_als_r_);
    len = spalteToUnsichtbar.length;
    if (hiddenTrueVisibleFalse) {
        for (var i=0; i<len; i++) 
            spalteToUnsichtbar[i].style.display = 'none';
        delete visibleHeadingsSelectUnsorted[momentaneSpalte_als_r_];
    } /*else {
        for (var i=0; i<len; i++) 
            spalteToUnsichtbar[i].style.display = 'table-cell'
        visibleHeadingsSelectUnsorted['r_'+momentaneSpalte_als_r_]=spalteToUnsichtbar;
    }*/
}

var erstesMal = true;

function headingSelected(gewaehlteSpalte_plusgleich1, momentaneSpalte_als_r_) {
    gewaehlteSpalte_plusgleich1 = gewaehlteSpalte_plusgleich1.value;
    //for (var i=0; i<optionsS.length; i++) {
    zwei = gewaehlteSpalte_plusgleich1.split(",");
    gewaehlteSpalte_plusgleich1 = zwei[0];
    gewaehlteSpalte_als_r_ = zwei[1];
	var spalte2ToChange = document.getElementsByClassName('r_'+momentaneSpalte_als_r_);
    if (gewaehlteSpalte_plusgleich1 == '-') {
        makeSpalteUnsichtbar(spalte2ToChange, momentaneSpalte_als_r_, true);
        refresh();
        return;
    }
    if (erstesMal) {
        //window.alert("Das Dauert! Geduld mitbringen! Alles friert kurz ein!");
        erstesMal = false;
    }
    momentaneSpalte_plusgleich1 = visibleHeadingsNumbers[momentaneSpalte_als_r_]; // dieses mal als +=1 angabe statt als r_
    zwei = momentaneSpalte_plusgleich1.split(",");
    momentaneSpalte_plusgleich1 = zwei[0];
	var spalte1ToChange = document.getElementsByClassName('r_'+gewaehlteSpalte_als_r_);
    seli = spalte1ToChange[0].getElementsByTagName("select")[0].getElementsByTagName("option");
    selival = selectionsBefore[momentaneSpalte_plusgleich1] + 1;
    gewaehlteSpalte_plusgleich1 = selival - 2; // 1 bis +=1
    seli[selival].selected = 'selected';
	var tabellenKopf = document.getElementsByClassName('z_0');
    var aa = 0;
    var bb = 0;
    for (var z=0; z<tabellenKopf.length; z++) {
        if (tabellenKopf[z] === spalte2ToChange[0])
            aa = z;
        if (tabellenKopf[z] === spalte1ToChange[0])
            bb = z;
    }

    var merke;
    if (aa>bb)
        for (var i=0; i<spalte1ToChange.length; i++) {
            merke = spalte2ToChange[i].outerHTML
            spalte2ToChange[i].outerHTML = spalte1ToChange[i].outerHTML;
            spalte1ToChange[i].outerHTML = merke;
        }
    else
        for (var i=0; i<spalte1ToChange.length; i++) {
            merke = spalte1ToChange[i].outerHTML
            spalte1ToChange[i].outerHTML = spalte2ToChange[i].outerHTML;
            spalte2ToChange[i].outerHTML = merke;
        }

    visibleHeadingsSelectUnsorted[gewaehlteSpalte_als_r_] = spalte1ToChange[0].getElementsByTagName('select')[0];
    visibleHeadingsSelectUnsorted[momentaneSpalte_als_r_] = spalte2ToChange[0].getElementsByTagName('select')[0];
    refresh();
}

var selectionsBefore = {};
var optionsS = [];
var sichtbareSpaltenNummern;

function sortedKeysOfHeadingNumbersByVisibility() {
	tableHeadline = document.getElementsByTagName("table")[1].getElementsByTagName('tr')[0].getElementsByTagName('td');
    sichtbareSpaltenNummern = []
    for (var i=0; i<tableHeadline.length; i++) {
        if (tableHeadline[i].style.display == 'table-cell') {
            sichtbareSpaltenNummern.push(tableHeadline[i].className.match(/r_(\d+)/g)[0].substring(2));
        }
    }
    //reihenfolgenstring = sichtbareSpaltenNummern.join(", ");
    //window.alert('sichtb spalten r_ nummern: '+reihenfolgenstring);
}

function setAllListsInHeadings() {
    var options;
    optionsS = [];
    var keys = Object.keys(visibleHeadingsSelectUnsorted);
    var len = keys.length;
    for (var k=0; k<len; k++) {
        options = ["<option value='-,null'>-</option>"];
        for (var i=0; i<len; i++)
            if (i != k) 
                options.push("<option value='"+i+","+sichtbareSpaltenNummern[i]+"'>"+(i+1)+"</option>");
            else {
                options.push("<option selected value='"+i+","+sichtbareSpaltenNummern[i]+"'>"+(i+1)+"</option>");
                selection = i
            }
        selectionsBefore[k] = k
        optionsS.push(options);
    }
    if (len != sichtbareSpaltenNummern.length) {
        window.alert("beides sichtbares und beide Längen nicht gleich: td spalten zellen anzahl als dict mir _r keys und die _r Nummerierung derer als array, sichtbareSpaltenNummern ist "+sichtbareSpaltenNummern.length+" und visibleHeadingsSelectUnsorted ist "+len);
    }
    for (var i=0; i<sichtbareSpaltenNummern.length; i++) {
        visibleHeadingsSelectUnsorted[sichtbareSpaltenNummern[i]].innerHTML = optionsS[i].join("");
    }
}

function toggleChkSpalten(radiobutton) {
	chk_spalten = document.getElementById("chk_spalten");
	inputZeilen = document.getElementById("inputZeilen");
	spaltenWahl = document.getElementById("spaltenWahl");
	zeilenWahl = document.getElementById("zeilenWahl");

	if (inputZeilen.style.display == 'none' && zeilenWahl.checked)
		inputZeilen.style.display = 'initial';
    else
        if (! zeilenWahl.checked) 
		    inputZeilen.style.display = 'none';

	if (chk_spalten.style.display == 'none' && spaltenWahl.checked)
		chk_spalten.style.display = 'initial';
    else
        if (! spaltenWahl.checked) 
		    chk_spalten.style.display = 'none';
}

function potenzenAngabenToContainer() {
    text = document.getElementById('potenzenErlaubtText').value;
    var zeilenAngaben = new Set();
    text = text.split(",");
    for (var i=0; i<text.length; i++) {
        number = parseInt(text[i]);
        if (number != 'NaN') 
            zeilenAngaben.add(number);
    }
    return zeilenAngaben;
}

function zeilenAngabenToContainer(welches) {
    if (welches == 1)
        text = document.getElementById('zeilenErlaubtText').value;
    if (welches == 2)
        text = document.getElementById('zaehlungErlaubtText').value;
    if (welches == 3)
        text = document.getElementById('primVielfache').value;
    var zeilenAngaben = new Set();
    text = text.split(",");
    for (var i=0; i<text.length; i++) {
        text2 = text[i].split("-");

        richtig = true;
        if (text2.length < 3) 
            for (var k=0; k<text2.length; k++)
                if (parseInt(text2[k]) == 'NaN')
                    richtig = false;
                else
                    text2[k] = parseInt(text2[k]);
        else
            richtig = false;
        
        if (richtig) {
            if (text2.length == 1) 
                text2.push(text2[0]);
            zeilenAngaben.add(text2);
        }
    }    
    return zeilenAngaben;
}

function vielfacherAngabentoContainer() {
    text = document.getElementById('VielfacheErlaubtText').value;
    var vielfacherAngaben = new Set();
    text = text.split(",");
    for (var i=0; i<text.length; i++) {
        text2 = text[i].split("+");
        richtig = true;
        for (var k=0; k<text2.length; k++)
            if (parseInt(text2[k]) == 'NaN')
                richtig = false;
            else
                text2[k] = parseInt(text2[k]);
        if (richtig)
            vielfacherAngaben.add(text2);
    }
    return vielfacherAngaben;
}

var erlaubteZeilen = new Set();

function makeAllerlaubteZeilenVielfacher(zeilenAngaben) {
    zeilenAngaben = Array.from(zeilenAngaben);
    var muls;
    erlaubteZeilen = new Set();
    for (var i=0; i<zeilenAngaben.length; i++) { 
        last = zeilenAngaben[i][0];
        muls = []
        mul = 1;
        last = mul * zeilenAngaben[i][0];
        while (last<1025) {
            muls.push(last);
            last = mul * zeilenAngaben[i][0];
            mul++;
        }
        for (var h=0; h<muls.length; h++) {
            if (zeilenAngaben[i].length == 1) {
                erlaubteZeilen.add(muls[h]);
            } else
                for (var k=1; k<zeilenAngaben[i].length; k++) {
                    erlaubteZeilen.add(muls[h] - zeilenAngaben[i][k]);
                    //window.alert(parseInt(muls[h]}-zeilenAngaben[i][k]));
                    erlaubteZeilen.add(zeilenAngaben[i][k]+muls[h]);
                } 
        }
    }
    return erlaubteZeilen;
}


function makeAllerlaubteZeilenPotenzen(zeilenAngaben) {
    zeilenAngaben = Array.from(zeilenAngaben);
    erlaubteZeilen = new Set();
    for (var i=0; i<zeilenAngaben.length; i++) {
        if (zeilenAngaben[i]>0) {
            exponent = 1
            potenz = Math.pow(zeilenAngaben[i], exponent);
            while (potenz < 1025) {
                erlaubteZeilen.add(potenz);
                potenz = Math.pow(zeilenAngaben[i], exponent);
                //window.alert(potenz);
                exponent++;
            }
        }
    }
    return erlaubteZeilen;
}

function makeAllAllowedZeilenPrimRichtungen() {
    innen = document.getElementById("proInnen").checked;
    aussen = document.getElementById("proAussen").checked;
    hand = document.getElementById("gegenDritte").checked;
    faehig = document.getElementById("proDritte").checked;
    erlaubteZeilen = new Set();
    

    if (hand || faehig) {
        inkrement = (3 ? hand : (2 ? faehig : null));
        for (var i=0; i<1025; i+= inkrement) 
            erlaubteZeilen.add(i)
        return erlaubteZeilen; 
    }

    if (innen || aussen) {
        begin = (3 ? aussen : (2 ? innen : null));
        for (var i=0; i<1025;i++) {
            innenPrimZahl = false;
            for (k=begin; k<primZahlen.length; k+=2) {
                vielfacher = 1;
                while (vielfacher * i < 1025)
                    if (primZahlen[k] == i * vielfacher)
                        innenPrimZahl = true;
            }
            if (innenPrimZahl)
                erlaubteZeilen.add(i);
        }
        return erlaubteZeilen;
    }
}

function makeAllAllowedZeilenHimmelskoerper() {
    sonneWahl = document.getElementById("sonneWahl").checked;
    mondWahl = document.getElementById("mondWahl").checked;
    planetWahl = document.getElementById("planetWahl").checked;
    schwarzeSonneWahl = document.getElementById("schwarzeSonneWahl").checked;
    erlaubteZeilen = new Set();
    if (mondWahl) {
        erlaubteZeilen = new Set(alleMonde);
        return erlaubteZeilen;
    }
    if (sonneWahl) {
        alleMondeSet = new Set(alleMonde)
        for (var i=1; i<1025; i++) {
            if (!alleMondeSet.has(i))
                erlaubteZeilen.add(i);
        }
        return erlaubteZeilen;
    }
    if (planetWahl) {
        for (var i=2; i<1025;i+=2) 
            erlaubteZeilen.add(i);
        return erlaubteZeilen
    }
    if (schwarzeSonneWahl) {
        for (var i=3; i<1025;i+=3) 
            erlaubteZeilen.add(i);
        return erlaubteZeilen
    }
}
function makeAllowedZeilenFromPrimVielfacher(zeilenAngaben) {
    zeilenAngaben = Array.from(zeilenAngaben);
    erlaubteZeilen = new Set();
    ersteSpalte = document.getElementsByTagName("table")[1].getElementsByClassName("r_0");
    for (var i=0; i<1025;i++)
        for (var k=0; k<zeilenAngaben.length; k++) 
            if (zahlIstVielfacherEinerPrimzahl(i, zeilenAngaben[k]))
                erlaubteZeilen.add(i);
    return erlaubteZeilen;
}

function zahlIstVielfacherEinerPrimzahl(zahl, vielfacher) {
    zahl = parseInt(zahl);
    vielfacher = parseInt(vielfacher);
    if (zahl === "NaN" || vielfacher === "Nan")
        return false;

    stimmt = false;
    for (var i=0;i<primZahlen.length; i++)
        if (primZahlen[i] == zahl / vielfacher)
            stimmt=true;
    return stimmt;
}

function makeAllowedZeilenFromZaehlung(zeilenAngaben) {
    zeilenAngaben = Array.from(zeilenAngaben);
    erlaubteZeilen = new Set();
    ersteSpalte = document.getElementsByTagName("table")[1].getElementsByClassName("r_0");
    erlaubteZaehlungen = new Set();
    for (var i=0; i<zeilenAngaben.length; i++) 
        for (var k=zeilenAngaben[i][0]; k<=zeilenAngaben[i][1]; k++) 
            erlaubteZaehlungen.add(k);

    for (i=0; i<ersteSpalte.length; i++) {
        zaehlung = parseInt(ersteSpalte[i].innerHTML.trim());
        if (zaehlung != "NaN" && erlaubteZaehlungen.has(zaehlung)) {
            wirklicheZeile = ersteSpalte[i].className.match(/z_(\d+)/g);
            if (wirklicheZeile.length > 0) {
                wirklicheZeile = wirklicheZeile[0].substr(2);
                erlaubteZeilen.add(parseInt(wirklicheZeile));
            }
        }
    }
    return erlaubteZeilen;
}

function makeAllAllowedZeilen(zeilenAngaben) {
    zeilenAngaben = Array.from(zeilenAngaben);
    erlaubteZeilen = new Set();
    for (var i=0; i<zeilenAngaben.length; i++) {
        for (var k=zeilenAngaben[i][0]; k<=zeilenAngaben[i][1]; k++) {
            erlaubteZeilen.add(k);
        } 
    }
    return erlaubteZeilen;
}

var spalten_r__ = new Set();

function get_r__SpaltenNummern() {
    tabelenkopfZeile = tdClasses;
    for (var i=0; i<tabelenkopfZeile.length; i++) {
        if (tabelenkopfZeile[i].style.display === 'table-cell') {
            num = tabelenkopfZeile[i].className.match(/r_(\d+)/);
	        if (num != null && num.length > 1)
    			num = num[1];
            spalten_r__.add(num);
        }
    }
}

/*
var verboteneZeilen = [];

function invertErlaubteZeilen() {
    verboteneZeilen = [];
    for (var i=0; i<1025; i++) {
        if ((!i in erlaubteZeilen))
            verboteneZeilen.push(i);
    }
}
*/



function erlaubeVerbieteZeilenBeiZeilenErlaubenVerbieten(which) {
    Spalten_r__Array = Array.from(spalten_r__);
    erlaubteZeilen_Array = Array.from(erlaubteZeilen);
    erlaubteZeilen_String = erlaubteZeilen_Array.join(",");
    neuErlauben = document.getElementsByClassName("neuErlauben")[which].checked;
    neuHinfort = document.getElementsByClassName("neuHinfort")[which].checked;
    dazuErlauben = document.getElementsByClassName("dazuErlauben")[which].checked;
    dazuHinfort = document.getElementsByClassName ("dazuHinfort")[which].checked;
    //window.alert(neuErlauben+" "+neuHinfort+" "+dazuErlauben+" "+dazuHinfort);
    spalte = document.getElementsByTagName("table")[1].getElementsByTagName("tr");
    for (var s=1; s<spalte.length; s++) {
        tabellenZelle = spalte[s];
        if (s<115)
            zeilenLetztendlichZeigenVerstecken(s, neuErlauben, dazuErlauben, neuHinfort, dazuHinfort, tabellenZelle);
        else {
            echteZeilenNummer = spalte[s].getElementsByTagName("td")[0].className.match(/z_(\d+)/g);
            if (echteZeilenNummer != null && echteZeilenNummer.length > 0) {
                echteZeilenNummer = parseInt(echteZeilenNummer[0].substr(2));
                zeilenLetztendlichZeigenVerstecken(echteZeilenNummer, neuErlauben, dazuErlauben, neuHinfort, dazuHinfort, tabellenZelle);
            }

        }
    }
}

function zeilenLetztendlichZeigenVerstecken(s, neuErlauben, dazuErlauben, neuHinfort, dazuHinfort, tabellenZelle) {
    if (((erlaubteZeilen.has(s) && (neuErlauben || dazuErlauben)) || (! erlaubteZeilen.has(s) && neuHinfort)) && (! dazuHinfort))
        tabellenZelle.style.display = 'table-row';
    else
        if (((neuErlauben || neuHinfort) && !dazuErlauben) || (dazuHinfort && erlaubteZeilen.has(s)))
            tabellenZelle.style.display = 'none';
}


function clickPotenzenErlaubenUsw() {
    makeAllerlaubteZeilenPotenzen(potenzenAngabenToContainer());
    get_r__SpaltenNummern();
    erlaubeVerbieteZeilenBeiZeilenErlaubenVerbieten(2);
}


function clickVielfacheErlaubenUsw() {
    makeAllerlaubteZeilenVielfacher(vielfacherAngabentoContainer());
    get_r__SpaltenNummern();
    erlaubeVerbieteZeilenBeiZeilenErlaubenVerbieten(1);
}

function clickHimmelskoerperErlaubenUsw() {
    erlaubteZeilen = makeAllAllowedZeilenHimmelskoerper();
    get_r__SpaltenNummern();
    erlaubeVerbieteZeilenBeiZeilenErlaubenVerbieten(3);
}

function clickZeilenErlaubenUsw() {
    makeAllAllowedZeilen(zeilenAngabenToContainer(1));
    get_r__SpaltenNummern();
    erlaubeVerbieteZeilenBeiZeilenErlaubenVerbieten(0);
}

function clickZaehlungenErlaubenUsw() {
    makeAllowedZeilenFromZaehlung(zeilenAngabenToContainer(2));
    get_r__SpaltenNummern();
    erlaubeVerbieteZeilenBeiZeilenErlaubenVerbieten(4);
}
function clickPrimVielfacheErlaubenUsw() {
    makeAllowedZeilenFromPrimVielfacher(zeilenAngabenToContainer(3));
    get_r__SpaltenNummern();
    erlaubeVerbieteZeilenBeiZeilenErlaubenVerbieten(5);
}
function clickPrimRichtungenErlaubenUsw() {
    erlaubteZeilen = makeAllAllowedZeilenPrimRichtungen();
    get_r__SpaltenNummern();
    erlaubeVerbieteZeilenBeiZeilenErlaubenVerbieten(6);
}
