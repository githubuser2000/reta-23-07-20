import sys
from copy import copy, deepcopy
from enum import Enum
from typing import Optional

import reta
from center import (BereichToNumbers2, Primzahlkreuz_pro_contra_strs,
                    isZeilenAngabe, isZeilenAngabe_betweenKommas,
                    isZeilenBruchOrGanzZahlAngabe)

retaProgram = reta.Program([sys.argv[0], "-nichts"])
mainParas = ["-" + a for a in retaProgram.mainParaCmds]
spalten = ["--" + a[0] + "=" for a in retaProgram.paraDict.keys()]
eigsN, eigsR = [], []
for pp in retaProgram.paraDict.keys():
    if pp[0] == "konzept":
        eigsN += [pp[1]]
    elif pp[0] == "konzept2":
        eigsR += [pp[1]]


class PromptModus(Enum):
    normal = 0
    speichern = 1
    loeschenStart = 2
    speicherungAusgaben = 3
    loeschenSelect = 4
    speicherungAusgabenMitZusatz = 5
    AusgabeSelektiv = 6


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

zeilenTypen = ["sonne", "mond", "planet", "schwarzesonne"]
zeilenZeit = ["heute", "gestern", "morgen"]


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
    "--keineleereninhalte",
    "--keinenummerierung",
]
kombiMainParas = ["--galaxie=", "--universum="]
zeilenParas = [
    # "--nichts",
    "--zeit=",
    "--zaehlung=",
    "--vorhervonausschnitt=",
    "--vorhervonausschnittteiler",
    "--primzahlvielfache=",
    "--nachtraeglichneuabzaehlung=",
    "--nachtraeglichneuabzaehlungvielfache=",
    "--alles",
    "--potenzenvonzahlen=",
    "--typ=",
    "--vielfachevonzahlen=",
    "--oberesmaximum=",
]
hauptForNeben = ("-zeilen", "-spalten", "-kombination", "-ausgabe", "-h", "-help")

notParameterValues = ausgabeParas + zeilenParas + kombiMainParas + spalten + mainParas
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
    "_10": "Wirklichkeiten_Wahrheit_Wahrnehmung_(10)",
    "_12": "Meta-Systeme_(12),Ordnung_und_Filterung_12_und_1pro12",
    "_13": "Paradigmen_sind_Absichten_(13)",
    "_17": "Gedanken_sind_Positionen_(17)",
    "_18": "Verbundenheiten_(18)",
    "_6": "Triebe_und_Bedürfnisse_(6)",
    "_9": "Lust_(9)",
    "_3": "Reflexe_(3),Existenzialien_(3)",
    "_13_6": "Absicht_6_ist_Vorteilsmaximierung",
    "_13_7": "Absicht_7_ist_Selbstlosigkeit",
    "_13_10": "Absicht_10_ist_Wirklichkeit_erkennen",
    "_13_17": "Absicht_17_ist_zu_meinen",
    "_10_4": "Zeit_(4)_als_Wirklichkeit",
    "_16": "Funktionen_Vorstellungen_(16)",
    "_4": "Achtung_(4)",
    "_13_1pro8": "Absicht_1/8",
    "_13_1pro6": "Absicht_1/6_ist_Reinigung_und_Klarheit",
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
    "_13_16": "Absicht_16_ist_zu_genügen",
    "_18_7": "Liebe_(7)",
    "_18_10": "Koalitionen_(10)",
    "_18_17": "Ansichten_Standpunkte_(18_17)",
    "_1pro8": "Prinzipien(1/8)",
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
    "_13_13": "Absicht_13_ist_Helfen",
    "_1pro12": "Karte_Filter_und_Unterscheidung_(1/12)",
}

zumVergleich = []
gebrochenErlaubteZahlen: set = set()
for a in reta.Program(["reta", "-zeilen"]).paraNdataMatrix:
    for b in a[1]:
        zumVergleich += [b]
        if len(set(a[0]) & {"gebrochenuniversum", "gebrochengalaxie"}) > 0:
            gebrochenErlaubteZahlen |= {int(b)}
gebrochenErlaubteZahlen -= {max(gebrochenErlaubteZahlen)}

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
    # "x",
    "BefehlSpeichernDavor",
    "keineEinZeichenZeilenPlusKeineAusgabeWelcherBefehlEsWar",
]
befehle += ["EIGN" + a for a in eigsN] + ["EIGR" + a for a in eigsR]

befehle2: set = set(befehle) - {"reta"}


def isReTaParameter(t: str):
    return (
        len(t) > 0
        and t[0] == "-"
        and not isZeilenAngabe(t)
        and t.split("=")[0] in [str(c).split("=")[0] for c in notParameterValues]
    )


def stextFromKleinKleinKleinBefehl(ifKurzKurz, promptMode2, stext, stext2, textDazu):
    for s_ in tuple(deepcopy(stext)):
        s_m = s_
        if s_[2:] not in wahl15 and s_ not in befehle and stext[0] != "reta":
            textDazu = []
            nn: Optional[int] = 0
            for iii, s_3 in enumerate(s_[::-1]):
                if s_3.isdecimal():
                    nn = iii
                    break
            if nn > 0:
                s_b = s_[-nn:] + s_[:-nn]
            else:
                s_b = s_
            n: Optional[int] = None
            for ii, s_3 in enumerate(s_b):
                if s_3.isdecimal():
                    n = ii
                    break
            try:
                if s_b[int(n) - 1] == "-":
                    n -= 1
            except:
                pass

            if n is not None:
                # (
                #    brueche_Z,
                #    zahlenAngaben__Z,
                #    fullBlockIsZahlenbereichAndBruch_Z,
                # ) = getFromZahlenBereichBruchAndZahlenbereich(s_b[n:], [], [])
                (
                    bruchAndGanzZahlEtwaKorrekterBereich,
                    bruchBereichsAngaben,
                    bruchRanges,
                    zahlenAngaben__Z,
                    fullBlockIsZahlenbereichAndBruch_Z,
                ) = verifyBruchNganzZahlCommaList(
                    [],
                    "",
                    [],
                    [],
                    [],
                    s_b[n:],
                    [],
                )

                if fullBlockIsZahlenbereichAndBruch_Z:
                    s_ = s_b
                    buchst = set(s_[:n]) & {
                        "a",
                        "t",
                        "v",
                        "u",
                        "p",
                        "r",
                        "w",
                        "s",
                        "o",
                        "S",
                        "e",
                        # "keineEinZeichenZeilenPlusKeineAusgabeWelcherBefehlEsWar",
                    }
                    setTextLenIs1 = (
                        len(
                            set(stext)
                            - {
                                "e",
                                "keineEinZeichenZeilenPlusKeineAusgabeWelcherBefehlEsWar",
                            }
                        )
                        == 1
                    )

                    if (len(buchst) != len(s_[:n]) or len(buchst) == 0) and not (
                        setTextLenIs1 and fullBlockIsZahlenbereichAndBruch_Z
                    ):
                        s_ = s_m
                    else:
                        ifKurzKurz = True
                        # erst hier passiert wirklich etwas
                        if n == len(buchst):
                            buchst2: list = [
                                a if a != "p" else "mulpri" for a in buchst
                            ]
                            textDazu += buchst2 + [str(s_[n:])]
                        if (
                            setTextLenIs1
                            and len(buchst) == 0
                            and promptMode2 != PromptModus.AusgabeSelektiv
                        ):
                            textDazu += [
                                "mulpri",
                                "a",
                                "t",
                                "w",
                                "keineEinZeichenZeilenPlusKeineAusgabeWelcherBefehlEsWar",
                            ]
                            if "/" in stext[0]:
                                textDazu += ["u"]
        else:
            textDazu += [s_]
        if len(textDazu) > 0:
            stext2 += textDazu
        else:
            stext2 += [str(s_)]
    stext = stext2
    return ifKurzKurz, stext


def verifyBruchNganzZahlCommaList(
    bruchAndGanzZahlEtwaKorrekterBereich,
    bruchBereichsAngabe,
    bruchBereichsAngaben,
    bruchRange,
    bruchRanges,
    commaListe,
    zahlenAngaben_,
):
    _bruchAndGanzZahlEtwaKorrekterBereich = []
    _bruchBereichsAngaben = []
    _bruchRanges = []
    _zahlenAngaben_ = []
    _etwaAllTrue = []

    for etwaBruch in commaListe.split(","):
        (
            bruchAndGanzZahlEtwaKorrekterBereich1,
            bruchBereichsAngaben1,
            bruchRanges1,
            zahlenAngaben_1,
            etwaAllTrue1,
        ) = verifyBruchNganzZahlBetweenCommas(
            bruchAndGanzZahlEtwaKorrekterBereich,
            bruchBereichsAngabe,
            bruchBereichsAngaben,
            bruchRange,
            bruchRanges,
            etwaBruch,
            zahlenAngaben_,
        )
        _bruchAndGanzZahlEtwaKorrekterBereich += [bruchAndGanzZahlEtwaKorrekterBereich1]
        _bruchBereichsAngaben += [bruchBereichsAngaben1]
        _bruchRanges += [bruchRanges1]
        _zahlenAngaben_ += [zahlenAngaben_1]
        _etwaAllTrue += [etwaAllTrue1]
    return (
        _bruchAndGanzZahlEtwaKorrekterBereich,
        _bruchBereichsAngaben,
        _bruchRanges,
        _zahlenAngaben_,
        all(_bruchAndGanzZahlEtwaKorrekterBereich),
    )


def verifyBruchNganzZahlBetweenCommas(
    bruchAndGanzZahlEtwaKorrekterBereich,
    bruchBereichsAngabe,
    bruchBereichsAngaben,
    bruchRange,
    bruchRanges,
    etwaBruch,
    zahlenAngaben_,
):

    # print("x {}".format(bruchBereichsAngabe))
    isBruch, isGanzZahl = isZeilenAngabe_betweenKommas(
        bruchBereichsAngabe
    ), isZeilenAngabe_betweenKommas(etwaBruch)
    # print("y {}".format(bruchBereichsAngabe))
    if isBruch != isGanzZahl:
        bruchAndGanzZahlEtwaKorrekterBereich += [True]
        if isBruch:
            bruchRanges += [bruchRange]
            bruchBereichsAngaben += [bruchBereichsAngabe]
        elif isGanzZahl:
            zahlenAngaben_ += [etwaBruch]
    else:
        bruchAndGanzZahlEtwaKorrekterBereich += [False]
    # if isZeilenAngabe_betweenKommas(etwaBruch):
    #    zahlenAngaben_ += [etwaBruch]
    # print("h {},{}".format(bruchBereichsAngaben, bruchAndGanzZahlEtwaKorrekterBereich))
    return (
        bruchAndGanzZahlEtwaKorrekterBereich,
        bruchBereichsAngaben,
        bruchRanges,
        zahlenAngaben_,
        all(bruchAndGanzZahlEtwaKorrekterBereich),
    )


# def getFromZahlenBereichBruchAndZahlenbereich(a, brueche, zahlenAngaben_):
#    ifAllTrue = []
#    first = True
#    for innerKomma in a.split(","):
#        bruch = [bruch for bruch in innerKomma.split("/")]
#        isBruch_ = [bruch1.isdecimal() for bruch1 in bruch] == [True, True]
#        if first:
#            isZahlenangabe_ = isZeilenAngabe(innerKomma)
#        else:
#            isZahlenangabe_ = isZeilenAngabe_betweenKommas(innerKomma)
#        if isBruch_ or isZahlenangabe_:
#            ifAllTrue += [True]
#            if isBruch_:
#                brueche += [bruch]
#            if isZahlenangabe_:
#                zahlenAngaben_ += [innerKomma]
#        else:
#            ifAllTrue += [True]
#        first = False
#    return brueche, zahlenAngaben_, all(ifAllTrue)
def verkuerze_dict(dictionary: dict) -> dict:
    dict2: dict = {}
    for key, value in dictionary.items():
        if value not in dict2.values():
            dict2[key] = value
    return dict2
