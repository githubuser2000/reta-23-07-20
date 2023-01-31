import sys

import reta
from center import Primzahlkreuz_pro_contra_strs

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

wahl15 = {
    #    "_": "Strukturalien_bzw_Meta-Paradigmen_bzw_Transzendentalien_(15),Geist_(15)",
    "_15": "Strukturalien_bzw_Meta-Paradigmen_bzw_Transzendentalien_(15),Geist_(15),"
    + Primzahlkreuz_pro_contra_strs[1],
    "_2": "Konkreta_und_Focus_(2)",
    "_5": "Impulse_(5)",
    "_7": "Gefühle_(7)",
    "_8": "Modus_und_Sein_(8)",
    "_10": "Wirklichkeiten_(10),Wirklichkeiten_Wahrheit_Wahrnehmung_(10)",
    "_12": "Meta-Systeme_(12),Ordnung_und_Filterung_12_und_1pro12",
    "_13": "Paradigmen_sind_Absichten_(13)",
    "_17": "Gedanken_sind_Positionen_(17)",
    "_18": "Verbundenheiten_(18)",
    "_6": "Triebe_und_Bedürfnisse_(6)",
    "_9": "Lust_(9)",
    "_3": "Reflexe_(3),Existenzialien_(3)",
    "_13_6": "Absicht_6",
    "_13_7": "Absicht_7",
    "_13_10": "Absicht_10",
    "_13_17": "Absicht_17",
    "_10_4": "Zeit_(4)_als_Wirklichkeit",
    "_16": "Funktionen_Vorstellungen_(16)",
    "_4": "Achtung_(4)",
    "_13_1pro8": "Absicht_1/8",
    "_13_1pro6": "Absicht_1/6",
    "_1pro15": "Reflektion_und_Kategorien_(1/15)",
    "_1": "Regungen_(1)",
    "_30": "Energie_und_universelle_Eigenschaften_(30)",
    "_14": "Stimmungen_Kombinationen_(14)",
    "_20": "Klassen_(20)",
    "_37": "Empathie_(37)",
    "_31": "Garben_und_Verhalten_nachfühlen(31)",
    "_11": "Verhalten_(11)",
    "_5_10": "Bedeutung_(10)",
    "_17_6": "Themen_(6)",
    "_17_6_10mit4": "Optimierung_(10)",
    "_36": "Attraktionen_(36)",
    "_13_16": "Absicht_16",
    "_18_7": "Liebe_(7)",
    "_18_10": "Koalitionen_(10)",
    "_18_17": "Ansichten_Standpunkte_(18_17)",
    "_1pro8": "Reziproke_Prinzipien(1/8)",
    "_1pro5": "Bestrebungen(1/5)",
    "_1pro3": "Bedingung_und_Auslöser_(1/3)",
    "_10_4_18_6": "relativer_Zeit-Betrag_(15_10_4_18_6)",
    "_18_6": "Zahlenvergleich_(15_18_6)",
    "_21": "Leidenschaften_(21)",
    "_26": "Erwartungshaltungen_(26)",
    "_19": "Extremalien_(19),Ziele_(19)",
    "_18_15": "universeller_Komperativ_(18→15)",
    "_18_15_n-vs-1pron": "Relation_zueinander_reziprok_Universellen_(18→n_vs._1/n)",
    "_1pro13": "Sollen_Frage_Vorgehensweise_(1/13)",
    "_1pro19": "Fundament_(1/19)",
    "_90": "abhängige_Verbundenheit_(90)",
    "_13_13": "Helfen_(13)",
}

zumVergleich = []
for a in reta.Program(["reta", "-zeilen"]).paraNdataMatrix:
    for b in a[1]:
        zumVergleich += [b]

for a in wahl15.values():
    for b in a.split(","):
        assert b in zumVergleich


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
