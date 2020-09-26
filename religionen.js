var col =  document.getElementsByClassName('RowNumber 1');
window.onload = function() {
  var headingsDiv =  document.getElementById('Tabelle01');
  let div = document.createElement('div');
  div.className = "headingsDiv";
  tdClasses = document.getElementsByTagName("td");
	var str = "", sArr = [], tdClassesSet = new Set();
	for (i = 0; i < tdClasses.length; i++) {
		name = tdClasses[i].className
		if (name.includes("RowNumber")) {
			tdClassesSet.add(tdClasses[i].className);
		}
	}
	var tdClasses2 = Array.from(tdClassesSet);
	for (i = 0; i < tdClasses2.length; i++) {
		sArr[i] = tdClasses2[i];
	}
	var sArr2 = [], eachClasses = [];
	for (i = 0; i < tdClasses2.length; i++) {
		eachClasses = document.getElementsByClassName(tdClasses2[i]);
		if ( eachClasses[0].innerHTML.trim().length == 0)
			textfield = eachClasses[1].innerHTML + ' - ' + eachClasses[eachClasses.length-1].innerHTML
		else
			textfield = eachClasses[0].innerHTML
		checkbox = '<input type="checkbox" value="'+textfield+'" onchange="toggleCol(\''+tdClasses2[i]+'\');"><label>'+textfield+'</label>'
		sArr2[i]=checkbox
	}
	str = sArr2.join(" ");
 	document.body.before(div);
	tdClasses = document.getElementsByTagName("td");
	SpaltenArray = new Array();
	p1map = {},p2map = {},mapMapMap = {}, str = "";
	for (i = 0; i < tdClasses.length; i++) {
		name = tdClasses[i].className;
		var num = name.match(/r_(\d+)/)
		if (num != null) {
			//num = num.substring(2,0);
			num = parseInt(num[1]);
			str = num[1];
			//num = i
			var p1 = name.match(/p1_([^\s]+)/);
			if (p1 != null) {
				p1 = p1[1].match(/([^,]+)/);
				if (p1 != null) {
					if (typeof p1map[p1[1]] === 'undefined')
						p1map[p1[1]]= new Set();
					p1map[p1[1]].add(name);
				}
			}
			var p2 = name.match(/p2_([^\s]+)/)
			if (p2 != null) {
				p2 = p2[1].match(/([^,]+)/);
				if (p2 != null) {
					if (typeof p2map[p2[1]] === 'undefined')
						p2map[p2[1]]= new Set();
					p2map[p2[1]].add(name);
				}
			}

			if (p2 != null && p1 != null) {
				p2 = p2[1].match(/([^,]+)/);
				p1 = p1[1].match(/([^,]+)/);
				if (p2 != null && p1 != null) {
					if (typeof SpaltenArray[num] === 'undefined')
						SpaltenArray[num]= new Set();
					SpaltenArray[num].add(name);

					if (typeof mapMapMap[p1[1]] === 'undefined')
						mapMapMap[p1[1]]= new Array();
					if (typeof mapMapMap[p1[1]][p2[1]] === 'undefined')
						mapMapMap[p1[1]][p2[1]]= new Set();
					//if (typeof mapMapMap[p1[1]][p2[1]][num] === 'undefined')
					//	mapMapMap[p1[1]][p2[1]][num]= new Set();
					mapMapMap[p1[1]][p2[1]].add(num);
					//str = mapMapMap[p1[1]][p2[1]][num].values().next().value;
					str2 = '';
					var p1mapSetIterator = p1map[p1[1]].values();
					for (k = 0; k < p1map[p1[1]].size; k++) {
						str2 = str2 + p1mapSetIterator.next().value + ', ';

					}
				}
			}
		}
	}

	var p1keys = Object.keys(p1map);
	checkboxes = "";
	for (i = 0; i < p1keys.length; i++) {
		var chk2s = "";
		if (typeof mapMapMap[p1keys[i]] !== 'undefined')
			for (k = 0; k < mapMapMap[p1keys[i]].length; i++) {
				chk2 = '<input type="checkbox" value="'+mapMapMap[p1keys[i]][k]+'" onchange="toggleP1(\''+mapMapMap[p1keys[i]][k]+'\');"><label>'+mapMapMap[p1keys[i]][k]+'</label>';
				chk2s = chk2s + chk2;
			}
		checkbox = '<input type="checkbox" value="'+p1keys[i]+'" onchange="toggleP1(\''+p1keys[i]+'\');"><label>'+p1keys[i]+'</label><div id="'+p1keys[i]+'" style="display:none">'+chk2s+'</div>';
		checkboxes = checkboxes + checkbox;
	}
	str2 = checkboxes;
	/*
	var p2keys = Object.keys(p2map);
	checkboxes = ""
	for (i = 0; i < p2keys.length; i++) {
		checkbox = '<input type="checkbox" value="'+p2keys[i]+'" onchange="toggleCol(\''+tdClasses2[i]+'\');"><label>'+p2keys[i]+'</label>';
		checkboxes = checkboxes + checkbox;
	}
	str2 = checkboxes;
	*/
	//str = SpaltenArray[1].values();
	//str = tdClasses.length;
	div.innerHTML = str2;
}

function toggleP1(p1) {
	p2 = document.getElementById(p1);
	if (typeof(p2.style) != "undefined") 
 		if (p2.style.display != 'none') 
			p2.style.display = 'none';
		else 
			p2.style.display = 'table-cell';
	else 
		window.alert(p2.innerHTML + ' ! ');
	
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
