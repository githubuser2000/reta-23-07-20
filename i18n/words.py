import gettext
import os
import sys
# import sys
from collections import OrderedDict, defaultdict, namedtuple
# from dataclasses import dataclass
from typing import Any, NamedTuple, Optional, Tuple, Union

# from typing import Optional, Union

try:
    from orderedset import OrderedSet
except (ModuleNotFoundError, ImportError):
    OrderedSet = set


sprachen: defaultdict[str, str] = defaultdict(lambda: "de")
sprachen["english"] = "en"
sprachen["englisch"] = "en"
sprachen["deutsch"] = "de"
sprachen["german"] = "de"

sprachen2: defaultdict[str, str] = defaultdict(lambda: "messages")
sprachen2["english"] = "messages"
sprachen2["englisch"] = "messages"
sprachen2["deutsch"] = "messages"
sprachen2["german"] = "messages"


sprachenWahl = ""
sprachenParameterWort = "-language="

flagS = False
for arg in sys.argv:
    if arg[: len(sprachenParameterWort)] == sprachenParameterWort:
        sprachenWahl = arg[len(sprachenParameterWort) :]
        flagS = True
        break
if "-debug" in sys.argv:
    print("Sprachenwahl: {}".format(sprachenWahl))
if flagS and sprachenWahl not in sprachen.keys():
    print(
        "allowed are: {}\nwrong: {}".format(
            str(tuple(sprachen.keys()))[1:-1], sprachenWahl
        )
    )

if len({"deutsch", "german", ""} & {sprachenWahl}) == 0:
    subFolder = sprachen[sprachenWahl]
    sprachenFileName = sprachen2[sprachenWahl]
    i18nPath = os.path.join(os.path.dirname(__file__))
    t = gettext.translation(
        sprachenFileName, localedir=i18nPath, languages=[subFolder], fallback=False
    )
    t.install()
    _ = t.gettext
else:
    localedir = os.path.join(os.path.abspath(os.path.dirname(__file__)))
    translate = gettext.translation("messages", localedir, fallback=True)
    _ = translate.gettext

# sys.path.insert(1, "./..")
Multiplikationen = [(_("Multiplikationen"), "")]
"""
ES FEHLEN NOCH ALLE ''
fertig: in prepare ist nichts
fertig: concat fertig
fertig: center fertig
fertig: lib4tables fertig
fertig: reta.py fertig
nichts drin: enum
nichts drin: multis
nichts drin: grundstruk html
die aus den anderen dateien: nestedcompleter
LibRetaPrompt: größten Teil entnommen

ES FEHLEN NOCH ALLE ''
"""
Primzahlkreuz_pro_contra_strs: tuple[str, str] = (
    "Primzahlkreuz_pro_contra",
    "nachvollziehen_emotional_oder_geistig_durch_Primzahl-Kreuz-Algorithmus_(15)",
)

Primzahlkreuz_pro_contra_strs_Fkt: tuple[str, str] = (
    _("Primzahlkreuz_pro_contra"),
    _("nachvollziehen_emotional_oder_geistig_durch_Primzahl-Kreuz-Algorithmus_(15)"),
)
Primzahlkreuz_pro_contra_strs_Dict = {
    Primzahlkreuz_pro_contra_strs: Primzahlkreuz_pro_contra_strs_Fkt,
}
gebrochenSpaltenMaximumPlus1: int = 24  # Das ist nicht die Spaltenbreite, sondern wie weit gebrochene Zahlen gehen dürfen bei Zähler und Nenner

# DOPPELT
# spalten: dict = {}
# spalten |= {
#    "breite": _("breite"),
#    "breiten": _("breiten"),
#    "keinenummerierung": _("keinenummerierung"),
# }

ausgabeParas: dict = {
    "nocolor": _("nocolor"),
    "justtext": _("justtext"),
    "art": _("art"),
    "onetable": _("onetable"),
    "spaltenreihenfolgeundnurdiese": _("spaltenreihenfolgeundnurdiese"),
    "endlessscreen": _("endlessscreen"),
    "endless": _("endless"),
    "dontwrap": _("dontwrap"),
    "breite": _("breite"),
    "breiten": _("breiten"),
    "keineleereninhalte": _("keineleereninhalte"),
    "keinenummerierung": _("keinenummerierung"),
    "keineueberschriften": _("keineueberschriften"),
}
ausgabeParasEqSign: dict = {
    "nocolor": False,
    "justtext": False,
    "art": True,
    "onetable": False,
    "spaltenreihenfolgeundnurdiese": True,
    "endlessscreen": False,
    "endless": False,
    "dontwrap": False,
    "breite": True,
    "breiten": True,
    "keineleereninhalte": False,
    "keinenummerierung": False,
    "keineueberschriften": False,
}

ausgabeParasLen = {key: len(value) for (key, value) in ausgabeParas.items()}
kombiMainParas: dict = {
    "galaxie": _("galaxie"),
    "universum": _("universum"),
}
zeilenParas: dict = {
    "alles": _("alles"),
    "gestern": _("gestern"),
    "heute": _("heute"),
    "hoehemaximal": _("hoehemaximal"),
    "mond": _("mond"),
    "morgen": _("morgen"),
    "nachtraeglichneuabzaehlung": _("nachtraeglichneuabzaehlung"),
    "nachtraeglichneuabzaehlungvielfache": _("nachtraeglichneuabzaehlungvielfache"),
    "oberesmaximum": _("oberesmaximum"),
    "planet": _("planet"),
    "potenzenvonzahlen": _("potenzenvonzahlen"),
    "primzahlvielfache": _("primzahlvielfache"),
    "schwarzesonne": _("schwarzesonne"),
    "sonne": _("sonne"),
    "typ": _("typ"),
    "vielfachevonzahlen": _("vielfachevonzahlen"),
    "vorhervonausschnitt": _("vorhervonausschnitt"),
    "vorhervonausschnittteiler": _("vorhervonausschnittteiler"),
    "zaehlung": _("zaehlung"),
    "zeit": _("zeit"),
}

zeilenParasLen = {key: len(value) for (key, value) in zeilenParas.items()}
# zeilenParasLenPlus2 = {key: len(value) + 2 for (key, value) in zeilenParas.items()}
hauptForNeben: dict = {
    "zeilen": _("zeilen"),
    "spalten": _("spalten"),
    "kombination": _("kombination"),
    "ausgabe": _("ausgabe"),
    "h": _("h"),
    "help": _("help"),
    "debug": _("debug"),
}


ausgabeArt: dict = {
    "bbcode": _("bbcode"),
    "html": _("html"),
    "csv": _("csv"),
    "shell": _("shell"),
    "markdown": _("markdown"),
    "emacs": _("emacs"),
}


wahl15Words: dict = {
    "Strukturalien_bzw_Meta-Paradigmen_bzw_Transzendentalien_(15),Geist_(15),Model_of_Hierarchical_Complexity,"
    + Primzahlkreuz_pro_contra_strs[1]: ",".join(
        (
            _("Strukturalien_bzw_Meta-Paradigmen_bzw_Transzendentalien_(15)"),
            _("Geist_(15)"),
            _("Model_of_Hierarchical_Complexity),"),
            Primzahlkreuz_pro_contra_strs_Fkt[1],
        ),
    ),
    "Konkreta_und_Focus_(2)": _("Konkreta_und_Focus_(2)"),
    "Impulse_(5)": _("Impulse_(5)"),
    "Gefühle_(7)": _("Gefühle_(7)"),
    "Modus_und_Sein_(8)": _("Modus_und_Sein_(8)"),
    "Wirklichkeiten_Wahrheit_Wahrnehmung_(10)": _(
        "Wirklichkeiten_Wahrheit_Wahrnehmung_(10)"
    ),
    "Meta-Systeme_(12),Ordnung_und_Filterung_12_und_1pro12": ",".join(
        (("Meta-Systeme_(12)"), _("Ordnung_und_Filterung_12_und_1pro12"))
    ),
    "Paradigmen_sind_Absichten_(13)": _("Paradigmen_sind_Absichten_(13)"),
    "Gedanken_sind_Positionen_(17)": _("Gedanken_sind_Positionen_(17)"),
    "Verbundenheiten_(18)": _("Verbundenheiten_(18)"),
    "Triebe_und_Bedürfnisse_(6)": _("Triebe_und_Bedürfnisse_(6)"),
    "Lust_(9)": _("Lust_(9)"),
    "Reflexe_(3),Existenzialien_(3)": ",".join(
        (_("Reflexe_(3)"), _("Existenzialien_(3)"))
    ),
    "Absicht_6_ist_Vorteilsmaximierung": _("Absicht_6_ist_Vorteilsmaximierung"),
    "Absicht_7_ist_Selbstlosigkeit": _("Absicht_7_ist_Selbstlosigkeit"),
    "Absicht_10_ist_Wirklichkeit_erkennen": _("Absicht_10_ist_Wirklichkeit_erkennen"),
    "Absicht_17_ist_zu_meinen": _("Absicht_17_ist_zu_meinen"),
    "Zeit_(4)_als_Wirklichkeit": _("Zeit_(4)_als_Wirklichkeit"),
    "Funktionen_Vorstellungen_(16)": _("Funktionen_Vorstellungen_(16)"),
    "Achtung_(4)": _("Achtung_(4)"),
    "Absicht_1/8": _("Absicht_1/8"),
    "Absicht_1/6_ist_Reinigung_und_Klarheit": _(
        "Absicht_1/6_ist_Reinigung_und_Klarheit"
    ),
    "Reflektion_und_Kategorien_(1/15)": _("Reflektion_und_Kategorien_(1/15)"),
    "Regungen_(1)": _("Regungen_(1)"),
    "Energie_und_universelle_Eigenschaften_(30)": _(
        "Energie_und_universelle_Eigenschaften_(30)"
    ),
    "Stimmungen_Kombinationen_(14)": _("Stimmungen_Kombinationen_(14)"),
    "Klassen_(20)": _("Klassen_(20)"),
    "Empathie_(37)": _("Empathie_(37)"),
    "Garben_und_Verhalten_nachfühlen(31)": _("Garben_und_Verhalten_nachfühlen(31)"),
    "Verhalten_(11)": _("Verhalten_(11)"),
    "Bedeutung_(10)": _("Bedeutung_(10)"),
    "Themen_(6)": _("Themen_(6)"),
    "Optimierung_(10)": _("Optimierung_(10)"),
    "Attraktionen_(36)": _("Attraktionen_(36)"),
    "Absicht_16_ist_zu_genügen": _("Absicht_16_ist_zu_genügen"),
    "Liebe_(7)": _("Liebe_(7)"),
    "Koalitionen_(10)": _("Koalitionen_(10)"),
    "Ansichten_Standpunkte_(18_17)": _("Ansichten_Standpunkte_(18_17)"),
    "Prinzipien(1/8)": _("Prinzipien(1/8)"),
    "Bestrebungen(1/5)": _("Bestrebungen(1/5)"),
    "Bedingung_und_Auslöser_(1/3)": _("Bedingung_und_Auslöser_(1/3)"),
    "relativer_Zeit-Betrag_(15_10_4_18_6)": _("relativer_Zeit-Betrag_(15_10_4_18_6)"),
    "Zahlenvergleich_(15_18_6)": _("Zahlenvergleich_(15_18_6)"),
    "Leidenschaften_(21)": _("Leidenschaften_(21)"),
    "Erwartungshaltungen_(26)": _("Erwartungshaltungen_(26)"),
    "Extremalien_(19),Ziele_(19)": ",".join((_("Extremalien_(19)"), _("Ziele_(19)"))),
    "universeller_Komperativ_(18→15)": _("universeller_Komperativ_(18→15)"),
    "Relation_zueinander_reziprok_Universellen_(18→n_vs._1/n)": _(
        "Relation_zueinander_reziprok_Universellen_(18→n_vs._1/n)"
    ),
    "Sollen_Frage_Vorgehensweise_(1/13)": _("Sollen_Frage_Vorgehensweise_(1/13)"),
    "Fundament_(1/19)": _("Fundament_(1/19)"),
    "abhängige_Verbundenheit_(90)": _("abhängige_Verbundenheit_(90)"),
    "Absicht_13_ist_Helfen": _("Absicht_13_ist_Helfen"),
    "Karte_Filter_und_Unterscheidung_(1/12)": _(
        "Karte_Filter_und_Unterscheidung_(1/12)"
    ),
    "Maßnahmen_39": _("Maßnahmen_(39)"),
}

wahl15: dict = {
    #    "_": _("Strukturalien_bzw_Meta-Paradigmen_bzw_Transzendentalien_(15),Geist_(15)"),
    "_15": ",".join(
        (
            _("Strukturalien_bzw_Meta-Paradigmen_bzw_Transzendentalien_(15)"),
            _("Geist_(15)"),
            _("Model_of_Hierarchical_Complexity"),
            Primzahlkreuz_pro_contra_strs_Fkt[1],
        )
    ),
    "_2": _("Konkreta_und_Focus_(2)"),
    "_5": _("Impulse_(5)"),
    "_7": _("Gefühle_(7)"),
    "_8": _("Modus_und_Sein_(8)"),
    "_10": _("Wirklichkeiten_Wahrheit_Wahrnehmung_(10)"),
    "_12": ",".join((_("Meta-Systeme_(12)"), _("Ordnung_und_Filterung_12_und_1pro12"))),
    "_13": _("Paradigmen_sind_Absichten_(13)"),
    "_17": _("Gedanken_sind_Positionen_(17)"),
    "_18": _("Verbundenheiten_(18)"),
    "_6": _("Triebe_und_Bedürfnisse_(6)"),
    "_9": _("Lust_(9)"),
    "_3": _("Reflexe_(3),Existenzialien_(3)"),
    "_13_6": _("Absicht_6_ist_Vorteilsmaximierung"),
    "_13_7": _("Absicht_7_ist_Selbstlosigkeit"),
    "_13_10": _("Absicht_10_ist_Wirklichkeit_erkennen"),
    "_13_17": _("Absicht_17_ist_zu_meinen"),
    "_10_4": _("Zeit_(4)_als_Wirklichkeit"),
    "_16": _("Funktionen_Vorstellungen_(16)"),
    "_4": _("Achtung_(4)"),
    "_13_1pro8": _("Absicht_1/8"),
    "_13_1pro6": _("Absicht_1/6_ist_Reinigung_und_Klarheit"),
    "_1pro15": _("Reflektion_und_Kategorien_(1/15)"),
    "_1": _("Regungen_(1)"),
    "_30": _("Energie_und_universelle_Eigenschaften_(30)"),
    "_14": _("Stimmungen_Kombinationen_(14)"),
    "_20": _("Klassen_(20)"),
    "_37": _("Empathie_(37)"),
    "_31": _("Garben_und_Verhalten_nachfühlen(31)"),
    "_11": _("Verhalten_(11)"),
    "_5_10": _("Bedeutung_(10)"),
    "_17_6": _("Themen_(6)"),
    "_17_6_10mit4": _("Optimierung_(10)"),
    "_36": _("Attraktionen_(36)"),
    "_13_16": _("Absicht_16_ist_zu_genügen"),
    "_18_7": _("Liebe_(7)"),
    "_18_10": _("Koalitionen_(10)"),
    "_18_17": _("Ansichten_Standpunkte_(18_17)"),
    "_1pro8": _("Prinzipien(1/8)"),
    "_1pro5": _("Bestrebungen(1/5)"),
    "_1pro3": _("Bedingung_und_Auslöser_(1/3)"),
    "_10_4_18_6": _("relativer_Zeit-Betrag_(15_10_4_18_6)"),
    "_18_6": _("Zahlenvergleich_(15_18_6)"),
    "_21": _("Leidenschaften_(21)"),
    "_26": _("Erwartungshaltungen_(26)"),
    "_19": _("Extremalien_(19),Ziele_(19)"),
    "_18_15": _("universeller_Komperativ_(18→15)"),
    "_18_15_n-vs-1pron": _("Relation_zueinander_reziprok_Universellen_(18→n_vs._1/n)"),
    "_1pro13": _("Sollen_Frage_Vorgehensweise_(1/13)"),
    "_1pro19": _("Fundament_(1/19)"),
    "_90": _("abhängige_Verbundenheit_(90)"),
    "_13_13": _("Absicht_13_ist_Helfen"),
    "_1pro12": _("Karte_Filter_und_Unterscheidung_(1/12)"),
    "_39": _("Maßnahmen_(39)"),
}

# WICHTIG WICHTIG: die Befehle mit nur einem zeichen dürfen  nur ein Zeichen haben !!!!!!!
befehle2: dict = {"15" + a: "15" + a for a in wahl15.keys()} | {
    "mond": _("mond"),
    "reta": _("reta"),
    "absicht": _("absicht"),
    "motiv": _("motiv"),
    "thomas": _("thomas"),
    "universum": _("universum"),
    "motive": _("motive"),
    "absichten": _("absichten"),
    "vielfache": _("vielfache"),
    "einzeln": _("einzeln"),
    "multis": _("multis"),
    "modulo": _("modulo"),
    "prim": _("prim"),
    "primfaktorzerlegung": _("primfaktorzerlegung"),
    "prim24": _("prim24"),
    "primfaktorzerlegungModulo24": _("primfaktorzerlegungModulo24"),
    "help": _("help"),
    "hilfe": _("hilfe"),
    "abc": _("abc"),
    "abcd": _("abcd"),
    "alles": _("alles"),
    "a": _("a"),
    "u": _("u"),
    "befehle": _("befehle"),
    "t": _("t"),
    "richtung": _("richtung"),
    "r": _("r"),
    "v": _("v"),
    "h": _("h"),
    "p": _("p"),
    "mo": _("mo"),
    "mu": _("mu"),
    "primzahlkreuz": _("primzahlkreuz"),
    "ende": _("ende"),
    "exit": _("exit"),
    "quit": _("quit"),
    "q": _("q"),
    ":q": _(":q"),
    "shell": _("shell"),
    "s": _("s"),
    "math": _("math"),
    "loggen": _("loggen"),
    "nichtloggen": _("nichtloggen"),
    "mulpri": _("mulpri"),
    "python": _("python"),
    "w": _("w"),
    "teiler": _("teiler"),
    "BefehlSpeichernDanach": _("BefehlSpeichernDanach"),
    "S": _("S"),
    "BefehlSpeicherungLöschen": _("BefehlSpeicherungLöschen"),
    "l": _("l"),
    "BefehlSpeicherungAusgeben": _("BefehlSpeicherungAusgeben"),
    "o": _("o"),
    "e": _("e"),
    # "BefehlsSpeicherungsModusAus": _("BefehlsSpeicherungsModusAus"),
    # "x": _("x"),
    "BefehlSpeichernDavor": _("BefehlSpeichernDavor"),
    "keineEinZeichenZeilenPlusKeineAusgabeWelcherBefehlEsWar": _(
        "keineEinZeichenZeilenPlusKeineAusgabeWelcherBefehlEsWar"
    ),
    "abstand": _("abstand"),
}

# KurzLangBefehle sind die Befehle, die mehr als ein Zeichen groß sind und für reta dennoch Abkürzungen sind.

# KurzKurzBefehle müssen auch in Fremdsprachen ein Zeichen groß bleiben!
assert all(
    [len(value) == 1 if len(key) == 1 else True for (key, value) in befehle2.items()]
)

# WICHTIG WICHTIG: die Befehle mit nur einem zeichen dürfen  nur ein Zeichen haben !!!!!!!
befehle: list = list(befehle2.values())
# ["15" + a for a in wahl15.keys()] + [
#    _("mond"),
#    _("reta"),
#    _("absicht"),
#    _("motiv"),
#    _("thomas"),
#    _("universum"),
#    _("motive"),
#    _("absichten"),
#    _("vielfache"),
#    _("einzeln"),
#    _("multis"),
#    _("modulo"),
#    _("prim"),
#    _("primfaktorzerlegung"),
#    _("prim24"),
#    _("primfaktorzerlegungModulo24"),
#    _("help"),
#    _("hilfe"),
#    _("abc"),
#    _("abcd"),
#    _("alles"),
#    _("a"),
#    _("u"),
#    _("befehle"),
#    _("t"),
#    _("richtung"),
#    _("r"),
#    _("v"),
#    _("h"),
#    _("p"),
#    _("mo"),
#    _("mu"),
#    _("primzahlkreuz"),
#    _("ende"),
#    _("exit"),
#    _("quit"),
#    _("q"),
#    ":q",
#    _("shell"),
#    _("s"),
#    _("math"),
#    _("loggen"),
#    _("nichtloggen"),
#    _("mulpri"),
#    _("python"),
#    _("w"),
#    _("teiler"),
#    _("BefehlSpeichernDanach"),
#    _("S"),
#    _("BefehlSpeicherungLöschen"),
#    _("l"),
#    _("BefehlSpeicherungAusgeben"),
#    _("o"),
#    _("e"),
#    # _("BefehlsSpeicherungsModusAus"),
#    # _("x"),
#    _("BefehlSpeichernDavor"),
#    _("keineEinZeichenZeilenPlusKeineAusgabeWelcherBefehlEsWar"),
#    _("abstand"),
# ]

ParametersMain: NamedTuple = namedtuple(
    "ParametersMain",
    "wichtigste wichtigste2 religionen galaxie strukturgroesse universum wirtschaft menschliches procontra licht bedeutung symbole Multiplikationen konzept konzept2 inkrementieren operationen universummetakonkret primzahlwirkung gebrochenuniversum gebrochengalaxie primvielfache planet strukturenkleinere grundstrukturen alles",
)
konzeptE = {"konzept": _("konzept"), "konzept2": _("konzept2")}
gebrochenUniGal = {
    "gebrochenuniversum": _("gebrochen-rational_Universum_n/m"),
    "gebrochengalaxie": _("gebrochen-rational_Galaxie n/m"),
}
ParametersMain: NamedTuple = ParametersMain(
    (
        _("Wichtigstes_zum_verstehen"),
        _("wichtigsteverstehen"),
    ),
    (
        _("Wichtigstes_zum_gedanklich_einordnen"),
        _("wichtigsteeinordnen"),
    ),
    (
        _("Religionen"),
        _("religionen"),
        _("religion"),
    ),
    (
        _("Galaxie"),
        _("galaxie"),
        _("alteschriften"),
        _("kreis"),
        _("galaxien"),
        _("kreise"),
    ),
    (
        _("Größenordnung"),
        _("groessenordnung"),
        _("strukturgroesse"),
        _("strukturgroeße"),
        _("strukturgrösse"),
        _("strukturgröße"),
        _("groesse"),
        _("stufe"),
        _("organisationen"),
    ),
    (
        _("Universum"),
        _("universum"),
        _("transzendentalien"),
        _("strukturalien"),
        _("kugel"),
        _("kugeln"),
        _("ball"),
        _("baelle"),
        _("bälle"),
    ),
    (_("Wirtschaft"), _("wirtschaft")),
    (
        _("Menschliches"),
        _("menschliches"),
    ),
    (
        _("Pro_Contra"),
        _("procontra"),
        _("dagegendafuer"),
    ),
    (
        _("Licht"),
        _("licht"),
    ),
    (
        _("Bedeutung"),
        _("bedeutung"),
    ),
    (
        _("Symbole"),
        _("symbole"),
    ),
    [a[0] for a in Multiplikationen],
    (
        _("Eigenschaften_n"),
        _("eigenschaften"),
        _("eigenschaft"),
        konzeptE["konzept"],
        _("konzepte"),
    ),
    (
        _("Eigenschaften_1/n"),
        konzeptE["konzept2"],
        _("konzepte2"),
    ),
    (
        _("Inkrementieren"),
        _("inkrementieren"),
    ),
    (
        _("Operationen"),
        _("operationen"),
    ),
    (
        _("Meta_vs_Konkret_(Universum)"),
        _("universummetakonkret"),
    ),
    (
        _("Primzahlwirkung"),
        _("primzahlwirkung"),
    ),
    (gebrochenUniGal["gebrochenuniversum"],),
    (gebrochenUniGal["gebrochengalaxie"],),
    (
        _("Multiplikationen"),
        _("multiplikationen"),
    ),
    (_("Planet_(10_und_oder_12)"), _("planet")),
    (
        _("Strukturen_1_bis_9"),
        _("strukturkleinerzehn"),
    ),
    (_("Grundstrukturen"), _("grundstrukturen")),
    (_("alles"),),
)

thomasWort = _("thomas")
motivationWort = _("motivation")
transzendentalienWort = _("transzendentalien")
transzendentaliereziprokeWort = _("transzendentaliereziproke")
verhaeltnisgleicherzahlWort = _("verhaeltnisgleicherzahl")
gestirnWort = _("gestirn")
primzahlkreuzWort = _("primzahlkreuz")
GalaxieabsichtWort = _("Galaxieabsicht")
paraNdataMatrix: list = [
    (
        ParametersMain.wichtigste,
        (
            _("Wichtigste"),
            _("wichtigste"),
        ),
        {10, 5, 4, 8},
    ),
    (
        ParametersMain.menschliches,
        (
            _("Mensch-zu-Tier"),
            _("menschtier"),
            _("tiermensch"),
        ),
        {314},
    ),
    (
        ParametersMain.menschliches,
        (
            _("Ansichten_Standpunkte_(18_17)"),
            _("ansichten"),
        ),
        {240, 346},
    ),
    (
        ParametersMain.menschliches,
        (
            _("(politische)_Richtungen_(7)"),
            _("richtungen"),
            _("politische"),
        ),
        {235},
    ),
    (
        ParametersMain.planet,
        (
            _("Wirklichkeiten_(10)"),
            _("wirklichkeit"),
            _("wirklichkeiten"),
        ),
        {233, 265, 268, 322},
    ),
    (
        ParametersMain.planet,
        (
            _("Meta-Systeme_(12)"),
            _("metasysteme"),
            _("metasystem"),
            _("meta-systeme"),
            _("meta-system"),
        ),
        {232, 288, 334},
    ),
    (
        ParametersMain.planet,
        (_("Intelligenz"), _("intelligenz")),
        {214},
    ),
    (
        ParametersMain.planet,
        (
            _("Gleichheit_Freiheit_Ordnung"),
            _("gleichheit"),
            _("freiheit"),
            _("ordnung"),
        ),
        {132, 324, 328, 79, 80, 331, 335},
    ),
    (
        ParametersMain.planet,
        (
            _("Komplexität"),
            _("komplexität"),
            _("komplexitaet"),
        ),
        {213},
    ),
    (
        ParametersMain.planet,
        (
            _("Mechanismen"),
            _("mechanismen"),
            _("mechanismus"),
        ),
        {107},
    ),
    (
        ParametersMain.wichtigste,
        (
            _("Zweitwichtigste"),
            _("zweitwichtigste"),
        ),
        {19, 65, 183},
        set(),
        set(),
        set(),
        {(10,)},
    ),
    (
        ParametersMain.wichtigste,
        (
            _("Drittwichtigste"),
            _("drittwichtigste"),
        ),
        {64},
    ),
    (
        ParametersMain.wichtigste,
        (
            _("Motive_Sternpolygone"),
            _("viertwichtigste"),
        ),
        set(),
        set(),
        set(),
        set(),
        set(),
        set(),
        set(),
        {"primMotivStern"},
    ),
    (
        ParametersMain.wichtigste2,
        (_("Wichtigste"), _("wichtigstes")),
        {0, 1, 2, 36, 37, 207},
    ),
    (
        ParametersMain.wichtigste2,
        (
            _("Zweitwichtigste"),
            _("zweitwichtigste"),
        ),
        {30},
    ),
    (
        ParametersMain.operationen,
        (
            _("Halbierung"),
            _("halbierung"),
            _("halbierungen"),
        ),
        {86},
    ),
    (
        ParametersMain.religionen,
        (
            _("Religions-Gründer-Typ"),
            _("religionsgründertyp"),
            _("prophet"),
            _("archon"),
            _("religionsgruendertyp"),
        ),
        {72},
    ),
    (
        ParametersMain.religionen,
        (_("Hinduismus"), _("hinduismus")),
        {217},
    ),
    (
        ParametersMain.religionen,
        (_("Sternpolygon"), _("sternpolygon")),
        {0, 6, 36},
    ),
    (
        ParametersMain.religionen,
        (
            _("der_Tierkreiszeichen"),
            _("dertierkreiszeichen"),
            _("babylon"),
        ),
        {0, 36, 207},
    ),
    (
        ParametersMain.religionen,
        (
            _("Sternpolygon_vs_gleichförmiges"),
            _("vergleich"),
            _("sternpolygonvsgleichfoermiges"),
            _("vergleichnvs1divn"),
        ),
        {87},
    ),
    (
        ParametersMain.religionen,
        (
            _("Messias"),
            _("messias"),
            _("heptagramm"),
            _("hund"),
            _("messiase"),
            _("messiasse"),
        ),
        {7},
    ),
    (
        ParametersMain.religionen,
        (
            _("gleichförmiges_Polygon"),
            _("gleichförmigespolygon"),
            _("gleichfoermigespolygon"),
            _("nichtsternpolygon"),
            _("polygon"),
        ),
        {16, 37},
    ),
    (
        ParametersMain.religionen,
        (
            _("Vertreter_höherer_Konzepte"),
            _("vertreterhoehererkonzepte"),
            _("galaxien"),
            _("galaxie"),
            _("schwarzesonne"),
            _("schwarzesonnen"),
            _("universum"),
            _("universen"),
            _("kreis"),
            _("kreise"),
            _("kugel"),
            _("kugeln"),
        ),
        {23},
    ),
    (
        ParametersMain.galaxie,
        (
            _("Offenbarung_des_Johannes"),
            _("offenbarung"),
            _("offenbarungdesjohannes"),
            _("johannes"),
            _("bibel"),
            _("offenbarungjohannes"),
        ),
        {90},
    ),
    (
        ParametersMain.inkrementieren,
        (
            _("Teilchen-Meta-Physik"),
            _("addition"),
            _("identitaet"),
            _("Identität"),
        ),
        {219, 223, 307, 308, 333},
    ),
    (
        ParametersMain.galaxie,
        (
            _("Hochzüchten"),
            _("hochzüchten"),
            _("hochzuechten"),
        ),
        {318, 319},
    ),
    (
        ParametersMain.universum,
        (_("Universelles_Verhältnis_gleicher_Zahlen"), verhaeltnisgleicherzahlWort),
        {383},
    ),
    (
        ParametersMain.universum,
        (
            _("universelles_Recht"),
            _("recht"),
            _("jura"),
        ),
        {382, 34, 65},
    ),
    (
        ParametersMain.universum,
        (
            _("sowas_wie_Kombinieren_Verknüpfen"),
            _("kombinierenetc"),
        ),
        {320},
    ),
    (
        ParametersMain.universum,
        (
            _("Hochzüchten"),
            _("hochzüchten"),
            _("hochzuechten"),
        ),
        {318, 319},
    ),
    (
        ParametersMain.universum,
        (
            _("Teilchen-Meta-Physik"),
            _("addition"),
            _("identitaet"),
            _("Identität"),
        ),
        {219, 223, 307, 308, 333},
    ),
    (
        ParametersMain.universum,
        (
            _("keine_Nur-Paradigma-Religionen"),
            _("metaparadigmareligion"),
        ),
        {190, 191, 196},
    ),
    (
        ParametersMain.universum,
        (
            _("Kugeln_Kreise"),
            _("kugelnkreise"),
            _("kugeln"),
            _("kreise"),
        ),
        {77, 145},
    ),
    (
        ParametersMain.galaxie,
        (
            _("Kugeln_Kreise"),
            _("kugelnkreise"),
            _("kugeln"),
            _("kreise"),
        ),
        {77, 145},
    ),
    (
        ParametersMain.galaxie,
        (
            _("chinesisches_Horoskop"),
            _("chinesischeshoroskop"),
            _("china"),
        ),
        {91},
    ),
    (
        ParametersMain.galaxie,
        (
            _("babylonische_Tierkreiszeichen"),
            _("tierkreiszeichen"),
            _("babylon"),
        ),
        {1, 2},
    ),
    (
        ParametersMain.galaxie,
        (_("Thomasevangelium"), _("thomasevangelium"), thomasWort),
        {0, 3, 303},
    ),
    (
        ParametersMain.galaxie,
        (
            _("analytische_Ontologie"),
            _("analytischeontologie"),
            _("ontologie"),
        ),
        {84},
    ),
    (
        ParametersMain.galaxie,
        (
            _("Transzendentalien_innen_außen"),
            _("innenaussenstrukur"),
            _("strukturalieninnenaußen"),
            _("strukturalieninnenaussen"),
            _("innenaußenstrukur"),
            _("transzendentalieninnenaußen"),
            _("transzendentalieninnenaussen"),
        ),
        {149},
    ),
    (
        ParametersMain.galaxie,
        (
            _("Modallogik"),
            _("modallogik"),
        ),
        {148},
    ),
    (
        ParametersMain.operationen,
        (
            _("5"),
            _("fünf"),
            _("fünfer"),
            _("fünferstruktur"),
            _("fuenf"),
            _("fuenfer"),
            _("fuenferstruktur"),
        ),
        {96},
    ),
    (
        ParametersMain.operationen,
        (
            _("9"),
            _("neun"),
            _("neuner"),
            _("neunerstruktur"),
        ),
        {94},
    ),
    (
        ParametersMain.operationen,
        (
            _("3"),
            _("drei"),
            _("dreier"),
            _("dreierstruktur"),
        ),
        {92, 93, 315, 316},
    ),
    (
        ParametersMain.strukturgroesse,
        (
            _("Licht"),
            _("licht"),
        ),
        {20, 27, 313},
    ),
    (
        ParametersMain.strukturgroesse,
        (
            _("Strukturgrösse"),
            _("größe"),
            _("groesse"),
            _("gross"),
            _("strukturgroesse"),
            _("strukturgroeße"),
            _("strukturgrösse"),
            _("strukturgröße"),
        ),
        {4, 21, 54, 197},
    ),
    (
        ParametersMain.strukturgroesse,
        (
            _("Organisationen"),
            _("organisationen"),
            _("organisation"),
        ),
        {30, 82},
    ),
    (
        ParametersMain.strukturgroesse,
        (
            _("politische_Systeme"),
            _("politischesysteme"),
            _("politik"),
        ),
        {83},
    ),
    (
        ParametersMain.universummetakonkret,
        (_("meta"),),
        set(),
        set(),
        set(),
        set(),
        (
            (
                2,
                0,
            ),
        ),
    ),
    (
        ParametersMain.universummetakonkret,
        (_("konkret"),),
        set(),
        set(),
        set(),
        set(),
        (
            (
                2,
                1,
            ),
        ),
    ),
    (
        ParametersMain.universummetakonkret,
        (_("Theorie"), _("theorie")),
        set(),
        set(),
        set(),
        set(),
        (
            (
                3,
                0,
            ),
        ),
    ),
    (
        ParametersMain.universummetakonkret,
        (_("Praxis"), _("praxis")),
        set(),
        set(),
        set(),
        set(),
        (
            (
                3,
                1,
            ),
        ),
    ),
    (
        ParametersMain.universummetakonkret,
        (
            _("Management"),
            _("management"),
            _("stau"),
        ),
        set(),
        set(),
        set(),
        set(),
        (
            (
                4,
                0,
            ),
        ),
    ),
    (
        ParametersMain.universummetakonkret,
        (
            _("verändernd"),
            _("veraendernd"),
            _("fluss"),
        ),
        set(),
        set(),
        set(),
        set(),
        (
            (
                4,
                1,
            ),
        ),
    ),
    (
        ParametersMain.universummetakonkret,
        (
            _("ganzheitlich"),
            _("mathematisch_diskret"),
            _("diskret"),
        ),
        set(),
        set(),
        set(),
        set(),
        (
            (
                5,
                0,
            ),
        ),
    ),
    (
        ParametersMain.universummetakonkret,
        (
            _("darüber_hinausgehend"),
            _("hinausgehend"),
            _("kontinuierlich"),
        ),
        set(),
        set(),
        set(),
        set(),
        (
            (
                5,
                1,
            ),
        ),
    ),
    (
        ParametersMain.primzahlwirkung,
        (
            _("Universum_Strukturalien_Transzendentalien"),
            _("universum"),
            _("strukturalie"),
            _("strukturalien"),
            transzendentalienWort,
            _("transzendentalie"),
        ),
        set(),
        set(),
        set(),
        set(),
        {(5,)},
    ),
    (
        ParametersMain.primzahlwirkung,
        (
            _("Richtung_als_Richtung"),
            _("richtungrichtung"),
        ),
        set(),
        set(),
        set(),
        set(),
        {(None,)},
    ),
    (
        ParametersMain.primzahlwirkung,
        (
            GalaxieabsichtWort,
            _("absichtgalaxie"),
            _("absicht"),
            _("motive"),
            _("motiv"),
            _("absichten"),
            _("galaxie"),
        ),
        set(),
        set(),
        set(),
        set(),
        {(10,)},
    ),
    (
        ParametersMain.primzahlwirkung,
        (
            _("Absicht_Reziproke_Galaxie"),
            _("absichtgalaxiereziproke"),
            _("absichtreziproke"),
            _("motivereziproke"),
            _("motivreziproke"),
            _("absichtenreziproke"),
            _("galaxiereziproke"),
        ),
        set(),
        set(),
        set(),
        set(),
        {(42,)},
    ),
    (
        ParametersMain.primzahlwirkung,
        (
            _("Universum_Reziproke"),
            _("universumreziproke"),
            _("strukturaliereziproke"),
            _("strukturalienreziproke"),
            _("transzendentalienreziproke"),
            transzendentaliereziprokeWort,
        ),
        set(),
        set(),
        set(),
        set(),
        {(131,)},
    ),
    (
        ParametersMain.primzahlwirkung,
        (
            _("Dagegen-Gegentranszendentalie"),
            _("dagegengegentranszendentalie"),
            _("dagegengegentranszendentalien"),
            _("dagegengegenstrukturalien"),
            _("dagegengegenstrukturalie"),
        ),
        set(),
        set(),
        set(),
        set(),
        {(138,)},
    ),
    (
        ParametersMain.primzahlwirkung,
        (
            _("neutrale_Gegentranszendentalie"),
            _("neutralegegentranszendentalie"),
            _("neutralegegentranszendentalien"),
            _("neutralegegenstrukturalien"),
            _("neutralegegenstrukturalie"),
        ),
        set(),
        set(),
        set(),
        set(),
        {(202,)},
    ),
    (
        ParametersMain.universummetakonkret,
        (
            _("Unternehmung_Geschäft"),
            _("unternehmen"),
            _("unternehmung"),
            _("geschaeft"),
            _("geschäft"),
        ),
        set(),
        set(),
        set(),
        set(),
        (
            (
                6,
                0,
            ),
        ),
    ),
    (
        ParametersMain.universummetakonkret,
        (_("wertvoll"), _("wert")),
        set(),
        set(),
        set(),
        set(),
        (
            (
                6,
                1,
            ),
        ),
    ),
    (
        ParametersMain.universummetakonkret,
        (
            _("Beherrschen"),
            _("regieren"),
            _("beherrschen"),
        ),
        set(),
        set(),
        set(),
        set(),
        (
            (
                7,
                0,
            ),
        ),
    ),
    (
        ParametersMain.universummetakonkret,
        (
            _("Richtung"),
            _("richtung"),
            _("gut"),
        ),
        set(),
        set(),
        set(),
        set(),
        (
            (
                7,
                1,
            ),
        ),
    ),
    (
        ParametersMain.universum,
        (
            _("analytische_Ontologie"),
            _("analytischeontologie"),
            _("ontologie"),
        ),
        {84},
    ),
    (
        ParametersMain.universum,
        (
            _("Gegentranszendentalien"),
            _("gegentranszendentalien"),
            _("gegentranszendentalie"),
            _("gegenstrukturalien"),
            _("gegenalien"),
            _("gegenuniversalien"),
        ),
        {138, 202},
    ),
    (
        ParametersMain.universum,
        (_("Systemsachen"), _("systemsachen")),
        (150,),
    ),
    (
        ParametersMain.universum,
        (
            _("Transzendentalien"),
            _("transzendentalien"),
            _("transzendentalie"),
            _("strukturalien"),
            _("alien"),
            _("universalien"),
        ),
        {5, 54, 55, 198},
    ),
    (
        ParametersMain.universum,
        (
            _("Reziproke_von_Transzendentalien"),
            _("transzendentalienreziproke"),
            _("transzendentaliereziproke"),
            _("strukturalienreziproke"),
            _("alienreziproke"),
            _("universalienreziproke"),
        ),
        {131, 201},
    ),
    (
        ParametersMain.universum,
        (_("Netzwerk"), _("netzwerk")),
        {25},
    ),
    (
        ParametersMain.universum,
        (
            _("warum_Transzendentalie_=_Strukturgroesse_=_Charakter"),
            _("warumtranszendentaliezustrukturgroesseundcharakter"),
        ),
        {4, 54, 5, 165},
    ),
    (
        ParametersMain.universum,
        (_("Kategorie"), _("kategorie")),
        {204, 205, 281},
    ),
    (
        ParametersMain.universum,
        (_("Raum-Missionen"), _("weltall")),
        {218},
    ),
    (
        ParametersMain.universum,
        (
            _("Programmier-Paradigmen"),
            _("programmierparadigmen"),
        ),
        {351},
    ),
    (
        ParametersMain.galaxie,
        (_("Raum-Missionen"), _("weltall")),
        {218},
    ),
    (
        ParametersMain.universum,
        (_("Geist__(15)"), _("geist")),
        {242},
    ),
    (
        ParametersMain.universum,
        (
            _("warum_Transzendentalie_=_Komplexität_von_Michael_Commons"),
            _("warumtranszendentaliegleichkomplexitaet"),
        ),
        {65, 5, 166},
    ),
    (
        ParametersMain.grundstrukturen,
        (
            _("Model_of_Hierarchical_Complexity"),
            _("modelofhierarchicalcomplexity"),
            _("komplex"),
            _("komplexität"),
            _("komplexitaet"),
            _("complexity"),
            _("model"),
            _("abstraktion"),
        ),
        {65, 75, 203},
    ),
    (
        ParametersMain.universum,
        (
            _("Model_of_Hierarchical_Complexity"),
            _("modelofhierarchicalcomplexity"),
            _("komplex"),
            _("komplexität"),
            _("komplexitaet"),
            _("complexity"),
            _("model"),
            _("abstraktion"),
        ),
        {65, 75, 203},
    ),
    (
        ParametersMain.operationen,
        (
            _("2"),
            _("zwei"),
            _("gerade"),
            _("ungerade"),
            _("alternierung"),
            _("alternierend"),
            _("zweierstruktur"),
        ),
        {78, 79, 80, 331},
    ),
    (
        ParametersMain.operationen,
        (
            _("Multiplikation"),
            _("multiplikation"),
        ),
        {158},
    ),
    (
        ParametersMain.operationen,
        (
            _("4"),
            _("vier"),
            _("viererstruktur"),
            _("viererabfolgen"),
        ),
        {76, 77, 81, 104, 145},
    ),
    (
        ParametersMain.menschliches,
        (
            _("Gesellschaftsschicht"),
            _("klasse"),
            _("klassen"),
        ),
        {241},
    ),
    (
        ParametersMain.menschliches,
        (_("Moral"), _("moral"), _("warummoral")),
        {215, 216},
        {(216, 221)},
    ),
    (
        ParametersMain.menschliches,
        (
            _("Fachgebiete"),
            _("fachgebiete"),
            _("fachbereiche"),
            _("themen"),
        ),
        {183},
    ),
    (
        ParametersMain.wirtschaft,
        (
            _("Fachgebiete"),
            _("fachgebiete"),
            _("fachbereiche"),
            _("themen"),
        ),
        {183},
    ),
    (
        ParametersMain.wirtschaft,
        (
            _("Pflanzen"),
            _("pflanzen"),
        ),
        {113},
    ),
    (
        ParametersMain.wirtschaft,
        (
            _("Maschinen"),
            _("maschinen"),
            _("maschine"),
            _("gerät"),
            _("geräte"),
            _("geraete"),
            _("geraet"),
        ),
        {89},
    ),
    (
        ParametersMain.wirtschaft,
        (
            _("Organisationsform"),
            _("organisationsform"),
            _("organisationsart"),
            _("firma"),
            _("verein"),
        ),
        {99},
    ),
    (
        ParametersMain.wirtschaft,
        (
            _("System"),
            _("system"),
        ),
        (69,),
    ),
    (
        ParametersMain.wirtschaft,
        (
            _("realistisch"),
            _("funktioniert"),
        ),
        {70},
    ),
    (
        ParametersMain.wirtschaft,
        (
            _("Erklärung"),
            _("erklärung"),
            _("erklaerung"),
        ),
        {71},
    ),
    (
        ParametersMain.wirtschaft,
        (
            _("BWL"),
            _("bwl"),
        ),
        {109},
    ),
    (
        ParametersMain.menschliches,
        (
            _("Sinn_des_Lebens"),
            _("sinndeslebens"),
            _("lebenssinn"),
            _("sinn"),
            _("sinnsuche"),
        ),
        {88, 189},
        {(181, 182)},
    ),
    (
        ParametersMain.menschliches,
        (
            _("Intelligenzprobleme"),
            _("intelligenzprobleme"),
            _("intelligenzmaengel"),
            _("intelligenzmängel"),
        ),
        {147},
    ),
    (
        ParametersMain.menschliches,
        (
            _("Denkweise_von_Lebewesen"),
            _("lebewesendenkweise"),
            _("denkweise"),
        ),
        {146},
    ),
    (
        ParametersMain.menschliches,
        (
            _("Gegentranszendentalien"),
            _("gegentranszendentalien"),
            _("gegenstrukturalien"),
        ),
        {138, 139, 202},
    ),
    (
        ParametersMain.menschliches,
        (
            _("Gleichheit_Freiheit"),
            _("gleichheitfreiheit"),
            _("ungleichheit"),
            _("dominieren"),
            _("gleichheit"),
            _("freiheit"),
        ),
        {132, 328, 331, 335},
    ),
    (
        ParametersMain.menschliches,
        (
            _("Gefühle"),
            _("emotionen"),
            _("gefuehle"),
            _("emotion"),
            _("gefühl"),
            _("gefuehl"),
        ),
        {105, 230, 243, 283, 284, 285, 286, 305},
    ),
    (
        ParametersMain.menschliches,
        (
            _("Egoismus"),
            _("egoismus"),
            _("altruismus"),
            _("selbstlosigkeit"),
        ),
        {136},
        {(66, 67)},
    ),
    (
        ParametersMain.menschliches,
        (
            _("Wirkung"),
            _("wirkung"),
        ),
        {135},
    ),
    (
        ParametersMain.menschliches,
        (
            _("INCELs"),
            _("incel"),
            _("incels"),
        ),
        {68},
    ),
    (
        ParametersMain.menschliches,
        (
            _("irrationale_Zahlen_durch_Wurzelbildung"),
            _("irrationalezahlendurchwurzelbildung"),
            _("ausgangslage"),
        ),
        {73},
    ),
    (
        ParametersMain.menschliches,
        (
            _("dominierendes_Geschlecht"),
            _("dominierendesgeschlecht"),
            _("maennlich"),
            _("männlich"),
            _("weiblich"),
        ),
        {51},
    ),
    (
        ParametersMain.menschliches,
        (
            _("Liebe"),
            _("liebe"),
            _("ethik"),
        ),
        {8, 9, 28, 208, 330},
        {(121, 122)},
    ),
    (
        ParametersMain.menschliches,
        (
            _("Glaube_Erkenntnis"),
            _("glauben"),
            _("erkenntnis"),
            _("glaube"),
        ),
        {59},
    ),
    (
        ParametersMain.menschliches,
        (
            _("Angreifbarkeit"),
            _("angreifbarkeit"),
            _("angreifbar"),
        ),
        {58, 57},
    ),
    (
        ParametersMain.grundstrukturen,
        (
            _("Strukturalien_bzw_Meta-Paradigmen_bzw_Transzendentalien_(15)"),
            _("Transzendentalien"),
            _("transzendentalien"),
            _("transzendentalie"),
            _("strukturalien"),
            _("alien"),
            _("universalien"),
            _("meta-paradigmen"),
        ),
        {5, 229, 131},
    ),
    (
        ParametersMain.grundstrukturen,
        (
            _("Bedingung_und_Auslöser_(1/3)"),
            _("bedingung"),
            _("bedingungen"),
            _("auslöser"),
            _("ausloeser"),
        ),
        {338},
    ),
    (
        ParametersMain.grundstrukturen,
        (
            _("Maßnahmen_(39)"),
            _("massnahmen"),
        ),
        {384},
    ),
    (
        ParametersMain.grundstrukturen,
        (
            _("Relation_zueinander_reziprok_Universellen_(18→n_vs._1/n)"),
            _("relativreziprokuniversell"),
        ),
        {350},
    ),
    (
        ParametersMain.grundstrukturen,
        (
            _("universeller_Komperativ_(18→15)"),
            _("universellerkomperativ"),
        ),
        {349},
    ),
    (
        ParametersMain.grundstrukturen,
        (
            _("Existenzialien_(3)"),
            _("existenzialien"),
        ),
        {348},
    ),
    (
        ParametersMain.grundstrukturen,
        (_("Extremalien_(19)"), _("extremalien")),
        {347, 352},
    ),
    (
        ParametersMain.grundstrukturen,
        (
            _("Erwartungshaltungen_(26)"),
            _("erwartungen"),
            _("erwartungshaltungen"),
        ),
        {344},
    ),
    (
        ParametersMain.grundstrukturen,
        (
            _("Leidenschaften_(21)"),
            _("leidenschaft"),
            _("leidenschaften"),
        ),
        {343},
    ),
    (
        ParametersMain.grundstrukturen,
        (
            _("relativer_Zeit-Betrag_(15_10_4_18_6)"),
            _("relativerzeitbetrag"),
        ),
        {339},
    ),
    (
        ParametersMain.grundstrukturen,
        (
            _("Zahlenvergleich_(15_18_6)"),
            _("zahlenvergleich"),
        ),
        {340},
    ),
    (
        ParametersMain.grundstrukturen,
        (
            _("Bestrebungen(1/5)"),
            _("bestrebung"),
            _("bestrebungen"),
        ),
        {332},
    ),
    (
        ParametersMain.grundstrukturen,
        (_("Prinzipien(1/8)"), _("prinzipien")),
        {329, 378},
    ),
    (
        ParametersMain.grundstrukturen,
        (
            _("Attraktionen_(36)"),
            _("attraktionen"),
        ),
        {311},
    ),
    (
        ParametersMain.grundstrukturen,
        (
            _("Optimierung_(10)"),
            _("optimierung"),
        ),
        {310},
    ),
    (
        ParametersMain.grundstrukturen,
        (
            _("Themen_(6)"),
            _("themen"),
            _("thema"),
        ),
        {309},
    ),
    (
        ParametersMain.grundstrukturen,
        (
            _("Bedeutung_(10)"),
            _("bedeutung"),
        ),
        {306},
    ),
    (
        ParametersMain.grundstrukturen,
        (
            _("Reziprokes"),
            _("reziproke"),
            _("reziprokes"),
        ),
        (
            42,
            131,
            204,
            231,
            273,
            257,
            284,
            285,
            257,
            204,
            205,
            281,
            326,
            327,
            328,
            329,
            330,
            331,
            332,
            334,
            335,
            338,
        ),
    ),
    (
        ParametersMain.grundstrukturen,
        (
            _("Achtung_(4)"),
            _("achtung"),
            _("achten"),
        ),
        {270},
    ),
    (
        ParametersMain.grundstrukturen,
        (
            _("Zeit_(4)_als_Wirklichkeit"),
            _("zeit"),
        ),
        {266, 267},
    ),
    (
        ParametersMain.grundstrukturen,
        (
            _("Absicht_16_ist_zu_genügen"),
            _("absicht16"),
        ),
        {312},
    ),
    (
        ParametersMain.grundstrukturen,
        (
            _("Absicht_17_ist_zu_meinen"),
            _("absicht17"),
        ),
        {263},
    ),
    (
        ParametersMain.grundstrukturen,
        (
            _("Absicht_6_ist_Vorteilsmaximierung"),
            _("absicht6"),
        ),
        {262},
    ),
    (
        ParametersMain.grundstrukturen,
        (
            _("Absicht_7_ist_Selbstlosigkeit"),
            _("absicht7"),
        ),
        {261},
    ),
    (
        ParametersMain.grundstrukturen,
        (
            _("Regungen_(1)"),
            _("regung"),
            _("regungen"),
        ),
        {282},
    ),
    (
        ParametersMain.grundstrukturen,
        (_("Verhalten_(11)"), _("verhalten")),
        {301, 302},
    ),
    (
        ParametersMain.grundstrukturen,
        (
            _("Energie_und_universelle_Eigenschaften_(30)"),
            _("energie"),
            _("universelleeigenschaften"),
            _("lebensenergie"),
        ),
        {287, 293},
    ),
    (
        ParametersMain.grundstrukturen,
        (
            _("Garben_und_Verhalten_nachfühlen(31)"),
            _("garben"),
            _("verhaltenfuehlen"),
            _("verhaltenfühlen"),
        ),
        {295},
    ),
    (
        ParametersMain.grundstrukturen,
        (
            Primzahlkreuz_pro_contra_strs_Fkt[1],
            _("nachvollziehen"),
        ),
        {242, 297},
        set(),
        set(),
        set(),
        set(),
        set(),
        set(),
        {"primzahlkreuzprocontra"},
    ),
    (
        ParametersMain.grundstrukturen,
        (
            _("Empathie_(37)"),
            _("empathie"),
            _("mitgefuehl"),
        ),
        {294},
    ),
    (
        ParametersMain.grundstrukturen,
        (
            _("Absicht_1/6_ist_Reinigung_und_Klarheit"),
            _("absicht1/6"),
            _("absicht1pro6"),
        ),
        {298},
    ),
    (
        ParametersMain.grundstrukturen,
        (
            _("Absicht_10_ist_Wirklichkeit_erkennen"),
            _("absicht10"),
        ),
        {260},
    ),
    (
        ParametersMain.grundstrukturen,
        (
            _("Geist_(15)"),
            _("geist"),
            _("bewusstsein"),
        ),
        {229, 231, 242, 273, 297, 304},
    ),
    (
        ParametersMain.grundstrukturen,
        (
            _("Reflexe_(3)"),
            _("reflex"),
            _("reflexe"),
        ),
        {256},
    ),
    (
        ParametersMain.grundstrukturen,
        (
            _("Lust_(9)"),
            _("lust"),
        ),
        {255},
    ),
    (
        ParametersMain.grundstrukturen,
        (
            _("Paradigmen_sind_Absichten_(13)"),
            _("paradigmen"),
            _("absichten"),
        ),
        {10, 42},
    ),
    (
        ParametersMain.grundstrukturen,
        (
            _("Wirklichkeiten_Wahrheit_Wahrnehmung_(10)"),
            _("wirklichkeit"),
            _("wirklichkeiten"),
            _("wahrheit"),
            _("wahrnehmung"),
        ),
        {233, 265, 268, 322, 342},
    ),
    (
        ParametersMain.grundstrukturen,
        (
            _("Stimmungen_Kombinationen_(14)"),
            _("stimmung"),
            _("stimmungen"),
            _("kombination"),
            _("kombinationen"),
        ),
        {290, 296, 325, 326, 327},
    ),
    (
        ParametersMain.grundstrukturen,
        (
            _("Klassen_(20)"),
            _("klasse"),
            _("klassen"),
        ),
        {241, 289},
    ),
    (
        ParametersMain.grundstrukturen,
        (
            _("Ordnung_und_Filterung_12_und_1pro12"),
            _("ordnen"),
            _("ordnenundfiltern"),
            _("filtern"),
        ),
        {132, 328, 331, 335},
    ),
    (
        ParametersMain.grundstrukturen,
        (
            _("Meta-Systeme_(12)"),
            _("metasysteme"),
            _("metasystem"),
            _("meta-systeme"),
            _("meta-system"),
            _("menge"),
            _("mengen"),
        ),
        {232, 288, 334},
    ),
    (
        ParametersMain.grundstrukturen,
        (
            _("Absicht_1/8"),
            _("absicht1pro8"),
            _("absicht1/8"),
        ),
        {272, 379},
    ),
    (
        ParametersMain.grundstrukturen,
        (
            _("Ziele_(19)"),
            _("ziele"),
            _("maxima"),
            _("höhenvorstellungen"),
        ),
        {271},
    ),
    (
        ParametersMain.grundstrukturen,
        (
            _("Konkreta_und_Focus_(2)"),
            _("konkreta"),
            _("focus"),
            _("fokus"),
        ),
        {250, 269},
    ),
    (
        ParametersMain.grundstrukturen,
        (
            _("Gefühle_(7)"),
            _("gefuehle"),
            _("emotionen"),
            _("gefühle"),
        ),
        {243, 283, 284, 285, 286, 305},
    ),
    (
        ParametersMain.grundstrukturen,
        (
            _("abhängige_Verbundenheit_(90)"),
            _("abhaengigkeit"),
            _("abhängigkeit"),
        ),
        {357},
    ),
    (
        ParametersMain.grundstrukturen,
        (
            _("Karte_Filter_und_Unterscheidung_(1/12)"),
            _("karte"),
            _("filter"),
            _("unterscheidung"),
        ),
        {377},
    ),
    (
        ParametersMain.grundstrukturen,
        (_("Fundament_(1/19)"), _("fundament")),
        {356},
    ),
    (
        ParametersMain.grundstrukturen,
        (
            _("Gedanken_sind_Positionen_(17)"),
            _("positionen"),
            _("gedanken"),
        ),
        {249, 317, 323},
    ),
    (
        ParametersMain.grundstrukturen,
        (
            _("Funktionen_Vorstellungen_(16)"),
            _("vorstellungen"),
            _("vorstellung"),
            _("funktionen"),
        ),
        {345, 264},
    ),
    (
        ParametersMain.grundstrukturen,
        (
            _("Sollen_Frage_Vorgehensweise_(1/13)"),
            _("sollen"),
            _("frage"),
            _("vorgehensweise"),
        ),
        {353, 354},
    ),
    (
        ParametersMain.grundstrukturen,
        (
            _("Ansichten_Standpunkte_(18_17)"),
            _("ansichten"),
        ),
        {240, 346},
    ),
    (
        ParametersMain.grundstrukturen,
        (
            _("Verbundenheiten_(18)"),
            _("verbundenheiten"),
        ),
        {252, 299, 300, 336},
    ),
    (
        ParametersMain.grundstrukturen,
        (
            _("Absicht_13_ist_Helfen"),
            _("absicht13"),
            _("helfen"),
        ),
        {370},
    ),
    (
        ParametersMain.grundstrukturen,
        (_("Liebe_(7)"), _("liebe")),
        {8, 9, 28, 208, 221, 330},
        {(121, 122)},
    ),
    (
        ParametersMain.grundstrukturen,
        (_("Koalitionen_(10)"), _("koalitionen")),
        {321},
    ),
    (
        ParametersMain.grundstrukturen,
        (_("Impulse_(5)"), _("impulse")),
        {251, 253, 257, 341},
    ),
    (
        ParametersMain.grundstrukturen,
        (
            _("Triebe_und_Bedürfnisse_(6)"),
            _("trieb"),
            _("triebe"),
            _("bedürfnis"),
            _("bedürfnisse"),
        ),
        {254},
    ),
    (
        ParametersMain.grundstrukturen,
        (
            _("Reflektion_und_Kategorien_(1/15)"),
            _("reflektion"),
            _("kategorien"),
        ),
        {204, 205, 281},
    ),
    (
        ParametersMain.grundstrukturen,
        (
            _("Modus_und_Sein_(8)"),
            _("zustaende"),
            _("zustände"),
            _("modus"),
            _("modi"),
            _("sein"),
        ),
        {234, 337},
    ),
    (
        ParametersMain.menschliches,
        (
            _("Motive"),
            _("motive"),
            motivationWort,
            _("motiv"),
            _("absicht"),
            _("absichten"),
        ),
        {10, 18, 42, 167, 168, 149, 229, 230},
    ),
    (
        ParametersMain.menschliches,
        (
            _("Gedanken_sind_Positionen_(17)"),
            _("positionen"),
            _("gedanken"),
        ),
        {249, 276},
    ),
    (
        ParametersMain.menschliches,
        (
            _("Bewusstsein_und_Wahrnehmung"),
            _("bewusstsein"),
            _("wahrnehmung"),
        ),
        {265, 229, 231, 281, 304, 342},
    ),
    (
        ParametersMain.menschliches,
        (
            _("Errungenschaften"),
            _("errungenschaften"),
            _("ziele"),
            _("erhalten"),
        ),
        {11, 257, 251},
    ),
    (
        ParametersMain.menschliches,
        (
            _("evolutionär_erwerben_und_Intelligenz_Kreativität"),
            _("evolutionärerwerbenundintelligenz"),
            _("intelligenz"),
            _("erwerben"),
            _("erlernen"),
            _("lernen"),
            _("evolutionaer"),
            _("evolutionär"),
            _("kreativität"),
            _("kreativitaet"),
            _("kreativ"),
        ),
        {12, 47, 27, 13, 32},
    ),
    (
        ParametersMain.menschliches,
        (
            _("brauchen"),
            _("benoetigen"),
            _("benötigen"),
            _("notwendig"),
        ),
        {13, 14},
    ),
    (
        ParametersMain.menschliches,
        (
            _("Krankheit"),
            _("krankheit"),
            _("krankheiten"),
            _("pathologisch"),
            _("pathologie"),
            _("psychiatrisch"),
        ),
        {24},
    ),
    (
        ParametersMain.menschliches,
        (
            _("alpha_beta"),
            _("alphabeta"),
            _("alpha"),
            _("beta"),
            _("omega"),
            _("sigma"),
        ),
        {46},
    ),
    (
        ParametersMain.menschliches,
        (
            _("Anführer"),
            _("anfuehrer"),
            _("chef"),
        ),
        {29, 170},
    ),
    (
        ParametersMain.menschliches,
        (
            _("Manipulation"),
            _("manipulation"),
        ),
        {153},
    ),
    (
        ParametersMain.menschliches,
        (
            _("Berufe"),
            _("berufe"),
            _("beruf"),
        ),
        {30},
    ),
    (
        ParametersMain.menschliches,
        (
            _("Lösungen"),
            _("lösungen"),
            _("loesungen"),
            _("loesung"),
            _("lösungen"),
        ),
        {31},
    ),
    (ParametersMain.menschliches, (_("Musik"), _("musik")), {33}),
    (
        ParametersMain.procontra,
        (
            _("ergibt_Sinn"),
            _("ergibtsinn"),
            _("machtsinn"),
            _("sinn"),
        ),
        {140},
    ),
    (
        ParametersMain.procontra,
        (
            _("Veränderung"),
            _("veraenderung"),
            _("veraendern"),
            _("veränderung"),
            _("verändern"),
        ),
        {142},
    ),
    (
        ParametersMain.procontra,
        (
            _("bändigen_kontrollieren"),
            _("baendigenkontrollieren"),
            _("kontrollieren"),
            _("baendigen"),
            _("bändigen"),
        ),
        {143},
    ),
    (
        ParametersMain.procontra,
        (
            _("vereinen"),
            _("einheit"),
        ),
        {144},
    ),
    (
        ParametersMain.procontra,
        (
            _("Vorteile"),
            _("vorteile"),
            _("veraenderungnutzen"),
        ),
        {141},
    ),
    (
        ParametersMain.procontra,
        (
            _("Gegenspieler"),
            _("gegenspieler"),
            _("antagonist"),
        ),
        {137},
    ),
    (
        ParametersMain.procontra,
        (_("nervig"),),
        {120},
    ),
    (
        ParametersMain.procontra,
        (
            _("pro_nutzen"),
            _("pronutzen"),
        ),
        {117},
    ),
    (
        ParametersMain.procontra,
        (
            _("Gegenposition"),
            _("gegenposition"),
        ),
        {116},
    ),
    (
        ParametersMain.procontra,
        (
            _("Hilfe_erhalten"),
            _("hilfeerhalten"),
        ),
        {114},
    ),
    (
        ParametersMain.procontra,
        (
            _("Helfen"),
            _("helfen"),
            _("hilfe"),
        ),
        {115},
    ),
    (
        ParametersMain.procontra,
        (
            _("Pro"),
            _("pro"),
            _("dafür"),
            _("dafuer"),
        ),
        {17, 48},
    ),
    (
        ParametersMain.procontra,
        (
            _("nicht_miteinander_auskommen"),
            _("nichtauskommen"),
        ),
        {123},
    ),
    (
        ParametersMain.procontra,
        (
            _("nicht_dagegen"),
            _("nichtdagegen"),
        ),
        {124},
    ),
    (
        ParametersMain.procontra,
        (
            _("kein_Gegenteil"),
            _("keingegenteil"),
        ),
        {125},
    ),
    (
        ParametersMain.procontra,
        (
            _("nicht_dafür"),
            _("nichtdafuer"),
        ),
        {126},
    ),
    (
        ParametersMain.procontra,
        (
            _("Hilfe_nicht_gebrauchen"),
            _("hilfenichtgebrauchen"),
        ),
        {127},
    ),
    (
        ParametersMain.procontra,
        (
            _("nicht_helfen_können"),
            _("nichthelfenkoennen"),
        ),
        {128},
    ),
    (
        ParametersMain.procontra,
        (
            _("nicht_abgeneigt"),
            _("nichtabgeneigt"),
        ),
        {129},
    ),
    (
        ParametersMain.procontra,
        (_("unmotivierbar"),),
        {130},
    ),
    (
        ParametersMain.procontra,
        (
            _("contra"),
            _("dagegen"),
        ),
        {15, 26},
    ),
    (
        ParametersMain.procontra,
        (
            _("Gegenteil"),
            _("gegenteil"),
        ),
        {100, 101, 222},
    ),
    (
        ParametersMain.procontra,
        (
            _("Harmonie"),
            _("harmonie"),
        ),
        {102, 103},
    ),
    (ParametersMain.licht, (), {20, 27, 313}),
    (
        ParametersMain.procontra,
        (
            Primzahlkreuz_pro_contra_strs_Fkt[0],
            _("primzahlkreuz"),
        ),
        set(),
        set(),
        set(),
        set(),
        set(),
        set(),
        set(),
        {"primzahlkreuzprocontra"},
    ),
    (
        ParametersMain.bedeutung,
        (
            Primzahlkreuz_pro_contra_strs_Fkt[0],
            primzahlkreuzWort,
        ),
        set(),
        set(),
        set(),
        set(),
        set(),
        set(),
        set(),
        {"primzahlkreuzprocontra"},
    ),
    (
        ParametersMain.bedeutung,
        (
            _("in_ReTa"),
            _("inreta"),
        ),
        {209, 210},
    ),
    (
        ParametersMain.bedeutung,
        (
            _("Vorzeichen"),
            _("vorzeichen"),
        ),
        {118, 119},
    ),
    (
        ParametersMain.bedeutung,
        (
            _("Primzahlen"),
            _("primzahlen"),
            _("vielfache"),
            _("vielfacher"),
        ),
        {19},
    ),
    (
        ParametersMain.bedeutung,
        (
            _("Anwendung_der_Sonnen_und_Monde"),
            _("anwendungdersonnenundmonde"),
            _("anwendungdersonnen"),
            _("anwendungenfuermonde"),
        ),
        {22},
    ),
    (
        ParametersMain.bedeutung,
        (
            _("Zählungen"),
            _("zählungen"),
            _("zaehlung"),
            _("zaehlungen"),
            _("zählung"),
        ),
        {25, 45, 169, 188},
    ),
    (
        ParametersMain.bedeutung,
        (
            _("Jura"),
            _("jura"),
            _("gesetzeslehre"),
            _("recht"),
        ),
        {34},
    ),
    (
        ParametersMain.bedeutung,
        (
            _("Vollkommenheit_des_Geistes"),
            _("vollkommenheit"),
            _("geist"),
        ),
        {35},
    ),
    (
        ParametersMain.bedeutung,
        (
            _("Gestirn"),
            gestirnWort,
            _("mond"),
            _("sonne"),
            _("planet"),
        ),
        {64, 154},
        set(),
        set(),
        set(),
    ),
    (
        ParametersMain.bedeutung,
        (
            _("Konjunktiv_Wurzelbildung"),
            _("konjunktiv"),
            _("wurzel"),
        ),
        {106},
    ),
    (
        ParametersMain.bedeutung,
        (
            _("Mechanismen_der_Züchtung"),
            _("mechanismen"),
            _("wesen"),
            _("zuechtung"),
            _("züchtung"),
            _("züchten"),
            _("zuechten"),
        ),
        {107, 108, 109},
    ),
    (
        ParametersMain.gebrochengalaxie,
        set([str(a) for a in range(2, gebrochenSpaltenMaximumPlus1)]),
        set(),
        set(),
        set(),
        set(),
        set(),
        set(),
        set([str(a) for a in range(2, gebrochenSpaltenMaximumPlus1)]),
    ),
    (
        ParametersMain.gebrochenuniversum,
        set([str(a) for a in range(2, gebrochenSpaltenMaximumPlus1)]),
        set(),
        set(),
        set(),
        set(),
        set(),
        set([str(a) for a in range(2, gebrochenSpaltenMaximumPlus1)]),
    ),
    (ParametersMain.symbole, (), {36, 37}),
    # (
    #    ParametersMain.Multiplikationen,
    #    allowedPrimNumbersForCommand,
    #    set(),
    #    set(),
    #    (
    #        lambda: {  # nur noch ein Platzhalter
    #            None,
    #        },
    #    ),
    # ),
    (
        ParametersMain.konzept,
        (
            _("Weisheit_etc"),
            _("weisheit"),
            _("metaweisheit"),
            _("meta-weisheit"),
            _("idiot"),
            _("weise"),
            _("optimal"),
            _("optimum"),
        ),
        {112},
        {(40, 41)},
    ),
    (
        ParametersMain.konzept,
        (
            _("Dein_Recht_bekommen"),
            _("rechte"),
            _("recht"),
            _("selbstgerecht"),
        ),
        set(),
        {(291, 292)},
    ),
    (
        ParametersMain.konzept,
        (
            _("unterlegen_überlegen"),
            _("unterlegen"),
            _("ueberlegen"),
        ),
        set(),
        {(380, 381)},
    ),
    (
        ParametersMain.konzept,
        (
            _("Ehrlichkeit_und_Streit"),
            _("streit"),
            _("ehrlichkeit"),
        ),
        set(),
        {(375, 376)},
    ),
    (
        ParametersMain.konzept2,
        (_("Würdig"), _("wuerdig"), _("würdig")),
        set(),
        {(373, 374)},
    ),
    (
        ParametersMain.konzept2,
        (
            _("Regel_vs_Ausnahme"),
            _("regel"),
            _("ausnahme"),
        ),
        set(),
        {(371, 372)},
    ),
    (
        ParametersMain.konzept2,
        (
            _("Filterart_Widrigkeit"),
            _("filterart"),
            _("widrigkeit"),
        ),
        {331, 335},
    ),
    (
        ParametersMain.konzept2,
        (
            _("Werte"),
            _("werte"),
        ),
        set(),
        {(360, 361)},
    ),
    (
        ParametersMain.konzept2,
        (
            _("Gutartigkeits-Egoismus"),
            _("position"),
            _("gutesreziprok"),
        ),
        set(),
        {(362, 363)},
    ),
    (
        ParametersMain.konzept2,
        (
            _("Reflektieren_Erkenntnis-Erkennen"),
            _("reflektieren"),
            _("erkenntnis"),
        ),
        set(),
        {(364, 365)},
    ),
    (
        ParametersMain.konzept2,
        (
            _("Vertrauen_wollen"),
            _("vertrauenwollen"),
        ),
        set(),
        {(366, 367)},
    ),
    (
        ParametersMain.konzept,
        (
            _("einklinken_vertrauen_anprangern"),
            _("einklinken"),
            _("vertrauenerhalten"),
            _("anprangern"),
        ),
        set(),
        {(368, 369)},
    ),
    (
        ParametersMain.konzept2,
        (
            _("Ausrichten_Einrichten"),
            _("einrichten"),
            _("ausrichten"),
        ),
        set(),
        {(358, 359)},
    ),
    (
        ParametersMain.konzept2,
        (
            _("Toleranz_Respekt_Akzeptanz_Willkommen"),
            _("toleranz"),
            _("respekt"),
            _("akzeptanz"),
            _("willkommen"),
        ),
        set(),
        # {(359, 360)},
        {(62, 63)},
    ),
    (
        ParametersMain.konzept,
        (_("familiebrauchen"),),
        set(),
        {(279, 280)},
    ),
    (
        ParametersMain.konzept,
        (_("ego"), _("bescheiden")),
        set(),
        {(277, 278)},
    ),
    (
        ParametersMain.konzept,
        (
            _("Selbstsucht_Ichsucht_etc"),
            _("selbstsucht"),
            _("ichsucht"),
        ),
        set(),
        {(274, 275)},
    ),
    (
        ParametersMain.konzept,
        (
            _("Forschen_Erfinden_Einklinken"),
            _("wissenschaft"),
            _("forschen"),
            _("einklinken"),
            _("erfinden"),
        ),
        set(),
        {(258, 259)},
    ),
    (
        ParametersMain.konzept,
        (
            _("Kooperation_vs_Arsch"),
            _("arschloch"),
            _("kooperation"),
            _("arsch"),
        ),
        set(),
        {(245, 246)},
    ),
    (
        ParametersMain.konzept,
        (_("Liebe_usw"), _("liebe"), _("zuneigung")),
        set(),
        {(247, 248)},
    ),
    (
        ParametersMain.konzept,
        (
            _("Selbstlosigkeit_Ichlosigkeit_etc"),
            _("selbstlos"),
            _("ichlos"),
        ),
        set(),
        {(238, 239)},
    ),
    (
        ParametersMain.konzept,
        (
            _("variationsreich_eintönig"),
            _("eintönig"),
            _("eintoenig"),
            _("variationsreich"),
        ),
        set(),
        {(236, 237)},
    ),
    (
        ParametersMain.konzept,
        (
            _("Zuneigung_Abneigung"),
            _("abgeneigt"),
            _("zugewandt"),
            _("reserviert"),
            _("zugeneigt"),
        ),
        set(),
        {(199, 200)},
    ),
    (
        ParametersMain.menschliches,
        (
            _("ehrlich_vs_höflich"),
            _("ehrlich"),
            _("höflich"),
            _("hoeflich"),
        ),
        set(),
        {(224, 225)},
    ),
    # (
    #    ParametersMain.konzept,
    #    (_("delegieren"), _("ansammlung")),
    #    set(),
    #    {(227, 228)},
    # ),
    (
        ParametersMain.konzept,
        (
            _("ehrlich_vs_höflich"),
            _("ehrlich"),
            _("höflich"),
            _("hoeflich"),
        ),
        set(),
        {(224, 225)},
    ),
    (
        ParametersMain.konzept,
        (_("Tragweite"), _("tragweite")),
        set(),
        {(211, 212)},
    ),
    (
        ParametersMain.konzept,
        (_("wertvoll"), _("wertlos")),
        set(),
        {(186, 187)},
    ),
    (
        ParametersMain.konzept,
        (
            _("Götter_Propheten_Familien_Freunde"),
            _("familiaer"),
            _("goettlich"),
            _("freunde"),
            _("propheten"),
        ),
        set(),
        {(184, 185)},
    ),
    (
        ParametersMain.konzept,
        (
            _("sanft_vs_hart"),
            _("sanft"),
            _("hart"),
        ),
        set(),
        {(159, 160), (161, 162)},
    ),
    (
        ParametersMain.konzept,
        (
            _("vereinen_vs_verbinden"),
            _("vereinenverbinden"),
            _("vereinen"),
            _("verbinden"),
            _("einheit"),
            _("verbindung"),
        ),
        set(),
        {(133, 134)},
    ),
    (
        ParametersMain.konzept,
        (
            _("ähnlich"),
            _("aehnlich"),
        ),
        {220},
    ),
    (
        ParametersMain.konzept,
        (
            _("gut_böse_lieb_schlecht"),
            _("gut"),
            _("böse"),
            _("boese"),
            _("lieb"),
            _("schlecht"),
        ),
        {52, 53},
        {(38, 39)},
    ),
    (
        ParametersMain.konzept,
        (
            _("Sinn_und_Zweck_des_Lebens"),
            _("sinn"),
            _("zweck"),
            _("bedeutung"),
        ),
        {88, 189},
        {(181, 182)},
    ),
    (
        ParametersMain.konzept,
        (
            _("Zeit_vs_Raum"),
            _("zeit"),
            _("raum"),
            _("zeitlich"),
            _("räumlich"),
        ),
        set(),
        {(49, 50)},
    ),
    (
        ParametersMain.konzept,
        (
            _("egalitär_vs_autoritär"),
            _("egalitaerautoritaer"),
            _("egalitaer"),
            _("autoritaer"),
            _("egalitär"),
            _("autoritär"),
        ),
        set(),
        {(163, 164)},
    ),
    (
        ParametersMain.konzept,
        (
            _("Meinungen_und_Ruf"),
            _("meinungen"),
            _("anderemenschen"),
            _("ruf"),
        ),
        set(),
        {(60, 61)},
    ),
    (
        ParametersMain.konzept,
        (
            _("Meinungsintelligenz"),
            _("meinungsintelligenz"),
            _("ursprungsintelligenz"),
        ),
        set(),
        {(151, 152)},
    ),
    (
        ParametersMain.konzept,
        (
            _("Sittlichkeit"),
            _("sittlichkeit"),
            _("annaehrerung"),
        ),
        set(),
        {(179, 180)},
    ),
    (
        ParametersMain.konzept,
        (_("Führung"), _("führung"), _("fuehrung")),
        set(),
        {(173, 174)},
    ),
    (
        ParametersMain.konzept,
        (
            _("Durchleuchten"),
            _("durchleuchten"),
            _("erleuchten"),
        ),
        set(),
        {(177, 178)},
    ),
    (
        ParametersMain.konzept,
        (
            _("Fördern_Sensiblisieren_und_Gedeihen"),
            _("foerdern"),
            _("fördern"),
            _("begrenzen"),
            _("sensibilisieren"),
            _("gedeihen"),
            _("verderben"),
        ),
        set(),
        {(175, 176)},
    ),
    (
        ParametersMain.konzept,
        (
            _("Überheblichkeit"),
            _("überheblich"),
            _("ueberheblichkeit"),
            _("ueberheblich"),
            _("überheblichkeit"),
        ),
        set(),
        {(171, 172)},
    ),
    (
        ParametersMain.konzept,
        (
            _("Polung_der_Liebe"),
            _("liebepolung"),
        ),
        set(),
        {(121, 122)},
    ),
    (
        ParametersMain.konzept,
        (
            _("Egoismus_vs_Altruismus"),
            _("egoismus"),
            _("altruismus"),
            _("egoist"),
            _("altruist"),
        ),
        {136},
        {(66, 67)},
    ),
    (
        ParametersMain.konzept,
        (_("kausal"), _("geltung"), _("genese")),
        set(),
        {(110, 111)},
    ),
    (
        ParametersMain.konzept,
        (_("Gleichheit"), _("gleich")),
        set(),
        {(192, 193)},
    ),
    (
        ParametersMain.konzept,
        (_("Überleben"), _("ueberleben")),
        set(),
        {(194, 195)},
    ),
    (ParametersMain.inkrementieren, set(), {43, 54, 74, 95}),
    (ParametersMain.inkrementieren, (_("um1"),), {155}),
    (ParametersMain.inkrementieren, (_("um2"),), {156}),
    (ParametersMain.inkrementieren, (_("um3"),), {157}),
    (
        ParametersMain.inkrementieren,
        (
            _("warum_Transzendentalie_=_Strukturgroesse_=_Charakter"),
            _("warumtranszendentaliezustrukturgroesseundcharakter"),
        ),
        {4, 54, 5, 165},
    ),
    (
        ParametersMain.inkrementieren,
        (
            _("warum_Transzendentalie_=_Komplexität_von_Michael_Commons"),
            _("warumtranszendentaliegleichkomplexitaet"),
        ),
        {65, 5, 166},
    ),
    (
        ParametersMain.primvielfache,
        (_("Rahmen-Bedingungen"), _("rahmen")),
        {226},
    ),
    (
        ParametersMain.primvielfache,
        (
            _("Motive_gleichförmige_Polygone"),
            _("motivgleichfoermig"),
        ),
        set(),
        set(),
        set(),
        set(),
        set(),
        set(),
        set(),
        {"primMotivGleichf"},
    ),
    (
        ParametersMain.primvielfache,
        (
            _("Struktur_gleichförmige_Polygone"),
            _("strukturgleichfoermig"),
        ),
        set(),
        set(),
        set(),
        set(),
        set(),
        set(),
        set(),
        {"primStrukGleichf"},
    ),
    (
        ParametersMain.primvielfache,
        (
            _("Motive_Sternpolygone"),
            _("motivstern"),
        ),
        set(),
        set(),
        set(),
        set(),
        set(),
        set(),
        set(),
        {"primMotivStern"},
    ),
    (
        ParametersMain.primvielfache,
        (
            _("Struktur_Sternpolygone"),
            _("strukturstern"),
        ),
        set(),
        set(),
        set(),
        set(),
        set(),
        set(),
        set(),
        {"primStrukStern"},
    ),
    (
        ParametersMain.primvielfache,
        (
            _("Motiv_Sternpolygon_gebrochen-rational"),
            _("motivgebrstern"),
        ),
        set(),
        set(),
        set(),
        set(),
        set(),
        set(),
        set(),
        {"primMotivSternGebr"},
    ),
    (
        ParametersMain.primvielfache,
        (
            _("Struktur_Sternpolyon_gebrochen-rational"),
            _("strukgebrstern"),
        ),
        set(),
        set(),
        set(),
        set(),
        set(),
        set(),
        set(),
        {"primStrukSternGebr"},
    ),
    (
        ParametersMain.primvielfache,
        (
            _("Motiv_gleichförmige_Polygone_gebrochen-rational"),
            _("motivgebrgleichf"),
        ),
        set(),
        set(),
        set(),
        set(),
        set(),
        set(),
        set(),
        {"primMotivGleichfGebr"},
    ),
    (
        ParametersMain.primvielfache,
        (
            _("Struktur_gleichförmige_Polygone_gebrochen-rational"),
            _("strukgebrgleichf"),
        ),
        set(),
        set(),
        set(),
        set(),
        set(),
        set(),
        set(),
        {"primStrukGleichfGebr"},
    ),
    (
        ParametersMain.primvielfache,
        (_("beschrieben"),),
        set(),
        set(),
        set(),
        set(),
        set(),
        set(),
        set(),
        {"PrimCSV"},
    ),
]
paraNdataMatrix = paraNdataMatrix

kombiParaNdataMatrix: OrderedDict = OrderedDict(
    {
        1: (
            _("Lebewesen"),
            _("tiere"),
            _("tier"),
            _("lebewesen"),
        ),
        2: (_("Berufe"), _("berufe"), _("beruf")),
        3: (
            _("Kreativität_und_Intelligenz"),
            _("kreativität"),
            _("intelligenz"),
            _("kreativitaet"),
        ),
        4: (
            _("Liebe"),
            _("liebe"),
        ),
        7: (
            _("Männer"),
            _("männer"),
            _("maenner"),
            _("frauen"),
        ),
        8: (
            _("Persönlichkeit_evolutionär_erwerben"),
            _("evolution"),
            _("erwerben"),
            _("persoenlichkeit"),
            _("persönlichkeit"),
        ),
        9: (
            _("Religion"),
            _("religion"),
            _("religionen"),
        ),
        10: (
            _("Motive_Ziele"),
            _("motivation"),
            _("ziele"),
            _("ziel"),
            _("motive"),
        ),
        12: (
            _("Emotionen"),
            _("emotionen"),
            _("gefuehle"),
            _("emotion"),
            _("gefühl"),
            _("gefühle"),
        ),
        13: (
            _("Personen"),
            _("personen"),
            _("berühmtheiten"),
            _("beruehmtheiten"),
        ),
        16: (
            _("Wirtschaftssysteme"),
            _("wirtschaftssystem"),
            _("wirtschaftssysteme"),
            _("kombinierteswirtschaftssystem"),
            _("kombiniertewirtschaftssysteme"),
        ),
    }
)

kombiParaNdataMatrix2: OrderedDict = OrderedDict(
    {
        1: (
            _("Lebewesen"),
            _("tiere"),
            _("tier"),
            _("lebewesen"),
        ),
        2: (_("Berufe"), _("berufe"), _("beruf")),
        # 3: (
        #    _("Kreativität_und_Intelligenz"),
        #    _("kreativität"),
        #    _("intelligenz"),
        #    _("kreativitaet"),
        # ),
        # 4: (
        #    _("Liebe"),
        #    _("liebe"),
        # ),
        5: (
            _("Transzendentalien_Strukturalien"),
            _("transzendenz"),
            _("transzendentalien"),
            _("strukturalien"),
            _("alien"),
        ),
        6: (
            _("Primzahlkreuz"),
            _("leibnitz"),
            _("primzahlkreuz"),
        ),
        # 7: (
        #    _("Männer"),
        #    _("männer"),
        #    _("maenner"),
        #    _("frauen"),
        # ),
        8: (
            _("Persönlichkeit_evolutionär_erwerben"),
            _("evolution"),
            _("erwerben"),
            _("persoenlichkeit"),
            _("persönlichkeit"),
        ),
        # 9: (
        #    _("Religion"),
        #    _("religion"),
        #    _("religionen"),
        # ),
        10: (
            _("Motive_Ziele"),
            _("motivation"),
            _("motive"),
            _("ziele"),
            _("ziel"),
        ),
        11: (
            _("analytische_Ontologie"),
            _("analytischeontologie"),
            _("ontologie"),
        ),
        # 12: (
        #    _("Emotionen"),
        #    _("emotionen"),
        #    _("gefuehle"),
        #    _("gefühle"),
        #    _("emotion"),
        #    _("gefühl"),
        #    _("gefühle"),
        # ),
        # 13: (_("Personen"), "personen": _("personen"), "berühmtheiten": _("berühmtheiten"), "beruehmtheiten": _("beruehmtheiten")),
        14: (
            _("Mechanismen_der_Zuechtung"),
            _("mechanismen"),
            _("wesen"),
            _("zuechten"),
            _("züchten"),
        ),
        15: (
            _("Gegentranszendentalien"),
            _("gegentranszendentalien"),
            _("gegenstrukturalien"),
        ),
        # 16: (
        #    _("Wirtschaftssysteme"),
        #    _("wirtschaftssystem"),
        #    _("wirtschaftssysteme"),
        #    _("kombinierteswirtschaftssystem"),
        #    _("kombiniertewirtschaftssysteme"),
        # ),
        17: (
            _("Maschinen"),
            _("maschinen"),
            _("geräte"),
            _("geraete"),
        ),
        18: (_("Geist"), _("geist")),
        19: (_("Bewusstsein"), _("bewusstsein")),
    }
)


def classify(mod):
    if mod == 0:
        return _("ja")
    elif mod == 1:
        return _("Gegenteil")
    elif mod == 2:
        return _("ähnlich")
    elif mod == 3:
        return _("entferntes Gegenteil")
    elif mod == 4:
        return _("entfernt ähnlich")


class tableHandling:
    parameterName: dict = {"kombination": _("kombination")}
    art = ausgabeArt
    into = {
        "Kombination_(Galaxie_und_schwarzes_Loch)_(14_mit_13)": _(
            "Kombination_(Galaxie_und_schwarzes_Loch)_(14_mit_13)"
        ),
        "Wichtigstes_zum_gedanklich_einordnen": _(
            "Wichtigstes_zum_gedanklich_einordnen"
        ),
        "Zweitwichtigste": _("Zweitwichtigste"),
        "berufe": _("berufe"),
        "intelligenz": _("intelligenz"),
        "tiere": _("tiere"),
        "Kombination_(Universum_und_Galaxie)_(14_mit_15)": _(
            "Kombination_(Universum_und_Galaxie)_(14_mit_15)"
        ),
    }
    gestirnGrossschrift = {
        "Gestirn": _("Gestirn"),
        "Mond": _("Mond"),
        "Sonne": _("Sonne"),
        "Planet": _("Planet"),
    }


class concat:
    themaWort = _("Thema: ")
    polygon1 = {" der eigenen Strukturgröße (": _(" der eigenen Strukturgröße (")}
    polygon2 = {
        ") auf dich bei gleichförmigen Polygonen": _(
            ") auf dich bei gleichförmigen Polygonen"
        )
    }
    energietopologie1 = {
        "eine Denkart": _("eine Denkart"),
        "eine Gefühlsart": _("eine Gefühlsart"),
        "total eine Art, etwas geistig zu erzeugen": _(
            "total eine Art, etwas geistig zu erzeugen"
        ),
        "total eine Art zu erleben": _("total eine Art zu erleben"),
        "total eine Energie-Art": _("total eine Energie-Art"),
        "etwas eine Art zu erleben": _("etwas eine Art zu erleben"),
        "etwas eine Art, etwas geistig zu erzeugen": _(
            "etwas eine Art, etwas geistig zu erzeugen"
        ),
        "wenig eine Art, etwas geistig zu erzeugen": _(
            "wenig eine Art, etwas geistig zu erzeugen"
        ),
        "einigermaßen eine Energie-Art": _("einigermaßen eine Energie-Art"),
        "kaum eine Energie-Art": _("kaum eine Energie-Art"),
        "kaum eine Art, etwas geistig zu erzeugen": _(
            "kaum eine Art, etwas geistig zu erzeugen"
        ),
        "eine Denkart": _("eine Denkart"),
        "eine Gefühlsart": _("eine Gefühlsart"),
        "total eine Art, etwas geistig zu erzeugen": _(
            "total eine Art, etwas geistig zu erzeugen"
        ),
        "total eine Art zu erleben": _("total eine Art zu erleben"),
        "total eine Energie-Art": _("total eine Energie-Art"),
        "etwas eine Art zu erleben": _("etwas eine Art zu erleben"),
        "etwas eine Art, etwas geistig zu erzeugen": _(
            "etwas eine Art, etwas geistig zu erzeugen"
        ),
        "wenig eine Art, etwas geistig zu erzeugen": _(
            "wenig eine Art, etwas geistig zu erzeugen"
        ),
        "einigermaßen eine Energie-Art": _("einigermaßen eine Energie-Art"),
        "kaum eine Energie-Art": _("kaum eine Energie-Art"),
        "kaum eine Art, etwas geistig zu erzeugen": _(
            "kaum eine Art, etwas geistig zu erzeugen"
        ),
    }
    ausgabeString = {
        "Energie oder Denkart oder Gefühlsart oder Materie-Art oder Topologie-Art": _(
            "Energie oder Denkart oder Gefühlsart oder Materie-Art oder Topologie-Art"
        )
    }
    kreaZahl = {
        "Evolutions-Züchtungs-Kreativität": _("Evolutions-Züchtungs-Kreativität"),
        "0. Primzahl 1": _("0. Primzahl 1"),
        "1. Primzahl und Sonnenzahl": _("1. Primzahl und Sonnenzahl"),
        "2. Sonnenzahl, aber keine Primzahl": _("2. Sonnenzahl, aber keine Primzahl"),
        "3. Mondzahl": _("3. Mondzahl"),
    }
    mondExpLog1 = {
        "Mond-Typ eines Sternpolygons": _("Mond-Typ eines Sternpolygons"),
        "Mond-Typ eines gleichförmigen Polygons": _(
            "Mond-Typ eines gleichförmigen Polygons"
        ),
    }

    mondExpLog2 = {"kein Mond": _("kein Mond")}
    # wohl nich nötig zu übersetzen modalA_
    # modalA1 = {"modalS": _("modalS")}
    # modalA2 = {"vervielfachter": _("vervielfachter")}
    # modalA3 = {"i_origS": _("i_origS")}

    modalB = {
        "mittelstark überdurchschnittlich: ": _("mittelstark überdurchschnittlich: "),
        "überdurchschnittlich: ": _("überdurchschnittlich: "),
        "mittelleicht überdurchschnittlich: ": _("mittelleicht überdurchschnittlich: "),
        "sehr: ": _("sehr: "),
        "sehr leicht überdurchschnittlich: ": _("sehr leicht überdurchschnittlich: "),
    }
    modalC = {
        "intrinsisch": _("intrinsisch"),
        "zuerst": _("zuerst"),
        "extrinsisch": _("extrinsisch"),
        "als zweites": _("als zweites"),
    }
    modalD = {
        ", nicht: ": _(", nicht: "),
        " (das alles nicht): ": _(" (das alles nicht): "),
        "extrinsisch": _("extrinsisch"),
        "als zweites": _("als zweites"),
        "intrinsisch": _("intrinsisch"),
        "zuerst": _("zuerst"),
    }

    generiertWort = {"Generiert: ": _("Generiert: ")}
    allesNurBezogenAufSatz = _("Alles nur bezogen auf die selbe Strukturgröße einer ")
    headline1 = "Gegen / pro: Nach Rechenregeln auf Primzahlkreuz und Vielfachern von Primzahlen"
    gegen = {"gegen ": _("gegen ")}
    pro = {"pro ": _("pro ")}
    hineinversetzen = {
        " Darin kann sich die ": _(" Darin kann sich die "),
        " am Besten hineinversetzten.": _(" am Besten hineinversetzten."),
    }
    proIst = {
        "pro dieser Zahl sind: ": _("pro dieser Zahl sind: "),
        "pro dieser Zahl ist ": _("pro dieser Zahl ist "),
    }
    contraIst = {
        " contra dieser Zahl sind: ": _(" contra dieser Zahl sind: "),
        " contra dieser Zahl ist ": _(" contra dieser Zahl ist "),
    }
    hineinversetzenSatz = " - Die Zahlen, die für oder gegen diese Zahlen hier sind, können sich in diese am Besten gedanklich hineinversetzen."
    polygone = {
        "Sternpolygone": _("Sternpolygone"),
        "gleichförmige Polygone": _("gleichförmige Polygone"),
    }

    kombisNamen: dict = {
        "Motiv -> Motiv": _("Motiv -> Motiv"),
        "Motiv -> Strukur": _("Motiv -> Strukur"),
        "Struktur -> Motiv": _("Struktur -> Motiv"),
        "Struktur -> Strukur": _("Struktur -> Strukur"),
    }
    # kombisNamen2: dict = {
    #    "GalGal": _("GalGal"),
    #    "GalUni": _("GalUni"),
    #    "UniGal": _("UniGal"),
    #    "UniUni": _("UniUni"),
    # }

    faktorenbla = {
        ", mit Faktoren aus gebrochen-rationalen Zahlen": _(
            ", mit Faktoren aus gebrochen-rationalen Zahlen"
        )
    }
    genMul = {"generierte Multiplikationen ": _("generierte Multiplikationen ")}
    ausserdem = {", außerdem: ": _(", außerdem: "), "| außerdem: ": _("| außerdem: ")}
    Multiplikationen_ = {"Multiplikationen": _("Multiplikationen")}
    nWichtigste = {
        "Wichtigstes_zum_verstehen": _("Wichtigstes_zum_verstehen"),
        "Viertwichtigste": _("Viertwichtigste"),
    }
    metaOrWhat = {
        "Meta-Thema: ": _("Meta-Thema: "),
        "Konkretes: ": _("Konkretes: "),
        "Meta-": _("Meta-"),
        "Konkret-": _("Konkret-"),
        "Theorie-Thema: ": _("Theorie-Thema: "),
        "Praxis: ": _("Praxis: "),
        "Theorie-": _("Theorie-"),
        "Praxis-": _("Praxis-"),
        "Planungs-Thema: ": _("Planungs-Thema: "),
        "Umsetzungs-Thema: ": _("Umsetzungs-Thema: "),
        "Planung-": _("Planung-"),
        "Umsetzung-": _("Umsetzung-"),
        "Anlass-Thema: ": _("Anlass-Thema: "),
        "Wirkungs-Thema: ": _("Wirkungs-Thema: "),
        "Anlass-": _("Anlass-"),
        "wirkung-": _("wirkung-"),
        "Kraft-Gebung: ": _("Kraft-Gebung: "),
        "Verstärkungs-Thema: ": _("Verstärkungs-Thema: "),
        "Kraft-geben-": _("Kraft-geben-"),
        "Verstärkung-": _("Verstärkung-"),
        "Beherrschung: ": _("Beherrschung: "),
        "Richtung-Thema: ": _("Richtung-Thema: "),
        "beherrschend-": _("beherrschend-"),
        "Richtung-": _("Richtung-"),
    }
    metaKonkret = {
        "Meta": _("Meta"),
        "Theorie": _("Theorie"),
        "Management": _("Management"),
        "ganzheitlich": _("ganzheitlich"),
        "Verwertung, Unternehmung, Geschäft": _("Verwertung, Unternehmung, Geschäft"),
        "regieren, beherrschen": _("regieren, beherrschen"),
        "Konkretes": _("Konkretes"),
        "Praxis": _("Praxis"),
        "verändernd": _("verändernd"),
        "darüber hinaus gehend": _("darüber hinaus gehend"),
        "wertvoll": _("wertvoll"),
        "Richtung": _("Richtung"),
        " für 1/n statt n": _(" für 1/n statt n"),
        " für n": _(" für n"),
    }
    innenAussen = {
        "für innen": _("für innen"),
        "für außen": _("für außen"),
        '"für seitlich und gegen Schwächlinge innen"': _(
            '"für seitlich und gegen Schwächlinge innen"'
        ),
        '"gegen seitlich und für Schwächlinge innen"': _(
            '"gegen seitlich und für Schwächlinge innen"'
        ),
        "für außen": _("für außen"),
    }
    spaltenNamen = OrderedDict(
        {
            "Transzendentalien, Strukturalien, Universum n": _(
                "Transzendentalien, Strukturalien, Universum n"
            ),
            "Galaxie n": _("Galaxie n"),
            "Galaxie 1/n": _("Galaxie 1/n"),
            "Transzendentalien, Strukturalien, Universum 1/n": _(
                "Transzendentalien, Strukturalien, Universum 1/n"
            ),
            "Dagegen-Gegen-Transzendentalien, Gegen-Strukturalien, Universum n": _(
                "Dagegen-Gegen-Transzendentalien, Gegen-Strukturalien, Universum n"
            ),
            "neutrale Gegen-Transzendentalien, Gegen-Strukturalien, Universum n": _(
                "neutrale Gegen-Transzendentalien, Gegen-Strukturalien, Universum n"
            ),
            "Richtung-Richtung": _("Richtung-Richtung"),
        }
    )

    primRicht = {"Primzahlwirkung (7, Richtung) ": _("Primzahlwirkung (7, Richtung) ")}

    letztEnd = {"] * letztendlich: ": _("] * letztendlich: ")}

    primVielGen = {
        "Primzahlvielfache, nicht generiert": _("Primzahlvielfache, nicht generiert")
    }
    GalOrUniOrFehler = {
        "Fehler": _("Fehler"),
        "Universum": _("Universum"),
        "Galaxie": _("Galaxie"),
    }

    multipl = {"Multiplikationen": _("Multiplikationen")}
    notGen = {"Nicht_generiert": _("Nicht_generiert")}


class lib4tables:
    zaehlung = {"zaehlung": _("zaehlung")}
    nummerier = {"nummerierung": _("nummerierung")}
    alles = {"alles": _("alles")}


class retapy:

    beschriebenWort = _("beschrieben")
    nichtsWort = _("nichts")
    cliout1Saetze = (
        _('Der Haupt-Parameter "'),
        _('" existiert hier nicht als Befehl!'),
        _(" Es ist nur möglich: -"),
    )

    keineNumWort = _("keinenummerierung")
    cliout2Saetze = (
        _('Der Unter-Paramaeter "--'),
        _('" existiert, aber nicht mit dem Textwert "'),
        _('". Mögliche Nebenparameter-Textwerte, für diesen Unter-Parameter, sind: "'),
        _('". Stattdessen gibt keine Nebenparameter-Textwerte.'),
    )
    cliout3Saetze = (
        _('Der Unter-Paramaeter "--'),
        _('" mit dem Textwert "'),
        _('" existiert hier nicht als Befehl für Haupt-Parameter'),
        " -" + hauptForNeben["spalten"],
        _(" !"),
        _(" Es ist nur möglich:\n--"),
        "".join((", --", ausgabeParas["breiten"], " --", ausgabeParas["breite"])),
        _("\nmit dem Werten dahinter:\n"),
    )
    cliout4Saetze = (
        _('Der Unter-Parameter "--'),
        _('" existiert hier nicht als Befehl für Haupt-Parameter'),
        " -" + hauptForNeben["spalten"],
        _(
            ", oder dieser Parameter braucht Werte analog wie: \n--unterParameter=Wert1\n"
        ),
        _("Es ist nur möglich: --"),
        ", --" + ausgabeParas["keinenummerierung"],
    )
    kombinationenWort = _("kombinationen")
    cliout5Saetze = (
        _('Die Kombispalte "'),
        _('" existiert so nicht als Befehl. Möglich sind die Parameter für '),
    )
    cliout6Satz = "".join(
        (
            _("kein Unter-Parameter"),
            "--",
            kombiMainParas["galaxie"],
            '= ",',
            _(", oder"),
            ', "--',
            kombiMainParas["universum"],
            '=", ',
            _("angegeben für Hauptparameter"),
            " -" + hauptForNeben["kombination"],
            _(" oder einen nicht zugehörigen Parameter: "),
        )
    )
    cliout7Saetze = (
        _("Es muss ein Hauptparameter, bzw. der richtige, gesetzt sein, damit ein"),
        _(' Nebenparameter, wie möglicherweise: "'),
        _('" ausgeführt werden kann. Hauptparameter sind: -'),
    )
    # breiteParameterWort = _("breite")

    cliout8SatzVersucheParaH = _("Versuche Parameter -h")
    cliout9Saetze = (
        _('Den Neben-Parameter "'),
        _('" gibt es hier nicht für den Hauptparameter "-'),
        _('". Oder ein = fehlt dahinter.'),
        _(" Möglich sind: "),
    )
    cliout10Saetze = (
        _('Den Neben-Parameter "'),
        _('" gibt es hier nicht für den Hauptparameter "-'),
        _('". Oder es fehlt ein = dahinter.'),
    )


class nested:
    galWort = kombiMainParas["galaxie"]
    uniWort = kombiMainParas["universum"]
    artWort = ausgabeParas["art"]
    zeitWort = zeilenParas["zeit"]
    typWort = zeilenParas["typ"]


class retaPrompt:
    infoDebugAktiv = _("Debug Log aktiviert.")
    abstandMeldung = (
        _("der Befehl '")
        + befehle2["abstand"]
        + _(
            "' ist nur erlaubt mit 2 weiteren Angaben mit Leerzeichen getrennt, einer Zahl und einem Zahlenbereich, z.B. '"
        )
        + befehle2["abstand"]
        + " 7 17-25'"
    )
    befehleBeenden = {_("ende"), _("exit"), _("quit"), _("q"), _(":q")}
    befehleWort = {"Befehle": _("Befehle")}
    promptModeSatz = _("promptmode vorher: {} , {}")
    promptModeSatz2 = _("'{}' ergibt sich aus '{}' und ergibt danach reta-Befehl:")
    out1Saetze = (
        _("Dies ('"),
        _(
            "') ist tatsächlich ein Befehl (oder es sind mehrere), aber es gibt nichts auszugeben."
        ),
    )
    out2Satz = _("Das ist kein Befehl! -> '{}''")
    out3Saetze = _(
        'Wenn im Zähler oder Nenner eine 1 ist, so werden davon oft (nicht immer) keine Vielfacher gebildet.\nFür Brüche "n/1=ganze Zahl" gibt es die gewöhnlichen Befehle für ganze Zahlen.\nDas ist eine Design-Entscheidung, die getroffen worden ist.'
    )
    replacements = {
        befehle2["e"]: befehle2[
            "keineEinZeichenZeilenPlusKeineAusgabeWelcherBefehlEsWar"
        ],
        befehle2["a"]: befehle2["absicht"],
        befehle2["u"]: befehle2["universum"],
        befehle2["t"]: befehle2["thomas"],
        befehle2["r"]: befehle2["richtung"],
        befehle2["v"]: befehle2["vielfache"],
        befehle2["h"]: befehle2["help"],
        befehle2["w"]: befehle2["teiler"],
        befehle2["S"]: befehle2["BefehlSpeichernDanach"],
        befehle2["s"]: befehle2["BefehlSpeichernDavor"],
        befehle2["l"]: befehle2["BefehlSpeicherungLöschen"],
        befehle2["o"]: befehle2["BefehlSpeicherungAusgeben"],
    }
    retaPromptParameter = {
        "vi": _("vi"),
        "log": _("log"),
        "h": _("h"),
        "help": _("help"),
        "e": _("e"),
        "debug": _("debug"),
        "befehl": _("befehl"),
    }

    debugLog = _("Debug Log aktiviert.")
    helptext = "".join(
        (
            _(
                """Erlaube Parameter sind
            -"""
            ),
            retaPromptParameter["vi"],
            _(
                """, für vi mode statt emacs mode,
            -"""
            ),
            "language=",
            _(""",  um eine andere Sprache zu wählen und möglich sind: """),
            str([s for s in sprachen.keys() if s.strip() != ""])[1:-1],
            """
            -""",
            retaPromptParameter["log"],
            _(
                """,  um Logging zu aktivieren,
            -"""
            ),
            retaPromptParameter["debug"],
            _(
                """, um Debugging-Log-Ausgabe zu aktivieren. Das ist nur für Entwickler gedacht.
            -"""
            ),
            retaPromptParameter["befehl"],
            _(
                """ bewirkt, dass bis zum letzten Programmparameter retaPrompt Befehl nur ein RetaPrompt-Befehl ausgeführt wird.
            -"""
            ),
            retaPromptParameter["e"],
            _(" bewirkt, dass bei allen Befehlen das '"),
            befehle2["e"],
            _("' Kommando bzw. '"),
            befehle2["keineEinZeichenZeilenPlusKeineAusgabeWelcherBefehlEsWar"],
            _(
                "' jedes mal verwendet wird - außer wenn der erste Befehl reta war, weil dieser anders funktioniert "
            ),
        )
    )

    wspeichernWort = _("was speichern>")
    wloeschenWort = _("was löschen>")
    reziInfoText = _(
        'Wenn im Zähler oder Nenner eine 1 ist, so werden davon oft (nicht immer) keine Vielfacher gebildet.\nFür Brüche "n/1=ganze Zahl" gibt es die gewöhnlichen Befehle für ganze Zahlen.\nDas ist eine Design-Entscheidung, die getroffen worden ist.'
    )


mainParaCmds: dict = {
    "zeilen": _("zeilen"),
    "spalten": _("spalten"),
    tuple(tableHandling.parameterName.keys())[0]: tuple(
        tableHandling.parameterName.values()
    )[0],
    "ausgabe": _("ausgabe"),
    "debug": _("debug"),
    "h": _("h"),
    "help": _("help"),
}


# @dataclass
class csvFileNames:
    kombi13 = _("kombi.csv")
    kombi15 = _("kombi-meta.csv")
    religion = _("religion.csv")
    prim = _("primenumbers.csv")
    bruch15 = _("gebrochen-rational-universum.csv")
    bruch13 = _("gebrochen-rational-galaxie.csv")
    bruch7 = _("gebrochen-rational-emotionen.csv")
    burchGroesse = _("gebrochen-rational-strukturgroesse.csv")
    kombi_17_13_15 = _("kombi-gedanken17-absichten13-bewusstsein15.csv")
    kombi_11_15 = _("kombi-meta-systeme.csv")
    kombi_10_15 = _("kombi-universelle-wirklichkeit.csv")
    kreis18 = _("kreisVomTyp18.csv")
    sunMoon = _("sunMoonEtc.csv")
    meaningOfLife = _("meaningOfLife.csv")
    dualitaetenTrinities = _("dualism-trinities-etc.csv")


EIGS_N_R = (_("EIGN"), _("EIGR"))


class readMeFileNames:
    reta = _("readme-reta.md")
    retaPrompt = _("readme-retaPrompt.md")
    startFiles = _("readme-startFiles.md")
    developer = _("readme.org")


wrongLangSentence = (
    _("für '-languages=' sind die Paramter-Werte erlaubt: ")
    + str(tuple(sprachen.values()))[1:-1]
)
