var col =  document.getElementsByClassName('RowNumber 1');
var selectedSpaltenMany1 = {};
var selectedSpaltenMany2 = {};
window.onload = function() {
  var headingsDiv =  document.getElementById('Tabelle01');
  let div = document.createElement('div');
  div.className = "headingsDiv";
  tdClasses = document.getElementsByTagName("td");
 	document.body.before(div);
	tdClasses = document.getElementsByTagName("td");
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
	checkboxes = "<span style=\"white-space: nowrap;\">";
	for (i = 0; i < p1keys.length; i++) {
		var chk2s = "";
		var p2keys = Object.keys(mapMapMap[p1keys[i]]);
		for (k = 0; k < p2keys.length; k++) {
			numbers = Array.from(mapMapMap[p1keys[i]][p2keys[k]]);
			if (p2keys[k] != null && p2keys[k] != 'null') {
				chk2 = '<input type="checkbox" value="'+p2keys[k]+'" onchange="toggleP2(\''+numbers+'\',\''+[p1keys[i],p2keys[k]]+'\');"><label>'+p2keys[k]+'</label>';
				chk2s = chk2s + chk2;
			}
			
		}
		if ( mapMapMap[p1keys[i]][null] !== undefined ) {
			numbers = Array.from(mapMapMap[p1keys[i]][null]);
			insertnull = 'toggleP2(\''+numbers+'\',\''+[p1keys[i],null]+'\');'
		} else {
			insertnull = '';
		}
		checkbox = '<br><input type="checkbox" value="'+p1keys[i]+'" onchange="toggleP1(\''+p1keys[i]+'\');'+insertnull+'"><label>'+p1keys[i]+'</label><div id="'+p1keys[i]+'" style="display:none">'+chk2s+'</div>';
		checkboxes += checkbox;
	}
	str2 = checkboxes + "</span>";
	div.innerHTML = str2;
}


function toggleP2(numbers,para1u2) {
	numbers = numbers.split(',');
	existingParameterNamesArrayIndex = MatrixHasCouple(para1u2, selectedSpaltenMany2);
	//window.alert((existingParameterNamesArrayIndex.size > 0));
	if (existingParameterNamesArrayIndex.size > 0) {
		existingParameterNamesKeys = Array.from(existingParameterNamesArrayIndex);
		//window.alert(existingParameterNamesKey);
		/*window.alert(existingParameterNamesArrayIndex);
		window.alert("obj: "+selectedSpaltenMany2[0]);*/
		//for (i=0; i<existingParameterNamesArrayIndex.length; i++) {
		//window.alert("index: "+existingParameterNamesArrayIndex[i]);
		//selectedSpaltenMany2 .splice(existingParameterNamesArrayIndex[i], 1);
		for (i=0; i<existingParameterNamesKeys.length; i++){
			for (k=0; k<selectedSpaltenMany2[existingParameterNamesKeys[i]].length; k++) {
				if (selectedSpaltenMany2[existingParameterNamesKeys[i]][k] == para1u2 ) {
					selectedSpaltenMany2[existingParameterNamesKeys[i]].splice(k,1);
					//window.alert("yes: "+i+" "+k+" para:"+para1u2);
				} else {
					//window.alert("no");
				}
			}
		}
		toggleForNums(numbers);
	} else {
		for (i=0; i<numbers.length; i++)
			if (typeof(selectedSpaltenMany2[numbers[i]]) !== "undefined")
				selectedSpaltenMany2[numbers[i]].push(para1u2);
			else
				selectedSpaltenMany2[numbers[i]]=[para1u2];
		toggleForNums(numbers);
	}
}

function MatrixHasCouple(couple, SpaltenNumberToParameters) {
	//matrix = Array.from(matrix);
	existing = new Set();
	//window.alert("drin: "+Object.keys(SpaltenNumberToParameters).length);
	for (var key in SpaltenNumberToParameters) {
		for (i=0; i<SpaltenNumberToParameters[key].length; i++) {
			for (k=0; k<SpaltenNumberToParameters[key].length; k++) {
				//really = true;
				if (SpaltenNumberToParameters[key][k] != couple) {
					//window.alert("YES couple: "+couple);
					//window.alert("YES matrix el: "+SpaltenNumberToParameters[key][k]);
					//really = false
				} else {
					existing.add(key);
					//window.alert("NO couple: "+couple);
					//window.alert("NO matrix el: "+SpaltenNumberToParameters[key][k]);
				}
			}
		}
		/*
		if (really) {
			window.alert("ja: "+k);
			//existing.add(key);
		}*/
	}
	return existing;
}

function toggleForNums(numbers) {
	for (n = 0; n < numbers.length; n++) {
		if (typeof(selectedSpaltenMany2[numbers]) === 'undefined')
			toggleSpalten(numbers[n]);
		else {
			//window.alert(numbers+" has "+selectedSpaltenMany2[numbers].length+" length");
			/*NumbersFilled = [];
			for (i=0; i<numbers[n].length; i++) {
				window.alert("place "+[numbers[i]]+"("+i+") has "+selectedSpaltenMany2[numbers[i]].length+" length: ");
				NumbersFilled.push(selectedSpaltenMany2[numbers[i]].length!=0);
			}*/
			//toggleSpalten('r_'+numbers[n],NumbersFilled);
			toggleSpalten(numbers[n]);
		}
	}
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
	col = document.getElementsByClassName('r_'+colNumber);
	if (typeof(selectedSpaltenMany2[colNumber]) === 'undefined') { 
		away = true;
		window.alert("undefined "+colNumber);
	} else
		away = selectedSpaltenMany2[colNumber].length==0;
	//window.alert("Stelle "+colNumber+"hat Länge "+selectedSpaltenMany2[colNumber].length);
	if (typeof(col[0].style) != "undefined") 
		for (i=0; i < col.length; i++) { 
			if (col[i].style.display == 'none')
				col[i].style.display = 'table-cell';
			else 
				if (away)
					col[i].style.display = 'none';
		}
	 else 
		window.alert(col[0].innerHTML + ' ! '+colNumber);
}
