var col = document.getElementsByClassName("RowNumber 1");
var selectedSpaltenMany1 = {};
var selectedSpaltenMany2 = {};
var labelstyle = "white-space: nowrap;font-size: 100%;";
var labelstylekl = "white-space: nowrap;font-size: 80%;color: grey;";
var Enume = new Set([0, 1, 3, 4]);
window.onload = function () {
  let div = document.createElement("div");
  let div2 = document.createElement("div");
  div.className = "headingsDiv";
  /* 
    sternPolygon = 0
    gleichfoermigesPolygon = 1
    keinPolygon = 2
    galaxie = 3
    universum = 4
*/
  document.body.insertBefore(div, document.getElementsByTagName("table")[0]);
  chk_spalten =
    '<fieldset style="font-size: 100%;"><input type="radio" id="spaltenWahl" name="spaltOrZeilWahl" onchange="toggleChkSpalten(this);" checked="true"><label>Spalten Checkboxen</label><input type="radio" id="zeilenWahl" name="spaltOrZeilWahl" onchange="toggleChkSpalten(this);"><label>Zeilen Eingabefelder</label><input type="radio" id="keinsWahl" name="spaltOrZeilWahl" onchange="toggleChkSpalten(this);"><label>frei machen zur Tabellenansicht</label></fieldset>';
  radio_tags =
    '<fieldset style="font-size: 100%;float:left; display:inline-block;"><input type="radio" id="galaxieuniversum" name="galaxieuniversum" onchange="disEnAbleChks([3,4]);" checked="true"><label>Galaxie und Universum</label><input type="radio" id="galaxie" name="galaxieuniversum" onchange="disEnAbleChks([3]);"><label>Galaxie (14)</label><input type="radio" id="universum" name="galaxieuniversum" onchange="disEnAbleChks([4]);"><label>Universum (15)</label></fieldset><fieldset style="font-size: 100%;"><input type="radio" id="sternpolygongleichfoermigespolygon" name="sternpolygongleichfoermigespolygon" onchange="disEnAbleChks([0,1]);" checked="true"><label>Sternpolygon und gleichförmiges Polygon</label><input type="radio" id="sternpolygon" name="sternpolygongleichfoermigespolygon" onchange="disEnAbleChks([0]);"><label>Sternpolygon (n)</label><input type="radio" id="gleichfoermigespolygon" name="sternpolygongleichfoermigespolygon" onchange="disEnAbleChks([1]);"><label>gleichförmiges Polygon (1/n)</label></fieldset>';
  div.innerHTML = chk_spalten;
  tdClasses = document.getElementsByClassName("z_0");
  /*tdClasses = []
for (i = 0; i < tdClasses1.length; i++) 
	if (tdClasses1[i].className.includes("z_0"))
		tdClasses.push(tdClasses1[i]);*/
  (p1map = {}),
    (p2map = {}),
    (mapMapMap = {}),
    (str = ""),
    (p1Bmap = {}),
    (mapMapMapTags = {}),
    (spaltenTags = []),
    (spalten4spaltenTags = {});
  str3 = "";

  TRs = document.getElementsByTagName("tr");
  for (var i = 0; i < TRs.length; i++) {
    TDs = TRs[i].getElementsByTagName("td");
    for (var k = 0; k < TDs.length; k++) {
      if (typeof spalten4spaltenTags[k] == "undefined")
        spalten4spaltenTags[k] = [];
      spalten4spaltenTags[k].push(TDs[k]);
    }
  }

  for (i = 0; i < tdClasses.length; i++) {
    name = tdClasses[i].className;
    var num = name.match(/r_(\d+)/);

    var tags = name.match(/p4_([\d,]+)/g);
    if (tags === null) tags = [];
    else tags = String(tags).substr(3).split(",");
    tags = Array.from(new Set(tags));
    spaltenTags.push(tags);

    if (num != null) {
      //num = num.substring(2,0);
      num = parseInt(num[1]);
      str = num[1];
      //num = i
      var p1a = name.match(/p1_([^\s])+/g);
      var p2a = name.match(/p2_([^\s])+/g);
      if (p1a != null) {
        for (p1i = 0; p1i < p1a.length; p1i++) {
          if (p1a[p1i].includes("p1_")) p1a[p1i] = p1a[p1i].substring(3);
          p1b = p1a[p1i].match(/[^,]+/g);
          if (p1b != null) {
            for (p1k = 0; p1k < p1b.length; p1k++) {
              p1 = p1b[p1k];
              if (typeof mapMapMap[p1] === "undefined") mapMapMap[p1] = {};
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
                            if (p2.length > 0)
                              makeMapsOfHeadLCheckB(p1, p2, num, tags);
                            else makeMapsOfHeadLCheckB(p1, null, num, tags);
                          }
                        }
                      } else makeMapsOfHeadLCheckB(p1, null, num, tags);
                    }
                  }
                }
              } else makeMapsOfHeadLCheckB(p1, null, num, tags);
            }
          }
        }
      }
    }
  }

  var p1keys = Object.keys(mapMapMap);
  var p1Bkeys = Object.keys(p1Bmap);
  //checkboxes = "<span style=\"white-space: nowrap;\"><input type=\"checkbox\" onchange=\"toggleSpalten(\'r_0\');\"><label>Nummererierung</label>";
  checkboxes =
    '<div id="chk_spalten" style="display:none;">' +
    radio_tags +
    '<span style="">';
  for (i = 0; i < p1keys.length; i++) {
    var chk2s = "";
    var p2keys = Object.keys(mapMapMap[p1keys[i]]);
    for (k = 0; k < p2keys.length; k++) {
      numbers = Array.from(mapMapMap[p1keys[i]][p2keys[k]]);
      if (p2keys[k] != null && p2keys[k] != "null") {
        chk2 =
          '<label style="' +
          labelstyle +
          '" class="chks c_' +
          Array.from(mapMapMapTags[p1keys[i]][p2keys[k]]).join(",") +
          '" ><input type="checkbox" class="chks c_' +
          Array.from(mapMapMapTags[p1keys[i]][p2keys[k]]).join(",") +
          '" value="' +
          p2keys[k] +
          '" onchange="toggleP2(this,\'' +
          numbers +
          "','" +
          [p1keys[i], p2keys[k]] +
          "');\">" +
          makeSpacesOutOf_(p2keys[k]) +
          '</label><label style="white-space: normal;">&nbsp; </label>';
        chk2s += chk2;
      }
    }
    if (mapMapMap[p1keys[i]][null] !== undefined) {
      numbers = Array.from(mapMapMap[p1keys[i]][null]);
      insertnull =
        "toggleP2(this,'" + numbers + "','" + [p1keys[i], null] + "');";
    } else {
      insertnull = "";
    }
    mapsTagsif = mapMapMapTags[p1keys[i]][null];
    if (typeof mapsTagsif == "undefined") mapsTagsif = [];
    else mapsTagsif = Array.from(mapMapMapTags[p1keys[i]][null]);
    //window.alert(mapsTagsif);

    checkbox =
      '<div class="chksA"><input type="checkbox" ' + // class="chks c_' +
      //Array.from(mapMapMap[p1keys[i]][null]).join(",") +
      //'"  value="' +
      ' value="' +
      p1keys[i] +
      '" onchange="toggleP1(\'' +
      p1keys[i] +
      "');" +
      insertnull +
      '"><label class="chksA1 c1_' +
      mapsTagsif.join(",") +
      '" style="' +
      labelstyle +
      '">' +
      makeSpacesOutOf_(p1keys[i]) +
      '</label><div id="' +
      p1keys[i] +
      '" style="display:none;white-space: normal; border-left: 40px solid rgba(0, 0, 0, .0);">' +
      chk2s +
      "</div></div>";
    checkboxes += checkbox;
  }
  str2 = checkboxes + "</span></div>";
  div.innerHTML += str2;
  chks1 = document.getElementsByClassName("chks");
  chks2 = [];
  for (var i = 0; i < chks1.length; i++) {
    chks2.push(
      String(chks1[i].className.match(/c_([\d,]+)/g))
        .substr(2)
        .split(",")
    );
    //window.alert(chks2[i]);
  }

  str4 =
    '<div id="inputZeilen" style="display:none"><table borders="0" id="table2">';
  str5 =
    '<tr><td><label>von bis und Einzelnes: </label></td><td><input typ="text" id="zeilenErlaubtText" value="1-10,12"></input></td><td>' +
    returnChangeButtons(1) +
    '<input onclick="clickZeilenErlaubenUsw();" type="submit" value="auswählen"></td></tr>';
  str6 =
    '<tr><td><label>Vielfacher und Nachbarn: </label></td><td><input typ="text" id="VielfacheErlaubtText" value="10+0+1,7+0"></td><td>' +
    returnChangeButtons(2) +
    '<input onclick="clickVielfacheErlaubenUsw();" type="submit" value="auswählen"></td></tr>';
  str8 =
    '<tr><td><label>Potenzen: </label></td><td><input typ="text" id="potenzenErlaubtText" value="3,5"></input></td><td>' +
    returnChangeButtons(3) +
    '<input onclick="clickPotenzenErlaubenUsw();" type="submit" value="auswählen"></td></tr>';
  str9 =
    '<tr><td colspan="2"><input type="radio" id="sonneWahl" name="sunmoonplanetblackhole" onchange="" checked="true"><label>Sonne</label><input type="radio" id="mondWahl" name="sunmoonplanetblackhole" onchange=""><label>Mond</label><input type="radio" id="planetWahl" name="sunmoonplanetblackhole" onchange=""><label>Planet</label><input type="radio" id="schwarzeSonneWahl" name="sunmoonplanetblackhole" onchange="" onclick="window.alert(\'Schwarze Sonnen kehren die Orginalbedeutung ins Gegenteil.\');"><label>schwarze Sonne</label></td><td>' +
    returnChangeButtons(4) +
    '<input onclick="clickHimmelskoerperErlaubenUsw();" type="submit" value="auswählen"></td></tr>';
  str10 =
    '<tr><td><label>Zählung: </label></td><td><input typ="text" id="zaehlungErlaubtText" value="1,3-4"></input></td><td>' +
    returnChangeButtons(5) +
    '<input onclick="clickZaehlungenErlaubenUsw();" type="submit" value="auswählen"></td></tr>';
  str11 =
    '<tr><td><label>Primzahlvielfacher: </label></td><td><input typ="text" id="primVielfache" value="1"></input></td><td>' +
    returnChangeButtons(6) +
    '<input onclick="clickPrimVielfacheErlaubenUsw();" type="submit" value="auswählen"></td></tr>';
  str12 =
    '<tr><td colspan="2"><input type="radio" id="proInnen" name="proContra4Richtungen" onchange="" checked="true"><label>pro innen</label><input type="radio" id="proAussen" name="proContra4Richtungen" onchange=""><label>pro außen</label><input type="radio" id="gegenDritte" name="proContra4Richtungen" onchange=""><label>gegen Dritte</label><input type="radio" id="proDritte" name="proContra4Richtungen" onchange="" onclick=""><label>pro Dritte</label></td><td>' +
    returnChangeButtons(7) +
    '<input onclick="clickPrimRichtungenErlaubenUsw();" type="submit" value="auswählen"></td></tr>';
  str13 =
    '<tr><td><label>Primzahlkreuzradius: </label></td><td><input typ="text" id="primZahlKreuzRadius" value="1"></input></td><td>' +
    returnChangeButtons(8) +
    '<input onclick="clickPrimZahlKreuzRadiusErlaubenUsw();" type="submit" value="auswählen"></td></tr>';
  str7 = "</table></div>";
  div.innerHTML +=
    str4 + str5 + str6 + str8 + str9 + str10 + str11 + str12 + str13 + str7;
  // Spaltenreihenfolge
  tableHeadline = document
    .getElementsByTagName("table")[1]
    .getElementsByTagName("tr")[0]
    .getElementsByTagName("td");
  for (var u = 0; u < tableHeadline.length; u++) {
    tableHeadline[u].innerHTML =
      '<select id="hselec_' +
      u +
      '" value="' +
      u +
      '" onchange="headingSelected(this, ' +
      u +
      ');"></select>' +
      tableHeadline[u].innerHTML;
  }
  toggleChkSpalten();
};

function makeMapsOfHeadLCheckB(p1, p2, num, tags) {
  if (typeof mapMapMap[p1][p2] === "undefined") mapMapMap[p1][p2] = new Set();
  mapMapMap[p1][p2].add(num);
  if (typeof mapMapMapTags[p1] === "undefined") mapMapMapTags[p1] = {};
  if (typeof mapMapMapTags[p1][p2] === "undefined")
    mapMapMapTags[p1][p2] = new Set();
  if (typeof tags != "undefined" && tags != "null")
    mapMapMapTags[p1][p2] = Set.union(mapMapMapTags[p1][p2], tags);
  //window.alert(Array.from(mapMapMapTags[p1][p2]))
}

Set.union = function (s1, s2) {
  if (typeof s1 == "undefined" || typeof s2 == "undefined") return null;
  if (!s1 instanceof Set || !s2 instanceof Set) {
    //console.log("The given objects are not of type Set");
    return null;
  }
  //if ( s1 == null || s2 == null)
  //   return null;
  let newSet = new Set();
  s1.forEach((elem) => newSet.add(elem));
  s2.forEach((elem) => newSet.add(elem));
  return newSet;
};

function disEnAbleChks(Enums) {
  Enums = new Set(Enums);
  abzug = [];
  if (Enums.has(1) && !Enums.has(0)) abzug.push(0);
  if (Enums.has(0) && !Enums.has(1)) abzug.push(1);
  if (Enums.has(3) && !Enums.has(4)) abzug.push(4);
  if (Enums.has(4) && !Enums.has(3)) abzug.push(3);
  Enume = Set.union(Enums, Enume);
  for (var i = 0; i < abzug.length; i++) Enume.delete(abzug[i]);
  Enums = Array.from(Enume);

  for (var i = 0; i < chks2.length; i++) {
    enumi = new Set();
    for (var k = 0; k < chks2[i].length; k++)
      for (var l = 0; l < Enums.length; l++)
        if (chks2[i][k] == Enums[l]) enumi.add(Enums[l]);
    if ((!enumi.has(0) && !enumi.has(1)) || (!enumi.has(3) && !enumi.has(4))) {
      chks1[i].disabled = true;
      chks1[i].style = labelstylekl;
    } else {
      chks1[i].disabled = false;
      chks1[i].style = labelstyle;
    }
  }

  for (var i = 0; i < spaltenTags.length; i++) {
    enumi = new Set();
    for (var k = 0; k < spaltenTags[i].length; k++)
      for (var l = 0; l < Enums.length; l++)
        if (spaltenTags[i][k] == Enums[l]) enumi.add(Enums[l]);

    if ((!enumi.has(0) && !enumi.has(1)) || (!enumi.has(3) && !enumi.has(4))) {
      for (var k = 0; k < spalten4spaltenTags[i].length; k++)
        spaltenTags2 = spalten4spaltenTags[i][k].getElementsByTagName(
          "label"
        )[0].style = "font-size: 80%;color: grey";
    } else {
      for (var k = 0; k < spalten4spaltenTags[i].length; k++)
        spaltenTags2 = spalten4spaltenTags[i][k].getElementsByTagName(
          "label"
        )[0].style = "";
    }
  }
  var Achks = document.getElementsByClassName("chksA");
  for (var i = 0; i < Achks.length; i++) {
    Bchks = Achks[i]
      .getElementsByTagName("div")[0]
      .getElementsByTagName("input");
    deakAmount = 0;
    for (var k = 0; k < Bchks.length; k++) if (Bchks[k].disabled) deakAmount++;
    if (deakAmount == Bchks.length && deakAmount != 0)
      Achks[i].getElementsByTagName("label")[0].style = labelstylekl;
    else Achks[i].getElementsByTagName("label")[0].style = labelstyle;
  }
  //'"><label class="chksA1 c1_' +
  chksA1label = document.getElementsByClassName("chksA1");
  for (var i = 0; i < chksA1label.length; i++) {
    tagsPerA1Label = chksA1label[i].className.match(/c1_([\d,]+)/g);
    if (tagsPerA1Label == null) tagsPerA1Label = [];
    else
      tagsPerA1Label = String(chksA1label[i].className.match(/c1_([\d,]+)/g))
        .substr(3)
        .split(",");
    if (tagsPerA1Label.length != 0) {
      enumo = new Set();
      for (var k = 0; k < tagsPerA1Label.length; k++)
        for (var l = 0; l < Enums.length; l++)
          if (tagsPerA1Label[k] == Enums[l]) enumo.add(Enums[l]);
      if (enumo.size > 0)
        if (
          (!enumo.has(0) && !enumo.has(1)) ||
          (!enumo.has(3) && !enumo.has(4))
        )
          chksA1label[i].style = labelstylekl;
    }
  }
}
function returnChangeButtons(number) {
  return (
    '<label style="white-space: nowrap;font-size: 100%;"><input type="radio" class="neuErlauben" name="zeilenDazuOrWeg' +
    number +
    '" onchange="" checked="true">neu sichtbar</label><label style="white-space: normal;">&nbsp; </label><label style="white-space: nowrap;font-size: 100%;"><input type="radio" class="neuHinfort" name="zeilenDazuOrWeg' +
    number +
    '" onchange="">neu unsichtbar</label><label style="white-space: normal;">&nbsp; </label><label style="white-space: nowrap;font-size: 100%;"><input type="radio" class="dazuErlauben" name="zeilenDazuOrWeg' +
    number +
    '" onchange="">zusätzlich sichtbar</label><label style="white-space: normal;">&nbsp; </label><label style="white-space: nowrap;font-size: 100%;"><input type="radio" class="dazuEinschraenkend" name="zeilenDazuOrWeg' +
    number +
    '">zusätzlich eingeschränkt</label><label style="white-space: normal;">&nbsp; </label><label style="white-space: nowrap;font-size: 100%;"><input type="radio" class="dazuHinfort" name="zeilenDazuOrWeg' +
    number +
    '" onchange="">zusätzlich unsichtbar</label>'
  );
}

alleMonde = [
  4, 8, 9, 16, 25, 27, 32, 36, 49, 64, 81, 100, 121, 125, 128, 144, 169, 196,
  216, 225, 243, 256, 289, 324, 343, 361, 400, 441, 484, 512, 529, 576, 625,
  676, 729, 784, 841, 900, 961, 1000, 1024,
];

primZahlen = [
  2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
  73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151,
  157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233,
  239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317,
  331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419,
  421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503,
  509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607,
  613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701,
  709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811,
  821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911,
  919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013, 1019,
  1021,
];

function makeSpacesOutOf_(text) {
  if (text.length == 25)
    if (text == "primzahlvielfachesgalaxie") return "Primzahlvielfache Galaxie";
  if (text.length == 8) if (text == "zaehlung") return "Zählung";
  if (text.length == 12) if (text == "nummerierung") return "Nummerierung";
  if (text.length == 11) if (text == "kombination") return "Kombinationen";
  var forNewString = [];
  for (var i = 0; i < text.length; i++)
    if (text[i] == "_") forNewString.push(" ");
    else forNewString.push(text[i]);
  return forNewString.join("");
}

function toggleP2(dasTag, spaltenNummern, para1u2) {
  //window.alert('bla: '+dasTag.checked);
  spaltenNummern = spaltenNummern.split(",");
  existingParameterNamesArrayIndex = MatrixHasCouple(
    para1u2,
    selectedSpaltenMany2
  );
  if (existingParameterNamesArrayIndex.size > 0) {
    existingParameterNamesKeys = Array.from(existingParameterNamesArrayIndex);
    for (i = 0; i < existingParameterNamesKeys.length; i++) {
      for (
        k = 0;
        k < selectedSpaltenMany2[existingParameterNamesKeys[i]].length;
        k++
      ) {
        if (selectedSpaltenMany2[existingParameterNamesKeys[i]][k] == para1u2) {
          selectedSpaltenMany2[existingParameterNamesKeys[i]].splice(k, 1);
        } else {
        }
      }
    }
    toggleForNums(spaltenNummern);
  } else {
    for (i = 0; i < spaltenNummern.length; i++)
      if (typeof selectedSpaltenMany2[spaltenNummern[i]] !== "undefined")
        selectedSpaltenMany2[spaltenNummern[i]].push(para1u2);
      else selectedSpaltenMany2[spaltenNummern[i]] = [para1u2];
    toggleForNums(spaltenNummern);
  }
}

function MatrixHasCouple(couple, SpaltenNumberToParameters) {
  existing = new Set();
  for (var key in SpaltenNumberToParameters) {
    for (i = 0; i < SpaltenNumberToParameters[key].length; i++) {
      for (k = 0; k < SpaltenNumberToParameters[key].length; k++) {
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
  for (var i = 0; i < keys.length; i++) {
    visibleHeadingsNumbers[keys[i]] =
      visibleHeadingsSelectUnsorted[keys[i]].value;
  }
  keys2 = Object.keys(visibleHeadingsNumbers);
  //window.alert("vis num"+ keys2.length)
  //window.alert("vis num 0: "+ visibleHeadingsNumbers[keys2[0]])
}

function toggleName(p2) {
  if (p2.style.display != "none") p2.style.display = "none";
  else if (p2.getElementsByTagName("input").length > 0) {
    p2.style.display = "block";
    p2.style.fontSize = "100%";
  }
}

function toggleP1(p1) {
  p2 = document.getElementById(p1);
  if (typeof p2.style != "undefined") {
    var num = p2.className.match(/r_(\d+)/);
    if (num != null && num.length > 1) num = num[1];
    if (
      (selectedSpaltenMany1[num] === "undefined") ===
      (p2.style.display != "none")
    ) {
      selectedSpaltenMany1[num] = p2;
      toggleName(p2);
    } else {
      toggleName(p2);
      delete selectedSpaltenMany1[num];
    }
  } else window.alert(p2.innerHTML + " ! ");
}

function toggleSpalten(colNumber) {
  ZeileIhreZellen = document.getElementsByClassName("r_" + colNumber);
  if (typeof selectedSpaltenMany2[colNumber] === "undefined") {
    away = true;
    //window.alert("undefined "+colNumber);
  } else away = selectedSpaltenMany2[colNumber].length == 0;
  //window.alert("Stelle "+colNumber+"hat Länge "+selectedSpaltenMany2[colNumber].length);
  if (typeof ZeileIhreZellen[0].style != "undefined") {
    if (ZeileIhreZellen[0].style.display == "none")
      changeHeadline(ZeileIhreZellen[0], true);
    else if (away) changeHeadline(ZeileIhreZellen[0], false);

    if (ZeileIhreZellen[0].getElementsByTagName("option").length == 0)
      spalteEinzelnDeaktiviertWorden = false;
    else if (ZeileIhreZellen[0].getElementsByTagName("option")[0].selected)
      spalteEinzelnDeaktiviertWorden = true;
    else spalteEinzelnDeaktiviertWorden = false;

    for (i = 0; i < ZeileIhreZellen.length; i++) {
      if (
        ZeileIhreZellen[i].style.display == "none" &&
        !spalteEinzelnDeaktiviertWorden
      ) {
        ZeileIhreZellen[i].style.display = "table-cell";
        ZeileIhreZellen[i].style.fontSize = "100%";
      } else if (away || spalteEinzelnDeaktiviertWorden) {
        ZeileIhreZellen[i].style.display = "none";
      }
    }
    if (spalteEinzelnDeaktiviertWorden) {
      //window.alert('B '+ZeileIhreZellen[0].className.match(/r_(\d+)/g)[0]);
      //window.alert('B '+ZeileIhreZellen[0].className.match(/r_(\d+)/g)[0].substring(2));
      delete visibleHeadingsSelectUnsorted[
        parseInt(ZeileIhreZellen[0].className.match(/r_(\d+)/g)[0].substring(2))
      ];
      // sie wieder zu aktivieren, auf 1 statt 0 setzen (wobei hier die richtige zahl eigentlich besser wäre)
      // auf 1 setzen ist aber okay, weil die durch refresh usw. sowieso wieder umgesetzt wird
      ZeileIhreZellen[0].getElementsByTagName("option")[1].selected =
        "selected";
    }
  } else window.alert(ZeileIhreZellen[0].innerHTML + " ! " + colNumber);
}

var tableHeadline;
var visibleHeadingsSelectUnsorted = {};
var visibleHeadingsNumbers = {};

function changeHeadline(oneColHeading, addTrueRemoveFalse) {
  sel = oneColHeading.getElementsByTagName("select")[0];
  var num = oneColHeading.className.match(/r_(\d+)/g);
  if (num.length > 0) num = parseInt(num[0].substring(2));
  else num = 0;
  //window.alert(num);

  if (addTrueRemoveFalse) visibleHeadingsSelectUnsorted[num] = sel;
  else if (num in visibleHeadingsSelectUnsorted)
    delete visibleHeadingsSelectUnsorted[num];
  //window.alert(Object.keys(visibleHeadingsSelectUnsorted).length);
  //
}

function makeSpalteUnsichtbar(
  spalteToUnsichtbar,
  momentaneSpalte_als_r_,
  hiddenTrueVisibleFalse
) {
  //spalteToUnsichtbar = document.getElementsByClassName("r_"+momentaneSpalte_als_r_);
  len = spalteToUnsichtbar.length;
  if (hiddenTrueVisibleFalse) {
    for (var i = 0; i < len; i++) spalteToUnsichtbar[i].style.display = "none";
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
  var spalte2ToChange = document.getElementsByClassName(
    "r_" + momentaneSpalte_als_r_
  );
  if (gewaehlteSpalte_plusgleich1 == "-") {
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
  var spalte1ToChange = document.getElementsByClassName(
    "r_" + gewaehlteSpalte_als_r_
  );
  seli = spalte1ToChange[0]
    .getElementsByTagName("select")[0]
    .getElementsByTagName("option");
  selival = selectionsBefore[momentaneSpalte_plusgleich1] + 1;
  gewaehlteSpalte_plusgleich1 = selival - 2; // 1 bis +=1
  seli[selival].selected = "selected";
  var tabellenKopf = document.getElementsByClassName("z_0");
  var aa = 0;
  var bb = 0;
  for (var z = 0; z < tabellenKopf.length; z++) {
    if (tabellenKopf[z] === spalte2ToChange[0]) aa = z;
    if (tabellenKopf[z] === spalte1ToChange[0]) bb = z;
  }

  var merke;
  if (aa > bb)
    for (var i = 0; i < spalte1ToChange.length; i++) {
      merke = spalte2ToChange[i].outerHTML;
      spalte2ToChange[i].outerHTML = spalte1ToChange[i].outerHTML;
      spalte1ToChange[i].outerHTML = merke;
    }
  else
    for (var i = 0; i < spalte1ToChange.length; i++) {
      merke = spalte1ToChange[i].outerHTML;
      spalte1ToChange[i].outerHTML = spalte2ToChange[i].outerHTML;
      spalte2ToChange[i].outerHTML = merke;
    }

  visibleHeadingsSelectUnsorted[gewaehlteSpalte_als_r_] =
    spalte1ToChange[0].getElementsByTagName("select")[0];
  visibleHeadingsSelectUnsorted[momentaneSpalte_als_r_] =
    spalte2ToChange[0].getElementsByTagName("select")[0];
  refresh();
}

var selectionsBefore = {};
var optionsS = [];
var sichtbareSpaltenNummern;

function sortedKeysOfHeadingNumbersByVisibility() {
  tableHeadline = document
    .getElementsByTagName("table")[1]
    .getElementsByTagName("tr")[0]
    .getElementsByTagName("td");
  sichtbareSpaltenNummern = [];
  for (var i = 0; i < tableHeadline.length; i++) {
    if (tableHeadline[i].style.display == "table-cell") {
      sichtbareSpaltenNummern.push(
        tableHeadline[i].className.match(/r_(\d+)/g)[0].substring(2)
      );
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
  for (var k = 0; k < len; k++) {
    options = ["<option value='-,null'>-</option>"];
    for (var i = 0; i < len; i++)
      if (i != k)
        options.push(
          "<option value='" +
            i +
            "," +
            sichtbareSpaltenNummern[i] +
            "'>" +
            (i + 1) +
            "</option>"
        );
      else {
        options.push(
          "<option selected value='" +
            i +
            "," +
            sichtbareSpaltenNummern[i] +
            "'>" +
            (i + 1) +
            "</option>"
        );
        selection = i;
      }
    selectionsBefore[k] = k;
    optionsS.push(options);
  }
  if (len != sichtbareSpaltenNummern.length) {
    window.alert(
      "beides sichtbares und beide Längen nicht gleich: td spalten zellen anzahl als dict mir _r keys und die _r Nummerierung derer als array, sichtbareSpaltenNummern ist " +
        sichtbareSpaltenNummern.length +
        " und visibleHeadingsSelectUnsorted ist " +
        len
    );
  }
  for (var i = 0; i < sichtbareSpaltenNummern.length; i++) {
    visibleHeadingsSelectUnsorted[sichtbareSpaltenNummern[i]].innerHTML =
      optionsS[i].join("");
  }
}

function toggleChkSpalten(radiobutton) {
  chk_spalten = document.getElementById("chk_spalten");
  inputZeilen = document.getElementById("inputZeilen");
  spaltenWahl = document.getElementById("spaltenWahl");
  zeilenWahl = document.getElementById("zeilenWahl");

  if (inputZeilen.style.display == "none" && zeilenWahl.checked)
    inputZeilen.style.display = "initial";
  else if (!zeilenWahl.checked) inputZeilen.style.display = "none";

  if (chk_spalten.style.display == "none" && spaltenWahl.checked)
    chk_spalten.style.display = "initial";
  else if (!spaltenWahl.checked) chk_spalten.style.display = "none";
}

function potenzenAngabenToContainer() {
  text = document.getElementById("potenzenErlaubtText").value;
  var zeilenAngaben = new Set();
  text = text.split(",");
  for (var i = 0; i < text.length; i++) {
    number = parseInt(text[i]);
    if (number != "NaN") zeilenAngaben.add(number);
  }
  return zeilenAngaben;
}

function zeilenAngabenToContainer(welches) {
  if (welches == 1) text = document.getElementById("zeilenErlaubtText").value;
  if (welches == 2) text = document.getElementById("zaehlungErlaubtText").value;
  if (welches == 3) text = document.getElementById("primVielfache").value;
  if (welches == 4) text = document.getElementById("primZahlKreuzRadius").value;

  var zeilenAngaben = new Set();
  text = text.split(",");
  for (var i = 0; i < text.length; i++) {
    text2 = text[i].split("-");

    richtig = true;
    if (text2.length < 3)
      for (var k = 0; k < text2.length; k++)
        if (parseInt(text2[k]) == "NaN") richtig = false;
        else text2[k] = parseInt(text2[k]);
    else richtig = false;

    if (richtig) {
      if (text2.length == 1) text2.push(text2[0]);
      zeilenAngaben.add(text2);
    }
  }
  return zeilenAngaben;
}

function vielfacherAngabentoContainer() {
  text = document.getElementById("VielfacheErlaubtText").value;
  var vielfacherAngaben = new Set();
  text = text.split(",");
  for (var i = 0; i < text.length; i++) {
    text2 = text[i].split("+");
    richtig = true;
    for (var k = 0; k < text2.length; k++)
      if (parseInt(text2[k]) == "NaN") richtig = false;
      else text2[k] = parseInt(text2[k]);
    if (richtig) vielfacherAngaben.add(text2);
  }
  return vielfacherAngaben;
}

var erlaubteZeilen = new Set();

function makeAllerlaubteZeilenVielfacher(zeilenAngaben) {
  zeilenAngaben = Array.from(zeilenAngaben);
  var muls;
  erlaubteZeilen = new Set();
  for (var i = 0; i < zeilenAngaben.length; i++) {
    last = zeilenAngaben[i][0];
    muls = [];
    mul = 1;
    last = mul * zeilenAngaben[i][0];
    while (last < 1025) {
      muls.push(last);
      last = mul * zeilenAngaben[i][0];
      mul++;
    }
    for (var h = 0; h < muls.length; h++) {
      if (zeilenAngaben[i].length == 1) {
        erlaubteZeilen.add(muls[h]);
      } else
        for (var k = 1; k < zeilenAngaben[i].length; k++) {
          erlaubteZeilen.add(muls[h] - zeilenAngaben[i][k]);
          //window.alert(parseInt(muls[h]}-zeilenAngaben[i][k]));
          erlaubteZeilen.add(zeilenAngaben[i][k] + muls[h]);
        }
    }
  }
  return erlaubteZeilen;
}

function makeAllerlaubteZeilenPotenzen(zeilenAngaben) {
  zeilenAngaben = Array.from(zeilenAngaben);
  erlaubteZeilen = new Set();
  for (var i = 0; i < zeilenAngaben.length; i++) {
    if (zeilenAngaben[i] > 0) {
      exponent = 1;
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

function intersection(setA, setB) {
  var _intersection = new Set();
  for (var elem of setB) {
    if (setA.has(elem)) {
      _intersection.add(elem);
    }
  }
  return _intersection;
}

function makeAllAllowedZeilenPrimRichtungen() {
  innen = document.getElementById("proInnen").checked;
  aussen = document.getElementById("proAussen").checked;
  hand = document.getElementById("gegenDritte").checked;
  faehig = document.getElementById("proDritte").checked;
  erlaubteZeilen = new Set();

  if (hand || faehig) {
    if (hand) inkrement = 3;
    else inkrement = 2;
    for (var i = 0; i < 1025; i += inkrement) erlaubteZeilen.add(i);
    return erlaubteZeilen;
  }

  if (innen || aussen) {
    var innenAussen;
    if (aussen) innenAussen = new Set([1, 7, 13, 19]);
    if (innen) innenAussen = new Set([5, 11, 17, 23]);

    for (var i = 0; i < 1025; i++) {
      primZahlenModulo = new Set();
      for (k = 2; k < primZahlen.length; k += 1) {
        vielfacher = 1;
        while (i / vielfacher > 2) {
          if (primZahlen[k] == i / vielfacher) {
            vielfacher = i;
            primZahlenModulo.add(primZahlen[k] % 24);
          }
          vielfacher++;
        }
      }
      if (intersection(primZahlenModulo, innenAussen).size != 0)
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
    alleMondeSet = new Set(alleMonde);
    for (var i = 1; i < 1025; i++) {
      if (!alleMondeSet.has(i)) erlaubteZeilen.add(i);
    }
    return erlaubteZeilen;
  }
  if (planetWahl) {
    for (var i = 2; i < 1025; i += 2) erlaubteZeilen.add(i);
    return erlaubteZeilen;
  }
  if (schwarzeSonneWahl) {
    for (var i = 3; i < 1025; i += 3) erlaubteZeilen.add(i);
    return erlaubteZeilen;
  }
}
function makeAllowedZeilenFromPrimVielfacher(zeilenAngaben) {
  zeilenAngaben = Array.from(zeilenAngaben);
  erlaubteZeilen = new Set();
  ersteSpalte = document
    .getElementsByTagName("table")[1]
    .getElementsByClassName("r_0");
  for (var i = 0; i < 1025; i++)
    for (var k = 0; k < zeilenAngaben.length; k++)
      for (var l = zeilenAngaben[k][0]; l <= zeilenAngaben[k][1]; l++)
        if (zahlIstVielfacherEinerPrimzahl(i, l)) erlaubteZeilen.add(i);
  return erlaubteZeilen;
}

function zahlIstVielfacherEinerPrimzahl(zahl, vielfacher) {
  zahl = parseInt(zahl);
  vielfacher = parseInt(vielfacher);
  if (zahl === "NaN" || vielfacher === "Nan") return false;

  stimmt = false;
  for (var i = 0; i < primZahlen.length; i++)
    if (primZahlen[i] == zahl / vielfacher) stimmt = true;
  return stimmt;
}

function makeAllowedZeilenFromZaehlung(zeilenAngaben) {
  zeilenAngaben = Array.from(zeilenAngaben);
  erlaubteZeilen = new Set();
  ersteSpalte = document
    .getElementsByTagName("table")[1]
    .getElementsByClassName("r_0");
  erlaubteZaehlungen = new Set();
  for (var i = 0; i < zeilenAngaben.length; i++)
    for (var k = zeilenAngaben[i][0]; k <= zeilenAngaben[i][1]; k++)
      erlaubteZaehlungen.add(k);

  for (i = 0; i < ersteSpalte.length; i++) {
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
  for (var i = 0; i < zeilenAngaben.length; i++) {
    for (var k = zeilenAngaben[i][0]; k <= zeilenAngaben[i][1]; k++) {
      erlaubteZeilen.add(k);
    }
  }
  return erlaubteZeilen;
}

function makeAllowedZeilenFromPrimZahlKreuzRadius(zeilenAngaben) {
  zeilenAngaben = Array.from(zeilenAngaben);
  erlaubteZeilen = new Set();
  for (var i = 1; i < 1025; i++)
    for (var k = 0; k < zeilenAngaben.length; k++)
      for (var l = zeilenAngaben[k][0]; l <= zeilenAngaben[k][1]; l++)
        if (l == Math.floor((i - 1) / 24) + 1) erlaubteZeilen.add(i);

  return zeilenAngaben;
}

var spalten_r__ = new Set();

function get_r__SpaltenNummern() {
  tabelenkopfZeile = tdClasses;
  for (var i = 0; i < tabelenkopfZeile.length; i++) {
    if (tabelenkopfZeile[i].style.display === "table-cell") {
      num = tabelenkopfZeile[i].className.match(/r_(\d+)/);
      if (num != null && num.length > 1) num = num[1];
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
  dazuHinfort = document.getElementsByClassName("dazuHinfort")[which].checked;
  dazuEinschraenkend =
    document.getElementsByClassName("dazuEinschraenkend")[which].checked;
  //window.alert(neuErlauben+" "+neuHinfort+" "+dazuErlauben+" "+dazuHinfort);
  spalte = document.getElementsByTagName("table")[1].getElementsByTagName("tr");
  for (var s = 1; s < spalte.length; s++) {
    tabellenZelle = spalte[s];
    if (s < 115)
      zeilenLetztendlichZeigenVerstecken(
        s,
        neuErlauben,
        dazuErlauben,
        neuHinfort,
        dazuHinfort,
        tabellenZelle,
        dazuEinschraenkend
      );
    else {
      echteZeilenNummer = spalte[s]
        .getElementsByTagName("td")[0]
        .className.match(/z_(\d+)/g);
      if (echteZeilenNummer != null && echteZeilenNummer.length > 0) {
        echteZeilenNummer = parseInt(echteZeilenNummer[0].substr(2));
        zeilenLetztendlichZeigenVerstecken(
          echteZeilenNummer,
          neuErlauben,
          dazuErlauben,
          neuHinfort,
          dazuHinfort,
          tabellenZelle,
          dazuEinschraenkend
        );
      }
    }
  }
}

function zeilenLetztendlichZeigenVerstecken(
  s,
  neuErlauben,
  dazuErlauben,
  neuHinfort,
  dazuHinfort,
  tabellenZelle,
  dazuEinschraenkend
) {
  if (
    ((erlaubteZeilen.has(s) && (neuErlauben || dazuErlauben)) ||
      (!erlaubteZeilen.has(s) && neuHinfort)) &&
    !dazuHinfort
  )
    tabellenZelle.style.display = "table-row";
  else if (
    ((neuErlauben || neuHinfort) && !dazuErlauben) ||
    (dazuHinfort && erlaubteZeilen.has(s)) ||
    (dazuEinschraenkend && !erlaubteZeilen.has(s))
  )
    tabellenZelle.style.display = "none";
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

function clickPrimZahlKreuzRadiusErlaubenUsw() {
  makeAllowedZeilenFromPrimZahlKreuzRadius(zeilenAngabenToContainer(4));
  get_r__SpaltenNummern();
  erlaubeVerbieteZeilenBeiZeilenErlaubenVerbieten(7);
}
