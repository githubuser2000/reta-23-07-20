var col;
var selectedSpaltenMany1: Map<number, HTMLElement> = new Map<number, HTMLElement>();
var selectedSpaltenMany2: Map<number,string> = new Map<number,string>();
var labelstyle: string = "white-space: nowrap;font-size: 100%;";
var labelstylekl: string = "white-space: nowrap;font-size: 80%;color: grey;";
var tdStyleWhiteSpace: string = "nowrap";
var tdStyleFontSize: string = "100%";
var tdStyleFontSizeKl:string = "80%";
var tdStyleColorKl:string = "grey";
var Enume : Set<number> = new Set([0, 1, 3, 4, 5, 6]);
var mapMapMapTags: Map<number, string[]> = new Map<number, string[]>(),
var chks1: HTMLCollectionOf<HTMLInputElement>;
var chks2: string[];
var spaltenTags: Array<Array<any> > = [],
var spalten4spaltenTags: Map<number,Array<HTMLTableCellElement>> = new Map<number,Array<HTMLTableCellElement>>(),
var Achks: HTMLCollectionOf<HTMLInputElement | Element>;
let tdClasses: HTMLCollectionOf<HTMLTableCellElement> = document.getElementsByClassName("z_0");
var mapMapMap: Map<string, string | Map<string , string | Map<any, any>>> = new Map<string, string | Map<string , string | Map<any, any>>>();


function returnChangeButtons(number1: number | string): string {
  var number = number1.toString()
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



window.onload = function () {
  let div: HTMLDivElement = document.createElement("div");
  let div2: HTMLDivElement = document.createElement("div");
  div.className = "headingsDiv";
  /*
    sternPolygon = 0
    gleichfoermigesPolygon = 1
    keinPolygon = 2
    galaxie = 3
    universum = 4
*/
  document.body.insertBefore(div, document.getElementById("bigtable"));

  let chk_spalten: string =
    '<fieldset><label style="white-space: nowrap;"><input type="radio" id="spaltenWahl" name="spaltOrZeilWahl" onchange="toggleChkSpalten(this);" checked="true">Spalten (Einheiten [9]) wählen</label> <label style="white-space: nowrap;"><input type="radio" id="zeilenWahl" name="spaltOrZeilWahl" onchange="toggleChkSpalten(this);">Zeilen, welche ja nein, (6,13,14,15) (wenig: 7,8,10,12)</label> <label style="white-space: nowrap;"><input type="radio" id="keinsWahl" name="spaltOrZeilWahl" onchange="toggleChkSpalten(this);">frei machen zur Tabellenansicht <!-- | Lädt schneller mit Firefox statt Chrome --> </label></fieldset>';
  let radio_tags: string =
    '<fieldset><label style="white-space: nowrap;"><input type="radio" id="galaxieuniversum" name="galaxieuniversum" onchange="disEnAbleChks([3,4,5]);" checked="true">alles</label> <label style="white-space: nowrap;"><input type="radio" id="planet" name="galaxieuniversum" onchange="disEnAbleChks([5]);">alles andere als 13,15, ggf. jeweils mit 14</label> <label style="white-space: nowrap;"><input type="radio" id="galaxie" name="galaxieuniversum" onchange="disEnAbleChks([3]);">Himmelskörper um schwarzes Loch (13), z.B. eine Galaxie (14)</label> <label style="white-space: nowrap;"><input type="radio" id="universum" name="galaxieuniversum" onchange="disEnAbleChks([4]);">Universum (15)</label></fieldset><fieldset><label style="white-space: nowrap;"><input type="radio" id="sternpolygongleichfoermigespolygon" name="sternpolygongleichfoermigespolygon" onchange="disEnAbleChks([0,1,6]);" checked="true">Sternpolygon und gleichförmiges Polygon und gebrochen-rational</label> <label style="white-space: nowrap;"><input type="radio" id="sternpolygon" name="sternpolygongleichfoermigespolygon" onchange="disEnAbleChks([0]);">Sternpolygon (n)</label> <label style="white-space: nowrap;"><input type="radio" id="gleichfoermigespolygon" name="sternpolygongleichfoermigespolygon" onchange="disEnAbleChks([1]);">gleichförmiges Polygon (1/n)</label> <label style="white-space: nowrap;"><input type="radio" id="gebrrat" name="sternpolygongleichfoermigespolygon" onchange="disEnAbleChks([6]);">gebrochen-rational (m/n)</label></fieldset>';
  div.innerHTML = chk_spalten;
  /*tdClasses = []
for (i = 0; i < tdClasses1.length; i++)
	if (tdClasses1[i].className.includes("z_0"))
		tdClasses.push(tdClasses1[i]);*/
  //let p1map = new Map();
  //let p2map = new Map();
  // str: string = "",
  //let p1Bmap = new Map();
  var str3: string = "",
  var trStyles: Array<string> = [];

  const tAble:  HTMLTableElement = document.getElementById("bigtable") as HTMLTableElement;
  const TRs: HTMLCollectionOf<HTMLTableRowElement> = tAble.rows;
  for (var i: number = 0; i < TRs.length; i++) {
    trStyles.push(TRs[i].style.cssText);
    var TDs: HTMLCollectionOf<HTMLTableCellElement> = TRs[i].cells;
    for (var k: number = 0; k < TDs.length; k++) {
      if (typeof spalten4spaltenTags[k] === "undefined")
        spalten4spaltenTags[k] = [];
      spalten4spaltenTags[k].push(TDs[k]);
    }
  }

  for (var i: number = 0; i < tdClasses.length; i++) {
    var name: string = tdClasses[i].className;
    var num: Array<string> | number | null | null = name.match(/r_(\d+)/);

    var tags: Array<string> | null = name.match(/p4_([\d,]+)/g);
    if (tags === null) tags = [];
    else tags = String(tags).substr(3).split(",");
    tags = Array.from(new Set(tags));
    spaltenTags.push(tags);

    if (num != null) {
      //num = num.substring(2,0);
      num = parseInt(num[1]);
      //let str = num[1];
      //num = i
      var p1a: Array<string> | null = name.match(/p1_([^\s])+/g);
      var p2a: Array<string> | null = name.match(/p2_([^\s])+/g);
      if (p1a != null) {
        for (var p1i: number = 0; p1i < p1a.length; p1i++) {
          if (p1a[p1i].includes("p1_")) p1a[p1i] = p1a[p1i].substring(3);
          var p1b : Array<string> | null= p1a[p1i].match(/[^,]+/g);
          if (p1b != null) {
            for (let p1k: number = 0; p1k < p1b.length; p1k++) {
              var p1: string = p1b[p1k];
              if (typeof mapMapMap[p1] === "undefined") mapMapMap[p1] = new Map();
              if (p2a != null) {
                for (var p2i: number = 0; p2i < p2a.length; p2i++) {
                  if (p2a[p2i].includes("p2_"))
                    p2a[p2i] = p2a[p2i].substring(3);
                  var p2b: string[] | null = p2a[p2i].match(/[^,]+/g);
                  if (p2b != null) {
                    for (var p2k: number = 0; p2k < p2b.length; p2k++) {
                      var p2: string = p2b[p2k];
                      if (p2 != null) {
                        var p3a: string[] | null = p2.match(/p3_(\d+)_/);
                        if (p3a != null) {
                          var p3b: number = parseInt(p3a[1], 10);
                          var p2: string = p2.substring(p3a[1].length + 4);
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

  var p1keys: string[] = Object.keys(mapMapMap);
  //var p1Bkeys = Object.keys(p1Bmap);
  //checkboxes = "<span style=\"white-space: nowrap;\"><input type=\"checkbox\" onchange=\"toggleSpalten(\'r_0\');\"><label>Nummererierung</label>";
  var checkboxes : string =
    '<div id="chk_spalten" style="display:none;">' +
    radio_tags +
    '<span style="">';
  for (var i: number = 0; i < p1keys.length; i++) {
    var chk2s: string = "";
    var p2keys: Array<string | Map<any, any>> = Object.keys(mapMapMap[p1keys[i]]);
    for (var k: number = 0; k < p2keys.length; k++) {
      var numbers: Array<Map<any,any> = Array.from(mapMapMap[p1keys[i]][p2keys[k]]);
      if (p2keys[k] != null && p2keys[k] != "null") {
        // window.alert(p1keys[i]); '✗Grundstrukturen'
        // window.alert(p2keys[i]); klar
        // window.alert(numbers); // ach einfach die und daraus!
        // window.alert(Array.from(mapMapMapTags[p1keys[i]][p2keys[k]]).join(",")); // diese Zahlen
        var chk2: string =
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
          '</input></label><label style="white-space: normal;">&nbsp; </label>';
        chk2s += chk2;
      }
    }
    if (p1keys[i] === "✗Grundstrukturen") {
      var grunSi: number = i;
      grunp2Keys: Array<string | Map<any, any>> = p2keys;
    }
    if (mapMapMap[p1keys[i]][null] !== undefined) {
      let numbers: Array<string, Map<any, any> | null>  = Array.from(mapMapMap[p1keys[i]][null]);
      let insertnull: string = "toggleP2(this,'" + numbers + "','" + [p1keys[i], null] + "');";
    } else {
      let insertnull: string = "";
    }
    var mapsTagsif: string[] | Set<string> = mapMapMapTags[p1keys[i]][null];
    if (typeof mapsTagsif == "undefined") mapsTagsif = [];
    else mapsTagsif = Array.from(mapMapMapTags[p1keys[i]][null]);

    var checkbox: string =
      '<div class="chksA"><label class="chksA1 c1_' +
      mapsTagsif.join(",") +
      '" style="' +
      labelstyle +
      '"><input class="chksA2" type="checkbox" ' + // class="chks c_' +
      //Array.from(mapMapMap[p1keys[i]][null]).join(",") +
      //'"  value="' +
      ' value="' +
      String(p1keys[i]) +
      '" onchange="toggleP1(\'' +
      String(p1keys[i]) +
      "');" +
      String(insertnull) +
      '">' +
      String(makeSpacesOutOf_(p1keys[i])) +
      "</input></label>" +
      '<div id="' +
      String(p1keys[i]) +
      '" style="display:none;white-space: normal; border-left: 40px solid rgba(0, 0, 0, .0);">' +
      (p1keys[i] === "✗Grundstrukturen"
        ? '<input type="radio" class="grundRadio" id="grundRadioChaos" checked onchange="grundSDivToggle(0)"><label>unübersichtlich</label></input> <input type="radio" class="grundRadio" id="grundRadioOrdnung" onchange="grundSDivToggle(1)"><label>ordentlich</label></input><div id="grundSDiv0">'
        : "") +
      String(chk2s) +
      (p1keys[i] === "✗Grundstrukturen"
        ? '</div><div id="grundSDiv1" style="display:none;"></div>'
        : "") +
      "</div></div>";

    checkboxes += checkbox;
  }
  var str2: string = checkboxes + "</span></div>";
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

  var str4: string =
    '<div id="inputZeilen" style="display:none"><table borders="0" id="table2">';
  var str5: string =
    '<tr><td><label>von bis und Einzelnes: </label></td><td><input typ="text" id="zeilenErlaubtText" value="1-10,12"></input></td><td>' +
    returnChangeButtons(1) +
    '<input onclick="clickZeilenErlaubenUsw();" type="submit" value="auswählen"></td></tr>',;
  var str6: string = '<tr><td><label>Vielfacher und Nachbarn: </label></td><td><input typ="text" id="VielfacheErlaubtText" value="10+0+1,7+0"></td><td>' +
    returnChangeButtons(2) +
    '<input onclick="clickVielfacheErlaubenUsw();" type="submit" value="auswählen"></td></tr>';
  var str8: string =
    '<tr><td><label>Potenzen: </label></td><td><input typ="text" id="potenzenErlaubtText" value="3,5"></input></td><td>' ,
    returnChangeButtons(3) +
    '<input onclick="clickPotenzenErlaubenUsw();" type="submit" value="auswählen"></td></tr>';
  var str9: string =
    '<tr><td colspan="2"><input type="radio" id="sonneWahl" name="sunmoonplanetblackhole" onchange="" checked="true"><label>Sonne</label><input type="radio" id="mondWahl" name="sunmoonplanetblackhole" onchange=""><label>Mond</label><input type="radio" id="planetWahl" name="sunmoonplanetblackhole" onchange=""><label>Planet</label><input type="radio" id="schwarzeSonneWahl" name="sunmoonplanetblackhole" onchange="" onclick="window.alert(\'Schwarze Sonnen kehren die Originalbedeutung der 3*n ins Gegenteil (Paradigmen in Gegen-Paradigmen; und auch: Meta-Paradigmen, Transzendentalien in Gegen-Meta-Paradigmen, Gegen-Transzendentalien).\');"><label>schwarze Sonne</label></td><td>' +
    returnChangeButtons(4) +
    '<input onclick="clickHimmelskoerperErlaubenUsw();" type="submit" value="auswählen"></td></tr>',
  var str10: string =
    '<tr><td><label>Zählung: </label></td><td><input typ="text" id="zaehlungErlaubtText" value="1,3-4"></input></td><td>' +
    returnChangeButtons(5) +
    '<input onclick="clickZaehlungenErlaubenUsw();" type="submit" value="auswählen"></td></tr>';
  var str11: string =
    '<tr><td><label>Primzahlvielfacher: </label></td><td><input typ="text" id="primVielfache" value="1"></input></td><td>' +
    returnChangeButtons(6) +
    '<input onclick="clickPrimVielfacheErlaubenUsw();" type="submit" value="auswählen"></td></tr>',
  var str12: string =
    '<tr><td colspan="2"><input type="radio" id="proInnen" name="proContra4Richtungen" onchange="" checked="true"><label>pro innen</label><input type="radio" id="proAussen" name="proContra4Richtungen" onchange=""><label>pro außen</label><input type="radio" id="gegenDritte" name="proContra4Richtungen" onchange=""><label>gegen Dritte</label><input type="radio" id="proDritte" name="proContra4Richtungen" onchange="" onclick=""><label>pro Dritte</label></td><td>' +
    returnChangeButtons(7) +
    '<input onclick="clickPrimRichtungenErlaubenUsw();" type="submit" value="auswählen"></td></tr>',
  var str13: string =
    '<tr><td><label>Primzahlkreuzradius: </label></td><td><input typ="text" id="primZahlKreuzRadius" value="1"></input></td><td>' +
    returnChangeButtons(8) +
    '<input onclick="clickPrimZahlKreuzRadiusErlaubenUsw();" type="submit" value="auswählen"></td></tr>',
  var str7: string = "</table></div>";
  div.innerHTML +=
    str4 + str5 + str6 + str8 + str9 + str10 + str11 + str12 + str13 + str7;
  // Spaltenreihenfolge
  var tableHeadline: HTMLCollectionOf<HTMLTableCellElement>= document.getElementById("bigtable").rows[0].cells;
  for (var u: number = 0; u < tableHeadline.length; u++) {
    tableHeadline[ u].innerHTML =
      '<select id="hselec_' +
      u.toString() +
      '" value="' +
      u.toString() +
      '" onchange="headingSelected(this, ' +
      u.toString() +
      ');"></select>' +
      tableHeadline[u].innerHTML;
  }
  toggleChkSpalten();

  var tabelle: HTMLElement | null = document.getElementById("bigtable");
  var tds: HTMLCollectionOf<HTMLTableCellElement>  = tabelle.cells;
  /*
  for (var i = 0; i < tds.length; i++) {
    text = tds[i];
    text.innerHTML = [
      "<label>",
      //text.innerHTML.replaceAll(") | ", ") | <br>").trim(),
      text.innerHTML,
      "</label>",
    ].join("");
  }
  */

  var trs: HTMLCollectionOf<HTMLTableRowElement> = tabelle.rows;
  var tdsHeadlines: HTMLCollectionOf<HTMLTableCellElement> = trs[0].cells;
  var classnames: string[] = [];
  for (var i: number = 0; i < tdsHeadlines.length; i++)
    classnames.push(tdsHeadlines[i].className);
  for (var k: number = 1; k < trs.length; k++) {
    tds = trs[k].cells;
    for (var i: number = 0; i < tds.length; i++)
      tds[i].className = classnames[i].replace("z_0", "z_" + tds[1].innerHTML);
  }

  for (var k: number = 0; k < trs.length; k++) {
    var tds: HTMLCollectionOf<HTMLTableCellElement>  = trs[k].cells;
    tds[0].style.cssText += "display:none;";
    for (var i: number = 1; i < tds.length; i++)
      tds[i].style.cssText = [
        tds[i].style.cssText,
        "display:none;",
        trs[k].style.cssText,
      ].join("");
    tds[0].style.textAlign = "center";
    tds[1].style.textAlign = "center";
    trs[k].style.cssText = "";
  }
  /*
  for (var k = 0; k < trs.length; k++) {
    tds = trs[k].cells;
    for (var i = 2; i < tds.length; i++)
      tds[i].style.cssText = tds[1].style.cssText;
  }*/

  var inputs: HTMLCollectionOf<HTMLInputElement> = document.getElementsByTagName("input");
  var checkbox_i: Array<any> = [];
  for (var i: number = 0; i < inputs.length; i++) {
    if (inputs[i].type == "checkbox") checkbox_i.push(i);
    if (checkbox_i.length > 1) i = inputs.length;
  }
  const queryString: string = window.location.search;
  const urlParams: URLSearchParams = new URLSearchParams(queryString);
  const ifpreselect: string | null = urlParams.get("preselect");
  if (ifpreselect != "nothing" && checkbox_i != null && this != null) {
    inputs[checkbox_i[1]].checked = true;
    inputs[checkbox_i[1]].onchange(this);
  }

  //var sheets: StyleSheetList = document.styleSheets;
  //var sheet, rules, rule;
  document.body.style.display = "initial";
  /*
  for (var i: number = 0, iLen = sheets.length; i < iLen; i++) {
    sheet = sheets[i];
    // W3C model
    if (sheet.cssRules) {
      rules = sheet.cssRules;

      for (var j: number = 0, jLen = rules.length; j < jLen; j++) {
        rule = rules[j];
        if (rule.cssText == "body { display: none; }") {
          //window.alert(rule.cssText);
          if (typeof sheet.deleteRule == "function") {
            sheet.deleteRule(rule);
            jLen = rules.length;
          }
          //window.alert(rule.selectorText);
        }
      }
    }
  }*/
  document.getElementById("grundSDiv1").innerHTML =
    document.getElementById("grundstrukturenDiv").innerHTML;
  //window.alert(String(checkbox_i.length));
  // ✗Grundstrukturen
  // chksss = chks1 + Achks;
  var Achks: HTMLCollectionOf<Element> = document.getElementsByClassName("chksA2");
  var dinge: string[] = [
    "✗Grundstrukturen",
    "Universum",
    "Geist__(15)",
    "Strukturalien_bzw_Meta-Paradigmen_bzw_Transzendentalien_(15)",
  ];
  if (ifpreselect != "no_universal" && ifpreselect != "nothing") {
    var dinge2: Array<HTMLCollectionOf<HTMLInputElement| Element>> = [Achks, Achks, chks1, chks1];
    for (var x: number = 0; x < dinge.length; x++) {
      var checkx: HTMLInputElement[] = [];
      for (var k: number = 0; k < dinge2[x].length; k++)
        if (dinge2[x][k].value == dinge[x]) checkx.push(dinge2[x][k]);
      if (checkx.length > 0) {
        checkx[0].checked = true;
        checkx[0].onchange();
      }
    }
  }
  /*copyClassNameToOrderedGrunstruk(
    mapMapMap,
    mapMapMapTags,
    p1keys,
    p2keys,
    grunSi,
    grunp2Keys
  );*/
};

function makeMapsOfHeadLCheckB(p1: string, p2: string | null, num: string | number, tags: any): void {
  if (typeof mapMapMap[p1][p2] === "undefined") mapMapMap[p1][p2] = new Set();
  mapMapMap[p1][p2].add(num);
  if (typeof mapMapMapTags[p1] === "undefined") mapMapMapTags[p1] = {};
  if (typeof mapMapMapTags[p1][p2] === "undefined")
    mapMapMapTags[p1][p2] = new Set();
  if (typeof tags != "undefined" && tags != "null")
    mapMapMapTags[p1][p2] = Set.union(mapMapMapTags[p1][p2], tags);
}

Set.union = function (s1: any, s2: any): set<any> | null {
  if (typeof s1 == "undefined" || typeof s2 == "undefined") return null;
  if (!s1 instanceof Set || !s2 instanceof Set) {
    //console.log("The given objects are not of type Set");
    return null;
  }
  //if ( s1 == null || s2 == null)
  //   return null;
  let newSet: Set<any> = new Set();
  s1.forEach((elem) => newSet.add(elem));
  s2.forEach((elem) => newSet.add(elem));
  return newSet;
};

function disEnAbleChks(Enums1: Array<number> | Set<number> | HTMLCollectionOf<any>) {
  var Enums: Set<number> | Array<number> = new Set(Enums1);
  var abzug: number[] = [];
  if (Enums.has(6) && !Enums.has(0)) abzug.push(0);
  if (Enums.has(6) && !Enums.has(1)) abzug.push(1);
  if (Enums.has(1) && !Enums.has(0)) abzug.push(0);
  if (Enums.has(1) && !Enums.has(6)) abzug.push(6);
  if (Enums.has(0) && !Enums.has(1)) abzug.push(1);
  if (Enums.has(0) && !Enums.has(6)) abzug.push(6);
  if (Enums.has(3) && !Enums.has(4)) abzug.push(4);
  if (Enums.has(3) && !Enums.has(5)) abzug.push(5);
  if (Enums.has(4) && !Enums.has(3)) abzug.push(3);
  if (Enums.has(4) && !Enums.has(5)) abzug.push(5);
  if (Enums.has(5) && !Enums.has(3)) abzug.push(3);
  if (Enums.has(5) && !Enums.has(4)) abzug.push(4);
  var Enume: Set<number> = Set.union(Enums, Enume);
  for (var i = 0; i < abzug.length; i++) Enume.delete(abzug[i]);
  Enums  = Array.from(Enume);

  for (var i: number = 0; i < chks2.length; i++) {
    var enumi: Set<number> = new Set();
    for (var k: number = 0; k < chks2[i].length; k++)
      for (var l: number = 0; l < Enums.length; l++)
        if (chks2[i][k] == Enums[l].toString()) enumi.add(Enums[l]);
    if (
      (!enumi.has(0) && !enumi.has(1) && !enumi.has(6)) ||
      (!enumi.has(3) && !enumi.has(4) && !enumi.has(5)) ||
      enumi.size == 0
    ) {
      chks1[i].disabled = true;
      chks1[i].style.fontSize = tdStyleFontSizeKl;
      chks1[i].style.color = tdStyleColorKl;
      chks1[i].style.whiteSpace = tdStyleWhiteSpace;
    } else {
      chks1[i].disabled = false;
      chks1[i].style.fontSize = tdStyleFontSize;
      chks1[i].style.color = "";
      chks1[i].style.whiteSpace = tdStyleWhiteSpace;
    }
  }

  for (var i: number = 2; i < spaltenTags.length; i++) {
    var enumi: Set<number> = new Set();
    for (var k: number = 0; k < spaltenTags[i].length; k++)
      for (var l: number = 0; l < Enums.length; l++)
        if (spaltenTags[i][k] == Enums[l]) enumi.add(Enums[l]);

    if (
      (!enumi.has(0) && !enumi.has(1) && !enumi.has(6)) ||
      (!enumi.has(3) && !enumi.has(4) && !enumi.has(5)) ||
      enumi.size == 0
    ) {
      var spaltenTags2: HTMLTableCellElement;
      for (var k: number = 0; k < spalten4spaltenTags[i].length; k++) {
        spaltenTags2 = spalten4spaltenTags[i][k].style.fontSize = "80%";
        spaltenTags2 = spalten4spaltenTags[i][k].style.opacity = "0.4";
      }
    } else {
      for (var k = 0; k < spalten4spaltenTags[i].length; k++) {
        spaltenTags2 = spalten4spaltenTags[i][k].style.fontSize = "100%";
        spaltenTags2 = spalten4spaltenTags[i][k].style.opacity = "1.0";
      }
    }
  }
  Achks = document.getElementsByClassName("chksA");
  var Bchks: HTMLCollectionOf<HTMLInputElement>;
  for (var i: number = 0; i < Achks.length; i++) {
    Bchks = Achks[i]
      .getElementsByTagName("div")[0]
      .getElementsByTagName("input");
    var deakAmount: number = 0;
    for (var k: number = 0; k < Bchks.length; k++) if (Bchks[k].disabled) deakAmount++;
    if (deakAmount == Bchks.length && deakAmount != 0) {
      Achks[i].getElementsByTagName("label")[0].style.fontSize =
        tdStyleFontSizeKl;
      Achks[i].getElementsByTagName("label")[0].style.color = tdStyleColorKl;
      Achks[i].getElementsByTagName("label")[0].style.whiteSpace =
        tdStyleWhiteSpace;
    } else {
      Achks[i].getElementsByTagName("label")[0].style.fontSize =
        tdStyleFontSize;
      Achks[i].getElementsByTagName("label")[0].style.color = "";
      Achks[i].getElementsByTagName("label")[0].style.whiteSpace =
        tdStyleWhiteSpace;
    }
  }
  var chksA1label: HTMLCollectionOf<HTMLInputElement | Element> = document.getElementsByClassName("chksA1");
  for (var i: number = 0; i < chksA1label.length; i++) {
    var tagsPerA1Label: string[] | null = chksA1label[i].className.match(/c1_([\d,]+)/g);
    if (tagsPerA1Label == null) tagsPerA1Label = [];
    else
      var tagsPerA1Label: string[] | null = String(chksA1label[i].className.match(/c1_([\d,]+)/g))
        .substr(3)
        .split(",");
    if (tagsPerA1Label.length != 0) {
      var enumo: Set<number> = new Set();
      for (var k: number = 0; k < tagsPerA1Label.length; k++)
        for (var l:number  = 0; l < Enums.length; l++)
          if (tagsPerA1Label[k] == Enums[l].toString()) enumo.add(Enums[l]);
      if (
        (!enumo.has(0) && !enumo.has(1) && !enumo.has(6)) ||
        (!enumo.has(3) && !enumo.has(4) && !enumo.has(5)) ||
        enumo.size == 0
      ) {
        chksA1label[i].style.fontSize = tdStyleFontSizeKl;
        chksA1label[i].style.color = tdStyleColorKl;
        chksA1label[i].style.whiteSpace = tdStyleWhiteSpace;
      }
    }
  }
}
const alleMonde: number[] = [
  4, 8, 9, 16, 25, 27, 32, 36, 49, 64, 81, 100, 121, 125, 128, 144, 169, 196,
  216, 225, 243, 256, 289, 324, 343, 361, 400, 441, 484, 512, 529, 576, 625,
  676, 729, 784, 841, 900, 961, 1000, 1024,
];

const primZahlen: number[] = [
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

function makeSpacesOutOf_(text: string): string {
  //if (text.length == 10) if (text == "Wichtigste") return "<b>Wichtigste</b>";
  if (text.length == 25)
    if (text == "Wichtigstes_zum_verstehen")
      return "<b>Wichtigstes zum verstehen</b>";
  if (text.length == 36)
    if (text == "Wichtigstes_zum_gedanklich_einordnen")
      return "<b>Wichtigstes zum gedanklich einordnen</b>";
  /*
  if (text.length == 8) if (text == "zaehlung") return "Zählung";
  if (text.length == 12) if (text == "nummerierung") return "Nummerierung";
  if (text.length == 11)
    if (text == "kombination") return "Kombinationen (Galaxie)";
  if (text.length == 18)
    if (text == "gebrochenuniversum") return "gebrochen-rational Universum n/m";
  if (text.length == 16)
    if (text == "gebrochengalaxie") return "gebrochen-rational Galaxie n/m";
  */
  var forNewString = [];
  for (var i = 0; i < text.length; i++)
    if (text[i] == "_") forNewString.push(" ");
    else forNewString.push(text[i]);
  return forNewString.join("");
}

function copyClassNameToOrderedGrunstruk(
  mapMapMap: Map<string, string | Map<string , string | Map<any, any>>> ,
  mapMapMapTags: Map<number, string>,
  p1keys: string[],
  p2keys: Array<string | Map<any, any>>,
  grunSi: number,
  grunp2Keys: Array<string | Map<any, any>>
) {
  //checkboxesOrdnung = document.getElementsByClassName("ordGru");
  //checkboxesChaos = document.getElementsByClassName("chks");

  //var p1keysB = Object.keys(mapMapMap);
  //var p2keysB = Object.keys(mapMapMap["✗Grundstrukturen"]);
  //numbers = Array.from(mapMapMap["✗Grundstrukturen"][p2keys[0]]);
  //grundstrukThings = Array.from(mapMapMap["✗Grundstrukturen"]);
  //window.alert(String(numbers.join(",")));
  //window.alert(String(grundstrukThings[0].join(",")));
  // (p1keys[i] === "✗Grundstrukturen"
  // var p1keys = Object.keys(mapMapMap);
  //var p1keyGrund = Object.keys(mapMapMap["✗Grundstrukturen"]);
  //var p2keys = Object.keys(mapMapMap[p1);
  // var thingsB = Array.from(mapMapMapTags[p2keyGrund][p2keys[k]]).join(",");
  //var thingsB = Array.from(mapMapMapTags[p1keyGrund]);
  var TagIdGrustruk: any = document.getElementById("✗Grundstrukturen");
  var chaotische: Array<any> = [];
  var ordentliche: Array<any> = [];
  var ordentliche2: Array<any> = [];
  for (var i: number = 0; i < grunp2Keys.length; i++) {
    var nummern: Array<string> = Array.from(mapMapMapTags[p1keys[grunSi]][grunp2Keys[i]]).join(
      ","
    );
    var ordentlich: any = document.getElementById("ordGru" + grunp2Keys[i]);
    var ordentlich2: any = document.getElementById("ordGruB" + grunp2Keys[i]);
    var chaotisch: HTMLCollectionOf<HTMLInputElement> | null = TagIdGrustruk.getElementsByClassName("chks c_" + nummern);
    if (typeof chaotisch !== "undefined" && chaotisch !== null)
      chaotische.push(chaotisch);
    if (typeof ordentlich !== "undefined" && ordentlich !== null)
      ordentliche.push(ordentlich);
    if (typeof ordentlich2 !== "undefined" && ordentlich2 !== null)
      ordentliche2.push(ordentlich2);
    /*
    if (ordentlich !== null) {
      blax = ordentlich.parentElement.getElementsByClassName("OrdGru2");
      if (blax !== null && typeof blax !== "undefined") {
        try {
          //blay = blax.getElementsByTagName("label");

          window.alert(String(blax.innerHTML));
        } catch (error) {}
        //window.alert(String(blay.length));
      }
    }*/
    //bla3[zahl 0 bis n] value sind richtige Namen der checkboxen

    //'" ><input type="checkbox" class="chks c_' +
    //Array.from(mapMapMapTags[p1keys[i]][p2keys[k]]).join(",") +

    /*if (
      ordentlich !== null &&
      //typeof ordentlich.value !== "undefined" //&&
      //ordentlich.getElementsByTagName("label").length > 0
      ordentlich.innerHTML != ""
    )
      window.alert(String(ordentlich.innerHTML));
*/
    //  try {
    /*for (var k = 0; k < bla3.length; k++) {
      if (typeof bla3[k].value !== "undefined") {
        window.alert(
          //String(mapMapMapTags[p1keys[grunSi]][grunp2Keys[i]].join(","))
          // String(p1keys[grunSi]) ===== "Grund...."
          // String(grunp2Keys[i]) === diese dinge da drin
          String(bla3[k].value)
        );
      }
    }*/
    //} catch (error) {}
    //
  }
  //window.alert(String(chaotische.length));
  //window.alert(String(ordentliche.length));
  for (var i: number = 0; i < chaotische.length; i++) {
    chaotisch = chaotische[i];
    for (var m: number = 0; m < chaotisch.length; m++) {
      for (var k: number = 0; k < ordentliche.length; k++) {
        if (
          typeof ordentliche[k].value !== "undefined" &&
          chaotisch != null &&
          typeof chaotisch[m].value !== "undefined" &&
          chaotisch[m].className.substring(0, 4) === "chks" &&
          ordentliche[k].value === chaotisch[m].value
        ) {
          ordentliche[k].className =
            "chks " + chaotisch[m].className.substring(4);
          ordentliche2[k].className =
            "chks " + chaotisch[m].className.substring(4);
          //window.alert(String(ordentliche[k].className));
        }
      }
      // Der Klassen-Inhalt setzt sich zusammen aus:
      //       '" ><input type="checkbox" class="chks c_' +
      //       Array.from(mapMapMapTags[p1keys[i]][p2keys[k]]).join(",") +
    }
  }
}
function grundSDivToggleBeachte(para: string = "", dasTag: boolean = false) {
  var checkboxesOrdnung: HTMLCollectionOf<any> = document.getElementsByClassName("ordGru");
  var checkboxesChaos: HTMLCollectionOf<any> = document.getElementsByClassName("chks");
  if (para !== "") {
    if (!dasTag) {
      for (var i: number = 0; i < checkboxesOrdnung.length; i++) {
        for (var k: number = 0; k < checkboxesOrdnung.length; k++) {
          if (typeof checkboxesChaos[i].value !== "undefined" && k != i) {
            //window.alert(String(checkboxesChaos[i].value));
            if (
              checkboxesOrdnung[k].value === checkboxesOrdnung[i].value
              // checkboxesOrdnung[k].checked != checkboxesOrdnung[i].checked
            ) {
              if (checkboxesOrdnung[k].value === para) {
                checkboxesOrdnung[k].checked = false;
                checkboxesOrdnung[i].checked = false;
              }
            }
          }
        }
      }
      for (var i: number = 0; i < checkboxesChaos.length; i++) {
        for (var k: number = 0; k < checkboxesOrdnung.length; k++) {
          if (typeof checkboxesChaos[i].value !== "undefined") {
            //window.alert(String(checkboxesChaos[i].value));
            if (
              checkboxesOrdnung[k].value === checkboxesChaos[i].value
              //checkboxesOrdnung[k].checked != checkboxesChaos[i].checked
            ) {
              if (checkboxesOrdnung[k].value === para) {
                checkboxesOrdnung[k].checked = false;
                checkboxesChaos[i].checked = false;
              }
            }
          }
        }
      }
    } else {
      if (dasTag) {
        for (var i: number = 0; i < checkboxesOrdnung.length; i++) {
          for (var k: number = 0; k < checkboxesOrdnung.length; k++) {
            if (typeof checkboxesChaos[i].value !== "undefined" && k != i) {
              //window.alert(String(checkboxesChaos[i].value));
              if (
                checkboxesOrdnung[k].value === checkboxesOrdnung[i].value
                //checkboxesOrdnung[k].checked != checkboxesOrdnung[i].checked
              ) {
                if (checkboxesOrdnung[k].value === para) {
                  checkboxesOrdnung[k].checked = true;
                  checkboxesOrdnung[i].checked = true;
                }
              }
            }
          }
        }
        for (var i: number = 0; i < checkboxesChaos.length; i++) {
          for (var k: number = 0; k < checkboxesOrdnung.length; k++) {
            if (typeof checkboxesChaos[i].value !== "undefined") {
              //window.alert(String(checkboxesChaos[i].value));
              if (
                checkboxesOrdnung[k].value === checkboxesChaos[i].value
                // checkboxesOrdnung[k].checked != checkboxesChaos[i].checked
              ) {
                if (checkboxesOrdnung[k].value === para) {
                  checkboxesOrdnung[k].checked = true;
                  checkboxesChaos[i].checked = true;
                }
              }
            }
          }
        }
      }
    }
  } else {
    for (var k: number = 0; k < checkboxesOrdnung.length; k++) {
      for (var k2: number = 0; k2 < checkboxesOrdnung.length; k2++) {
        if (k != k2) {
          //window.alert(String(checkboxesChaos[i].value));
          if (
            checkboxesOrdnung[k2].value === checkboxesOrdnung[k].value &&
            checkboxesOrdnung[k2].checked != checkboxesOrdnung[k].checked
          ) {
            if (checkboxesOrdnung[k2].checked == false)
              checkboxesOrdnung[k2].checked = true;
          }
        }
      }
    }
    for (var i: number = 0; i < checkboxesChaos.length; i++) {
      for (var k: number = 0; k < checkboxesOrdnung.length; k++) {
        if (typeof checkboxesChaos[i].value !== "undefined" && k != i) {
          //window.alert(String(checkboxesChaos[i].value));
          if (
            checkboxesOrdnung[k].value === checkboxesChaos[i].value &&
            checkboxesOrdnung[k].checked != checkboxesChaos[i].checked
          ) {
            if (checkboxesOrdnung[k].checked == false)
              checkboxesOrdnung[k].checked = true;
            if (checkboxesChaos[i].checked == false)
              checkboxesChaos[i].checked = true;
          }
        }
      }
    }
  }
}
function grundSDivToggle(id_: number) {
  //checkboxesChaos = document.getElementsByTagName("input");
  if (id_ == 1) {
    document.getElementById("grundRadioChaos").checked = false;
    document.getElementById("grundRadioOrdnung").checked = true;
    document.getElementById("grundSDiv0").style.display = "none";
    document.getElementById("grundSDiv1").style.display = "inline";
  } else {
    document.getElementById("grundRadioChaos").checked = true;
    document.getElementById("grundRadioOrdnung").checked = false;
    document.getElementById("grundSDiv0").style.display = "inline";
    document.getElementById("grundSDiv1").style.display = "none";
    //checkboxes = document.getElementsByClassName("ordentlicheGrundStrukChk");
    //for (var checkbox in checkboxes) {
    //  checkbox.checked = false;
    //}
  }
  grundSDivToggleBeachte("", false);
  //window.alert(String(checkboxesOrdnung.length));
  //
}

function toggleP2(dasTag: HTMLInputElement, spaltenNummern1: Array<Map<any,any>>, para1u2: string) {
  var pa1u2: string[] = para1u2.split(",");
  var spaltenNummern: string[];
  try {
    /*window.alert(String();
    window.alert(String(pa1u2[1]));
    window.alert(String(Array.from(mapMapMap[pa1u2[0]][pa1u2[1]])));*/
    spaltenNummern = Array.from(mapMapMap[pa1u2[0]][pa1u2[1]]);
    //window.alert(String(spaltenNummern));
  } catch (error) {
    spaltenNummern = spaltenNummern1.split(",");
  }
  var existingParameterNamesArrayIndex: Set<number> = MatrixHasCouple(
    para1u2,
    selectedSpaltenMany2
  );
  if (existingParameterNamesArrayIndex.size > 0) {
    var existingParameterNamesKeys: any[] = Array.from(existingParameterNamesArrayIndex);
    for (var i: number = 0; i < existingParameterNamesKeys.length; i++) {
      for (
        var k: number = 0;
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
    for (var i: number = 0; i < spaltenNummern.length; i++)
      if (typeof selectedSpaltenMany2[spaltenNummern[i]] !== "undefined")
        selectedSpaltenMany2[spaltenNummern[i]].push(para1u2);
      else selectedSpaltenMany2[spaltenNummern[i]] = [para1u2];
    toggleForNums(spaltenNummern);
  }
  grundSDivToggleBeachte(pa1u2[1], dasTag.checked);
}

function MatrixHasCouple(couple: string, SpaltenNumberToParameters: Map<number,string>): Set<number> {
  var existing: Set<any> = new Set();
  for (var key in SpaltenNumberToParameters) {
    for (var i: number = 0; i < SpaltenNumberToParameters[key].length; i++) {
      for (var k: number = 0; k < SpaltenNumberToParameters[key].length; k++) {
        if (SpaltenNumberToParameters[key][k] != couple) {
        } else {
          existing.add(key);
        }
      }
    }
  }
  return existing;
}

function toggleForNums(colNums: string[]) {
  for (var n: number = 0; n < colNums.length; n++) {
    /*if (typeof(selectedSpaltenMany2[colNums]) === 'undefined')
			toggleSpalten(colNums[n]);
		else {
			toggleSpalten(colNums[n]);
		}*/
    toggleSpalten(parseInt(colNums[n]));
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
  var keys: Array<number | string> = Object.keys(visibleHeadingsSelectUnsorted);
  for (var i: number = 0; i < keys.length; i++) {
    visibleHeadingsNumbers[keys[i]] =
      visibleHeadingsSelectUnsorted[keys[i]].value;
  }
  var keys2: string[] = Object.keys(visibleHeadingsNumbers);
  //window.alert("vis num"+ keys2.length)
  //window.alert("vis num 0: "+ visibleHeadingsNumbers[keys2[0]])
}

function toggleName(p2: HTMLElement) {
  if (p2.style.display != "none") p2.style.display = "none";
  else if (p2.getElementsByTagName("input").length > 0) {
    p2.style.display = "block";
    p2.style.fontSize = "100%";
  }
}

function toggleP1(p1: string) {
  var p2: HTMLElement | null = document.getElementById(p1);
  if (p2 != null && typeof p2.style != "undefined") {
    var num1: string[] | null = p2.className.match(/r_(\d+)/);
    if (num1 != null && num1.length > 1) {
        var num: number = parseInt(num1[1]);
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
}

function toggleSpalten(colNumber: number) {
  var ZeileIhreZellen: HTMLCollectionOf<HTMLElement> | HTMLElement[] = document.getElementsByClassName("r_" + colNumber);
  if (typeof selectedSpaltenMany2[colNumber] === "undefined") {
    var away: boolean = true;
  } else away = selectedSpaltenMany2[colNumber].length == 0;
  //window.alert("Stelle "+colNumber+"hat Länge "+selectedSpaltenMany2[colNumber].length);
  if (typeof ZeileIhreZellen[0].style != "undefined") {
    if (ZeileIhreZellen[0].style.display == "none")
      changeHeadline(ZeileIhreZellen[0], true);
    else if (away) changeHeadline(ZeileIhreZellen[0], false);

    if (ZeileIhreZellen[0].getElementsByTagName("option").length == 0)
      var spalteEinzelnDeaktiviertWorden: boolean = false;
    else if (ZeileIhreZellen[0].getElementsByTagName("option")[0].selected)
      spalteEinzelnDeaktiviertWorden = true;
    else spalteEinzelnDeaktiviertWorden = false;

    for (var i: number = 0; i < ZeileIhreZellen.length; i++) {
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

var tableHeadline: HTMLTableCellElement;
var visibleHeadingsSelectUnsorted: Map<number, HTMLElement> = new Map();
//var visibleHeadingsNumbers: Map<number, Map<number, HTMLElement>> = new Map();
var visibleHeadingsNumbers: Map<number, string[]> = new Map();

function changeHeadline(oneColHeading: HTMLTableCellElement, addTrueRemoveFalse: boolean) {
  var sel: HTMLSelectElement = oneColHeading.getElementsByTagName("select")[0];
  var num1: string[] | null = oneColHeading.className.match(/r_(\d+)/g);
  var num: number;
  if (!!num1 && num1.length > 0) num = parseInt(num[0].substring(2));
  else num = 0;
  //window.alert(num);

  if (addTrueRemoveFalse) visibleHeadingsSelectUnsorted[num] = sel;
  else if (num in visibleHeadingsSelectUnsorted)
    delete visibleHeadingsSelectUnsorted[num];
  //window.alert(Object.keys(visibleHeadingsSelectUnsorted).length);
  //
}

function makeSpalteUnsichtbar(
  spalteToUnsichtbar: HTMLCollectionOf<HTMLTableCellElement>,
  momentaneSpalte_als_r_: number,
  hiddenTrueVisibleFalse: boolean
) {
  //spalteToUnsichtbar = document.getElementsByClassName("r_"+momentaneSpalte_als_r_);
  var len: number = spalteToUnsichtbar.length;
  if (hiddenTrueVisibleFalse) {
    for (var i: number = 0; i < len; i++) spalteToUnsichtbar[i].style.display = "none";
    delete visibleHeadingsSelectUnsorted[momentaneSpalte_als_r_];
  } /*else {
        for (var i=0; i<len; i++)
            spalteToUnsichtbar[i].style.display = 'table-cell'
        visibleHeadingsSelectUnsorted['r_'+momentaneSpalte_als_r_]=spalteToUnsichtbar;
    }*/
}

var erstesMal: boolean = true;

function headingSelected(gewaehlteSpalte_plusgleich1a: HTMLSelectElement, momentaneSpalte_als_r_1: string) {
  var momentaneSpalte_als_r_ : number = parseInt(momentaneSpalte_als_r_1)
  var gewaehlteSpalte_plusgleich1: string = gewaehlteSpalte_plusgleich1a.value;
  //for (var i=0; i<optionsS.length; i++) {
  var zwei: string[] = gewaehlteSpalte_plusgleich1.split(",");
  gewaehlteSpalte_plusgleich1 = zwei[0];
  var gewaehlteSpalte_als_r_: string = zwei[1];
  var spalte2ToChange: HTMLCollectionOf<HTMLTableCellElement | Element> = document.getElementsByClassName(
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
  //var momentaneSpalte_plusgleich1: Map<number, HTMLElement> = visibleHeadingsNumbers[momentaneSpalte_als_r_]; // dieses mal als +=1 angabe statt als r_
  var momentaneSpalte_plusgleich1: string[] = visibleHeadingsNumbers[momentaneSpalte_als_r_]; // dieses mal als +=1 angabe statt als r_
  var zwei: string[] = momentaneSpalte_plusgleich1.split(",");
  var momentaneSpalte_plusgleich1: string = zwei[0];
  var spalte1ToChange: HTMLCollectionOf<HTMLTableCellElement | Element> = document.getElementsByClassName(
    "r_" + gewaehlteSpalte_als_r_
  );
  var seli: HTMLCollectionOf<HTMLOptionElement> = spalte1ToChange[0]
    .getElementsByTagName("select")[0]
    .getElementsByTagName("option");
  var selival: number = selectionsBefore[momentaneSpalte_plusgleich1] + 1;
  var gewaehlteSpalte_plusgleich1: number = selival - 2; // 1 bis +=1
  seli[selival].selected = true;
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

var selectionsBefore: number;
var optionsS: string[][]  = [];
var sichtbareSpaltenNummern: string[];

function sortedKeysOfHeadingNumbersByVisibility() {
  var tableHeadline: HTMLCollectionOf<HTMLTableCellElement> = document.getElementById("bigtable").rows[0].cells;
  var sichtbareSpaltenNummern: string[] = [];
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
  var options: string[];
  var optionsS: string[][]  = [];
  var keys: Array<number | string> = Object.keys(visibleHeadingsSelectUnsorted);
  var len: number = keys.length;
  for (var k: number = 0; k < len; k++) {
    options = ["<option value='-,null'>-</option>"];
    for (var i: number = 0; i < len; i++)
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
        var selection: number = i;
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
  for (var i: number = 0; i < sichtbareSpaltenNummern.length; i++) {
    visibleHeadingsSelectUnsorted[sichtbareSpaltenNummern[i]].innerHTML =
      optionsS[i].join("");
  }
}

function toggleChkSpalten(radiobutton: HTMLInputElement) {
  chk_spalten: HTMLDivElement = document.getElementById("chk_spalten");
  inputZeilen: HTMLDivElement = document.getElementById("inputZeilen");
  spaltenWahl: HTMLInputElement = document.getElementById("spaltenWahl");
  zeilenWahl: HTMLInputElement = document.getElementById("zeilenWahl");

  if (inputZeilen.style.display == "none" && zeilenWahl.checked)
    inputZeilen.style.display = "initial";
  else if (!zeilenWahl.checked) inputZeilen.style.display = "none";

  if (chk_spalten.style.display == "none" && spaltenWahl.checked)
    chk_spalten.style.display = "initial";
  else if (!spaltenWahl.checked) chk_spalten.style.display = "none";
}

/*
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
*/
/*function isZeilenAngabe_betweenKommas(g) {
  const x = (g.match(/[0-9]+-[0-9]+/g) || []).length;
  const y = (g.match(/[0-9]+-[0-9]+-[0-9]+/g) || []).length;
  return (
    /^([0-9-]+[\+0-9,-]*)$/.test(g) &&
    !["-", "+"].includes(g.slice(-1)) &&
    ((x < 2 && y == 0) || (/^\-?[0-9]+[\+0-9,]*$/.test(g) && x == 0)) &&
    !/--|\+\+|\+\-|\-\+|,\+|\+,|-,/.test(g)
  );
}*/
function isZeilenAngabe_betweenKommas(g: string): boolean {
  const pattern: RegExp = /^(v?-?\d+)(-\d+)?((\+)(\d+))*$/;
  return !!g.match(pattern);
  /*const x = (g.match(/[0-9]+-[0-9]+/g) || []).length;
  const y = (g.match(/[0-9]+-[0-9]+-[0-9]+/g) || []).length;
  return (
    /^([0-9-]+[\+0-9,-]*)$/.test(g) &&
    !["-", "+"].includes(g.slice(-1)) &&
    ((x < 2 && y == 0) || (/^\-?[0-9]+[\+0-9,]*$/.test(g) && x == 0)) &&
    !/--|\+\+|\+\-|\-\+|,\+|\+,|-,/.test(g)
  );*/
}
function isZeilenAngabe(text: string): boolean {
  var text: string;
  if (text.length > 0 && text[0] === "v") {
    text = text.substring(1);
  }
  var a: boolean[] = [];
  var splittedText: string[] = text.split(",");
  for (var i = 0; i < splittedText.length; i++) {
    a.push(isZeilenAngabe_betweenKommas(splittedText[i]));
  }

  return a.every(function (x) {
    return x;
  });
}
/*
function isZeilenAngabe(g) {
  const x = (g.match(/[0-9]+\-[0-9]+/g) || []).length;
  const y = (g.match(/[0-9]+\-[0-9]+\-[0-9]+/g) || []).length;
  return (
    /^(v?[0-9-]+[\+0-9,-]*)$/.test(g) &&
    !["-", "+"].includes(g.slice(-1)) &&
    ((x < 2 && y == 0) || (/^v?\-?[0-9]+[\+0-9,]*$/.test(g) && x == 0)) &&
    !/--|\+\+|\+\-|\-\+|,\+|\+,|-,/.test(g)
  );
}
*/
/*
function isZeilenAngabe(g) {
  let pattern = new RegExp("^v?[0-9-]+[\\+0-9,-]*$");
  return (
    pattern.test(g) &&
    !["-", "+"].includes(g.slice(-1)) &&
    !g.includes("--") &&
    !g.includes("++") &&
    !g.includes("+-") &&
    !g.includes("-+") &&
    !g.includes(",+") &&
    !g.includes("+,") &&
    !g.includes("-,")
  );
}
*/
function BereichToNumbers2(MehrereBereiche: string, vielfache: boolean = false, maxZahl: number = 1028): Set<number> {
  var MehrereBereiche: string = MehrereBereiche.split(",")
    .filter((s) => s.trim())
    .join(",");
  const Bereiche: string[] = MehrereBereiche.split(",");
  if (!isZeilenAngabe(MehrereBereiche)) {
    return new Set();
  }

  if (!vielfache && maxZahl === 0) {
    maxZahl = Infinity;
  }

  var dazu: Set<number> = new Set();
  var hinfort: Set<number> = new Set();
  var EinBereich: string;
  var EinBereich2: string;
  var vielfache2: boolean = true;
  var vielfache: boolean;

  for (const EinBereich of Bereiche) {
    if (EinBereich.length > 0 && EinBereich[0] === "v") {
      EinBereich2 = EinBereich.slice(1);
      vielfache2 = true;
    } else {
      EinBereich2 = EinBereich;
      vielfache2 = false;
    }
    //window.alert(EinBereich);
    BereichToNumbers2_EinBereich(
      EinBereich2,
      dazu,
      hinfort,
      (vielfache || vielfache2) && maxZahl == Infinity ? 1028 : maxZahl,
      vielfache || vielfache2,
    );
  }

  return new Set<number>([...dazu].filter((x) => !hinfort.has(x)));
}

function BereichToNumbers2_EinBereich(
  EinBereich: string,
  dazu: Set<number>,
  hinfort: Set<number>,
  maxZahl: number,
  vielfache: boolean,
) {
  var menge: Set<number> | null = null;
  if (EinBereich.length > 1 && EinBereich[0] === "-") {
    EinBereich = EinBereich.substring(1);
    menge = hinfort;
  } else if (EinBereich.length > 0 && EinBereich[0] !== "-") {
    menge = dazu;
  } else {
    menge = null;
  }

  const around: number[] = [];
  if (menge !== null) {
    const BereichTuple2: string[] = EinBereich.split("+");
    if (EinBereich.match(/^\d+$/)) {
      EinBereich = EinBereich + "-" + EinBereich;
    } else if (BereichTuple2.length > 0 && BereichTuple2[0].match(/^\d+$/)) {
      EinBereich = BereichTuple2[0] + "-" + BereichTuple2[0];
      if (BereichTuple2.length > 1) {
        EinBereich += "+" + BereichTuple2.slice(1).join("+");
      }
    }
    const BereichCouple: string[] = EinBereich.split("-");
    BereichToNumbers2_EinBereich_Menge(
      BereichCouple,
      around,
      maxZahl,
      menge,
      vielfache
    );
  }
}

function BereichToNumbers2_EinBereich_Menge(
  BereichCouple: string[],
  around: number[],
  maxZahl: number,
  menge: Set<number>,
  vielfache: boolean
) {
  var richtig: boolean;
  if (
    BereichCouple.length == 2 &&
    /^\d+$/.test(BereichCouple[0]) &&
    BereichCouple[0] != "0"
  ) {
    let BereichPlusTuples = BereichCouple[1].split("+");
    if (BereichPlusTuples.length < 2) {
      around = [0];
    } else {
      let richtig = true;
      let numList = [];
      for (let i = 0; i < BereichPlusTuples.length; i++) {
        if (/^\d+$/.test(BereichPlusTuples[i])) {
          numList.push(parseInt(BereichPlusTuples[i]));
        } else {
          richtig = false;
        }
      }
      if (richtig && numList.length > 0) {
        around = numList.slice(1);
        BereichCouple[1] = numList[0].toString();
      }
    }
    if (vielfache) {
      BereichToNumbers2_EinBereich_Menge_vielfache(
        BereichCouple,
        around,
        maxZahl,
        menge
      );
    } else {
      BereichToNumbers2_EinBereich_Menge_nichtVielfache(
        BereichCouple,
        around,
        maxZahl,
        menge
      );
    }
  }
}

function BereichToNumbers2_EinBereich_Menge_vielfache(
  BereichCouple: string[],
  around: number[],
  maxZahl: number,
  menge: Set<number>
) {
  let i: number = 0;
  var aroundSet: Set<number> = new Set(around);
  aroundSet.delete(0);
  //window.alert(Array.from(around).join(","));
  if (around.length === 0 || aroundSet.size == 0) {
    while (around.every((a) => parseInt(BereichCouple[0]) * i < maxZahl - a)) {
      i += 1;
      for (
        let number = parseInt(BereichCouple[0]);
        number <= parseInt(BereichCouple[1]);
        number++
      ) {
        for (const a of around) {
          const c = number * i;
          if (c <= maxZahl) {
            menge.add(c);
          }
        }
      }
    }
  } else {
    while (around.every((a) => parseInt(BereichCouple[0]) * i < maxZahl - a)) {
      i += 1;
      for (
        let number = parseInt(BereichCouple[0]);
        number <= parseInt(BereichCouple[1]);
        number++
      ) {
        for (const a of around) {
          const c = number * i + a;
          if (c <= maxZahl) {
            menge.add(c);
          }
          const d = number * i - a;
          if (d > 0 && d < maxZahl) {
            menge.add(d);
          }
        }
      }
    }
  }
}
function BereichToNumbers2_EinBereich_Menge_nichtVielfache(
  BereichCouple: string[],
  around: number[],
  maxZahl: number,
  menge: Set<number>
) {
  for (
    let number = parseInt(BereichCouple[0]);
    number <= parseInt(BereichCouple[1]);
    number++
  ) {
    for (let a of around) {
      let c = number + a;
      if (c < maxZahl) {
        menge.add(c);
      }
      let d = number - a;
      if (d > 0 && d < maxZahl) {
        menge.add(d);
      }
    }
  }
}
function zeilenAngabenToMengeDirekt(welches: number = 0, v: boolean = false) {
  let text: string;
  switch (welches) {
    case 1:
      text = document.getElementById("zeilenErlaubtText").value;
      break;
    case 2:
      text = document.getElementById("zaehlungErlaubtText").value;
      break;
    case 3:
      text = document.getElementById("primVielfache").value;
      break;
    case 4:
      text = document.getElementById("primZahlKreuzRadius").value;
      break;
    case 5:
      text = document.getElementById("VielfacheErlaubtText").value;
      break;
    case 6:
      text = document.getElementById("potenzenErlaubtText").value;
      break;
    default:
      text = "Ungültige Auswahl";
      break;
  }
  const erlaubteZeilen: Set<number> = BereichToNumbers2(text, welches == 5 || v ? true : false);
  //window.alert(Array.from(erlaubteZeilen).join(" "));
  return erlaubteZeilen;
}
/*
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
*/
/*
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
*/
var erlaubteZeilen: Set<number> = new Set();

function makeAllerlaubteZeilenVielfacher(zeilenAngaben1: Set<number[]>) {
  const zeilenAngaben: number[][] = Array.from(zeilenAngaben1);
  var muls: number[];
  var mul: number
  erlaubteZeilen = new Set();
  var last: number;
  for (var i: number = 0; i < zeilenAngaben.length; i++) {
    last = zeilenAngaben[i][0];
    muls = [];
    mul = 1;
    last = mul * zeilenAngaben[i][0];
    while (last < 1025) {
      muls.push(last);
      last = mul * zeilenAngaben[i][0];
      mul++;
    }
    for (var h: number = 0; h < muls.length; h++) {
      if (zeilenAngaben[i].length == 1) {
        erlaubteZeilen.add(muls[h]);
      } else
        for (var k: number = 1; k < zeilenAngaben[i].length; k++) {
          erlaubteZeilen.add(muls[h] - zeilenAngaben[i][k]);
          //window.alert(parseInt(muls[h]}-zeilenAngaben[i][k]));
          erlaubteZeilen.add(zeilenAngaben[i][k] + muls[h]);
        }
    }
  }
  return erlaubteZeilen;
}

function makeAllerlaubteZeilenPotenzen(zeilenAngaben1: Set<number>) {
  const zeilenAngaben: number[] = Array.from(zeilenAngaben1);
  var erlaubteZeilen: Set<number> = new Set();
  var exponent, potenz: number;
  for (var i: number = 0; i < zeilenAngaben.length; i++) {
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

function intersection(setA: Set<any>, setB: Set<any>) {
  var _intersection = new Set();
  for (var elem of setB) {
    if (setA.has(elem)) {
      _intersection.add(elem);
    }
  }
  return _intersection;
}

function makeAllAllowedZeilenPrimRichtungen(): Set<number> {
  var innen: boolean = document.getElementById("proInnen").checked;
  var aussen: boolean = document.getElementById("proAussen").checked;
  var hand: boolean = document.getElementById("gegenDritte").checked;
  var faehig: boolean = document.getElementById("proDritte").checked;
  var erlaubteZeilen: Set<number> = new Set();
  var inkrement: number;

  if (hand || faehig) {
    if (hand) inkrement = 3;
    else inkrement = 2;
    for (var i: number = 0; i < 1025; i += inkrement) erlaubteZeilen.add(i);
    return erlaubteZeilen;
  }

  if (innen || aussen) {
    var innenAussen: Set<number> = new Set();
    if (aussen) innenAussen = new Set([1, 7, 13, 19]);
    if (innen) innenAussen = new Set([5, 11, 17, 23]);
    var primZahlenModulo: Set<number>;
    var vielfacher: number;

    for (var i: number = 0; i < 1025; i++) {
      primZahlenModulo = new Set();
      for (var k: number = 2; k < primZahlen.length; k += 1) {
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

function makeAllAllowedZeilenHimmelskoerper(): Set<number> {
  const sonneWahl: boolean = document.getElementById("sonneWahl").checked;
  const mondWahl: boolean = document.getElementById("mondWahl").checked;
  const planetWahl: boolean = document.getElementById("planetWahl").checked;
  const schwarzeSonneWahl: boolean = document.getElementById("schwarzeSonneWahl").checked;
  var erlaubteZeilen: Set<number> = new Set();
  if (mondWahl) {
    erlaubteZeilen = new Set(alleMonde);
    return erlaubteZeilen;
  }
  if (sonneWahl) {
    const alleMondeSet: Set<number> = new Set(alleMonde);
    for (var i: number = 1; i < 1025; i++) {
      if (!alleMondeSet.has(i)) erlaubteZeilen.add(i);
    }
    return erlaubteZeilen;
  }
  if (planetWahl) {
    for (var i: number = 2; i < 1025; i += 2) erlaubteZeilen.add(i);
    return erlaubteZeilen;
  }
  if (schwarzeSonneWahl) {
    for (var i: number = 3; i < 1025; i += 3) erlaubteZeilen.add(i);
    return erlaubteZeilen;
  }
}
function makeAllowedZeilenFromPrimVielfacher(zeilenAngaben1: Set<number>): Set<number> {
  const zeilenAngaben: number[] = Array.from(zeilenAngaben1);
  const erlaubteZeilen: Set<number> = new Set();
  const ersteSpalte: HTMLCollectionOf<HTMLTableCellElement> = document
    .getElementById("bigtable")
    .getElementsByClassName("r_0");
  for (var i = 0; i < 1025; i++)
    for (var k = 0; k < zeilenAngaben.length; k++)
      if (zahlIstVielfacherEinerPrimzahl(i, zeilenAngaben[k]))
        erlaubteZeilen.add(i);
  return erlaubteZeilen;
}

function zahlIstVielfacherEinerPrimzahl(zahl1: number | string, vielfacher1: string | number): boolean {
  const zahl: number = parseInt(zahl1);
  const vielfacher: number = parseInt(vielfacher1);
  if (isNaN(zahl) || isNaN(vielfacher)) return false;

  var stimmt: boolean = false;
  for (var i: number = 0; i < primZahlen.length; i++)
    if (primZahlen[i] == zahl / vielfacher) stimmt = true;
  return stimmt;
}

function makeAllowedZeilenFromZaehlung(zeilenMenge: Set<number>): Set<number> {
  const ersteSpalte: HTMLCollectionOf<HTMLTableCellElement> = document
    .getElementById("bigtable")
    .getElementsByClassName("r_0");
  const erlaubteZaehlungen: Set<number> = zeilenMenge;
  const erlaubteZeilen: Set<number> = new Set();
  //window.alert(Array.from(erlaubteZaehlungen).join(" "));
  //window.alert(ersteSpalte.length.toString());
  var zaehlung: number;
  var wirklicheZeile1: RegExpMatchArray | null;
  var wirklicheZeile: string;

  for (var i: number = 0; i < ersteSpalte.length; i++) {
    //window.alert(ersteSpalte[i].getElementsByTagName("label")[0].innerHTML);
    zaehlung = parseInt(ersteSpalte[i].innerHTML.trim());
    //window.alert(zaehlung.toString());
    if (isNaN(zaehlung) && erlaubteZaehlungen.has(zaehlung)) {
        wirklicheZeile1 = ersteSpalte[i].className.match(/z_\s*(\d+)/g);
        if (wirklicheZeile1 != null) {
            wirklicheZeile = wirklicheZeile1.toString();
            //window.alert(ersteSpalte[i].className);
            //window.alert(wirklicheZeile);
            if (wirklicheZeile.length > 0) {
                wirklicheZeile = wirklicheZeile[0].substr(2);
                erlaubteZeilen.add(parseInt(wirklicheZeile));
            }
        }
    }
  }
  return erlaubteZeilen;
}

function makeAllAllowedZeilen(zeilenAngaben1: Set<number[]>): Set<number> {
  const zeilenAngaben: number[][] = Array.from(zeilenAngaben1);
  const erlaubteZeilen: Set<number> = new Set();
  for (var i: number = 0; i < zeilenAngaben.length; i++) {
    for (var k: number = zeilenAngaben[i][0]; k <= zeilenAngaben[i][1]; k++) {
      erlaubteZeilen.add(k);
    }
  }
  return erlaubteZeilen;
}

function makeAllowedZeilenFromPrimZahlKreuzRadius(zeilenAngaben1: Set<number>): number[] {
  const zeilenAngaben: number[] = Array.from(zeilenAngaben1);
  const erlaubteZeilen: Set<number> = new Set();
  for (var i: number = 1; i < 1025; i++)
    for (var k: number = 0; k < zeilenAngaben.length; k++)
      if (zeilenAngaben[k] == Math.floor((i - 1) / 24) + 1)
        erlaubteZeilen.add(i);

  return zeilenAngaben;
}

var spalten_r__: Set<number> = new Set();

function get_r__SpaltenNummern() {
  let tabelenkopfZeile : HTMLCollectionOf<HTMLTableCellElement>;
  tabelenkopfZeile = tdClasses;
  var num1: RegExpMatchArray | null;
  var num: RegExpMatchArray;
  var num2: number;
  for (var i: number = 0; i < tabelenkopfZeile.length; i++) {
    if (tabelenkopfZeile[i].style.display === "table-cell") {
      num1 = tabelenkopfZeile[i].className.match(/r_(\d+)/);
      if (num1 != null) {
      num = num1
      if (num.length > 1) {
            num2 = parseInt(num[1]);
            spalten_r__.add(num2);

          }
      }
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

function erlaubeVerbieteZeilenBeiZeilenErlaubenVerbieten(which: number) {
  const Spalten_r__Array: number[] = Array.from(spalten_r__);
  const erlaubteZeilen_Array: number[] = Array.from(erlaubteZeilen);
  const erlaubteZeilen_String: string = erlaubteZeilen_Array.join(",");
  const neuErlauben: boolean = document.getElementsByClassName("neuErlauben")[which].checked;
  const neuHinfort: boolean = document.getElementsByClassName("neuHinfort")[which].checked;
  const dazuErlauben: boolean = document.getElementsByClassName("dazuErlauben")[which].checked;
  const dazuHinfort: boolean = document.getElementsByClassName("dazuHinfort")[which].checked;
  const dazuEinschraenkend: boolean =
    document.getElementsByClassName("dazuEinschraenkend")[which].checked;
  //window.alert(neuErlauben+" "+neuHinfort+" "+dazuErlauben+" "+dazuHinfort);
  const spalte: HTMLCollectionOf<HTMLTableRowElement> = document.getElementById("bigtable").rows;
  var tabellenZelle: HTMLTableRowElement;
  var echteZeilenNummer1: RegExpMatchArray | null;
  var echteZeilenNummer: number;
  for (var s: number = 1; s < spalte.length; s++) {
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
      echteZeilenNummer1 = spalte[s].cells[0].className.match(/z_\s*(\d+)/g);
      if (echteZeilenNummer1 != null && echteZeilenNummer1.length > 0) {
        echteZeilenNummer = parseInt(echteZeilenNummer1[0].substr(2));
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
  s: number,
  neuErlauben: boolean,
  dazuErlauben: boolean,
  neuHinfort: boolean,
  dazuHinfort: boolean,
  tabellenZelle: HTMLTableRowElement,
  dazuEinschraenkend: boolean
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
  makeAllerlaubteZeilenPotenzen(zeilenAngabenToMengeDirekt(6));
  get_r__SpaltenNummern();
  erlaubeVerbieteZeilenBeiZeilenErlaubenVerbieten(2);
}

function clickVielfacheErlaubenUsw() {
  //makeAllerlaubteZeilenVielfacher(vielfacherAngabentoContainer());
  zeilenAngabenToMengeDirekt(5, true);
  get_r__SpaltenNummern();
  erlaubeVerbieteZeilenBeiZeilenErlaubenVerbieten(1);
}

function clickHimmelskoerperErlaubenUsw() {
  const erlaubteZeilen: Set<number> = makeAllAllowedZeilenHimmelskoerper();
  get_r__SpaltenNummern();
  erlaubeVerbieteZeilenBeiZeilenErlaubenVerbieten(3);
}

function clickZeilenErlaubenUsw() {
  zeilenAngabenToMengeDirekt(1);
  get_r__SpaltenNummern();
  erlaubeVerbieteZeilenBeiZeilenErlaubenVerbieten(0);
}

function clickZaehlungenErlaubenUsw() {
  makeAllowedZeilenFromZaehlung(zeilenAngabenToMengeDirekt(2));
  get_r__SpaltenNummern();
  erlaubeVerbieteZeilenBeiZeilenErlaubenVerbieten(4);
}
function clickPrimVielfacheErlaubenUsw() {
  makeAllowedZeilenFromPrimVielfacher(zeilenAngabenToMengeDirekt(3));
  get_r__SpaltenNummern();
  erlaubeVerbieteZeilenBeiZeilenErlaubenVerbieten(5);
}
function clickPrimRichtungenErlaubenUsw() {
  const erlaubteZeilen: Set<number> = makeAllAllowedZeilenPrimRichtungen();
  get_r__SpaltenNummern();
  erlaubeVerbieteZeilenBeiZeilenErlaubenVerbieten(6);
}

function clickPrimZahlKreuzRadiusErlaubenUsw() {
  makeAllowedZeilenFromPrimZahlKreuzRadius(zeilenAngabenToMengeDirekt(4));
  get_r__SpaltenNummern();
  erlaubeVerbieteZeilenBeiZeilenErlaubenVerbieten(7);
}
