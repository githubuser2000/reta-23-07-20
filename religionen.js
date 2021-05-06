var col =  document.getElementsByClassName('RowNumber 1');
var selectedSpaltenMany1 = {};
var selectedSpaltenMany2 = {};
window.onload = function() {
var headingsDiv =  document.getElementById('Tabelle01');
let div = document.createElement('div');
div.className = "headingsDiv";
document.body.before(div);
chk_spalten = "<input type=\"checkbox\" onchange=\"toggleChkSpalten();\"><label>Spalten Checkboxen</label>"
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
	checkboxes = "<div id=\"chk_spalten\" style=\"display:none\"><span style=\"white-space: nowrap;\">";
	for (i = 0; i < p1keys.length; i++) {
		var chk2s = "";
		var p2keys = Object.keys(mapMapMap[p1keys[i]]);
		for (k = 0; k < p2keys.length; k++) {
			numbers = Array.from(mapMapMap[p1keys[i]][p2keys[k]]);
			if (p2keys[k] != null && p2keys[k] != 'null') {
				chk2 = '<input type="checkbox" value="'+p2keys[k]+'" onchange="toggleP2(\''+numbers+'\',\''+[p1keys[i],p2keys[k]]+'\');"><label>'+makeSpacesOutOf_(p2keys[k])+'</label>';
				chk2s = chk2s + chk2;
			}
			
		}
		if ( mapMapMap[p1keys[i]][null] !== undefined ) {
			numbers = Array.from(mapMapMap[p1keys[i]][null]);
			insertnull = 'toggleP2(\''+numbers+'\',\''+[p1keys[i],null]+'\');'
		} else {
			insertnull = '';
		}
		checkbox = '<br><input type="checkbox" value="'+p1keys[i]+'" onchange="toggleP1(\''+p1keys[i]+'\');'+insertnull+'"><label>'+makeSpacesOutOf_(p1keys[i])+'</label><div id="'+p1keys[i]+'" style="display:none">'+chk2s+'</div>';
		checkboxes += checkbox;
	}
	str2 = checkboxes + "</span></div>";
	div.innerHTML += str2;

    // Spaltenreihenfolge
	tableHeadline = document.getElementsByTagName('tr')[0].getElementsByTagName('td');
    for (var u=0; u<tableHeadline.length; u++) {
        tableHeadline[u].innerHTML += '<select id="hselec_'+u+'" value="'+u+'" onchange="headingselected(this, '+u+');"></select>'
    }
}

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
    var forNewString = [];
    for (var i=0; i<text.length; i++)
        if (text[i] == '_')
            forNewString.push(' ');
        else
            forNewString.push(text[i]);
    return forNewString.join("");
}


function toggleP2(spaltenNummern, para1u2) {
	//window.alert(spaltenNummern);
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
    sortedKeysOfHeadingNumbers();
    setHeadingsAmount();
    updateSpaltenValues();
}

function updateSpaltenValues() {
    keys = Object.keys(visibleHeadingsSelect);
    for (var i=0; i<keys.length; i++) {
        visibleHeadingsNumbers[keys[i]] = visibleHeadingsSelect[keys[i]].value;
    }
    keys2 = Object.keys(visibleHeadingsNumbers);
    //window.alert("vis num"+ keys2.length)
    //window.alert("vis num 0: "+ visibleHeadingsNumbers[keys2[0]])
}

function toggleName(p2) {
	if (p2.style.display != 'none') 
		p2.style.display = 'none';
	else 
		p2.style.display = 'table-cell';
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
	cols = document.getElementsByClassName('r_'+colNumber);
	if (typeof(selectedSpaltenMany2[colNumber]) === 'undefined') { 
		away = true;
		//window.alert("undefined "+colNumber);
	} else
		away = selectedSpaltenMany2[colNumber].length==0;
	//window.alert("Stelle "+colNumber+"hat Länge "+selectedSpaltenMany2[colNumber].length);
	if (typeof(cols[0].style) != "undefined") {
		if (cols[0].style.display == 'none')
            changeHeadline(cols[0], true);
        else
            if (away)
                changeHeadline(cols[0], false);

		for (i=0; i < cols.length; i++) { 
			if (cols[i].style.display == 'none')
				cols[i].style.display = 'table-cell';
			else 
				if (away)
					cols[i].style.display = 'none';
		}
     }
	 else 
		window.alert(cols[0].innerHTML + ' ! '+colNumber);

}

var tableHeadline;
var visibleHeadingsSelect = {};
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
        visibleHeadingsSelect[num]=sel;
    else
        if (num in visibleHeadingsSelect)
            delete visibleHeadingsSelect[num];
	//window.alert(Object.keys(visibleHeadingsSelect).length);
}

function headingselected(gewaehlteSpalte_plusgleich1, momentaneSpalte_als_r_) {
    gewaehlteSpalte_plusgleich1 = gewaehlteSpalte_plusgleich1.value;
    //for (var i=0; i<optionsS.length; i++) {
    zwei = gewaehlteSpalte_plusgleich1.split(",");
    gewaehlteSpalte_plusgleich1 = zwei[0];
    gewaehlteSpalte_als_r_ = zwei[1];
    //window.alert('PROGRAMMIERBAUSTELLE! UNFERTIG! momenante Spalte als r_:  '+momentaneSpalte_als_r_+' gewählte als +=1: '+zwei[0]+' und '+zwei[1]);
    //window.alert(gewaehlteSpalte_plusgleich1);
    //window.alert(gewaehlteSpalte_plusgleich1.target.value);
/*
    visHeadSel = Object.keys(visibleHeadingsSelect);
    visHeadSel.sort((a,b) => a-b);

    gewaehlteSpalte_als_r_ = visHeadSel[gewaehlteSpalte_plusgleich1]; // dieses mal als r_ angabe statt +=1
    */
    //momentaneSpalte_plusgleich1 = visibleHeadingsSelect[momentaneSpalte_als_r_].value; // dieses mal als +=1 angabe statt als r_
    momentaneSpalte_plusgleich1 = visibleHeadingsNumbers[momentaneSpalte_als_r_]; // dieses mal als +=1 angabe statt als r_
    zwei = momentaneSpalte_plusgleich1.split(",");
    momentaneSpalte_plusgleich1 = zwei[0];
    /*
    //visibleHeadingsSelect[visHeadSel[i]].innerHTML; // = optionsS[i].join("");
    //window.alert(gewaehlteSpalte_als_r_);
    //window.alert(momentaneSpalte_als_r_);
    window.alert(Object.keys(visibleHeadingsSelect)[0]+' '+Object.keys(visibleHeadingsSelect)[1]+' '+Object.keys(visibleHeadingsSelect)[2]+' ');
    window.alert(visibleHeadingsSelect[2].value+' '+visibleHeadingsSelect[8].value+' '+visibleHeadingsSelect[38].value);
    window.alert(visibleHeadingsSelect[gewaehlteSpalte_als_r_].value);
    window.alert(visibleHeadingsSelect[momentaneSpalte_als_r_].value);
    //window.alert(visHeadSel[visibleHeadingsSelect[gewaehlteSpalte_als_r_].value]);
    //window.alert(visHeadSel[visibleHeadingsSelect[momentaneSpalte_als_r_].value]);
    */

    //window.alert(Object.keys(visibleHeadingsSelect)[0]+' '+Object.keys(visibleHeadingsSelect)[1]+' '+Object.keys(visibleHeadingsSelect)[2]+' ');
    //window.alert(visibleHeadingsSelect[2].value+' '+visibleHeadingsSelect[8].value+' '+visibleHeadingsSelect[38].value);
	var spalte1ToChange = document.getElementsByClassName('r_'+gewaehlteSpalte_als_r_);
    seli = spalte1ToChange[0].getElementsByTagName("select")[0].getElementsByTagName("option");
    //window.alert("momentane Spalte: "+momentaneSpalte_plusgleich1)
    selival = selectionsBefore[momentaneSpalte_plusgleich1] + 1;
    gewaehlteSpalte_plusgleich1 = selival - 2; // 1 bis +=1
    //window.alert("drüben selected gemacht Nummer: "+selival+" unter "+seli.length);
    //for (var k=0; k<seli.length; k++) {
    seli[selival].selected = 'selected';
    //}
    //window.alert(Object.keys(visibleHeadingsSelect)[0]+' '+Object.keys(visibleHeadingsSelect)[1]+' '+Object.keys(visibleHeadingsSelect)[2]+'\n'+visibleHeadingsSelect[2].value+' '+visibleHeadingsSelect[8].value+' '+visibleHeadingsSelect[38].value);

	var spalte2ToChange = document.getElementsByClassName('r_'+momentaneSpalte_als_r_);
    //window.alert(spalte2ToChange[0].innerHTML);
    //window.alert(spalte1ToChange[0].innerHTML);

    var name1 = [];
    var name2 = [];
    var c1 = spalte1ToChange[0].className;
    var c2 = spalte2ToChange[0].className;
    for (var u=0; u<c1.length; u++) {
        if (c1[])
        name1.push()
    }
    var g = document.querySelector('.'+spalte1ToChange[0].className+'+.'+spalte2ToChange[0].className) 
    window.alert(g)
    var merke = [];
    // window.alert("len of loop: "+spalte1ToChange.length);
    /*
    for (var i=0; i<spalte1ToChange.length; i++) {
        merke.push(spalte2ToChange[i].outerHTML)
        spalte2ToChange[i].outerHTML = spalte1ToChange[i].outerHTML;
        spalte1ToChange[i].outerHTML = merke[i];
    }
    setHeadingsAmount()
    */
}

var selectionsBefore = {};
var optionsS = [];
var sichtbareSpaltenNummern;

function sortedKeysOfHeadingNumbers() {
	tableHeadline = document.getElementsByTagName('tr')[0].getElementsByTagName('td');
    sichtbareSpaltenNummern = []
    for (var i=0; i<tableHeadline.length; i++) {
        if (tableHeadline[i].style.display == 'table-cell') {
            sichtbareSpaltenNummern.push(tableHeadline[i].className.match(/r_(\d+)/g)[0].substring(2));
        }
    }
    //window.alert('sichtb spalten nummern '+sichtbareSpaltenNummern[0]+' '+sichtbareSpaltenNummern[1]);
}

function setHeadingsAmount() {
    var options;
    optionsS = [];
    var keys = Object.keys(visibleHeadingsSelect);
    var len = keys.length;
	//window.alert(visibleHeadingsSelect.length);
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

    visHeadSel = Object.keys(visibleHeadingsSelect);
    visHeadSel.sort((a,b) => a-b);

    for (var i=0; i<optionsS.length; i++) {
	    //window.alert(visHeadSel[i]);
        visibleHeadingsSelect[visHeadSel[i]].innerHTML = optionsS[i].join("");
    }
}

function toggleChkSpalten() {
	chk_spalten = document.getElementById("chk_spalten");
	if (chk_spalten.style.display == 'none')
		chk_spalten.style.display = 'initial';
	else 
		chk_spalten.style.display = 'none';
}
