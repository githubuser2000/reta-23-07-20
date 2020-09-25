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
	for (i = 0; i < tdClasses.length; i++) {
		name = tdClasses[i].className;
		var num = name.match(/r_(\d+)/)
		if (num != null) {
			//num = num.substring(2,0);
			num = parseInt(num[1]);
			str = num[1]
			//num = i
			if (typeof SpaltenArray[num] === 'undefined')
				SpaltenArray[num]= new Set();
			SpaltenArray[num].add(name);
		}
	}
	//str = SpaltenArray[1].values();
	str = SpaltenArray.length;
	//str = tdClasses.length;
	div.innerHTML = str;
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

// geht nicht, weil Zellen verrutschen
/*		for (i = 0; i < col.length; i++)
			if (col[i].innerHTML.trim().length == 0) 
				col[i].style.display = 'none';
			else
				if (i == 0)
					window.alert(col[i].innerHTML + ' ! ');
*/
		

	} else {
		window.alert(col[0].innerHTML + ' ! ');
	}
}
