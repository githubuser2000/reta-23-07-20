var col = document.getElementsByClassName("RowNumber 1");
var selectedSpaltenMany1: Map<number,string> = new Map();
var selectedSpaltenMany2: Map<number,string> = new Map();
var labelstyle: string = "white-space: nowrap;font-size: 100%;";
var labelstylekl: string = "white-space: nowrap;font-size: 80%;color: grey;";
var tdStyleWhiteSpace: string = "nowrap";
var tdStyleFontSize: string = "100%";
var tdStyleFontSizeKl:string = "80%";
var tdStyleColorKl:string = "grey";
var Enume : Set<number> = new Set([0, 1, 3, 4, 5, 6]);
var mapMapMapTags: Map<number, string> = new Map(),
var chks1: HTMLCollectionOf<HTMLInputElement>;
var chks2: string[];
var spaltenTags: Array<Array<any> > = [],
var spalten4spaltenTags: Map<number,Array<HTMLTableCellElement>> = new Map(),
var Achks: HTMLCollectionOf<HTMLInputElement | Element>;

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
  let tdClasses: HTMLCollectionOf<Element> = document.getElementsByClassName("z_0");
  /*tdClasses = []
for (i = 0; i < tdClasses1.length; i++)
	if (tdClasses1[i].className.includes("z_0"))
		tdClasses.push(tdClasses1[i]);*/
  //let p1map = new Map();
  //let p2map = new Map();
  let mapMapMap: Map<string, string | Map<string , string | Map<any, any>>> = new Map();
  // str: string = "",
  //let p1Bmap = new Map();
  str3: string = "",
  trStyles: Array<string> = [];

  const tAble:  HTMLTableElement = document.getElementById("bigtable") as HTMLTableElement;
  const TRs: HTMLCollectionOf<HTMLTableRowElement> = tAble.rows;
  for (var i: number = 0; i < TRs.length; i++) {
    trStyles.push(TRs[i].style.cssText);
    let TDs: HTMLCollectionOf<HTMLTableCellElement> = TRs[i].cells;
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
  for (i = 0; i < p1keys.length; i++) {
    var chk2s: string = "";
    // @ts-expect-error TS(2304): Cannot find name 'mapMapMap'.
    var p2keys: Array<string | Map<any, any>> = Object.keys(mapMapMap[p1keys[i]]);
    for (var k: number = 0; k < p2keys.length; k++) {
      // @ts-expect-error TS(2304): Cannot find name 'numbers'.
      numbers: Array<string, Map<any,any> = Array.from(mapMapMap[p1keys[i]][p2keys[k]]);
      if (p2keys[k] != null && p2keys[k] != "null") {
        // window.alert(p1keys[i]); 'Grundstrukturen'
        // window.alert(p2keys[i]); klar
        // window.alert(numbers); // ach einfach die und daraus!
        // window.alert(Array.from(mapMapMapTags[p1keys[i]][p2keys[k]]).join(",")); // diese Zahlen
        var chk2: string =
          '<label style="' +
          labelstyle +
          '" class="chks c_' +
          // @ts-expect-error TS(2304): Cannot find name 'mapMapMapTags'.
          Array.from(mapMapMapTags[p1keys[i]][p2keys[k]]).join(",") +
          '" ><input type="checkbox" class="chks c_' +
          // @ts-expect-error TS(2304): Cannot find name 'mapMapMapTags'.
          Array.from(mapMapMapTags[p1keys[i]][p2keys[k]]).join(",") +
          '" value="' +
          p2keys[k] +
          '" onchange="toggleP2(this,\'' +
          // @ts-expect-error TS(2304): Cannot find name 'numbers'.
          numbers +
          "','" +
          [p1keys[i], p2keys[k]] +
          "');\">" +
          makeSpacesOutOf_(p2keys[k]) +
          '</input></label><label style="white-space: normal;">&nbsp; </label>';
        chk2s += chk2;
      }
    }
    if (p1keys[i] === "Grundstrukturen") {
      // @ts-expect-error TS(2304): Cannot find name 'grunSi'.
      grunSi = i;
      // @ts-expect-error TS(2304): Cannot find name 'grunp2Keys'.
      grunp2Keys = p2keys;
    }
    // @ts-expect-error TS(2304): Cannot find name 'mapMapMap'.
    if (mapMapMap[p1keys[i]][null] !== undefined) {
      let numbers: Array<string, Map<any, any>>  = Array.from(mapMapMap[p1keys[i]][null]);
      let insertnull: string = "toggleP2(this,'" + numbers + "','" + [p1keys[i], null] + "');";
    } else {
      let insertnull: string = "";
    }
    // @ts-expect-error TS(2304): Cannot find name 'mapsTagsif'.
    var mapsTagsif: string | Map<any,any> = mapMapMapTags[p1keys[i]][null];
    // @ts-expect-error TS(2304): Cannot find name 'mapsTagsif'.
    if (typeof mapsTagsif == "undefined") mapsTagsif = [];
    // @ts-expect-error TS(2304): Cannot find name 'mapsTagsif'.
    else mapsTagsif = Array.from(mapMapMapTags[p1keys[i]][null]);

    var checkbox: string =
      '<div class="chksA"><label class="chksA1 c1_' +
      // @ts-expect-error TS(2304): Cannot find name 'mapsTagsif'.
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
      // @ts-expect-error TS(2304): Cannot find name 'insertnull'.
      String(insertnull) +
      '">' +
      String(makeSpacesOutOf_(p1keys[i])) +
      "</input></label>" +
      '<div id="' +
      String(p1keys[i]) +
      '" style="display:none;white-space: normal; border-left: 40px solid rgba(0, 0, 0, .0);">' +
      (p1keys[i] === "Grundstrukturen"
        ? '<input type="radio" class="grundRadio" id="grundRadioChaos" checked onchange="grundSDivToggle(0)"><label>unübersichtlich</label></input> <input type="radio" class="grundRadio" id="grundRadioOrdnung" onchange="grundSDivToggle(1)"><label>ordentlich</label></input><div id="grundSDiv0">'
        : "") +
      String(chk2s) +
      (p1keys[i] === "Grundstrukturen"
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
      // @ts-expect-error TS(2304): Cannot find name 'chks1'.
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
  if (ifpreselect != "nothing") {
    inputs[checkbox_i[1]].checked = true;
    // @ts-expect-error TS(2721): Cannot invoke an object which is possibly 'null'.
    inputs[checkbox_i[1]].onchange(this);
  }

  //var sheets: StyleSheetList = document.styleSheets;
  //var sheet, rules, rule;
  // @ts-expect-error TS(2403): Subsequent variable declarations must have the sam... Remove this comment to see the full error message
  var i, j, k, l;

  document.body.style.display = "initial";
  /*
  for (i = 0, iLen = sheets.length; i < iLen; i++) {
    sheet = sheets[i];
    // W3C model
    if (sheet.cssRules) {
      rules = sheet.cssRules;

      for (j = 0, jLen = rules.length; j < jLen; j++) {
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
  // Grundstrukturen
  // chksss = chks1 + Achks;
  var Achks: HTMLCollectionOf<Element> = document.getElementsByClassName("chksA2");
  var dinge: string[] = [
    "Grundstrukturen",
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

function makeMapsOfHeadLCheckB(p1: string, p2: string, num: string | number, tags: any): void {
  if (typeof mapMapMap[p1][p2] === "undefined") mapMapMap[p1][p2] = new Set();
  mapMapMap[p1][p2].add(num);
  if (typeof mapMapMapTags[p1] === "undefined") mapMapMapTags[p1] = {};
  if (typeof mapMapMapTags[p1][p2] === "undefined")
    mapMapMapTags[p1][p2] = new Set();
  if (typeof tags != "undefined" && tags != "null")
    mapMapMapTags[p1][p2] = Set.union(mapMapMapTags[p1][p2], tags);
}

// @ts-expect-error TS(2339): Property 'union' does not exist on type 'SetConstr... Remove this comment to see the full error message
Set.union = function (s1: any, s2: any): set<any> | null {
  if (typeof s1 == "undefined" || typeof s2 == "undefined") return null;
  // @ts-expect-error TS(2358): The left-hand side of an 'instanceof' expression m... Remove this comment to see the full error message
  if (!s1 instanceof Set || !s2 instanceof Set) {
    //console.log("The given objects are not of type Set");
    return null;
  }
  //if ( s1 == null || s2 == null)
  //   return null;
  let newSet: Set<any> = new Set();
  // @ts-expect-error TS(7006): Parameter 'elem' implicitly has an 'any' type.
  s1.forEach((elem) => newSet.add(elem));
  // @ts-expect-error TS(7006): Parameter 'elem' implicitly has an 'any' type.
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
      var spaltenTags2: any;
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
// @ts-expect-error TS(2304): Cannot find name 'alleMonde'.
alleMonde = [
  4, 8, 9, 16, 25, 27, 32, 36, 49, 64, 81, 100, 121, 125, 128, 144, 169, 196,
  216, 225, 243, 256, 289, 324, 343, 361, 400, 441, 484, 512, 529, 576, 625,
  676, 729, 784, 841, 900, 961, 1000, 1024,
];

// @ts-expect-error TS(2304): Cannot find name 'primZahlen'.
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

function makeSpacesOutOf_(text: string): string {
  if (text.length == 10) if (text == "Wichtigste") return "<b>Wichtigste</b>";
  if (text.length == 25)
    if (text == "Wichtigstes_zum_verstehen")
      return "<b>Wichtigstes zum verstehen</b>";
  if (text.length == 36)
    if (text == "Wichtigstes_zum_gedanklich_einordnen")
      return "<b>Wichtigstes zum gedanklich einordnen</b>";
  if (text.length == 8) if (text == "zaehlung") return "Zählung";
  if (text.length == 12) if (text == "nummerierung") return "Nummerierung";
  if (text.length == 11)
    if (text == "kombination") return "Kombinationen (Galaxie)";
  if (text.length == 18)
    if (text == "gebrochenuniversum") return "gebrochen-rational Universum n/m";
  if (text.length == 16)
    if (text == "gebrochengalaxie") return "gebrochen-rational Galaxie n/m";
  var forNewString = [];
  for (var i = 0; i < text.length; i++)
    if (text[i] == "_") forNewString.push(" ");
    else forNewString.push(text[i]);
  return forNewString.join("");
}

function copyClassNameToOrderedGrunstruk(
  // @ts-expect-error TS(7006): Parameter 'mapMapMap' implicitly has an 'any' type... Remove this comment to see the full error message
  mapMapMap,
  // @ts-expect-error TS(7006): Parameter 'mapMapMapTags' implicitly has an 'any' ... Remove this comment to see the full error message
  mapMapMapTags,
  // @ts-expect-error TS(7006): Parameter 'p1keys' implicitly has an 'any' type.
  p1keys,
  // @ts-expect-error TS(7006): Parameter 'p2keys' implicitly has an 'any' type.
  p2keys,
  // @ts-expect-error TS(7006): Parameter 'grunSi' implicitly has an 'any' type.
  grunSi,
  // @ts-expect-error TS(7006): Parameter 'grunp2Keys' implicitly has an 'any' typ... Remove this comment to see the full error message
  grunp2Keys
) {
  //checkboxesOrdnung = document.getElementsByClassName("ordGru");
  //checkboxesChaos = document.getElementsByClassName("chks");

  //var p1keysB = Object.keys(mapMapMap);
  //var p2keysB = Object.keys(mapMapMap["Grundstrukturen"]);
  //numbers = Array.from(mapMapMap["Grundstrukturen"][p2keys[0]]);
  //grundstrukThings = Array.from(mapMapMap["Grundstrukturen"]);
  //window.alert(String(numbers.join(",")));
  //window.alert(String(grundstrukThings[0].join(",")));
  // (p1keys[i] === "Grundstrukturen"
  // var p1keys = Object.keys(mapMapMap);
  //var p1keyGrund = Object.keys(mapMapMap["Grundstrukturen"]);
  //var p2keys = Object.keys(mapMapMap[p1);
  // var thingsB = Array.from(mapMapMapTags[p2keyGrund][p2keys[k]]).join(",");
  //var thingsB = Array.from(mapMapMapTags[p1keyGrund]);
  // @ts-expect-error TS(2304): Cannot find name 'TagIdGrustruk'.
  TagIdGrustruk = document.getElementById("Grundstrukturen");
  // @ts-expect-error TS(2304): Cannot find name 'chaotische'.
  chaotische = [];
  // @ts-expect-error TS(2304): Cannot find name 'ordentliche'.
  ordentliche = [];
  // @ts-expect-error TS(2304): Cannot find name 'ordentliche2'.
  ordentliche2 = [];
  for (var i = 0; i < grunp2Keys.length; i++) {
    // @ts-expect-error TS(2304): Cannot find name 'nummern'.
    nummern = Array.from(mapMapMapTags[p1keys[grunSi]][grunp2Keys[i]]).join(
      ","
    );
    // @ts-expect-error TS(2304): Cannot find name 'ordentlich'.
    ordentlich = document.getElementById("ordGru" + grunp2Keys[i]);
    // @ts-expect-error TS(2304): Cannot find name 'ordentlich2'.
    ordentlich2 = document.getElementById("ordGruB" + grunp2Keys[i]);
    // @ts-expect-error TS(2304): Cannot find name 'chaotisch'.
    chaotisch = TagIdGrustruk.getElementsByClassName("chks c_" + nummern);
    // @ts-expect-error TS(2304): Cannot find name 'chaotisch'.
    if (typeof chaotisch !== "undefined" && chaotisch !== null)
      // @ts-expect-error TS(2304): Cannot find name 'chaotische'.
      chaotische.push(chaotisch);
    // @ts-expect-error TS(2304): Cannot find name 'ordentlich'.
    if (typeof ordentlich !== "undefined" && ordentlich !== null)
      // @ts-expect-error TS(2304): Cannot find name 'ordentliche'.
      ordentliche.push(ordentlich);
    // @ts-expect-error TS(2304): Cannot find name 'ordentlich2'.
    if (typeof ordentlich2 !== "undefined" && ordentlich2 !== null)
      // @ts-expect-error TS(2304): Cannot find name 'ordentliche2'.
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
  // @ts-expect-error TS(2304): Cannot find name 'chaotische'.
  for (var i = 0; i < chaotische.length; i++) {
    // @ts-expect-error TS(2304): Cannot find name 'chaotisch'.
    chaotisch = chaotische[i];
    // @ts-expect-error TS(2304): Cannot find name 'chaotisch'.
    for (var m = 0; m < chaotisch.length; m++) {
      // @ts-expect-error TS(2304): Cannot find name 'ordentliche'.
      for (var k = 0; k < ordentliche.length; k++) {
        if (
          // @ts-expect-error TS(2304): Cannot find name 'ordentliche'.
          typeof ordentliche[k].value !== "undefined" &&
          // @ts-expect-error TS(2304): Cannot find name 'chaotisch'.
          typeof chaotisch[m].value !== "undefined" &&
          // @ts-expect-error TS(2304): Cannot find name 'chaotisch'.
          chaotisch[m].className.substring(0, 4) === "chks" &&
          // @ts-expect-error TS(2304): Cannot find name 'ordentliche'.
          ordentliche[k].value === chaotisch[m].value
        ) {
          // @ts-expect-error TS(2304): Cannot find name 'ordentliche'.
          ordentliche[k].className =
            // @ts-expect-error TS(2304): Cannot find name 'chaotisch'.
            "chks " + chaotisch[m].className.substring(4);
          // @ts-expect-error TS(2304): Cannot find name 'ordentliche2'.
          ordentliche2[k].className =
            // @ts-expect-error TS(2304): Cannot find name 'chaotisch'.
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
function grundSDivToggleBeachte(para = "", dasTag = false) {
  // @ts-expect-error TS(2304): Cannot find name 'checkboxesOrdnung'.
  checkboxesOrdnung = document.getElementsByClassName("ordGru");
  // @ts-expect-error TS(2304): Cannot find name 'checkboxesChaos'.
  checkboxesChaos = document.getElementsByClassName("chks");
  if (para !== "") {
    // @ts-expect-error TS(2339): Property 'checked' does not exist on type 'boolean... Remove this comment to see the full error message
    if (!dasTag.checked) {
      // @ts-expect-error TS(2304): Cannot find name 'checkboxesOrdnung'.
      for (var i = 0; i < checkboxesOrdnung.length; i++) {
        // @ts-expect-error TS(2304): Cannot find name 'checkboxesOrdnung'.
        for (var k = 0; k < checkboxesOrdnung.length; k++) {
          // @ts-expect-error TS(2304): Cannot find name 'checkboxesChaos'.
          if (typeof checkboxesChaos[i].value !== "undefined" && k != i) {
            //window.alert(String(checkboxesChaos[i].value));
            if (
              // @ts-expect-error TS(2304): Cannot find name 'checkboxesOrdnung'.
              checkboxesOrdnung[k].value === checkboxesOrdnung[i].value
              // checkboxesOrdnung[k].checked != checkboxesOrdnung[i].checked
            ) {
              // @ts-expect-error TS(2304): Cannot find name 'checkboxesOrdnung'.
              if (checkboxesOrdnung[k].value === para) {
                // @ts-expect-error TS(2304): Cannot find name 'checkboxesOrdnung'.
                checkboxesOrdnung[k].checked = false;
                // @ts-expect-error TS(2304): Cannot find name 'checkboxesOrdnung'.
                checkboxesOrdnung[i].checked = false;
              }
            }
          }
        }
      }
      // @ts-expect-error TS(2304): Cannot find name 'checkboxesChaos'.
      for (var i = 0; i < checkboxesChaos.length; i++) {
        // @ts-expect-error TS(2304): Cannot find name 'checkboxesOrdnung'.
        for (var k = 0; k < checkboxesOrdnung.length; k++) {
          // @ts-expect-error TS(2304): Cannot find name 'checkboxesChaos'.
          if (typeof checkboxesChaos[i].value !== "undefined") {
            //window.alert(String(checkboxesChaos[i].value));
            if (
              // @ts-expect-error TS(2304): Cannot find name 'checkboxesOrdnung'.
              checkboxesOrdnung[k].value === checkboxesChaos[i].value
              //checkboxesOrdnung[k].checked != checkboxesChaos[i].checked
            ) {
              // @ts-expect-error TS(2304): Cannot find name 'checkboxesOrdnung'.
              if (checkboxesOrdnung[k].value === para) {
                // @ts-expect-error TS(2304): Cannot find name 'checkboxesOrdnung'.
                checkboxesOrdnung[k].checked = false;
                // @ts-expect-error TS(2304): Cannot find name 'checkboxesChaos'.
                checkboxesChaos[i].checked = false;
              }
            }
          }
        }
      }
    } else {
      // @ts-expect-error TS(2339): Property 'checked' does not exist on type 'boolean... Remove this comment to see the full error message
      if (dasTag.checked) {
        // @ts-expect-error TS(2304): Cannot find name 'checkboxesOrdnung'.
        for (var i = 0; i < checkboxesOrdnung.length; i++) {
          // @ts-expect-error TS(2304): Cannot find name 'checkboxesOrdnung'.
          for (var k = 0; k < checkboxesOrdnung.length; k++) {
            // @ts-expect-error TS(2304): Cannot find name 'checkboxesChaos'.
            if (typeof checkboxesChaos[i].value !== "undefined" && k != i) {
              //window.alert(String(checkboxesChaos[i].value));
              if (
                // @ts-expect-error TS(2304): Cannot find name 'checkboxesOrdnung'.
                checkboxesOrdnung[k].value === checkboxesOrdnung[i].value
                //checkboxesOrdnung[k].checked != checkboxesOrdnung[i].checked
              ) {
                // @ts-expect-error TS(2304): Cannot find name 'checkboxesOrdnung'.
                if (checkboxesOrdnung[k].value === para) {
                  // @ts-expect-error TS(2304): Cannot find name 'checkboxesOrdnung'.
                  checkboxesOrdnung[k].checked = true;
                  // @ts-expect-error TS(2304): Cannot find name 'checkboxesOrdnung'.
                  checkboxesOrdnung[i].checked = true;
                }
              }
            }
          }
        }
        // @ts-expect-error TS(2304): Cannot find name 'checkboxesChaos'.
        for (var i = 0; i < checkboxesChaos.length; i++) {
          // @ts-expect-error TS(2304): Cannot find name 'checkboxesOrdnung'.
          for (var k = 0; k < checkboxesOrdnung.length; k++) {
            // @ts-expect-error TS(2304): Cannot find name 'checkboxesChaos'.
            if (typeof checkboxesChaos[i].value !== "undefined") {
              //window.alert(String(checkboxesChaos[i].value));
              if (
                // @ts-expect-error TS(2304): Cannot find name 'checkboxesOrdnung'.
                checkboxesOrdnung[k].value === checkboxesChaos[i].value
                // checkboxesOrdnung[k].checked != checkboxesChaos[i].checked
              ) {
                // @ts-expect-error TS(2304): Cannot find name 'checkboxesOrdnung'.
                if (checkboxesOrdnung[k].value === para) {
                  // @ts-expect-error TS(2304): Cannot find name 'checkboxesOrdnung'.
                  checkboxesOrdnung[k].checked = true;
                  // @ts-expect-error TS(2304): Cannot find name 'checkboxesChaos'.
                  checkboxesChaos[i].checked = true;
                }
              }
            }
          }
        }
      }
    }
  } else {
    // @ts-expect-error TS(2304): Cannot find name 'checkboxesOrdnung'.
    for (var k = 0; k < checkboxesOrdnung.length; k++) {
      // @ts-expect-error TS(2304): Cannot find name 'checkboxesOrdnung'.
      for (var k2 = 0; k2 < checkboxesOrdnung.length; k2++) {
        if (k != k2) {
          //window.alert(String(checkboxesChaos[i].value));
          if (
            // @ts-expect-error TS(2304): Cannot find name 'checkboxesOrdnung'.
            checkboxesOrdnung[k2].value === checkboxesOrdnung[k].value &&
            // @ts-expect-error TS(2304): Cannot find name 'checkboxesOrdnung'.
            checkboxesOrdnung[k2].checked != checkboxesOrdnung[k].checked
          ) {
            // @ts-expect-error TS(2304): Cannot find name 'checkboxesOrdnung'.
            if (checkboxesOrdnung[k2].checked == false)
              // @ts-expect-error TS(2304): Cannot find name 'checkboxesOrdnung'.
              checkboxesOrdnung[k2].checked = true;
          }
        }
      }
    }
    // @ts-expect-error TS(2304): Cannot find name 'checkboxesChaos'.
    for (var i = 0; i < checkboxesChaos.length; i++) {
      // @ts-expect-error TS(2304): Cannot find name 'checkboxesOrdnung'.
      for (var k = 0; k < checkboxesOrdnung.length; k++) {
        // @ts-expect-error TS(2304): Cannot find name 'checkboxesChaos'.
        if (typeof checkboxesChaos[i].value !== "undefined" && k != k2) {
          //window.alert(String(checkboxesChaos[i].value));
          if (
            // @ts-expect-error TS(2304): Cannot find name 'checkboxesOrdnung'.
            checkboxesOrdnung[k].value === checkboxesChaos[i].value &&
            // @ts-expect-error TS(2304): Cannot find name 'checkboxesOrdnung'.
            checkboxesOrdnung[k].checked != checkboxesChaos[i].checked
          ) {
            // @ts-expect-error TS(2304): Cannot find name 'checkboxesOrdnung'.
            if (checkboxesOrdnung[k].checked == false)
              // @ts-expect-error TS(2304): Cannot find name 'checkboxesOrdnung'.
              checkboxesOrdnung[k].checked = true;
            // @ts-expect-error TS(2304): Cannot find name 'checkboxesChaos'.
            if (checkboxesChaos[i].checked == false)
              // @ts-expect-error TS(2304): Cannot find name 'checkboxesChaos'.
              checkboxesChaos[i].checked = true;
          }
        }
      }
    }
  }
}
// @ts-expect-error TS(7006): Parameter 'id_' implicitly has an 'any' type.
function grundSDivToggle(id_) {
  //checkboxesChaos = document.getElementsByTagName("input");
  if (id_ == 1) {
    // @ts-expect-error TS(2531): Object is possibly 'null'.
    document.getElementById("grundRadioChaos").checked = false;
    // @ts-expect-error TS(2531): Object is possibly 'null'.
    document.getElementById("grundRadioOrdnung").checked = true;
    // @ts-expect-error TS(2531): Object is possibly 'null'.
    document.getElementById("grundSDiv0").style.display = "none";
    // @ts-expect-error TS(2531): Object is possibly 'null'.
    document.getElementById("grundSDiv1").style.display = "inline";
  } else {
    // @ts-expect-error TS(2531): Object is possibly 'null'.
    document.getElementById("grundRadioChaos").checked = true;
    // @ts-expect-error TS(2531): Object is possibly 'null'.
    document.getElementById("grundRadioOrdnung").checked = false;
    // @ts-expect-error TS(2531): Object is possibly 'null'.
    document.getElementById("grundSDiv0").style.display = "inline";
    // @ts-expect-error TS(2531): Object is possibly 'null'.
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

// @ts-expect-error TS(7006): Parameter 'dasTag' implicitly has an 'any' type.
function toggleP2(dasTag, spaltenNummern, para1u2) {
  // @ts-expect-error TS(2304): Cannot find name 'pa1u2'.
  pa1u2 = para1u2.split(",");
  try {
    /*window.alert(String();
    window.alert(String(pa1u2[1]));
    window.alert(String(Array.from(mapMapMap[pa1u2[0]][pa1u2[1]])));*/
    // @ts-expect-error TS(2304): Cannot find name 'mapMapMap'.
    spaltenNummern = Array.from(mapMapMap[pa1u2[0]][pa1u2[1]]);
    //window.alert(String(spaltenNummern));
  } catch (error) {
    spaltenNummern = spaltenNummern.split(",");
  }
  // @ts-expect-error TS(2304): Cannot find name 'existingParameterNamesArrayIndex... Remove this comment to see the full error message
  existingParameterNamesArrayIndex = MatrixHasCouple(
    para1u2,
    selectedSpaltenMany2
  );
  // @ts-expect-error TS(2304): Cannot find name 'existingParameterNamesArrayIndex... Remove this comment to see the full error message
  if (existingParameterNamesArrayIndex.size > 0) {
    // @ts-expect-error TS(2304): Cannot find name 'existingParameterNamesKeys'.
    existingParameterNamesKeys = Array.from(existingParameterNamesArrayIndex);
    // @ts-expect-error TS(2304): Cannot find name 'i'.
    for (i = 0; i < existingParameterNamesKeys.length; i++) {
      for (
        // @ts-expect-error TS(2304): Cannot find name 'k'.
        k = 0;
        // @ts-expect-error TS(2304): Cannot find name 'k'.
        k < selectedSpaltenMany2[existingParameterNamesKeys[i]].length;
        // @ts-expect-error TS(2304): Cannot find name 'k'.
        k++
      ) {
        // @ts-expect-error TS(7053): Element implicitly has an 'any' type because expre... Remove this comment to see the full error message
        if (selectedSpaltenMany2[existingParameterNamesKeys[i]][k] == para1u2) {
          // @ts-expect-error TS(7053): Element implicitly has an 'any' type because expre... Remove this comment to see the full error message
          selectedSpaltenMany2[existingParameterNamesKeys[i]].splice(k, 1);
        } else {
        }
      }
    }
    toggleForNums(spaltenNummern);
  } else {
    // @ts-expect-error TS(2304): Cannot find name 'i'.
    for (i = 0; i < spaltenNummern.length; i++)
      // @ts-expect-error TS(7053): Element implicitly has an 'any' type because expre... Remove this comment to see the full error message
      if (typeof selectedSpaltenMany2[spaltenNummern[i]] !== "undefined")
        // @ts-expect-error TS(7053): Element implicitly has an 'any' type because expre... Remove this comment to see the full error message
        selectedSpaltenMany2[spaltenNummern[i]].push(para1u2);
      // @ts-expect-error TS(7053): Element implicitly has an 'any' type because expre... Remove this comment to see the full error message
      else selectedSpaltenMany2[spaltenNummern[i]] = [para1u2];
    toggleForNums(spaltenNummern);
  }
  // @ts-expect-error TS(2304): Cannot find name 'pa1u2'.
  grundSDivToggleBeachte(pa1u2[1], dasTag);
}

// @ts-expect-error TS(7006): Parameter 'couple' implicitly has an 'any' type.
function MatrixHasCouple(couple, SpaltenNumberToParameters) {
  // @ts-expect-error TS(2304): Cannot find name 'existing'.
  existing = new Set();
  for (var key in SpaltenNumberToParameters) {
    // @ts-expect-error TS(2304): Cannot find name 'i'.
    for (i = 0; i < SpaltenNumberToParameters[key].length; i++) {
      // @ts-expect-error TS(2304): Cannot find name 'k'.
      for (k = 0; k < SpaltenNumberToParameters[key].length; k++) {
        // @ts-expect-error TS(2304): Cannot find name 'k'.
        if (SpaltenNumberToParameters[key][k] != couple) {
        } else {
          // @ts-expect-error TS(2304): Cannot find name 'existing'.
          existing.add(key);
        }
      }
    }
  }
  // @ts-expect-error TS(2304): Cannot find name 'existing'.
  return existing;
}

// @ts-expect-error TS(7006): Parameter 'colNums' implicitly has an 'any' type.
function toggleForNums(colNums) {
  // @ts-expect-error TS(2304): Cannot find name 'n'.
  for (n = 0; n < colNums.length; n++) {
    /*if (typeof(selectedSpaltenMany2[colNums]) === 'undefined')
			toggleSpalten(colNums[n]);
		else {
			toggleSpalten(colNums[n]);
		}*/
    // @ts-expect-error TS(2304): Cannot find name 'n'.
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
  // @ts-expect-error TS(2304): Cannot find name 'keys'.
  keys = Object.keys(visibleHeadingsSelectUnsorted);
  // @ts-expect-error TS(2304): Cannot find name 'keys'.
  for (var i = 0; i < keys.length; i++) {
    // @ts-expect-error TS(7053): Element implicitly has an 'any' type because expre... Remove this comment to see the full error message
    visibleHeadingsNumbers[keys[i]] =
      // @ts-expect-error TS(7053): Element implicitly has an 'any' type because expre... Remove this comment to see the full error message
      visibleHeadingsSelectUnsorted[keys[i]].value;
  }
  // @ts-expect-error TS(2304): Cannot find name 'keys2'.
  keys2 = Object.keys(visibleHeadingsNumbers);
  //window.alert("vis num"+ keys2.length)
  //window.alert("vis num 0: "+ visibleHeadingsNumbers[keys2[0]])
}

// @ts-expect-error TS(7006): Parameter 'p2' implicitly has an 'any' type.
function toggleName(p2) {
  if (p2.style.display != "none") p2.style.display = "none";
  else if (p2.getElementsByTagName("input").length > 0) {
    p2.style.display = "block";
    p2.style.fontSize = "100%";
  }
}

// @ts-expect-error TS(7006): Parameter 'p1' implicitly has an 'any' type.
function toggleP1(p1) {
  // @ts-expect-error TS(2304): Cannot find name 'p2'.
  p2 = document.getElementById(p1);
  // @ts-expect-error TS(2304): Cannot find name 'p2'.
  if (typeof p2.style != "undefined") {
    // @ts-expect-error TS(2304): Cannot find name 'p2'.
    var num = p2.className.match(/r_(\d+)/);
    if (num != null && num.length > 1) num = num[1];
    if (
      // @ts-expect-error TS(7053): Element implicitly has an 'any' type because expre... Remove this comment to see the full error message
      (selectedSpaltenMany1[num] === "undefined") ===
      // @ts-expect-error TS(2304): Cannot find name 'p2'.
      (p2.style.display != "none")
    ) {
      // @ts-expect-error TS(7053): Element implicitly has an 'any' type because expre... Remove this comment to see the full error message
      selectedSpaltenMany1[num] = p2;
      // @ts-expect-error TS(2304): Cannot find name 'p2'.
      toggleName(p2);
    } else {
      // @ts-expect-error TS(2304): Cannot find name 'p2'.
      toggleName(p2);
      // @ts-expect-error TS(7053): Element implicitly has an 'any' type because expre... Remove this comment to see the full error message
      delete selectedSpaltenMany1[num];
    }
  // @ts-expect-error TS(2304): Cannot find name 'p2'.
  } else window.alert(p2.innerHTML + " ! ");
}

// @ts-expect-error TS(7006): Parameter 'colNumber' implicitly has an 'any' type... Remove this comment to see the full error message
function toggleSpalten(colNumber) {
  // @ts-expect-error TS(2304): Cannot find name 'ZeileIhreZellen'.
  ZeileIhreZellen = document.getElementsByClassName("r_" + colNumber);
  // @ts-expect-error TS(7053): Element implicitly has an 'any' type because expre... Remove this comment to see the full error message
  if (typeof selectedSpaltenMany2[colNumber] === "undefined") {
    // @ts-expect-error TS(2304): Cannot find name 'away'.
    away = true;
    //window.alert("undefined "+colNumber);
  // @ts-expect-error TS(2304): Cannot find name 'away'.
  } else away = selectedSpaltenMany2[colNumber].length == 0;
  //window.alert("Stelle "+colNumber+"hat Länge "+selectedSpaltenMany2[colNumber].length);
  // @ts-expect-error TS(2304): Cannot find name 'ZeileIhreZellen'.
  if (typeof ZeileIhreZellen[0].style != "undefined") {
    // @ts-expect-error TS(2304): Cannot find name 'ZeileIhreZellen'.
    if (ZeileIhreZellen[0].style.display == "none")
      // @ts-expect-error TS(2304): Cannot find name 'ZeileIhreZellen'.
      changeHeadline(ZeileIhreZellen[0], true);
    // @ts-expect-error TS(2304): Cannot find name 'away'.
    else if (away) changeHeadline(ZeileIhreZellen[0], false);

    // @ts-expect-error TS(2304): Cannot find name 'ZeileIhreZellen'.
    if (ZeileIhreZellen[0].getElementsByTagName("option").length == 0)
      // @ts-expect-error TS(2304): Cannot find name 'spalteEinzelnDeaktiviertWorden'.
      spalteEinzelnDeaktiviertWorden = false;
    // @ts-expect-error TS(2304): Cannot find name 'ZeileIhreZellen'.
    else if (ZeileIhreZellen[0].getElementsByTagName("option")[0].selected)
      // @ts-expect-error TS(2304): Cannot find name 'spalteEinzelnDeaktiviertWorden'.
      spalteEinzelnDeaktiviertWorden = true;
    // @ts-expect-error TS(2304): Cannot find name 'spalteEinzelnDeaktiviertWorden'.
    else spalteEinzelnDeaktiviertWorden = false;

    // @ts-expect-error TS(2304): Cannot find name 'i'.
    for (i = 0; i < ZeileIhreZellen.length; i++) {
      if (
        // @ts-expect-error TS(2304): Cannot find name 'ZeileIhreZellen'.
        ZeileIhreZellen[i].style.display == "none" &&
        // @ts-expect-error TS(2304): Cannot find name 'spalteEinzelnDeaktiviertWorden'.
        !spalteEinzelnDeaktiviertWorden
      ) {
        // @ts-expect-error TS(2304): Cannot find name 'ZeileIhreZellen'.
        ZeileIhreZellen[i].style.display = "table-cell";
        // @ts-expect-error TS(2304): Cannot find name 'ZeileIhreZellen'.
        ZeileIhreZellen[i].style.fontSize = "100%";
      // @ts-expect-error TS(2304): Cannot find name 'away'.
      } else if (away || spalteEinzelnDeaktiviertWorden) {
        // @ts-expect-error TS(2304): Cannot find name 'ZeileIhreZellen'.
        ZeileIhreZellen[i].style.display = "none";
      }
    }
    // @ts-expect-error TS(2304): Cannot find name 'spalteEinzelnDeaktiviertWorden'.
    if (spalteEinzelnDeaktiviertWorden) {
      //window.alert('B '+ZeileIhreZellen[0].className.match(/r_(\d+)/g)[0]);
      //window.alert('B '+ZeileIhreZellen[0].className.match(/r_(\d+)/g)[0].substring(2));
      // @ts-expect-error TS(7053): Element implicitly has an 'any' type because expre... Remove this comment to see the full error message
      delete visibleHeadingsSelectUnsorted[
        // @ts-expect-error TS(2304): Cannot find name 'ZeileIhreZellen'.
        parseInt(ZeileIhreZellen[0].className.match(/r_(\d+)/g)[0].substring(2))
      ];
      // sie wieder zu aktivieren, auf 1 statt 0 setzen (wobei hier die richtige zahl eigentlich besser wäre)
      // auf 1 setzen ist aber okay, weil die durch refresh usw. sowieso wieder umgesetzt wird
      // @ts-expect-error TS(2304): Cannot find name 'ZeileIhreZellen'.
      ZeileIhreZellen[0].getElementsByTagName("option")[1].selected =
        "selected";
    }
  // @ts-expect-error TS(2304): Cannot find name 'ZeileIhreZellen'.
  } else window.alert(ZeileIhreZellen[0].innerHTML + " ! " + colNumber);
}

var tableHeadline;
var visibleHeadingsSelectUnsorted = {};
var visibleHeadingsNumbers = {};

// @ts-expect-error TS(7006): Parameter 'oneColHeading' implicitly has an 'any' ... Remove this comment to see the full error message
function changeHeadline(oneColHeading, addTrueRemoveFalse) {
  // @ts-expect-error TS(2304): Cannot find name 'sel'.
  sel = oneColHeading.getElementsByTagName("select")[0];
  var num = oneColHeading.className.match(/r_(\d+)/g);
  if (num.length > 0) num = parseInt(num[0].substring(2));
  else num = 0;
  //window.alert(num);

  // @ts-expect-error TS(7053): Element implicitly has an 'any' type because expre... Remove this comment to see the full error message
  if (addTrueRemoveFalse) visibleHeadingsSelectUnsorted[num] = sel;
  else if (num in visibleHeadingsSelectUnsorted)
    // @ts-expect-error TS(7053): Element implicitly has an 'any' type because expre... Remove this comment to see the full error message
    delete visibleHeadingsSelectUnsorted[num];
  //window.alert(Object.keys(visibleHeadingsSelectUnsorted).length);
  //
}

function makeSpalteUnsichtbar(
  // @ts-expect-error TS(7006): Parameter 'spalteToUnsichtbar' implicitly has an '... Remove this comment to see the full error message
  spalteToUnsichtbar,
  // @ts-expect-error TS(7006): Parameter 'momentaneSpalte_als_r_' implicitly has ... Remove this comment to see the full error message
  momentaneSpalte_als_r_,
  // @ts-expect-error TS(7006): Parameter 'hiddenTrueVisibleFalse' implicitly has ... Remove this comment to see the full error message
  hiddenTrueVisibleFalse
) {
  //spalteToUnsichtbar = document.getElementsByClassName("r_"+momentaneSpalte_als_r_);
  // @ts-expect-error TS(2304): Cannot find name 'len'.
  len = spalteToUnsichtbar.length;
  if (hiddenTrueVisibleFalse) {
    // @ts-expect-error TS(2304): Cannot find name 'len'.
    for (var i = 0; i < len; i++) spalteToUnsichtbar[i].style.display = "none";
    // @ts-expect-error TS(7053): Element implicitly has an 'any' type because expre... Remove this comment to see the full error message
    delete visibleHeadingsSelectUnsorted[momentaneSpalte_als_r_];
  } /*else {
        for (var i=0; i<len; i++)
            spalteToUnsichtbar[i].style.display = 'table-cell'
        visibleHeadingsSelectUnsorted['r_'+momentaneSpalte_als_r_]=spalteToUnsichtbar;
    }*/
}

var erstesMal = true;

// @ts-expect-error TS(7006): Parameter 'gewaehlteSpalte_plusgleich1' implicitly... Remove this comment to see the full error message
function headingSelected(gewaehlteSpalte_plusgleich1, momentaneSpalte_als_r_) {
  gewaehlteSpalte_plusgleich1 = gewaehlteSpalte_plusgleich1.value;
  //for (var i=0; i<optionsS.length; i++) {
  // @ts-expect-error TS(2304): Cannot find name 'zwei'.
  zwei = gewaehlteSpalte_plusgleich1.split(",");
  // @ts-expect-error TS(2304): Cannot find name 'zwei'.
  gewaehlteSpalte_plusgleich1 = zwei[0];
  // @ts-expect-error TS(2304): Cannot find name 'gewaehlteSpalte_als_r_'.
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
  // @ts-expect-error TS(2304): Cannot find name 'momentaneSpalte_plusgleich1'.
  momentaneSpalte_plusgleich1 = visibleHeadingsNumbers[momentaneSpalte_als_r_]; // dieses mal als +=1 angabe statt als r_
  // @ts-expect-error TS(2304): Cannot find name 'zwei'.
  zwei = momentaneSpalte_plusgleich1.split(",");
  // @ts-expect-error TS(2304): Cannot find name 'momentaneSpalte_plusgleich1'.
  momentaneSpalte_plusgleich1 = zwei[0];
  var spalte1ToChange = document.getElementsByClassName(
    // @ts-expect-error TS(2304): Cannot find name 'gewaehlteSpalte_als_r_'.
    "r_" + gewaehlteSpalte_als_r_
  );
  // @ts-expect-error TS(2304): Cannot find name 'seli'.
  seli = spalte1ToChange[0]
    .getElementsByTagName("select")[0]
    .getElementsByTagName("option");
  // @ts-expect-error TS(2304): Cannot find name 'selival'.
  selival = selectionsBefore[momentaneSpalte_plusgleich1] + 1;
  // @ts-expect-error TS(2304): Cannot find name 'selival'.
  gewaehlteSpalte_plusgleich1 = selival - 2; // 1 bis +=1
  // @ts-expect-error TS(2304): Cannot find name 'seli'.
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

  // @ts-expect-error TS(7053): Element implicitly has an 'any' type because expre... Remove this comment to see the full error message
  visibleHeadingsSelectUnsorted[gewaehlteSpalte_als_r_] =
    spalte1ToChange[0].getElementsByTagName("select")[0];
  // @ts-expect-error TS(7053): Element implicitly has an 'any' type because expre... Remove this comment to see the full error message
  visibleHeadingsSelectUnsorted[momentaneSpalte_als_r_] =
    spalte2ToChange[0].getElementsByTagName("select")[0];
  refresh();
}

var selectionsBefore = {};
var optionsS = [];
// @ts-expect-error TS(7034): Variable 'sichtbareSpaltenNummern' implicitly has ... Remove this comment to see the full error message
var sichtbareSpaltenNummern;

function sortedKeysOfHeadingNumbersByVisibility() {
  // @ts-expect-error TS(2531): Object is possibly 'null'.
  tableHeadline = document.getElementById("bigtable").rows[0].cells;
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
            // @ts-expect-error TS(7005): Variable 'sichtbareSpaltenNummern' implicitly has ... Remove this comment to see the full error message
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
            // @ts-expect-error TS(7005): Variable 'sichtbareSpaltenNummern' implicitly has ... Remove this comment to see the full error message
            sichtbareSpaltenNummern[i] +
            "'>" +
            (i + 1) +
            "</option>"
        );
        // @ts-expect-error TS(2304): Cannot find name 'selection'.
        selection = i;
      }
    // @ts-expect-error TS(7053): Element implicitly has an 'any' type because expre... Remove this comment to see the full error message
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
    // @ts-expect-error TS(7053): Element implicitly has an 'any' type because expre... Remove this comment to see the full error message
    visibleHeadingsSelectUnsorted[sichtbareSpaltenNummern[i]].innerHTML =
      optionsS[i].join("");
  }
}

function toggleChkSpalten() {
  // @ts-expect-error TS(2304): Cannot find name 'chk_spalten'.
  chk_spalten = document.getElementById("chk_spalten");
  // @ts-expect-error TS(2304): Cannot find name 'inputZeilen'.
  inputZeilen = document.getElementById("inputZeilen");
  // @ts-expect-error TS(2304): Cannot find name 'spaltenWahl'.
  spaltenWahl = document.getElementById("spaltenWahl");
  // @ts-expect-error TS(2304): Cannot find name 'zeilenWahl'.
  zeilenWahl = document.getElementById("zeilenWahl");

  // @ts-expect-error TS(2304): Cannot find name 'inputZeilen'.
  if (inputZeilen.style.display == "none" && zeilenWahl.checked)
    // @ts-expect-error TS(2304): Cannot find name 'inputZeilen'.
    inputZeilen.style.display = "initial";
  // @ts-expect-error TS(2304): Cannot find name 'zeilenWahl'.
  else if (!zeilenWahl.checked) inputZeilen.style.display = "none";

  // @ts-expect-error TS(2304): Cannot find name 'chk_spalten'.
  if (chk_spalten.style.display == "none" && spaltenWahl.checked)
    // @ts-expect-error TS(2304): Cannot find name 'chk_spalten'.
    chk_spalten.style.display = "initial";
  // @ts-expect-error TS(2304): Cannot find name 'spaltenWahl'.
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
// @ts-expect-error TS(7006): Parameter 'g' implicitly has an 'any' type.
function isZeilenAngabe_betweenKommas(g) {
  const pattern = /^(v?-?\d+)(-\d+)?((\+)(\d+))*$/;
  return g.match(pattern);
  /*const x = (g.match(/[0-9]+-[0-9]+/g) || []).length;
  const y = (g.match(/[0-9]+-[0-9]+-[0-9]+/g) || []).length;
  return (
    /^([0-9-]+[\+0-9,-]*)$/.test(g) &&
    !["-", "+"].includes(g.slice(-1)) &&
    ((x < 2 && y == 0) || (/^\-?[0-9]+[\+0-9,]*$/.test(g) && x == 0)) &&
    !/--|\+\+|\+\-|\-\+|,\+|\+,|-,/.test(g)
  );*/
}
// @ts-expect-error TS(7006): Parameter 'text' implicitly has an 'any' type.
function isZeilenAngabe(text) {
  if (text.length > 0 && text[0] === "v") {
    text = text.substring(1);
  }
  var a = [];
  var splittedText = text.split(",");
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
// @ts-expect-error TS(7006): Parameter 'MehrereBereiche' implicitly has an 'any... Remove this comment to see the full error message
function BereichToNumbers2(MehrereBereiche, vielfache = false, maxZahl = 1028) {
  MehrereBereiche = MehrereBereiche.split(",")
    // @ts-expect-error TS(7006): Parameter 's' implicitly has an 'any' type.
    .filter((s) => s.trim())
    .join(",");
  const Bereiche = MehrereBereiche.split(",");
  if (!isZeilenAngabe(MehrereBereiche)) {
    return new Set();
  }

  if (!vielfache && maxZahl === 0) {
    maxZahl = Infinity;
  }

  const dazu = new Set();
  const hinfort = new Set();
  let menge;

  for (const EinBereich of Bereiche) {
    if (EinBereich.length > 0 && EinBereich[0] === "v") {
      // @ts-expect-error TS(2304): Cannot find name 'EinBereich2'.
      EinBereich2 = EinBereich.slice(1);
      // @ts-expect-error TS(2304): Cannot find name 'vielfache2'.
      vielfache2 = true;
    } else {
      // @ts-expect-error TS(2304): Cannot find name 'EinBereich2'.
      EinBereich2 = EinBereich;
      // @ts-expect-error TS(2304): Cannot find name 'vielfache2'.
      vielfache2 = false;
    }
    //window.alert(EinBereich);
    BereichToNumbers2_EinBereich(
      // @ts-expect-error TS(2304): Cannot find name 'EinBereich2'.
      EinBereich2,
      dazu,
      hinfort,
      // @ts-expect-error TS(2304): Cannot find name 'vielfache2'.
      (vielfache || vielfache2) && maxZahl == Infinity ? 1028 : maxZahl,
      // @ts-expect-error TS(2304): Cannot find name 'vielfache2'.
      vielfache || vielfache2
    );
  }

  return new Set([...dazu].filter((x) => !hinfort.has(x)));
}

function BereichToNumbers2_EinBereich(
  // @ts-expect-error TS(7006): Parameter 'EinBereich' implicitly has an 'any' typ... Remove this comment to see the full error message
  EinBereich,
  // @ts-expect-error TS(7006): Parameter 'dazu' implicitly has an 'any' type.
  dazu,
  // @ts-expect-error TS(7006): Parameter 'hinfort' implicitly has an 'any' type.
  hinfort,
  // @ts-expect-error TS(7006): Parameter 'maxZahl' implicitly has an 'any' type.
  maxZahl,
  // @ts-expect-error TS(7006): Parameter 'vielfache' implicitly has an 'any' type... Remove this comment to see the full error message
  vielfache
) {
  if (EinBereich.length > 1 && EinBereich[0] === "-") {
    EinBereich = EinBereich.substring(1);
    // @ts-expect-error TS(2304): Cannot find name 'menge'.
    menge = hinfort;
  } else if (EinBereich.length > 0 && EinBereich[0] !== "-") {
    // @ts-expect-error TS(2304): Cannot find name 'menge'.
    menge = dazu;
  } else {
    // @ts-expect-error TS(2304): Cannot find name 'menge'.
    menge = null;
  }

  // @ts-expect-error TS(7034): Variable 'around' implicitly has type 'any[]' in s... Remove this comment to see the full error message
  const around = [];
  // @ts-expect-error TS(2304): Cannot find name 'menge'.
  if (menge !== null) {
    const BereichTuple2 = EinBereich.split("+");
    if (EinBereich.match(/^\d+$/)) {
      EinBereich = EinBereich + "-" + EinBereich;
    } else if (BereichTuple2.length > 0 && BereichTuple2[0].match(/^\d+$/)) {
      EinBereich = BereichTuple2[0] + "-" + BereichTuple2[0];
      if (BereichTuple2.length > 1) {
        EinBereich += "+" + BereichTuple2.slice(1).join("+");
      }
    }
    const BereichCouple = EinBereich.split("-");
    BereichToNumbers2_EinBereich_Menge(
      BereichCouple,
      // @ts-expect-error TS(7005): Variable 'around' implicitly has an 'any[]' type.
      around,
      maxZahl,
      // @ts-expect-error TS(2304): Cannot find name 'menge'.
      menge,
      vielfache
    );
  }
}

function BereichToNumbers2_EinBereich_Menge(
  // @ts-expect-error TS(7006): Parameter 'BereichCouple' implicitly has an 'any' ... Remove this comment to see the full error message
  BereichCouple,
  // @ts-expect-error TS(7006): Parameter 'around' implicitly has an 'any' type.
  around,
  // @ts-expect-error TS(7006): Parameter 'maxZahl' implicitly has an 'any' type.
  maxZahl,
  // @ts-expect-error TS(7006): Parameter 'menge' implicitly has an 'any' type.
  menge,
  // @ts-expect-error TS(7006): Parameter 'vielfache' implicitly has an 'any' type... Remove this comment to see the full error message
  vielfache
) {
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
        BereichCouple[1] = numList[0];
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
  // @ts-expect-error TS(7006): Parameter 'BereichCouple' implicitly has an 'any' ... Remove this comment to see the full error message
  BereichCouple,
  // @ts-expect-error TS(7006): Parameter 'around' implicitly has an 'any' type.
  around,
  // @ts-expect-error TS(7006): Parameter 'maxZahl' implicitly has an 'any' type.
  maxZahl,
  // @ts-expect-error TS(7006): Parameter 'menge' implicitly has an 'any' type.
  menge
) {
  let i = 0;
  // @ts-expect-error TS(2304): Cannot find name 'aroundSet'.
  aroundSet = new Set(around);
  // @ts-expect-error TS(2304): Cannot find name 'aroundSet'.
  aroundSet.delete(0);
  //window.alert(Array.from(around).join(","));
  // @ts-expect-error TS(2304): Cannot find name 'aroundSet'.
  if (around.length === 0 || aroundSet.size == 0) {
    // @ts-expect-error TS(7006): Parameter 'a' implicitly has an 'any' type.
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
    // @ts-expect-error TS(7006): Parameter 'a' implicitly has an 'any' type.
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
  // @ts-expect-error TS(7006): Parameter 'BereichCouple' implicitly has an 'any' ... Remove this comment to see the full error message
  BereichCouple,
  // @ts-expect-error TS(7006): Parameter 'around' implicitly has an 'any' type.
  around,
  // @ts-expect-error TS(7006): Parameter 'maxZahl' implicitly has an 'any' type.
  maxZahl,
  // @ts-expect-error TS(7006): Parameter 'menge' implicitly has an 'any' type.
  menge
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
function zeilenAngabenToMengeDirekt(welches = 0, v = false) {
  switch (welches) {
    case 1:
      // @ts-expect-error TS(2304): Cannot find name 'text'.
      text = document.getElementById("zeilenErlaubtText").value;
      break;
    case 2:
      // @ts-expect-error TS(2304): Cannot find name 'text'.
      text = document.getElementById("zaehlungErlaubtText").value;
      break;
    case 3:
      // @ts-expect-error TS(2304): Cannot find name 'text'.
      text = document.getElementById("primVielfache").value;
      break;
    case 4:
      // @ts-expect-error TS(2304): Cannot find name 'text'.
      text = document.getElementById("primZahlKreuzRadius").value;
      break;
    case 5:
      // @ts-expect-error TS(2304): Cannot find name 'text'.
      text = document.getElementById("VielfacheErlaubtText").value;
      break;
    case 6:
      // @ts-expect-error TS(2304): Cannot find name 'text'.
      text = document.getElementById("potenzenErlaubtText").value;
      break;
    default:
      // @ts-expect-error TS(2304): Cannot find name 'text'.
      text = "Ungültige Auswahl";
      break;
  }
  // @ts-expect-error TS(2304): Cannot find name 'text'.
  erlaubteZeilen = BereichToNumbers2(text, welches == 5 || v ? true : false);
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
var erlaubteZeilen = new Set();

// @ts-expect-error TS(7006): Parameter 'zeilenAngaben' implicitly has an 'any' ... Remove this comment to see the full error message
function makeAllerlaubteZeilenVielfacher(zeilenAngaben) {
  zeilenAngaben = Array.from(zeilenAngaben);
  var muls;
  erlaubteZeilen = new Set();
  for (var i = 0; i < zeilenAngaben.length; i++) {
    // @ts-expect-error TS(2304): Cannot find name 'last'.
    last = zeilenAngaben[i][0];
    muls = [];
    // @ts-expect-error TS(2304): Cannot find name 'mul'.
    mul = 1;
    // @ts-expect-error TS(2304): Cannot find name 'last'.
    last = mul * zeilenAngaben[i][0];
    // @ts-expect-error TS(2304): Cannot find name 'last'.
    while (last < 1025) {
      // @ts-expect-error TS(2304): Cannot find name 'last'.
      muls.push(last);
      // @ts-expect-error TS(2304): Cannot find name 'last'.
      last = mul * zeilenAngaben[i][0];
      // @ts-expect-error TS(2304): Cannot find name 'mul'.
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

// @ts-expect-error TS(7006): Parameter 'zeilenAngaben' implicitly has an 'any' ... Remove this comment to see the full error message
function makeAllerlaubteZeilenPotenzen(zeilenAngaben) {
  zeilenAngaben = Array.from(zeilenAngaben);
  erlaubteZeilen = new Set();
  for (var i = 0; i < zeilenAngaben.length; i++) {
    if (zeilenAngaben[i] > 0) {
      // @ts-expect-error TS(2304): Cannot find name 'exponent'.
      exponent = 1;
      // @ts-expect-error TS(2304): Cannot find name 'potenz'.
      potenz = Math.pow(zeilenAngaben[i], exponent);
      // @ts-expect-error TS(2304): Cannot find name 'potenz'.
      while (potenz < 1025) {
        // @ts-expect-error TS(2304): Cannot find name 'potenz'.
        erlaubteZeilen.add(potenz);
        // @ts-expect-error TS(2304): Cannot find name 'potenz'.
        potenz = Math.pow(zeilenAngaben[i], exponent);
        //window.alert(potenz);
        // @ts-expect-error TS(2304): Cannot find name 'exponent'.
        exponent++;
      }
    }
  }
  return erlaubteZeilen;
}

// @ts-expect-error TS(7006): Parameter 'setA' implicitly has an 'any' type.
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
  // @ts-expect-error TS(2304): Cannot find name 'innen'.
  innen = document.getElementById("proInnen").checked;
  // @ts-expect-error TS(2304): Cannot find name 'aussen'.
  aussen = document.getElementById("proAussen").checked;
  // @ts-expect-error TS(2304): Cannot find name 'hand'.
  hand = document.getElementById("gegenDritte").checked;
  // @ts-expect-error TS(2304): Cannot find name 'faehig'.
  faehig = document.getElementById("proDritte").checked;
  erlaubteZeilen = new Set();

  // @ts-expect-error TS(2304): Cannot find name 'hand'.
  if (hand || faehig) {
    // @ts-expect-error TS(2304): Cannot find name 'hand'.
    if (hand) inkrement = 3;
    // @ts-expect-error TS(2304): Cannot find name 'inkrement'.
    else inkrement = 2;
    // @ts-expect-error TS(2304): Cannot find name 'inkrement'.
    for (var i = 0; i < 1025; i += inkrement) erlaubteZeilen.add(i);
    return erlaubteZeilen;
  }

  // @ts-expect-error TS(2304): Cannot find name 'innen'.
  if (innen || aussen) {
    var innenAussen;
    // @ts-expect-error TS(2304): Cannot find name 'aussen'.
    if (aussen) innenAussen = new Set([1, 7, 13, 19]);
    // @ts-expect-error TS(2304): Cannot find name 'innen'.
    if (innen) innenAussen = new Set([5, 11, 17, 23]);

    for (var i = 0; i < 1025; i++) {
      // @ts-expect-error TS(2304): Cannot find name 'primZahlenModulo'.
      primZahlenModulo = new Set();
      // @ts-expect-error TS(2304): Cannot find name 'k'.
      for (k = 2; k < primZahlen.length; k += 1) {
        // @ts-expect-error TS(2304): Cannot find name 'vielfacher'.
        vielfacher = 1;
        // @ts-expect-error TS(2304): Cannot find name 'vielfacher'.
        while (i / vielfacher > 2) {
          // @ts-expect-error TS(2304): Cannot find name 'primZahlen'.
          if (primZahlen[k] == i / vielfacher) {
            // @ts-expect-error TS(2304): Cannot find name 'vielfacher'.
            vielfacher = i;
            // @ts-expect-error TS(2304): Cannot find name 'primZahlenModulo'.
            primZahlenModulo.add(primZahlen[k] % 24);
          }
          // @ts-expect-error TS(2304): Cannot find name 'vielfacher'.
          vielfacher++;
        }
      }
      // @ts-expect-error TS(2304): Cannot find name 'primZahlenModulo'.
      if (intersection(primZahlenModulo, innenAussen).size != 0)
        erlaubteZeilen.add(i);
    }
    return erlaubteZeilen;
  }
}

function makeAllAllowedZeilenHimmelskoerper() {
  // @ts-expect-error TS(2304): Cannot find name 'sonneWahl'.
  sonneWahl = document.getElementById("sonneWahl").checked;
  // @ts-expect-error TS(2304): Cannot find name 'mondWahl'.
  mondWahl = document.getElementById("mondWahl").checked;
  // @ts-expect-error TS(2304): Cannot find name 'planetWahl'.
  planetWahl = document.getElementById("planetWahl").checked;
  // @ts-expect-error TS(2304): Cannot find name 'schwarzeSonneWahl'.
  schwarzeSonneWahl = document.getElementById("schwarzeSonneWahl").checked;
  erlaubteZeilen = new Set();
  // @ts-expect-error TS(2304): Cannot find name 'mondWahl'.
  if (mondWahl) {
    // @ts-expect-error TS(2304): Cannot find name 'alleMonde'.
    erlaubteZeilen = new Set(alleMonde);
    return erlaubteZeilen;
  }
  // @ts-expect-error TS(2304): Cannot find name 'sonneWahl'.
  if (sonneWahl) {
    // @ts-expect-error TS(2304): Cannot find name 'alleMondeSet'.
    alleMondeSet = new Set(alleMonde);
    for (var i = 1; i < 1025; i++) {
      // @ts-expect-error TS(2304): Cannot find name 'alleMondeSet'.
      if (!alleMondeSet.has(i)) erlaubteZeilen.add(i);
    }
    return erlaubteZeilen;
  }
  // @ts-expect-error TS(2304): Cannot find name 'planetWahl'.
  if (planetWahl) {
    for (var i = 2; i < 1025; i += 2) erlaubteZeilen.add(i);
    return erlaubteZeilen;
  }
  // @ts-expect-error TS(2304): Cannot find name 'schwarzeSonneWahl'.
  if (schwarzeSonneWahl) {
    for (var i = 3; i < 1025; i += 3) erlaubteZeilen.add(i);
    return erlaubteZeilen;
  }
}
// @ts-expect-error TS(7006): Parameter 'zeilenAngaben' implicitly has an 'any' ... Remove this comment to see the full error message
function makeAllowedZeilenFromPrimVielfacher(zeilenAngaben) {
  zeilenAngaben = Array.from(zeilenAngaben);
  erlaubteZeilen = new Set();
  // @ts-expect-error TS(2304): Cannot find name 'ersteSpalte'.
  ersteSpalte = document
    .getElementById("bigtable")
    .getElementsByClassName("r_0");
  for (var i = 0; i < 1025; i++)
    for (var k = 0; k < zeilenAngaben.length; k++)
      if (zahlIstVielfacherEinerPrimzahl(i, zeilenAngaben[k]))
        erlaubteZeilen.add(i);
  return erlaubteZeilen;
}

// @ts-expect-error TS(7006): Parameter 'zahl' implicitly has an 'any' type.
function zahlIstVielfacherEinerPrimzahl(zahl, vielfacher) {
  zahl = parseInt(zahl);
  vielfacher = parseInt(vielfacher);
  if (zahl === "NaN" || vielfacher === "Nan") return false;

  // @ts-expect-error TS(2304): Cannot find name 'stimmt'.
  stimmt = false;
  // @ts-expect-error TS(2304): Cannot find name 'primZahlen'.
  for (var i = 0; i < primZahlen.length; i++)
    // @ts-expect-error TS(2304): Cannot find name 'primZahlen'.
    if (primZahlen[i] == zahl / vielfacher) stimmt = true;
  // @ts-expect-error TS(2304): Cannot find name 'stimmt'.
  return stimmt;
}

// @ts-expect-error TS(7006): Parameter 'zeilenMenge' implicitly has an 'any' ty... Remove this comment to see the full error message
function makeAllowedZeilenFromZaehlung(zeilenMenge) {
  // @ts-expect-error TS(2304): Cannot find name 'ersteSpalte'.
  ersteSpalte = document
    .getElementById("bigtable")
    .getElementsByClassName("r_0");
  // @ts-expect-error TS(2304): Cannot find name 'erlaubteZaehlungen'.
  erlaubteZaehlungen = zeilenMenge;
  erlaubteZeilen = new Set();
  //window.alert(Array.from(erlaubteZaehlungen).join(" "));
  //window.alert(ersteSpalte.length.toString());

  // @ts-expect-error TS(2304): Cannot find name 'i'.
  for (i = 0; i < ersteSpalte.length; i++) {
    //window.alert(ersteSpalte[i].getElementsByTagName("label")[0].innerHTML);
    // @ts-expect-error TS(2304): Cannot find name 'zaehlung'.
    zaehlung = parseInt(ersteSpalte[i].innerHTML.trim());
    //window.alert(zaehlung.toString());
    // @ts-expect-error TS(2304): Cannot find name 'zaehlung'.
    if (zaehlung != "NaN" && erlaubteZaehlungen.has(zaehlung)) {
      // @ts-expect-error TS(2304): Cannot find name 'wirklicheZeile'.
      wirklicheZeile = ersteSpalte[i].className.match(/z_\s*(\d+)/g);
      //window.alert(ersteSpalte[i].className);
      //window.alert(wirklicheZeile);
      // @ts-expect-error TS(2304): Cannot find name 'wirklicheZeile'.
      if (wirklicheZeile.length > 0) {
        // @ts-expect-error TS(2304): Cannot find name 'wirklicheZeile'.
        wirklicheZeile = wirklicheZeile[0].substr(2);
        // @ts-expect-error TS(2304): Cannot find name 'wirklicheZeile'.
        erlaubteZeilen.add(parseInt(wirklicheZeile));
      }
    }
  }
  return erlaubteZeilen;
}

// @ts-expect-error TS(7006): Parameter 'zeilenAngaben' implicitly has an 'any' ... Remove this comment to see the full error message
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

// @ts-expect-error TS(7006): Parameter 'zeilenAngaben' implicitly has an 'any' ... Remove this comment to see the full error message
function makeAllowedZeilenFromPrimZahlKreuzRadius(zeilenAngaben) {
  zeilenAngaben = Array.from(zeilenAngaben);
  erlaubteZeilen = new Set();
  for (var i = 1; i < 1025; i++)
    for (var k = 0; k < zeilenAngaben.length; k++)
      if (zeilenAngaben[k] == Math.floor((i - 1) / 24) + 1)
        erlaubteZeilen.add(i);

  return zeilenAngaben;
}

var spalten_r__ = new Set();

function get_r__SpaltenNummern() {
  // @ts-expect-error TS(2304): Cannot find name 'tabelenkopfZeile'.
  tabelenkopfZeile = tdClasses;
  // @ts-expect-error TS(2304): Cannot find name 'tabelenkopfZeile'.
  for (var i = 0; i < tabelenkopfZeile.length; i++) {
    // @ts-expect-error TS(2304): Cannot find name 'tabelenkopfZeile'.
    if (tabelenkopfZeile[i].style.display === "table-cell") {
      // @ts-expect-error TS(2304): Cannot find name 'num'.
      num = tabelenkopfZeile[i].className.match(/r_(\d+)/);
      // @ts-expect-error TS(2304): Cannot find name 'num'.
      if (num != null && num.length > 1) num = num[1];
      // @ts-expect-error TS(2304): Cannot find name 'num'.
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

// @ts-expect-error TS(7006): Parameter 'which' implicitly has an 'any' type.
function erlaubeVerbieteZeilenBeiZeilenErlaubenVerbieten(which) {
  // @ts-expect-error TS(2304): Cannot find name 'Spalten_r__Array'.
  Spalten_r__Array = Array.from(spalten_r__);
  // @ts-expect-error TS(2304): Cannot find name 'erlaubteZeilen_Array'.
  erlaubteZeilen_Array = Array.from(erlaubteZeilen);
  // @ts-expect-error TS(2304): Cannot find name 'erlaubteZeilen_String'.
  erlaubteZeilen_String = erlaubteZeilen_Array.join(",");
  // @ts-expect-error TS(2304): Cannot find name 'neuErlauben'.
  neuErlauben = document.getElementsByClassName("neuErlauben")[which].checked;
  // @ts-expect-error TS(2304): Cannot find name 'neuHinfort'.
  neuHinfort = document.getElementsByClassName("neuHinfort")[which].checked;
  // @ts-expect-error TS(2304): Cannot find name 'dazuErlauben'.
  dazuErlauben = document.getElementsByClassName("dazuErlauben")[which].checked;
  // @ts-expect-error TS(2304): Cannot find name 'dazuHinfort'.
  dazuHinfort = document.getElementsByClassName("dazuHinfort")[which].checked;
  // @ts-expect-error TS(2304): Cannot find name 'dazuEinschraenkend'.
  dazuEinschraenkend =
    // @ts-expect-error TS(2339): Property 'checked' does not exist on type 'Element... Remove this comment to see the full error message
    document.getElementsByClassName("dazuEinschraenkend")[which].checked;
  //window.alert(neuErlauben+" "+neuHinfort+" "+dazuErlauben+" "+dazuHinfort);
  // @ts-expect-error TS(2304): Cannot find name 'spalte'.
  spalte = document.getElementById("bigtable").rows;
  // @ts-expect-error TS(2304): Cannot find name 'spalte'.
  for (var s = 1; s < spalte.length; s++) {
    // @ts-expect-error TS(2304): Cannot find name 'tabellenZelle'.
    tabellenZelle = spalte[s];
    if (s < 115)
      zeilenLetztendlichZeigenVerstecken(
        s,
        // @ts-expect-error TS(2304): Cannot find name 'neuErlauben'.
        neuErlauben,
        // @ts-expect-error TS(2304): Cannot find name 'dazuErlauben'.
        dazuErlauben,
        // @ts-expect-error TS(2304): Cannot find name 'neuHinfort'.
        neuHinfort,
        // @ts-expect-error TS(2304): Cannot find name 'dazuHinfort'.
        dazuHinfort,
        // @ts-expect-error TS(2304): Cannot find name 'tabellenZelle'.
        tabellenZelle,
        // @ts-expect-error TS(2304): Cannot find name 'dazuEinschraenkend'.
        dazuEinschraenkend
      );
    else {
      // @ts-expect-error TS(2304): Cannot find name 'echteZeilenNummer'.
      echteZeilenNummer = spalte[s].cells[0].className.match(/z_\s*(\d+)/g);
      // @ts-expect-error TS(2304): Cannot find name 'echteZeilenNummer'.
      if (echteZeilenNummer != null && echteZeilenNummer.length > 0) {
        // @ts-expect-error TS(2304): Cannot find name 'echteZeilenNummer'.
        echteZeilenNummer = parseInt(echteZeilenNummer[0].substr(2));
        zeilenLetztendlichZeigenVerstecken(
          // @ts-expect-error TS(2304): Cannot find name 'echteZeilenNummer'.
          echteZeilenNummer,
          // @ts-expect-error TS(2304): Cannot find name 'neuErlauben'.
          neuErlauben,
          // @ts-expect-error TS(2304): Cannot find name 'dazuErlauben'.
          dazuErlauben,
          // @ts-expect-error TS(2304): Cannot find name 'neuHinfort'.
          neuHinfort,
          // @ts-expect-error TS(2304): Cannot find name 'dazuHinfort'.
          dazuHinfort,
          // @ts-expect-error TS(2304): Cannot find name 'tabellenZelle'.
          tabellenZelle,
          // @ts-expect-error TS(2304): Cannot find name 'dazuEinschraenkend'.
          dazuEinschraenkend
        );
      }
    }
  }
}

function zeilenLetztendlichZeigenVerstecken(
  // @ts-expect-error TS(7006): Parameter 's' implicitly has an 'any' type.
  s,
  // @ts-expect-error TS(7006): Parameter 'neuErlauben' implicitly has an 'any' ty... Remove this comment to see the full error message
  neuErlauben,
  // @ts-expect-error TS(7006): Parameter 'dazuErlauben' implicitly has an 'any' t... Remove this comment to see the full error message
  dazuErlauben,
  // @ts-expect-error TS(7006): Parameter 'neuHinfort' implicitly has an 'any' typ... Remove this comment to see the full error message
  neuHinfort,
  // @ts-expect-error TS(7006): Parameter 'dazuHinfort' implicitly has an 'any' ty... Remove this comment to see the full error message
  dazuHinfort,
  // @ts-expect-error TS(7006): Parameter 'tabellenZelle' implicitly has an 'any' ... Remove this comment to see the full error message
  tabellenZelle,
  // @ts-expect-error TS(7006): Parameter 'dazuEinschraenkend' implicitly has an '... Remove this comment to see the full error message
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
  // @ts-expect-error TS(2322): Type 'Set<unknown> | undefined' is not assignable ... Remove this comment to see the full error message
  erlaubteZeilen = makeAllAllowedZeilenHimmelskoerper();
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
  //makeAllowedZeilenFromPrimVielfacher(zeilenAngabenToContainer(3));
  makeAllowedZeilenFromPrimVielfacher(zeilenAngabenToMengeDirekt(3));
  get_r__SpaltenNummern();
  erlaubeVerbieteZeilenBeiZeilenErlaubenVerbieten(5);
}
function clickPrimRichtungenErlaubenUsw() {
  // @ts-expect-error TS(2322): Type 'Set<unknown> | undefined' is not assignable ... Remove this comment to see the full error message
  erlaubteZeilen = makeAllAllowedZeilenPrimRichtungen();
  get_r__SpaltenNummern();
  erlaubeVerbieteZeilenBeiZeilenErlaubenVerbieten(6);
}

function clickPrimZahlKreuzRadiusErlaubenUsw() {
  makeAllowedZeilenFromPrimZahlKreuzRadius(zeilenAngabenToMengeDirekt(4));
  get_r__SpaltenNummern();
  erlaubeVerbieteZeilenBeiZeilenErlaubenVerbieten(7);
}