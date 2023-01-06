import sys

import reta

retaProgram = reta.Program([sys.argv[0], "-nichts"])
mainParas = ["-" + a for a in retaProgram.mainParaCmds]
spalten = ["--" + a[0] + "=" for a in retaProgram.paraDict.keys()]
#
#
# DAS SOLLTE ICH BESSER ALLES ORDENTLICH IN RETA.PY PACKEN, STATT ES HIER AUSZUSCHREIBEN, WEIL SONST DOPPELT!
# D.H. spezielle DatenTypen dafür in Reta.py anlegen!
# DAS GEHT SCHNELL, FLEIßARBEIT, WEIL KAUM BUGGEFAHR
#
# startpunkt: dict = {}
spaltenDict = {}
for tupel in retaProgram.paraNdataMatrix:
    for haupt in tupel[0]:
        try:
            spaltenDict[haupt] += list(tupel[1])
        except KeyError:
            spaltenDict[haupt] = list(tupel[1])

spalten += ["--breite=", "--breiten=", "--keinenummerierung"]

ausgabeParas = [
    "--nocolor",
    "--justtext",
    "--art=",
    "--onetable",
    "--spaltenreihenfolgeundnurdiese=",
    "--endlessscreen",
    "--endless",
    "--dontwrap",
    "--breite=",
    "--breiten=",
]
kombiMainParas = ["--galaxie=", "--universum="]
zeilenParas = [
    "--zeit=",
    "--zaehlung=",
    "--vorhervonausschnitt=",
    "--primzahlvielfache=",
    "--nachtraeglichdavon=",
    "--alles",
    "--potenzenvonzahlen=",
    "--typ=",
    "--vielfachevonzahlen=",
    "--oberesmaximum=",
]
hauptForNeben = ("-zeilen", "-spalten", "-kombination", "-ausgabe", "-h", "-help")

notParameterValues = (
    ausgabeParas + zeilenParas + kombiMainParas + spalten + mainParas,
)
hauptForNebenSet = set(hauptForNeben)

ausgabeArt = ["bbcode", "html", "csv", "shell", "markdown"]

# [*]--grundstrukturen[list][*]konkreta,impulse,gefuehle,zustaende,wirklichkeiten,metasysteme,paradigmen,meta-paradigmen,positionen,geist,verbundenheiten,triebe,lust,reflexe,absicht6,absicht7,absicht10,absicht17,zeit,funktionen,vorstellungen,wahrheit,wahrnehmung,achtung,focus,absicht1pro8,ziele,wachbewusstsein,kategorien,regung,energie,universelleeigenschaften,stimmungen,klassen,kombinationen,empathie,energie,garben,nachvollziehen,absicht1pro6,verhalten[/list]
wahl15 = {
    "_": "meta-paradigmen,geist",
    "_15": "meta-paradigmen,geist,nachvollziehen",
    "_2": "konkreta,focus",
    "_5": "impulse",
    "_7": "gefuehle",
    "_8": "zustaende",
    "_10": "wirklichkeiten,wahrheit,wahrnehmung",
    "_12": "metasysteme,ordnenundfiltern",
    "_13": "paradigmen",
    "_17": "positionen",
    "_18": "verbundenheiten",
    "_6": "triebe",
    "_9": "lust",
    "_3": "reflexe,existenzialien",
    "_13_6": "absicht6",
    "_13_7": "absicht7",
    "_13_10": "absicht10",
    "_13_17": "absicht17",
    "_10_4": "zeit",
    "_16": "funktionen,vorstellungen",
    "_4": "achtung",
    "_13_1pro8": "absicht1pro8",
    "_13_1pro6": "absicht1pro6",
    "_1pro15": "reflektion,kategorien",
    "_1": "regung",
    "_30": "energie,universelleeigenschaften",
    "_14": "stimmungen,kombinationen",
    "_20": "klassen",
    "_37": "empathie",
    "_31": "garben",
    "_11": "verhalten",
    "_5_10": "bedeutung",
    "_17_6": "themen",
    "_17_6_10mit4": "optimierung",
    "_36": "attraktionen",
    "_13_16": "absicht16",
    "_18_7": "liebe",
    "_18_10": "koalitionen",
    "_18_17": "ansichten",
    "_1pro8": "reziprokeprinzipien",
    "_1pro5": "bestrebungen",
    "_1pro3": "bedingung",
    "_10_4_18_6": "relativerzeitbetrag",
    "_18_6": "zahlenvergleich",
    "_21": "leidenschaften",
    "_26": "erwartungen",
    "_19": "extremalien,ziele",
    "_18_15": "universellerkomperativ",
    "_18_15_n_vs_1pro_n": "relativreziprokuniversell",
}

befehle = ["15" + a for a in wahl15.keys()] + [
    "mond",
    "reta",
    "absicht",
    "motiv",
    "thomas",
    "universum",
    "motive",
    "absichten",
    "vielfache",
    "einzeln",
    "multis",
    "modulo",
    "prim",
    "primfaktorzerlegung",
    "procontra",
    "prim24",
    "primfaktorzerlegungModulo24",
    "help",
    "hilfe",
    "abc",
    "abcd",
    "alles",
    "a",
    "u",
    "befehle",
    "t",
    "richtung",
    "r",
    "v",
    "h",
    "p",
    "mo",
    "mu",
    "primzahlkreuz",
    "ende",
    "exit",
    "quit",
    "q",
    ":q",
    "shell",
    "s",
    "math",
    "loggen",
    "nichtloggen",
    "mulpri",
    "b",
    "python",
    "w",
    "teiler",
    "BefehlSpeichernDanach",
    "S",
    "BefehlSpeicherungLöschen",
    "l",
    "BefehlSpeicherungAusgeben",
    "o",
    "BefehlsSpeicherungsModusAus",
    "x",
    "BefehlSpeichernDavor",
    "s",
]

befehle2: set = set(befehle) - {"reta"}
