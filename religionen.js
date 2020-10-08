var col =  document.getElementsByClassName('RowNumber 1');
var selectedSpaltenMany1 = {};
var selectedSpaltenMany2 = new Set();
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
			var p1a = name.match(/p1_[^\s]+/g);
			var p2a = name.match(/p2_[^\s]+/g);
			if (p1a != null) {
				for (p1i = 0; p1i < p1a.length; p1i++) {
					p1b = p1a[p1i].substring(3).match(/[^,]+/g);
					if (p1b != null) {
					for (p1k = 0; p1k < p1b.length; p1k++) {
							p1 = p1b[p1k];
							if (typeof mapMapMap[p1] === 'undefined')
								mapMapMap[p1]= {};
							if (p2a != null) {
								for (p2i = 0; p2i < p2a.length; p2i++) {
									p2b = p2a[p2i].substring(3).match(/[^,]+/g);
									if (p2b != null) {
										for (p2k = 0; p2k < p2b.length; p2k++) {
											p2 = p2b[p2k];
											if (p2 != null) {
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
	//checkboxes = "<span style=\"white-space: nowrap;\"><input type=\"checkbox\" onchange=\"toggleCol(\'r_0\');\"><label>Nummererierung</label>";
	checkboxes = "<span style=\"white-space: nowrap;\">";
	for (i = 0; i < p1keys.length; i++) {
		var chk2s = "";
		var p2keys = Object.keys(mapMapMap[p1keys[i]]);
		for (k = 0; k < p2keys.length; k++) {
			numbers = Array.from(mapMapMap[p1keys[i]][p2keys[k]]);
			if (p2keys[k] != null && p2keys[k] != 'null') {
				chk2 = '<input type="checkbox" value="'+p2keys[k]+'" onchange="toggleP2(\''+numbers+'\');"><label>'+p2keys[k]+'</label>';
				chk2s = chk2s + chk2;
			}
			
		}
		if ( mapMapMap[p1keys[i]][null] !== undefined ) {
			numbers = Array.from(mapMapMap[p1keys[i]][null]);
			insertnull = 'toggleP2(\''+numbers+'\');'
		} else {
			insertnull = '';
		}
		checkbox = '<br><input type="checkbox" value="'+p1keys[i]+'" onchange="toggleP1(\''+p1keys[i]+'\');'+insertnull+'"><label>'+p1keys[i]+'</label><div id="'+p1keys[i]+'" style="display:none">'+chk2s+'</div>';
		checkboxes += checkbox;
	}
	str2 = checkboxes + "</span>";
	div.innerHTML = str2;
}


function toggleP2(numbers) {
	numbers = numbers.split(',');
	if (selectedSpaltenMany2.has(numbers)) {
		toggleForNums(numbers,false);
		selectedSpaltenMany2.delete(numbers)
	} else {
		toggleForNums(numbers,true);
		selectedSpaltenMany2.add(numbers)
	}
}

function toggleForNums(numbers,really) {
	for (n = 0; n < numbers.length; n++) {
		for ( i=0 ; i < selectedSpaltenMany2.length; i++) {
			for (k=0; k < selectedSpaltenMany2[i].length; k++) {
				if ( (selectedSpaltenMany2[i][k] == numbers[n]) === really) {
					toggleCol('r_'+numbers[n], really);
				}
			}
		}
//		if (numbers[n] ==  )
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
function toggleCol2(col, really) {
	col = document.getElementsByClassName(col);
	if (typeof(col[0].style) != "undefined") {
 		if (col[0].style.display != 'none') 
			for (i = 0; i < col.length; i++)
				col[i].style.display = 'none';
		else 
			for (i = 0; i < col.length; i++)
				col[i].style.display = 'table-cell';
	} else {
		window.alert(col[0].innerHTML + ' ! ');
	}
}
function toggleCol(col) {
	col = document.getElementsByClassName(col);
	if (typeof(col[0].style) != "undefined") {
 		if (col[0].style.display != 'none') 
			for (i = 0; i < col.length; i++)
				col[i].style.display = 'none';
		else 
			for (i = 0; i < col.length; i++)
				col[i].style.display = 'table-cell';
	} else {
		window.alert(col[0].innerHTML + ' ! ');
	}
}
