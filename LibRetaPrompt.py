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
]
hauptForNeben = ("-zeilen", "-spalten", "-kombination", "-ausgabe", "-h", "-help")

notParameterValues = (
    ausgabeParas + zeilenParas + kombiMainParas + spalten + mainParas,
)
hauptForNebenSet = set(hauptForNeben)

ausgabeArt = ["bbcode", "html", "csv", "shell", "markdown"]

befehle = (
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
)

befehle2: set = set(befehle) - {"reta"}
