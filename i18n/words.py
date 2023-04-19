import gettext
import os
# import sys
from collections import OrderedDict, namedtuple
from typing import Any, NamedTuple, Optional, Tuple, Union

# from typing import Optional, Union

try:
    from orderedset import OrderedSet
except:
    OrderedSet = set

# sys.path.insert(1, "./..")
localedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "locale")
translate = gettext.translation("handroll", localedir, fallback=True)
_ = translate.gettext
Multiplikationen = [(_("Multiplikationen"), "")]
"""
ES FEHLEN NOCH ALLE ''
fertig: in prepare ist nichts
fertig: concat
fertig: center
fertig: lib4tables
fertig: reta.py
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

gebrochenSpaltenMaximumPlus1: int = 21  # Das ist nicht die Spaltenbreite, sondern wie weit gebrochene Zahlen gehen dürfen bei Zähler und Nenner
spalten: dict[str, str] = {}
spalten |= {
    "breite": _("breite"),
    "breiten": _("breiten"),
    "keinenummerierung": _("keinenummerierung"),
}

zeilenTypen: dict[str, str] = {
    "sonne": _("sonne"),
    "mond": _("mond"),
    "planet": _("planet"),
    "schwarzesonne": _("schwarzesonne"),
}
zeilenZeit: dict[str, str] = {
    "heute": _("heute"),
    "gestern": _("gestern"),
    "morgen": _("morgen"),
}

ausgabeParas: dict[str, str] = {
    "nocolor": _("nocolor"),
    "justtext": _("justtext"),
    "art": _("art"),
    "onetable": _("onetable"),
    "spaltenreihenfolgeundnurdiese=": _("spaltenreihenfolgeundnurdiese"),
    "endlessscreen": _("endlessscreen"),
    "endless": _("endless"),
    "dontwrap": _("dontwrap"),
    "breite": _("breite"),
    "breiten": _("breiten"),
    "keineleereninhalte": _("keineleereninhalte"),
    "keinenummerierung": _("keinenummerierung"),
    "keineueberschriften": _("keineueberschriften"),
}
kombiMainParas: dict[str, str] = {
    "galaxie": _("galaxie"),
    "universum": _("universum"),
}
zeilenParas: dict[str, str] = {
    "zeit": _("zeit"),
    "zaehlung": _("zaehlung"),
    "vorhervonausschnitt": _("vorhervonausschnitt"),
    "vorhervonausschnittteiler": _("vorhervonausschnittteiler"),
    "primzahlvielfache": _("primzahlvielfache"),
    "nachtraeglichneuabzaehlung": _("nachtraeglichneuabzaehlung"),
    "nachtraeglichneuabzaehlungvielfache": _("nachtraeglichneuabzaehlungvielfache"),
    "alles": _("alles"),
    "potenzenvonzahlen": _("potenzenvonzahlen"),
    "typ": _("typ"),
    "vielfachevonzahlen": _("vielfachevonzahlen"),
    "oberesmaximum": _("oberesmaximum"),
}

hauptForNeben: dict[str, str] = {
    "zeilen": _("zeilen"),
    "spalten": _("spalten"),
    "kombination": _("kombination"),
    "ausgabe": _("ausgabe"),
    "h": _("h"),
    "help": _("help"),
}


ausgabeArt: dict[str, str] = {
    "bbcode": _("bbcode"),
    "html": _("html"),
    "csv": _("csv"),
    "shell": _("shell"),
    "markdown": _("markdown"),
    "emacs": _("emacs"),
}


wahl15Words: dict[str, str] = {
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
    "Meta-Systeme_(12),Ordnung_und_Filterung_12_und_1pro12": _(
        "Meta-Systeme_(12),Ordnung_und_Filterung_12_und_1pro12"
    ),
    "Paradigmen_sind_Absichten_(13)": _("Paradigmen_sind_Absichten_(13)"),
    "Gedanken_sind_Positionen_(17)": _("Gedanken_sind_Positionen_(17)"),
    "Verbundenheiten_(18)": _("Verbundenheiten_(18)"),
    "Triebe_und_Bedürfnisse_(6)": _("Triebe_und_Bedürfnisse_(6)"),
    "Lust_(9)": _("Lust_(9)"),
    "Reflexe_(3),Existenzialien_(3)": _("Reflexe_(3),Existenzialien_(3)"),
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
    "Extremalien_(19),Ziele_(19)": _("Extremalien_(19),Ziele_(19)"),
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
}

wahl15: dict[str, str] = {
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
}

befehle: dict[str, str] = {"15" + a: "15" + a for a in wahl15.keys()} | {
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
    "procontra": _("procontra"),
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
    ":q": ":q",
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
}

ParametersMain: NamedTuple = namedtuple(
    "ParametersMain",
    "wichtigste wichtigste2 religionen galaxie strukturgroesse universum wirtschaft menschliches procontra licht bedeutung symbole Multiplikationen konzept konzept2 inkrementieren operationen universummetakonkret primzahlwirkung gebrochenuniversum gebrochengalaxie primvielfache planet strukturenkleinere grundstrukturen alles",
)

ParametersMain: NamedTuple = ParametersMain(
    {
        "Wichtigstes_zum_verstehen": _("Wichtigstes_zum_verstehen"),
        "wichtigsteverstehen": _("wichtigsteverstehen"),
    },
    {
        "Wichtigstes_zum_gedanklich_einordnen": _(
            "Wichtigstes_zum_gedanklich_einordnen"
        ),
        "wichtigsteeinordnen": _("wichtigsteeinordnen"),
    },
    {
        "Religionen": _("Religionen"),
        "religionen": _("religionen"),
        "religion": _("religion"),
    },
    {
        "Galaxie": _("Galaxie"),
        "galaxie": _("galaxie"),
        "alteschriften": _("alteschriften"),
        "kreis": _("kreis"),
        "galaxien": _("galaxien"),
        "kreise": _("kreise"),
    },
    {
        "Größenordnung": _("Größenordnung"),
        "groessenordnung": _("groessenordnung"),
        "strukturgroesse": _("strukturgroesse"),
        "strukturgroeße": _("strukturgroeße"),
        "strukturgrösse": _("strukturgrösse"),
        "strukturgröße": _("strukturgröße"),
        "groesse": _("groesse"),
        "stufe": _("stufe"),
        "organisationen": _("organisationen"),
    },
    {
        "Universum": _("Universum"),
        "universum": _("universum"),
        "transzendentalien": _("transzendentalien"),
        "strukturalien": _("strukturalien"),
        "kugel": _("kugel"),
        "kugeln": _("kugeln"),
        "ball": _("ball"),
        "baelle": _("baelle"),
        "bälle": _("bälle"),
    },
    {"Wirtschaft": _("Wirtschaft"), "wirtschaft": _("wirtschaft")},
    {
        "Menschliches": _("Menschliches"),
        "menschliches": _("menschliches"),
    },
    {
        "Pro_Contra": _("Pro_Contra"),
        "procontra": _("procontra"),
        "dagegendafuer": _("dagegendafuer"),
    },
    {
        "Licht": _("Licht"),
        "licht": _("licht"),
    },
    {
        "Bedeutung": _("Bedeutung"),
        "bedeutung": _("bedeutung"),
    },
    {
        "Symbole": _("Symbole"),
        "symbole": _("symbole"),
    },
    {a[0]: a[0] for a in Multiplikationen},
    {
        "Eigenschaften_n": _("Eigenschaften_n"),
        "eigenschaften": _("eigenschaften"),
        "eigenschaft": _("eigenschaft"),
        "konzept": _("konzept"),
        "konzepte": _("konzepte"),
    },
    {
        "Eigenschaften_1/n": _("Eigenschaften_1/n"),
        "konzept2": _("konzept2"),
        "konzepte2": _("konzepte2"),
    },
    {
        "Inkrementieren": _("Inkrementieren"),
        "inkrementieren": _("inkrementieren"),
    },
    {
        "Operationen": _("Operationen"),
        "operationen": _("operationen"),
    },
    {
        "Meta_vs_Konkret_(Universum)": _("Meta_vs_Konkret_(Universum)"),
        "universummetakonkret": _("universummetakonkret"),
    },
    {
        "Primzahlwirkung": _("Primzahlwirkung"),
        "primzahlwirkung": _("primzahlwirkung"),
    },
    {"gebrochenuniversum": _("gebrochenuniversum")},
    {"gebrochengalaxie": _("gebrochengalaxie")},
    {
        "Multiplikationen": _("Multiplikationen"),
        "multiplikationen": _("multiplikationen"),
    },
    {"Planet_(10_und_oder_12)": _("Planet_(10_und_oder_12)"), "planet": _("planet")},
    {
        "Strukturen_1_bis_9": _("Strukturen_1_bis_9"),
        "strukturkleinerzehn": _("strukturkleinerzehn"),
    },
    {"Grundstrukturen": _("Grundstrukturen"), "grundstrukturen": _("grundstrukturen")},
    {"alles": _("alles")},
)


paraNdataMatrix: list[Tuple[Any, dict[str, str], set[int], Optional[set]]] = [
    (
        ParametersMain.wichtigste,
        {
            "Wichtigste": _("Wichtigste"),
            "wichtigste": _("wichtigste"),
        },
        {10, 5, 4, 8},
    ),
    (
        ParametersMain.menschliches,
        {
            "Mensch-zu-Tier": _("Mensch-zu-Tier"),
            "menschtier": _("menschtier"),
            "tiermensch": _("tiermensch"),
        },
        {314},
    ),
    (
        ParametersMain.menschliches,
        {
            "Ansichten_Standpunkte_(18_17)": _("Ansichten_Standpunkte_(18_17)"),
            "ansichten": _("ansichten"),
        },
        {240, 346},
    ),
    (
        ParametersMain.menschliches,
        {
            "(politische)_Richtungen_(7)": _("(politische)_Richtungen_(7)"),
            "richtungen": _("richtungen"),
            "politische": _("politische"),
        },
        {235},
    ),
    (
        ParametersMain.planet,
        {
            "Wirklichkeiten_(10)": _("Wirklichkeiten_(10)"),
            "wirklichkeit": _("wirklichkeit"),
            "wirklichkeiten": _("wirklichkeiten"),
        },
        {233, 265, 268, 322},
    ),
    (
        ParametersMain.planet,
        {
            "Meta-Systeme_(12)": _("Meta-Systeme_(12)"),
            "metasysteme": _("metasysteme"),
            "metasystem": _("metasystem"),
            "meta-systeme": _("meta-systeme"),
            "meta-system": _("meta-system"),
        },
        {232, 288, 334},
    ),
    (
        ParametersMain.planet,
        {"Intelligenz": _("Intelligenz"), "intelligenz": _("intelligenz")},
        {214},
    ),
    (
        ParametersMain.planet,
        {
            "Gleichheit_Freiheit_Ordnung": _("Gleichheit_Freiheit_Ordnung"),
            "gleichheit": _("gleichheit"),
            "freiheit": _("freiheit"),
            "ordnung": _("ordnung"),
        },
        {132, 324, 328, 79, 80, 331, 335},
    ),
    (
        ParametersMain.planet,
        {
            "Komplexität": _("Komplexität"),
            "komplexität": _("komplexität"),
            "komplexitaet": _("komplexitaet"),
        },
        {213},
    ),
    (
        ParametersMain.planet,
        {
            "Mechanismen": _("Mechanismen"),
            "mechanismen": _("mechanismen"),
            "mechanismus": _("mechanismus"),
        },
        {107},
    ),
    (
        ParametersMain.wichtigste,
        {
            "Zweitwichtigste": _("Zweitwichtigste"),
            "zweitwichtigste": _("zweitwichtigste"),
        },
        {19, 65, 183},
        set(),
        set(),
        set(),
        {(10,)},
    ),
    (
        ParametersMain.wichtigste,
        {
            "Drittwichtigste": _("Drittwichtigste"),
            "drittwichtigste": _("drittwichtigste"),
        },
        {64},
    ),
    (
        ParametersMain.wichtigste,
        {
            "Motive_Sternpolygone": _("Motive_Sternpolygone"),
            "viertwichtigste": _("viertwichtigste"),
        },
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
        {"Wichtigste": _("Wichtigste"), "wichtigstes": _("wichtigstes")},
        {0, 1, 2, 36, 37, 207},
    ),
    (
        ParametersMain.wichtigste2,
        {
            "Zweitwichtigste": _("Zweitwichtigste"),
            "zweitwichtigste": _("zweitwichtigste"),
        },
        {30},
    ),
    (
        ParametersMain.operationen,
        {
            "Halbierung": _("Halbierung"),
            "halbierung": _("halbierung"),
            "halbierungen": _("halbierungen"),
        },
        {86},
    ),
    (
        ParametersMain.religionen,
        {
            "Religions-Gründer-Typ": _("Religions-Gründer-Typ"),
            "religionsgründertyp": _("religionsgründertyp"),
            "prophet": _("prophet"),
            "archon": _("archon"),
            "religionsgruendertyp": _("religionsgruendertyp"),
        },
        {72},
    ),
    (
        ParametersMain.religionen,
        {"Hinduismus": _("Hinduismus"), "hinduismus": _("hinduismus")},
        {217},
    ),
    (
        ParametersMain.religionen,
        {"Sternpolygon": _("Sternpolygon"), "sternpolygon": _("sternpolygon")},
        {0, 6, 36},
    ),
    (
        ParametersMain.religionen,
        {
            "der_Tierkreiszeichen": _("der_Tierkreiszeichen"),
            "dertierkreiszeichen": _("dertierkreiszeichen"),
            "babylon": _("babylon"),
        },
        {0, 36, 207},
    ),
    (
        ParametersMain.religionen,
        {
            "Sternpolygon_vs_gleichförmiges": _("Sternpolygon_vs_gleichförmiges"),
            "vergleich": _("vergleich"),
            "sternpolygonvsgleichfoermiges": _("sternpolygonvsgleichfoermiges"),
            "vergleichnvs1divn": _("vergleichnvs1divn"),
        },
        {87},
    ),
    (
        ParametersMain.religionen,
        {
            "Messias": _("Messias"),
            "messias": _("messias"),
            "heptagramm": _("heptagramm"),
            "hund": _("hund"),
            "messiase": _("messiase"),
            "messiasse": _("messiasse"),
        },
        {7},
    ),
    (
        ParametersMain.religionen,
        {
            "gleichförmiges_Polygon": _("gleichförmiges_Polygon"),
            "gleichförmigespolygon": _("gleichförmigespolygon"),
            "gleichfoermigespolygon": _("gleichfoermigespolygon"),
            "nichtsternpolygon": _("nichtsternpolygon"),
            "polygon": _("polygon"),
        },
        {16, 37},
    ),
    (
        ParametersMain.religionen,
        {
            "Vertreter_höherer_Konzepte": _("Vertreter_höherer_Konzepte"),
            "vertreterhoehererkonzepte": _("vertreterhoehererkonzepte"),
            "galaxien": _("galaxien"),
            "galaxie": _("galaxie"),
            "schwarzesonne": _("schwarzesonne"),
            "schwarzesonnen": _("schwarzesonnen"),
            "universum": _("universum"),
            "universen": _("universen"),
            "kreis": _("kreis"),
            "kreise": _("kreise"),
            "kugel": _("kugel"),
            "kugeln": _("kugeln"),
        },
        {23},
    ),
    (
        ParametersMain.galaxie,
        {
            "Offenbarung_des_Johannes": _("Offenbarung_des_Johannes"),
            "offenbarung": _("offenbarung"),
            "offenbarungdesjohannes": _("offenbarungdesjohannes"),
            "johannes": _("johannes"),
            "bibel": _("bibel"),
            "offenbarungjohannes": _("offenbarungjohannes"),
        },
        {90},
    ),
    (
        ParametersMain.inkrementieren,
        {
            "Teilchen-Meta-Physik": _("Teilchen-Meta-Physik"),
            "addition": _("addition"),
            "identitaet": _("identitaet"),
            "Identität": _("Identität"),
        },
        {219, 223, 307, 308, 333},
    ),
    (
        ParametersMain.galaxie,
        {
            "Hochzüchten": _("Hochzüchten"),
            "hochzüchten": _("hochzüchten"),
            "hochzuechten": _("hochzuechten"),
        },
        {318, 319},
    ),
    (
        ParametersMain.universum,
        {
            "Universelles_Verhältnis_gleicher_Zahlen": _(
                "Universelles_Verhältnis_gleicher_Zahlen"
            ),
            "verhaeltnisgleicherzahl": _("verhaeltnisgleicherzahl"),
        },
        {383},
    ),
    (
        ParametersMain.universum,
        {
            "universelles_Recht": _("universelles_Recht"),
            "recht": _("recht"),
            "jura": _("jura"),
        },
        {382, 34, 65},
    ),
    (
        ParametersMain.universum,
        {
            "sowas_wie_Kombinieren_Verknüpfen": _("sowas_wie_Kombinieren_Verknüpfen"),
            "kombinierenetc": _("kombinierenetc"),
        },
        {320},
    ),
    (
        ParametersMain.universum,
        {
            "Hochzüchten": _("Hochzüchten"),
            "hochzüchten": _("hochzüchten"),
            "hochzuechten": _("hochzuechten"),
        },
        {318, 319},
    ),
    (
        ParametersMain.universum,
        {
            "Teilchen-Meta-Physik": _("Teilchen-Meta-Physik"),
            "addition": _("addition"),
            "identitaet": _("identitaet"),
            "Identität": _("Identität"),
        },
        {219, 223, 307, 308, 333},
    ),
    (
        ParametersMain.universum,
        {
            "keine_Nur-Paradigma-Religionen": _("keine_Nur-Paradigma-Religionen"),
            "metaparadigmareligion": _("metaparadigmareligion"),
        },
        {190, 191, 196},
    ),
    (
        ParametersMain.universum,
        {
            "Kugeln_Kreise": _("Kugeln_Kreise"),
            "kugelnkreise": _("kugelnkreise"),
            "kugeln": _("kugeln"),
            "kreise": _("kreise"),
        },
        {77, 145},
    ),
    (
        ParametersMain.galaxie,
        {
            "Kugeln_Kreise": _("Kugeln_Kreise"),
            "kugelnkreise": _("kugelnkreise"),
            "kugeln": _("kugeln"),
            "kreise": _("kreise"),
        },
        {77, 145},
    ),
    (
        ParametersMain.galaxie,
        {
            "chinesisches_Horoskop": _("chinesisches_Horoskop"),
            "chinesischeshoroskop": _("chinesischeshoroskop"),
            "china": _("china"),
        },
        {91},
    ),
    (
        ParametersMain.galaxie,
        {
            "babylonische_Tierkreiszeichen": _("babylonische_Tierkreiszeichen"),
            "tierkreiszeichen": _("tierkreiszeichen"),
            "babylon": _("babylon"),
        },
        {1, 2},
    ),
    (
        ParametersMain.galaxie,
        {
            "Thomasevangelium": _("Thomasevangelium"),
            "thomasevangelium": _("thomasevangelium"),
            "thomas": _("thomas"),
        },
        {0, 3, 303},
    ),
    (
        ParametersMain.galaxie,
        {
            "analytische_Ontologie": _("analytische_Ontologie"),
            "analytischeontologie": _("analytischeontologie"),
            "ontologie": _("ontologie"),
        },
        {84},
    ),
    (
        ParametersMain.galaxie,
        {
            "Transzendentalien_innen_außen": _("Transzendentalien_innen_außen"),
            "innenaussenstrukur": _("innenaussenstrukur"),
            "strukturalieninnenaußen": _("strukturalieninnenaußen"),
            "strukturalieninnenaussen": _("strukturalieninnenaussen"),
            "innenaußenstrukur": _("innenaußenstrukur"),
            "transzendentalieninnenaußen": _("transzendentalieninnenaußen"),
            "transzendentalieninnenaussen": _("transzendentalieninnenaussen"),
        },
        {149},
    ),
    (
        ParametersMain.galaxie,
        {
            "Modallogik": _("Modallogik"),
            "modallogik": _("modallogik"),
        },
        {148},
    ),
    (
        ParametersMain.operationen,
        {
            "5": _("5"),
            "fünf": _("fünf"),
            "fünfer": _("fünfer"),
            "fünferstruktur": _("fünferstruktur"),
            "fuenf": _("fuenf"),
            "fuenfer": _("fuenfer"),
            "fuenferstruktur": _("fuenferstruktur"),
        },
        {96},
    ),
    (
        ParametersMain.operationen,
        {
            "9": _("9"),
            "neun": _("neun"),
            "neuner": _("neuner"),
            "neunerstruktur": _("neunerstruktur"),
        },
        {94},
    ),
    (
        ParametersMain.operationen,
        {
            "3": _("3"),
            "drei": _("drei"),
            "dreier": _("dreier"),
            "dreierstruktur": _("dreierstruktur"),
        },
        {92, 93, 315, 316},
    ),
    (
        ParametersMain.strukturgroesse,
        {
            "Licht": _("Licht"),
            "licht": _("licht"),
        },
        {20, 27, 313},
    ),
    (
        ParametersMain.strukturgroesse,
        {
            "Strukturgrösse": _("Strukturgrösse"),
            "größe": _("größe"),
            "groesse": _("groesse"),
            "gross": _("gross"),
            "strukturgroesse": _("strukturgroesse"),
            "strukturgroeße": _("strukturgroeße"),
            "strukturgrösse": _("strukturgrösse"),
            "strukturgröße": _("strukturgröße"),
        },
        {4, 21, 54, 197},
    ),
    (
        ParametersMain.strukturgroesse,
        {
            "Organisationen": _("Organisationen"),
            "organisationen": _("organisationen"),
            "organisation": _("organisation"),
        },
        {30, 82},
    ),
    (
        ParametersMain.strukturgroesse,
        {
            "politische_Systeme": _("politische_Systeme"),
            "politischesysteme": _("politischesysteme"),
            "politik": _("politik"),
        },
        {83},
    ),
    (
        ParametersMain.universummetakonkret,
        {"meta": _("meta")},
        set(),
        set(),
        set(),
        set(),
        {
            (
                2,
                0,
            )
        },
    ),
    (
        ParametersMain.universummetakonkret,
        {"konkret": _("konkret")},
        set(),
        set(),
        set(),
        set(),
        {
            (
                2,
                1,
            )
        },
    ),
    (
        ParametersMain.universummetakonkret,
        {"Theorie": _("Theorie"), "theorie": _("theorie")},
        set(),
        set(),
        set(),
        set(),
        {
            (
                3,
                0,
            )
        },
    ),
    (
        ParametersMain.universummetakonkret,
        {"Praxis": _("Praxis"), "praxis": _("praxis")},
        set(),
        set(),
        set(),
        set(),
        {
            (
                3,
                1,
            )
        },
    ),
    (
        ParametersMain.universummetakonkret,
        {
            "Management": _("Management"),
            "management": _("management"),
            "stau": _("stau"),
        },
        set(),
        set(),
        set(),
        set(),
        {
            (
                4,
                0,
            )
        },
    ),
    (
        ParametersMain.universummetakonkret,
        {
            "verändernd": _("verändernd"),
            "veraendernd": _("veraendernd"),
            "fluss": _("fluss"),
        },
        set(),
        set(),
        set(),
        set(),
        {
            (
                4,
                1,
            )
        },
    ),
    (
        ParametersMain.universummetakonkret,
        {
            "ganzheitlich": _("ganzheitlich"),
            "mathematisch_diskret": _("mathematisch_diskret"),
            "diskret": _("diskret"),
        },
        set(),
        set(),
        set(),
        set(),
        {
            (
                5,
                0,
            )
        },
    ),
    (
        ParametersMain.universummetakonkret,
        {
            "darüber_hinausgehend": _("darüber_hinausgehend"),
            "hinausgehend": _("hinausgehend"),
            "kontinuierlich": _("kontinuierlich"),
        },
        set(),
        set(),
        set(),
        set(),
        {
            (
                5,
                1,
            )
        },
    ),
    (
        ParametersMain.primzahlwirkung,
        {
            "Universum_Strukturalien_Transzendentalien": _(
                "Universum_Strukturalien_Transzendentalien"
            ),
            "universum": _("universum"),
            "strukturalie": _("strukturalie"),
            "strukturalien": _("strukturalien"),
            "transzendentalien": _("transzendentalien"),
            "transzendentalie": _("transzendentalie"),
        },
        set(),
        set(),
        set(),
        set(),
        {(5,)},
    ),
    (
        ParametersMain.primzahlwirkung,
        {
            "Richtung_als_Richtung": _("Richtung_als_Richtung"),
            "richtungrichtung": _("richtungrichtung"),
        },
        set(),
        set(),
        set(),
        set(),
        {(None,)},
    ),
    (
        ParametersMain.primzahlwirkung,
        {
            "Galaxieabsicht": _("Galaxieabsicht"),
            "absichtgalaxie": _("absichtgalaxie"),
            "absicht": _("absicht"),
            "motive": _("motive"),
            "motiv": _("motiv"),
            "absichten": _("absichten"),
            "galaxie": _("galaxie"),
        },
        set(),
        set(),
        set(),
        set(),
        {(10,)},
    ),
    (
        ParametersMain.primzahlwirkung,
        {
            "Absicht_Reziproke_Galaxie": _("Absicht_Reziproke_Galaxie"),
            "absichtgalaxiereziproke": _("absichtgalaxiereziproke"),
            "absichtreziproke": _("absichtreziproke"),
            "motivereziproke": _("motivereziproke"),
            "motivreziproke": _("motivreziproke"),
            "absichtenreziproke": _("absichtenreziproke"),
            "galaxiereziproke": _("galaxiereziproke"),
        },
        set(),
        set(),
        set(),
        set(),
        {(42,)},
    ),
    (
        ParametersMain.primzahlwirkung,
        {
            "Universum_Reziproke": _("Universum_Reziproke"),
            "universumreziproke": _("universumreziproke"),
            "strukturaliereziproke": _("strukturaliereziproke"),
            "strukturalienreziproke": _("strukturalienreziproke"),
            "transzendentalienreziproke": _("transzendentalienreziproke"),
            "transzendentaliereziproke": _("transzendentaliereziproke"),
        },
        set(),
        set(),
        set(),
        set(),
        {(131,)},
    ),
    (
        ParametersMain.primzahlwirkung,
        {
            "Dagegen-Gegentranszendentalie": _("Dagegen-Gegentranszendentalie"),
            "dagegengegentranszendentalie": _("dagegengegentranszendentalie"),
            "dagegengegentranszendentalien": _("dagegengegentranszendentalien"),
            "dagegengegenstrukturalien": _("dagegengegenstrukturalien"),
            "dagegengegenstrukturalie": _("dagegengegenstrukturalie"),
        },
        set(),
        set(),
        set(),
        set(),
        {(138,)},
    ),
    (
        ParametersMain.primzahlwirkung,
        {
            "neutrale_Gegentranszendentalie": _("neutrale_Gegentranszendentalie"),
            "neutralegegentranszendentalie": _("neutralegegentranszendentalie"),
            "neutralegegentranszendentalien": _("neutralegegentranszendentalien"),
            "neutralegegenstrukturalien": _("neutralegegenstrukturalien"),
            "neutralegegenstrukturalie": _("neutralegegenstrukturalie"),
        },
        set(),
        set(),
        set(),
        set(),
        {(202,)},
    ),
    (
        ParametersMain.universummetakonkret,
        {
            "Unternehmung_Geschäft": _("Unternehmung_Geschäft"),
            "unternehmen": _("unternehmen"),
            "unternehmung": _("unternehmung"),
            "geschaeft": _("geschaeft"),
            "geschäft": _("geschäft"),
        },
        set(),
        set(),
        set(),
        set(),
        {
            (
                6,
                0,
            )
        },
    ),
    (
        ParametersMain.universummetakonkret,
        {"wertvoll": _("wertvoll"), "wert": _("wert")},
        set(),
        set(),
        set(),
        set(),
        {
            (
                6,
                1,
            )
        },
    ),
    (
        ParametersMain.universummetakonkret,
        {
            "Beherrschen": _("Beherrschen"),
            "regieren": _("regieren"),
            "beherrschen": _("beherrschen"),
        },
        set(),
        set(),
        set(),
        set(),
        {
            (
                7,
                0,
            )
        },
    ),
    (
        ParametersMain.universummetakonkret,
        {
            "Richtung": _("Richtung"),
            "richtung": _("richtung"),
            "gut": _("gut"),
        },
        set(),
        set(),
        set(),
        set(),
        {
            (
                7,
                1,
            )
        },
    ),
    (
        ParametersMain.universum,
        {
            "analytische_Ontologie": _("analytische_Ontologie"),
            "analytischeontologie": _("analytischeontologie"),
            "ontologie": _("ontologie"),
        },
        {84},
    ),
    (
        ParametersMain.universum,
        {
            "Gegentranszendentalien": _("Gegentranszendentalien"),
            "gegentranszendentalien": _("gegentranszendentalien"),
            "gegentranszendentalie": _("gegentranszendentalie"),
            "gegenstrukturalien": _("gegenstrukturalien"),
            "gegenalien": _("gegenalien"),
            "gegenuniversalien": _("gegenuniversalien"),
        },
        {138, 202},
    ),
    (
        ParametersMain.universum,
        {"Systemsachen": _("Systemsachen"), "systemsachen": _("systemsachen")},
        {
            150,
        },
    ),
    (
        ParametersMain.universum,
        {
            "Transzendentalien": _("Transzendentalien"),
            "transzendentalien": _("transzendentalien"),
            "transzendentalie": _("transzendentalie"),
            "strukturalien": _("strukturalien"),
            "alien": _("alien"),
            "universalien": _("universalien"),
        },
        {5, 54, 55, 198},
    ),
    (
        ParametersMain.universum,
        {
            "Reziproke_von_Transzendentalien": _("Reziproke_von_Transzendentalien"),
            "transzendentalienreziproke": _("transzendentalienreziproke"),
            "transzendentaliereziproke": _("transzendentaliereziproke"),
            "strukturalienreziproke": _("strukturalienreziproke"),
            "alienreziproke": _("alienreziproke"),
            "universalienreziproke": _("universalienreziproke"),
        },
        {131, 201},
    ),
    (
        ParametersMain.universum,
        {"Netzwerk": _("Netzwerk"), "netzwerk": _("netzwerk")},
        {25},
    ),
    (
        ParametersMain.universum,
        {
            "warum_Transzendentalie_=_Strukturgroesse_=_Charakter": _(
                "warum_Transzendentalie_=_Strukturgroesse_=_Charakter"
            ),
            "warumtranszendentaliezustrukturgroesseundcharakter": _(
                "warumtranszendentaliezustrukturgroesseundcharakter"
            ),
        },
        {4, 54, 5, 165},
    ),
    (
        ParametersMain.universum,
        {"Kategorie": _("Kategorie"), "kategorie": _("kategorie")},
        {204, 205, 281},
    ),
    (
        ParametersMain.universum,
        {"Raum-Missionen": _("Raum-Missionen"), "weltall": _("weltall")},
        {218},
    ),
    (
        ParametersMain.universum,
        {
            "Programmier-Paradigmen": _("Programmier-Paradigmen"),
            "programmierparadigmen": _("programmierparadigmen"),
        },
        {351},
    ),
    (
        ParametersMain.galaxie,
        {"Raum-Missionen": _("Raum-Missionen"), "weltall": _("weltall")},
        {218},
    ),
    (
        ParametersMain.universum,
        {"Geist__(15)": _("Geist__(15)"), "geist": _("geist")},
        {242},
    ),
    (
        ParametersMain.universum,
        {
            "warum_Transzendentalie_=_Komplexität_von_Michael_Commons": _(
                "warum_Transzendentalie_=_Komplexität_von_Michael_Commons"
            ),
            "warumtranszendentaliegleichkomplexitaet": _(
                "warumtranszendentaliegleichkomplexitaet"
            ),
        },
        {65, 5, 166},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Model_of_Hierarchical_Complexity": _("Model_of_Hierarchical_Complexity"),
            "modelofhierarchicalcomplexity": _("modelofhierarchicalcomplexity"),
            "komplex": _("komplex"),
            "komplexität": _("komplexität"),
            "komplexitaet": _("komplexitaet"),
            "complexity": _("complexity"),
            "model": _("model"),
            "abstraktion": _("abstraktion"),
        },
        {65, 75, 203},
    ),
    (
        ParametersMain.universum,
        {
            "Model_of_Hierarchical_Complexity": _("Model_of_Hierarchical_Complexity"),
            "modelofhierarchicalcomplexity": _("modelofhierarchicalcomplexity"),
            "komplex": _("komplex"),
            "komplexität": _("komplexität"),
            "komplexitaet": _("komplexitaet"),
            "complexity": _("complexity"),
            "model": _("model"),
            "abstraktion": _("abstraktion"),
        },
        {65, 75, 203},
    ),
    (
        ParametersMain.operationen,
        {
            "2": _("2"),
            "zwei": _("zwei"),
            "gerade": _("gerade"),
            "ungerade": _("ungerade"),
            "alternierung": _("alternierung"),
            "alternierend": _("alternierend"),
            "zweierstruktur": _("zweierstruktur"),
        },
        {78, 79, 80, 331},
    ),
    (
        ParametersMain.operationen,
        {
            "Multiplikation": _("Multiplikation"),
            "multiplikation": _("multiplikation"),
        },
        {158},
    ),
    (
        ParametersMain.operationen,
        {
            "4": _("4"),
            "vier": _("vier"),
            "viererstruktur": _("viererstruktur"),
            "viererabfolgen": _("viererabfolgen"),
        },
        {76, 77, 81, 104, 145},
    ),
    (
        ParametersMain.menschliches,
        {
            "Gesellschaftsschicht": _("Gesellschaftsschicht"),
            "klasse": _("klasse"),
            "klassen": _("klassen"),
        },
        {241},
    ),
    (
        ParametersMain.menschliches,
        {"Moral": _("Moral"), "moral": _("moral"), "warummoral": _("warummoral")},
        {215, 216},
        {(216, 221)},
    ),
    (
        ParametersMain.menschliches,
        {
            "Fachgebiete": _("Fachgebiete"),
            "fachgebiete": _("fachgebiete"),
            "fachbereiche": _("fachbereiche"),
            "themen": _("themen"),
        },
        {183},
    ),
    (
        ParametersMain.wirtschaft,
        {
            "Fachgebiete": _("Fachgebiete"),
            "fachgebiete": _("fachgebiete"),
            "fachbereiche": _("fachbereiche"),
            "themen": _("themen"),
        },
        {183},
    ),
    (
        ParametersMain.wirtschaft,
        {
            "Pflanzen": _("Pflanzen"),
            "pflanzen": _("pflanzen"),
        },
        {113},
    ),
    (
        ParametersMain.wirtschaft,
        {
            "Maschinen": _("Maschinen"),
            "maschinen": _("maschinen"),
            "maschine": _("maschine"),
            "gerät": _("gerät"),
            "geräte": _("geräte"),
            "geraete": _("geraete"),
            "geraet": _("geraet"),
        },
        {89},
    ),
    (
        ParametersMain.wirtschaft,
        {
            "Organisationsform": _("Organisationsform"),
            "organisationsform": _("organisationsform"),
            "organisationsart": _("organisationsart"),
            "firma": _("firma"),
            "verein": _("verein"),
        },
        {99},
    ),
    (
        ParametersMain.wirtschaft,
        {
            "System": _("System"),
            "system": _("system"),
        },
        {
            69,
        },
    ),
    (
        ParametersMain.wirtschaft,
        {
            "realistisch": _("realistisch"),
            "funktioniert": _("funktioniert"),
        },
        {70},
    ),
    (
        ParametersMain.wirtschaft,
        {
            "Erklärung": _("Erklärung"),
            "erklärung": _("erklärung"),
            "erklaerung": _("erklaerung"),
        },
        {71},
    ),
    (
        ParametersMain.wirtschaft,
        {
            "BWL": _("BWL"),
            "bwl": _("bwl"),
        },
        {109},
    ),
    (
        ParametersMain.menschliches,
        {
            "Sinn_des_Lebens": _("Sinn_des_Lebens"),
            "sinndeslebens": _("sinndeslebens"),
            "lebenssinn": _("lebenssinn"),
            "sinn": _("sinn"),
            "sinnsuche": _("sinnsuche"),
        },
        {88, 189},
        {(181, 182)},
    ),
    (
        ParametersMain.menschliches,
        {
            "Intelligenzprobleme": _("Intelligenzprobleme"),
            "intelligenzprobleme": _("intelligenzprobleme"),
            "intelligenzmaengel": _("intelligenzmaengel"),
            "intelligenzmängel": _("intelligenzmängel"),
        },
        {147},
    ),
    (
        ParametersMain.menschliches,
        {
            "Denkweise_von_Lebewesen": _("Denkweise_von_Lebewesen"),
            "lebewesendenkweise": _("lebewesendenkweise"),
            "denkweise": _("denkweise"),
        },
        {146},
    ),
    (
        ParametersMain.menschliches,
        {
            "Gegentranszendentalien": _("Gegentranszendentalien"),
            "gegentranszendentalien": _("gegentranszendentalien"),
            "gegenstrukturalien": _("gegenstrukturalien"),
        },
        {138, 139, 202},
    ),
    (
        ParametersMain.menschliches,
        {
            "Gleichheit_Freiheit": _("Gleichheit_Freiheit"),
            "gleichheitfreiheit": _("gleichheitfreiheit"),
            "ungleichheit": _("ungleichheit"),
            "dominieren": _("dominieren"),
            "gleichheit": _("gleichheit"),
            "freiheit": _("freiheit"),
        },
        {132, 328, 331, 335},
    ),
    (
        ParametersMain.menschliches,
        {
            "Gefühle": _("Gefühle"),
            "emotionen": _("emotionen"),
            "gefuehle": _("gefuehle"),
            "emotion": _("emotion"),
            "gefühl": _("gefühl"),
            "gefuehl": _("gefuehl"),
        },
        {105, 230, 243, 283, 284, 285, 286, 305},
    ),
    (
        ParametersMain.menschliches,
        {
            "Egoismus": _("Egoismus"),
            "egoismus": _("egoismus"),
            "altruismus": _("altruismus"),
            "selbstlosigkeit": _("selbstlosigkeit"),
        },
        {136},
        {(66, 67)},
    ),
    (
        ParametersMain.menschliches,
        {
            "Wirkung": _("Wirkung"),
            "wirkung": _("wirkung"),
        },
        {135},
    ),
    (
        ParametersMain.menschliches,
        {
            "INCELs": _("INCELs"),
            "incel": _("incel"),
            "incels": _("incels"),
        },
        {68},
    ),
    (
        ParametersMain.menschliches,
        {
            "irrationale_Zahlen_durch_Wurzelbildung": _(
                "irrationale_Zahlen_durch_Wurzelbildung"
            ),
            "irrationalezahlendurchwurzelbildung": _(
                "irrationalezahlendurchwurzelbildung"
            ),
            "ausgangslage": _("ausgangslage"),
        },
        {73},
    ),
    (
        ParametersMain.menschliches,
        {
            "dominierendes_Geschlecht": _("dominierendes_Geschlecht"),
            "dominierendesgeschlecht": _("dominierendesgeschlecht"),
            "maennlich": _("maennlich"),
            "männlich": _("männlich"),
            "weiblich": _("weiblich"),
        },
        {51},
    ),
    (
        ParametersMain.menschliches,
        {
            "Liebe": _("Liebe"),
            "liebe": _("liebe"),
            "ethik": _("ethik"),
        },
        {8, 9, 28, 208, 330},
        {(121, 122)},
    ),
    (
        ParametersMain.menschliches,
        {
            "Glaube_Erkenntnis": _("Glaube_Erkenntnis"),
            "glauben": _("glauben"),
            "erkenntnis": _("erkenntnis"),
            "glaube": _("glaube"),
        },
        {59},
    ),
    (
        ParametersMain.menschliches,
        {
            "Angreifbarkeit": _("Angreifbarkeit"),
            "angreifbarkeit": _("angreifbarkeit"),
            "angreifbar": _("angreifbar"),
        },
        {58, 57},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Strukturalien_bzw_Meta-Paradigmen_bzw_Transzendentalien_(15)": _(
                "Strukturalien_bzw_Meta-Paradigmen_bzw_Transzendentalien_(15)"
            ),
            "Transzendentalien": _("Transzendentalien"),
            "transzendentalien": _("transzendentalien"),
            "transzendentalie": _("transzendentalie"),
            "strukturalien": _("strukturalien"),
            "alien": _("alien"),
            "universalien": _("universalien"),
            "meta-paradigmen": _("meta-paradigmen"),
        },
        {5, 229, 131},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Bedingung_und_Auslöser_(1/3)": _("Bedingung_und_Auslöser_(1/3)"),
            "bedingung": _("bedingung"),
            "bedingungen": _("bedingungen"),
            "auslöser": _("auslöser"),
            "ausloeser": _("ausloeser"),
        },
        {338},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Relation_zueinander_reziprok_Universellen_(18→n_vs._1/n)": _(
                "Relation_zueinander_reziprok_Universellen_(18→n_vs._1/n)"
            ),
            "relativreziprokuniversell": _("relativreziprokuniversell"),
        },
        {350},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "universeller_Komperativ_(18→15)": _("universeller_Komperativ_(18→15)"),
            "universellerkomperativ": _("universellerkomperativ"),
        },
        {349},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Existenzialien_(3)": _("Existenzialien_(3)"),
            "existenzialien": _("existenzialien"),
        },
        {348},
    ),
    (
        ParametersMain.grundstrukturen,
        {"Extremalien_(19)": _("Extremalien_(19)"), "extremalien": _("extremalien")},
        {347, 352},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Erwartungshaltungen_(26)": _("Erwartungshaltungen_(26)"),
            "erwartungen": _("erwartungen"),
            "erwartungshaltungen": _("erwartungshaltungen"),
        },
        {344},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Leidenschaften_(21)": _("Leidenschaften_(21)"),
            "leidenschaft": _("leidenschaft"),
            "leidenschaften": _("leidenschaften"),
        },
        {343},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "relativer_Zeit-Betrag_(15_10_4_18_6)": _(
                "relativer_Zeit-Betrag_(15_10_4_18_6)"
            ),
            "relativerzeitbetrag": _("relativerzeitbetrag"),
        },
        {339},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Zahlenvergleich_(15_18_6)": _("Zahlenvergleich_(15_18_6)"),
            "zahlenvergleich": _("zahlenvergleich"),
        },
        {340},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Bestrebungen(1/5)": _("Bestrebungen(1/5)"),
            "bestrebung": _("bestrebung"),
            "bestrebungen": _("bestrebungen"),
        },
        {332},
    ),
    (
        ParametersMain.grundstrukturen,
        {"Prinzipien(1/8)": _("Prinzipien(1/8)"), "prinzipien": _("prinzipien")},
        {329, 378},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Attraktionen_(36)": _("Attraktionen_(36)"),
            "attraktionen": _("attraktionen"),
        },
        {311},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Optimierung_(10)": _("Optimierung_(10)"),
            "optimierung": _("optimierung"),
        },
        {310},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Themen_(6)": _("Themen_(6)"),
            "themen": _("themen"),
            "thema": _("thema"),
        },
        {309},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Bedeutung_(10)": _("Bedeutung_(10)"),
            "bedeutung": _("bedeutung"),
        },
        {306},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Reziprokes": _("Reziprokes"),
            "reziproke": _("reziproke"),
            "reziprokes": _("reziprokes"),
        },
        {
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
        },
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Achtung_(4)": _("Achtung_(4)"),
            "achtung": _("achtung"),
            "achten": _("achten"),
        },
        {270},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Zeit_(4)_als_Wirklichkeit": _("Zeit_(4)_als_Wirklichkeit"),
            "zeit": _("zeit"),
        },
        {266, 267},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Absicht_16_ist_zu_genügen": _("Absicht_16_ist_zu_genügen"),
            "absicht16": _("absicht16"),
        },
        {312},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Absicht_17_ist_zu_meinen": _("Absicht_17_ist_zu_meinen"),
            "absicht17": _("absicht17"),
        },
        {263},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Absicht_6_ist_Vorteilsmaximierung": _("Absicht_6_ist_Vorteilsmaximierung"),
            "absicht6": _("absicht6"),
        },
        {262},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Absicht_7_ist_Selbstlosigkeit": _("Absicht_7_ist_Selbstlosigkeit"),
            "absicht7": _("absicht7"),
        },
        {261},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Regungen_(1)": _("Regungen_(1)"),
            "regung": _("regung"),
            "regungen": _("regungen"),
        },
        {282},
    ),
    (
        ParametersMain.grundstrukturen,
        {"Verhalten_(11)": _("Verhalten_(11)"), "verhalten": _("verhalten")},
        {301, 302},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Energie_und_universelle_Eigenschaften_(30)": _(
                "Energie_und_universelle_Eigenschaften_(30)"
            ),
            "energie": _("energie"),
            "universelleeigenschaften": _("universelleeigenschaften"),
            "lebensenergie": _("lebensenergie"),
        },
        {287, 293},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Garben_und_Verhalten_nachfühlen(31)": _(
                "Garben_und_Verhalten_nachfühlen(31)"
            ),
            "garben": _("garben"),
            "verhaltenfuehlen": _("verhaltenfuehlen"),
            "verhaltenfühlen": _("verhaltenfühlen"),
        },
        {295},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            Primzahlkreuz_pro_contra_strs[1]: Primzahlkreuz_pro_contra_strs_Fkt[1],
            "nachvollziehen": _("nachvollziehen"),
        },
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
        {
            "Empathie_(37)": _("Empathie_(37)"),
            "empathie": _("empathie"),
            "mitgefuehl": _("mitgefuehl"),
        },
        {294},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Absicht_1/6_ist_Reinigung_und_Klarheit": _(
                "Absicht_1/6_ist_Reinigung_und_Klarheit"
            ),
            "absicht1/6": _("absicht1/6"),
            "absicht1pro6": _("absicht1pro6"),
        },
        {298},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Absicht_10_ist_Wirklichkeit_erkennen": _(
                "Absicht_10_ist_Wirklichkeit_erkennen"
            ),
            "absicht10": _("absicht10"),
        },
        {260},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Geist_(15)": _("Geist_(15)"),
            "geist": _("geist"),
            "bewusstsein": _("bewusstsein"),
        },
        {229, 231, 242, 273, 297, 304},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Reflexe_(3)": _("Reflexe_(3)"),
            "reflex": _("reflex"),
            "reflexe": _("reflexe"),
        },
        {256},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Lust_(9)": _("Lust_(9)"),
            "lust": _("lust"),
        },
        {255},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Paradigmen_sind_Absichten_(13)": _("Paradigmen_sind_Absichten_(13)"),
            "paradigmen": _("paradigmen"),
            "absichten": _("absichten"),
        },
        {10, 42},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Wirklichkeiten_Wahrheit_Wahrnehmung_(10)": _(
                "Wirklichkeiten_Wahrheit_Wahrnehmung_(10)"
            ),
            "wirklichkeit": _("wirklichkeit"),
            "wirklichkeiten": _("wirklichkeiten"),
            "wahrheit": _("wahrheit"),
            "wahrnehmung": _("wahrnehmung"),
        },
        {233, 265, 268, 322, 342},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Stimmungen_Kombinationen_(14)": _("Stimmungen_Kombinationen_(14)"),
            "stimmung": _("stimmung"),
            "stimmungen": _("stimmungen"),
            "kombination": _("kombination"),
            "kombinationen": _("kombinationen"),
        },
        {290, 296, 325, 326, 327},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Klassen_(20)": _("Klassen_(20)"),
            "klasse": _("klasse"),
            "klassen": _("klassen"),
        },
        {241, 289},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Ordnung_und_Filterung_12_und_1pro12": _(
                "Ordnung_und_Filterung_12_und_1pro12"
            ),
            "ordnen": _("ordnen"),
            "ordnenundfiltern": _("ordnenundfiltern"),
            "filtern": _("filtern"),
        },
        {132, 328, 331, 335},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Meta-Systeme_(12)": _("Meta-Systeme_(12)"),
            "metasysteme": _("metasysteme"),
            "metasystem": _("metasystem"),
            "meta-systeme": _("meta-systeme"),
            "meta-system": _("meta-system"),
            "menge": _("menge"),
            "mengen": _("mengen"),
        },
        {232, 288, 334},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Absicht_1/8": _("Absicht_1/8"),
            "absicht1pro8": _("absicht1pro8"),
            "absicht1/8": _("absicht1/8"),
        },
        {272, 379},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Ziele_(19)": _("Ziele_(19)"),
            "ziele": _("ziele"),
            "maxima": _("maxima"),
            "höhenvorstellungen": _("höhenvorstellungen"),
        },
        {271},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Konkreta_und_Focus_(2)": _("Konkreta_und_Focus_(2)"),
            "konkreta": _("konkreta"),
            "focus": _("focus"),
            "fokus": _("fokus"),
        },
        {250, 269},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Gefühle_(7)": _("Gefühle_(7)"),
            "gefuehle": _("gefuehle"),
            "emotionen": _("emotionen"),
            "gefühle": _("gefühle"),
        },
        {243, 283, 284, 285, 286, 305},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "abhängige_Verbundenheit_(90)": _("abhängige_Verbundenheit_(90)"),
            "abhaengigkeit": _("abhaengigkeit"),
            "abhängigkeit": _("abhängigkeit"),
        },
        {357},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Karte_Filter_und_Unterscheidung_(1/12)": _(
                "Karte_Filter_und_Unterscheidung_(1/12)"
            ),
            "karte": _("karte"),
            "filter": _("filter"),
            "unterscheidung": _("unterscheidung"),
        },
        {377},
    ),
    (
        ParametersMain.grundstrukturen,
        {"Fundament_(1/19)": _("Fundament_(1/19)"), "fundament": _("fundament")},
        {356},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Gedanken_sind_Positionen_(17)": _("Gedanken_sind_Positionen_(17)"),
            "positionen": _("positionen"),
            "gedanken": _("gedanken"),
        },
        {249, 317, 323},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Funktionen_Vorstellungen_(16)": _("Funktionen_Vorstellungen_(16)"),
            "vorstellungen": _("vorstellungen"),
            "vorstellung": _("vorstellung"),
            "funktionen": _("funktionen"),
        },
        {345, 264},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Sollen_Frage_Vorgehensweise_(1/13)": _(
                "Sollen_Frage_Vorgehensweise_(1/13)"
            ),
            "sollen": _("sollen"),
            "frage": _("frage"),
            "vorgehensweise": _("vorgehensweise"),
        },
        {353, 354},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Ansichten_Standpunkte_(18_17)": _("Ansichten_Standpunkte_(18_17)"),
            "ansichten": _("ansichten"),
        },
        {240, 346},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Verbundenheiten_(18)": _("Verbundenheiten_(18)"),
            "verbundenheiten": _("verbundenheiten"),
        },
        {252, 299, 300, 336},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Absicht_13_ist_Helfen": _("Absicht_13_ist_Helfen"),
            "absicht13": _("absicht13"),
            "helfen": _("helfen"),
        },
        {370},
    ),
    (
        ParametersMain.grundstrukturen,
        {"Liebe_(7)": _("Liebe_(7)"), "liebe": _("liebe")},
        {8, 9, 28, 208, 221, 330},
        {(121, 122)},
    ),
    (
        ParametersMain.grundstrukturen,
        {"Koalitionen_(10)": _("Koalitionen_(10)"), "koalitionen": _("koalitionen")},
        {321},
    ),
    (
        ParametersMain.grundstrukturen,
        {"Impulse_(5)": _("Impulse_(5)"), "impulse": _("impulse")},
        {251, 253, 257, 341},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Triebe_und_Bedürfnisse_(6)": _("Triebe_und_Bedürfnisse_(6)"),
            "trieb": _("trieb"),
            "triebe": _("triebe"),
            "bedürfnis": _("bedürfnis"),
            "bedürfnisse": _("bedürfnisse"),
        },
        {254},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Reflektion_und_Kategorien_(1/15)": _("Reflektion_und_Kategorien_(1/15)"),
            "reflektion": _("reflektion"),
            "kategorien": _("kategorien"),
        },
        {204, 205, 281},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Modus_und_Sein_(8)": _("Modus_und_Sein_(8)"),
            "zustaende": _("zustaende"),
            "zustände": _("zustände"),
            "modus": _("modus"),
            "modi": _("modi"),
            "sein": _("sein"),
        },
        {234, 337},
    ),
    (
        ParametersMain.menschliches,
        {
            "Motive": _("Motive"),
            "motive": _("motive"),
            "motivation": _("motivation"),
            "motiv": _("motiv"),
            "absicht": _("absicht"),
            "absichten": _("absichten"),
        },
        {10, 18, 42, 167, 168, 149, 229, 230},
    ),
    (
        ParametersMain.menschliches,
        {
            "Gedanken_sind_Positionen_(17)": _("Gedanken_sind_Positionen_(17)"),
            "positionen": _("positionen"),
            "gedanken": _("gedanken"),
        },
        {249, 276},
    ),
    (
        ParametersMain.menschliches,
        {
            "Bewusstsein_und_Wahrnehmung": _("Bewusstsein_und_Wahrnehmung"),
            "bewusstsein": _("bewusstsein"),
            "wahrnehmung": _("wahrnehmung"),
        },
        {265, 229, 231, 281, 304, 342},
    ),
    (
        ParametersMain.menschliches,
        {
            "Errungenschaften": _("Errungenschaften"),
            "errungenschaften": _("errungenschaften"),
            "ziele": _("ziele"),
            "erhalten": _("erhalten"),
        },
        {11, 257, 251},
    ),
    (
        ParametersMain.menschliches,
        {
            "evolutionär_erwerben_und_Intelligenz_Kreativität": _(
                "evolutionär_erwerben_und_Intelligenz_Kreativität"
            ),
            "evolutionärerwerbenundintelligenz": _("evolutionärerwerbenundintelligenz"),
            "intelligenz": _("intelligenz"),
            "erwerben": _("erwerben"),
            "erlernen": _("erlernen"),
            "lernen": _("lernen"),
            "evolutionaer": _("evolutionaer"),
            "evolutionär": _("evolutionär"),
            "kreativität": _("kreativität"),
            "kreativitaet": _("kreativitaet"),
            "kreativ": _("kreativ"),
        },
        {12, 47, 27, 13, 32},
    ),
    (
        ParametersMain.menschliches,
        {
            "brauchen": _("brauchen"),
            "benoetigen": _("benoetigen"),
            "benötigen": _("benötigen"),
            "notwendig": _("notwendig"),
        },
        {13, 14},
    ),
    (
        ParametersMain.menschliches,
        {
            "Krankheit": _("Krankheit"),
            "krankheit": _("krankheit"),
            "krankheiten": _("krankheiten"),
            "pathologisch": _("pathologisch"),
            "pathologie": _("pathologie"),
            "psychiatrisch": _("psychiatrisch"),
        },
        {24},
    ),
    (
        ParametersMain.menschliches,
        {
            "alpha_beta": _("alpha_beta"),
            "alphabeta": _("alphabeta"),
            "alpha": _("alpha"),
            "beta": _("beta"),
            "omega": _("omega"),
            "sigma": _("sigma"),
        },
        {46},
    ),
    (
        ParametersMain.menschliches,
        {
            "Anführer": _("Anführer"),
            "anfuehrer": _("anfuehrer"),
            "chef": _("chef"),
        },
        {29, 170},
    ),
    (
        ParametersMain.menschliches,
        {
            "Manipulation": _("Manipulation"),
            "manipulation": _("manipulation"),
        },
        {153},
    ),
    (
        ParametersMain.menschliches,
        {
            "Berufe": _("Berufe"),
            "berufe": _("berufe"),
            "beruf": _("beruf"),
        },
        {30},
    ),
    (
        ParametersMain.menschliches,
        {
            "Lösungen": _("Lösungen"),
            "lösungen": _("lösungen"),
            "loesungen": _("loesungen"),
            "loesung": _("loesung"),
            "lösungen": _("lösungen"),
        },
        {31},
    ),
    (ParametersMain.menschliches, {"Musik": _("Musik"), "musik": _("musik")}, {33}),
    (
        ParametersMain.procontra,
        {
            "ergibt_Sinn": _("ergibt_Sinn"),
            "ergibtsinn": _("ergibtsinn"),
            "machtsinn": _("machtsinn"),
            "sinn": _("sinn"),
        },
        {140},
    ),
    (
        ParametersMain.procontra,
        {
            "Veränderung": _("Veränderung"),
            "veraenderung": _("veraenderung"),
            "veraendern": _("veraendern"),
            "veränderung": _("veränderung"),
            "verändern": _("verändern"),
        },
        {142},
    ),
    (
        ParametersMain.procontra,
        {
            "bändigen_kontrollieren": _("bändigen_kontrollieren"),
            "baendigenkontrollieren": _("baendigenkontrollieren"),
            "kontrollieren": _("kontrollieren"),
            "baendigen": _("baendigen"),
            "bändigen": _("bändigen"),
        },
        {143},
    ),
    (
        ParametersMain.procontra,
        {
            "vereinen": _("vereinen"),
            "einheit": _("einheit"),
        },
        {144},
    ),
    (
        ParametersMain.procontra,
        {
            "Vorteile": _("Vorteile"),
            "vorteile": _("vorteile"),
            "veraenderungnutzen": _("veraenderungnutzen"),
        },
        {141},
    ),
    (
        ParametersMain.procontra,
        {
            "Gegenspieler": _("Gegenspieler"),
            "gegenspieler": _("gegenspieler"),
            "antagonist": _("antagonist"),
        },
        {137},
    ),
    (
        ParametersMain.procontra,
        {"nervig": _("nervig")},
        {120},
    ),
    (
        ParametersMain.procontra,
        {
            "pro_nutzen": _("pro_nutzen"),
            "pronutzen": _("pronutzen"),
        },
        {117},
    ),
    (
        ParametersMain.procontra,
        {
            "Gegenposition": _("Gegenposition"),
            "gegenposition": _("gegenposition"),
        },
        {116},
    ),
    (
        ParametersMain.procontra,
        {
            "Hilfe_erhalten": _("Hilfe_erhalten"),
            "hilfeerhalten": _("hilfeerhalten"),
        },
        {114},
    ),
    (
        ParametersMain.procontra,
        {
            "Helfen": _("Helfen"),
            "helfen": _("helfen"),
            "hilfe": _("hilfe"),
        },
        {115},
    ),
    (
        ParametersMain.procontra,
        {
            "Pro": _("Pro"),
            "pro": _("pro"),
            "dafür": _("dafür"),
            "dafuer": _("dafuer"),
        },
        {17, 48},
    ),
    (
        ParametersMain.procontra,
        {
            "nicht_miteinander_auskommen": _("nicht_miteinander_auskommen"),
            "nichtauskommen": _("nichtauskommen"),
        },
        {123},
    ),
    (
        ParametersMain.procontra,
        {
            "nicht_dagegen": _("nicht_dagegen"),
            "nichtdagegen": _("nichtdagegen"),
        },
        {124},
    ),
    (
        ParametersMain.procontra,
        {
            "kein_Gegenteil": _("kein_Gegenteil"),
            "keingegenteil": _("keingegenteil"),
        },
        {125},
    ),
    (
        ParametersMain.procontra,
        {
            "nicht_dafür": _("nicht_dafür"),
            "nichtdafuer": _("nichtdafuer"),
        },
        {126},
    ),
    (
        ParametersMain.procontra,
        {
            "Hilfe_nicht_gebrauchen": _("Hilfe_nicht_gebrauchen"),
            "hilfenichtgebrauchen": _("hilfenichtgebrauchen"),
        },
        {127},
    ),
    (
        ParametersMain.procontra,
        {
            "nicht_helfen_können": _("nicht_helfen_können"),
            "nichthelfenkoennen": _("nichthelfenkoennen"),
        },
        {128},
    ),
    (
        ParametersMain.procontra,
        {
            "nicht_abgeneigt": _("nicht_abgeneigt"),
            "nichtabgeneigt": _("nichtabgeneigt"),
        },
        {129},
    ),
    (
        ParametersMain.procontra,
        {"unmotivierbar": _("unmotivierbar")},
        {130},
    ),
    (
        ParametersMain.procontra,
        {
            "contra": _("contra"),
            "dagegen": _("dagegen"),
        },
        {15, 26},
    ),
    (
        ParametersMain.procontra,
        {
            "Gegenteil": _("Gegenteil"),
            "gegenteil": _("gegenteil"),
        },
        {100, 101, 222},
    ),
    (
        ParametersMain.procontra,
        {
            "Harmonie": _("Harmonie"),
            "harmonie": _("harmonie"),
        },
        {102, 103},
    ),
    (ParametersMain.licht, (), {20, 27, 313}),
    (
        ParametersMain.procontra,
        {
            Primzahlkreuz_pro_contra_strs[0]: Primzahlkreuz_pro_contra_strs_Fkt[0],
            "primzahlkreuz": _("primzahlkreuz"),
        },
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
        {
            Primzahlkreuz_pro_contra_strs[0]: Primzahlkreuz_pro_contra_strs_Fkt[0],
            "primzahlkreuz": _("primzahlkreuz"),
        },
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
        {
            "in_ReTa": _("in_ReTa"),
            "inreta": _("inreta"),
        },
        {209, 210},
    ),
    (
        ParametersMain.bedeutung,
        {
            "Vorzeichen": _("Vorzeichen"),
            "vorzeichen": _("vorzeichen"),
        },
        {118, 119},
    ),
    (
        ParametersMain.bedeutung,
        {
            "Primzahlen": _("Primzahlen"),
            "primzahlen": _("primzahlen"),
            "vielfache": _("vielfache"),
            "vielfacher": _("vielfacher"),
        },
        {19},
    ),
    (
        ParametersMain.bedeutung,
        {
            "Anwendung_der_Sonnen_und_Monde": _("Anwendung_der_Sonnen_und_Monde"),
            "anwendungdersonnenundmonde": _("anwendungdersonnenundmonde"),
            "anwendungdersonnen": _("anwendungdersonnen"),
            "anwendungenfuermonde": _("anwendungenfuermonde"),
        },
        {22},
    ),
    (
        ParametersMain.bedeutung,
        {
            "Zählungen": _("Zählungen"),
            "zählungen": _("zählungen"),
            "zaehlung": _("zaehlung"),
            "zaehlungen": _("zaehlungen"),
            "zählung": _("zählung"),
        },
        {25, 45, 169, 188},
    ),
    (
        ParametersMain.bedeutung,
        {
            "Jura": _("Jura"),
            "jura": _("jura"),
            "gesetzeslehre": _("gesetzeslehre"),
            "recht": _("recht"),
        },
        {34},
    ),
    (
        ParametersMain.bedeutung,
        {
            "Vollkommenheit_des_Geistes": _("Vollkommenheit_des_Geistes"),
            "vollkommenheit": _("vollkommenheit"),
            "geist": _("geist"),
        },
        {35},
    ),
    (
        ParametersMain.bedeutung,
        {
            "Gestirn": _("Gestirn"),
            "gestirn": _("gestirn"),
            "mond": _("mond"),
            "sonne": _("sonne"),
            "planet": _("planet"),
        },
        {64, 154},
        set(),
        set(),
        set(),
    ),
    (
        ParametersMain.bedeutung,
        {
            "Konjunktiv_Wurzelbildung": _("Konjunktiv_Wurzelbildung"),
            "konjunktiv": _("konjunktiv"),
            "wurzel": _("wurzel"),
        },
        {106},
    ),
    (
        ParametersMain.bedeutung,
        {
            "Mechanismen_der_Züchtung": _("Mechanismen_der_Züchtung"),
            "mechanismen": _("mechanismen"),
            "wesen": _("wesen"),
            "zuechtung": _("zuechtung"),
            "züchtung": _("züchtung"),
            "züchten": _("züchten"),
            "zuechten": _("zuechten"),
        },
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
        {
            "Weisheit_etc": _("Weisheit_etc"),
            "weisheit": _("weisheit"),
            "metaweisheit": _("metaweisheit"),
            "meta-weisheit": _("meta-weisheit"),
            "idiot": _("idiot"),
            "weise": _("weise"),
            "optimal": _("optimal"),
            "optimum": _("optimum"),
        },
        {112},
        {(40, 41)},
    ),
    (
        ParametersMain.konzept,
        {
            "Dein_Recht_bekommen": _("Dein_Recht_bekommen"),
            "rechte": _("rechte"),
            "recht": _("recht"),
            "selbstgerecht": _("selbstgerecht"),
        },
        set(),
        {(291, 292)},
    ),
    (
        ParametersMain.konzept,
        {
            "unterlegen_überlegen": _("unterlegen_überlegen"),
            "unterlegen": _("unterlegen"),
            "ueberlegen": _("ueberlegen"),
        },
        set(),
        {(380, 381)},
    ),
    (
        ParametersMain.konzept,
        {
            "Ehrlichkeit_und_Streit": _("Ehrlichkeit_und_Streit"),
            "streit": _("streit"),
            "ehrlichkeit": _("ehrlichkeit"),
        },
        set(),
        {(375, 376)},
    ),
    (
        ParametersMain.konzept2,
        {"Würdig": _("Würdig"), "wuerdig": _("wuerdig"), "würdig": _("würdig")},
        set(),
        {(373, 374)},
    ),
    (
        ParametersMain.konzept2,
        {
            "Regel_vs_Ausnahme": _("Regel_vs_Ausnahme"),
            "regel": _("regel"),
            "ausnahme": _("ausnahme"),
        },
        set(),
        {(371, 372)},
    ),
    (
        ParametersMain.konzept2,
        {
            "Filterart_Widrigkeit": _("Filterart_Widrigkeit"),
            "filterart": _("filterart"),
            "widrigkeit": _("widrigkeit"),
        },
        {331, 335},
    ),
    (
        ParametersMain.konzept2,
        {
            "Werte": _("Werte"),
            "werte": _("werte"),
        },
        set(),
        {(360, 361)},
    ),
    (
        ParametersMain.konzept2,
        {
            "Gutartigkeits-Egoismus": _("Gutartigkeits-Egoismus"),
            "position": _("position"),
            "gutesreziprok": _("gutesreziprok"),
        },
        set(),
        {(362, 363)},
    ),
    (
        ParametersMain.konzept2,
        {
            "Reflektieren_Erkenntnis-Erkennen": _("Reflektieren_Erkenntnis-Erkennen"),
            "reflektieren": _("reflektieren"),
            "erkenntnis": _("erkenntnis"),
        },
        set(),
        {(364, 365)},
    ),
    (
        ParametersMain.konzept2,
        {
            "Vertrauen_wollen": _("Vertrauen_wollen"),
            "vertrauenwollen": _("vertrauenwollen"),
        },
        set(),
        {(366, 367)},
    ),
    (
        ParametersMain.konzept,
        {
            "einklinken_vertrauen_anprangern": _("einklinken_vertrauen_anprangern"),
            "einklinken": _("einklinken"),
            "vertrauenerhalten": _("vertrauenerhalten"),
            "anprangern": _("anprangern"),
        },
        set(),
        {(368, 369)},
    ),
    (
        ParametersMain.konzept2,
        {
            "Ausrichten_Einrichten": _("Ausrichten_Einrichten"),
            "einrichten": _("einrichten"),
            "ausrichten": _("ausrichten"),
        },
        set(),
        {(358, 359)},
    ),
    (
        ParametersMain.konzept2,
        {
            "Toleranz_Respekt_Akzeptanz_Willkommen": _(
                "Toleranz_Respekt_Akzeptanz_Willkommen"
            ),
            "toleranz": _("toleranz"),
            "respekt": _("respekt"),
            "akzeptanz": _("akzeptanz"),
            "willkommen": _("willkommen"),
        },
        set(),
        # {(359, 360)},
        {(62, 63)},
    ),
    (
        ParametersMain.konzept,
        {"familiebrauchen": _("familiebrauchen")},
        set(),
        {(279, 280)},
    ),
    (
        ParametersMain.konzept,
        {"ego": _("ego"), "bescheiden": _("bescheiden")},
        set(),
        {(277, 278)},
    ),
    (
        ParametersMain.konzept,
        {
            "Selbstsucht_Ichsucht_etc": _("Selbstsucht_Ichsucht_etc"),
            "selbstsucht": _("selbstsucht"),
            "ichsucht": _("ichsucht"),
        },
        set(),
        {(274, 275)},
    ),
    (
        ParametersMain.konzept,
        {
            "Forschen_Erfinden_Einklinken": _("Forschen_Erfinden_Einklinken"),
            "wissenschaft": _("wissenschaft"),
            "forschen": _("forschen"),
            "einklinken": _("einklinken"),
            "erfinden": _("erfinden"),
        },
        set(),
        {(258, 259)},
    ),
    (
        ParametersMain.konzept,
        {
            "Kooperation_vs_Arsch": _("Kooperation_vs_Arsch"),
            "arschloch": _("arschloch"),
            "kooperation": _("kooperation"),
            "arsch": _("arsch"),
        },
        set(),
        {(245, 246)},
    ),
    (
        ParametersMain.konzept,
        {"Liebe_usw": _("Liebe_usw"), "liebe": _("liebe"), "zuneigung": _("zuneigung")},
        set(),
        {(247, 248)},
    ),
    (
        ParametersMain.konzept,
        {
            "Selbstlosigkeit_Ichlosigkeit_etc": _("Selbstlosigkeit_Ichlosigkeit_etc"),
            "selbstlos": _("selbstlos"),
            "ichlos": _("ichlos"),
        },
        set(),
        {(238, 239)},
    ),
    (
        ParametersMain.konzept,
        {
            "variationsreich_eintönig": _("variationsreich_eintönig"),
            "eintönig": _("eintönig"),
            "eintoenig": _("eintoenig"),
            "variationsreich": _("variationsreich"),
        },
        set(),
        {(236, 237)},
    ),
    (
        ParametersMain.konzept,
        {
            "Zuneigung_Abneigung": _("Zuneigung_Abneigung"),
            "abgeneigt": _("abgeneigt"),
            "zugewandt": _("zugewandt"),
            "reserviert": _("reserviert"),
            "zugeneigt": _("zugeneigt"),
        },
        set(),
        {(199, 200)},
    ),
    (
        ParametersMain.menschliches,
        {
            "ehrlich vs höflich": _("ehrlich vs höflich"),
            "ehrlich": _("ehrlich"),
            "höflich": _("höflich"),
            "hoeflich": _("hoeflich"),
        },
        set(),
        {(224, 225)},
    ),
    # (
    #    ParametersMain.konzept,
    #    {"delegieren": _("delegieren"), "ansammlung": _("ansammlung")},
    #    set(),
    #    {(227, 228)},
    # ),
    (
        ParametersMain.konzept,
        {
            "ehrlich vs höflich": _("ehrlich vs höflich"),
            "ehrlich": _("ehrlich"),
            "höflich": _("höflich"),
            "hoeflich": _("hoeflich"),
        },
        set(),
        {(224, 225)},
    ),
    (
        ParametersMain.konzept,
        {"Tragweite": _("Tragweite"), "tragweite": _("tragweite")},
        set(),
        {(211, 212)},
    ),
    (
        ParametersMain.konzept,
        {"wertvoll": _("wertvoll"), "wertlos": _("wertlos")},
        set(),
        {(186, 187)},
    ),
    (
        ParametersMain.konzept,
        {
            "Götter_Propheten_Familien_Freunde": _("Götter_Propheten_Familien_Freunde"),
            "familiaer": _("familiaer"),
            "goettlich": _("goettlich"),
            "freunde": _("freunde"),
            "propheten": _("propheten"),
        },
        set(),
        {(184, 185)},
    ),
    (
        ParametersMain.konzept,
        {
            "sanft_vs_hart": _("sanft_vs_hart"),
            "sanft": _("sanft"),
            "hart": _("hart"),
        },
        set(),
        {(159, 160), (161, 162)},
    ),
    (
        ParametersMain.konzept,
        {
            "vereinen_vs_verbinden": _("vereinen_vs_verbinden"),
            "vereinenverbinden": _("vereinenverbinden"),
            "vereinen": _("vereinen"),
            "verbinden": _("verbinden"),
            "einheit": _("einheit"),
            "verbindung": _("verbindung"),
        },
        set(),
        {(133, 134)},
    ),
    (
        ParametersMain.konzept,
        {
            "ähnlich": _("ähnlich"),
            "aehnlich": _("aehnlich"),
        },
        {220},
    ),
    (
        ParametersMain.konzept,
        {
            "gut_böse_lieb_schlecht": _("gut_böse_lieb_schlecht"),
            "gut": _("gut"),
            "böse": _("böse"),
            "boese": _("boese"),
            "lieb": _("lieb"),
            "schlecht": _("schlecht"),
        },
        {52, 53},
        {(38, 39)},
    ),
    (
        ParametersMain.konzept,
        {
            "Sinn_und_Zweck_des_Lebens": _("Sinn_und_Zweck_des_Lebens"),
            "sinn": _("sinn"),
            "zweck": _("zweck"),
            "bedeutung": _("bedeutung"),
        },
        {88, 189},
        {(181, 182)},
    ),
    (
        ParametersMain.konzept,
        {
            "Zeit_vs_Raum": _("Zeit_vs_Raum"),
            "zeit": _("zeit"),
            "raum": _("raum"),
            "zeitlich": _("zeitlich"),
            "räumlich": _("räumlich"),
        },
        set(),
        {(49, 50)},
    ),
    (
        ParametersMain.konzept,
        {
            "egalitär_vs_autoritär": _("egalitär_vs_autoritär"),
            "egalitaerautoritaer": _("egalitaerautoritaer"),
            "egalitaer": _("egalitaer"),
            "autoritaer": _("autoritaer"),
            "egalitär": _("egalitär"),
            "autoritär": _("autoritär"),
        },
        set(),
        {(163, 164)},
    ),
    (
        ParametersMain.konzept,
        {
            "Meinungen_und_Ruf": _("Meinungen_und_Ruf"),
            "meinungen": _("meinungen"),
            "anderemenschen": _("anderemenschen"),
            "ruf": _("ruf"),
        },
        set(),
        {(60, 61)},
    ),
    (
        ParametersMain.konzept,
        {
            "Meinungsintelligenz": _("Meinungsintelligenz"),
            "meinungsintelligenz": _("meinungsintelligenz"),
            "ursprungsintelligenz": _("ursprungsintelligenz"),
        },
        set(),
        {(151, 152)},
    ),
    (
        ParametersMain.konzept,
        {
            "Sittlichkeit": _("Sittlichkeit"),
            "sittlichkeit": _("sittlichkeit"),
            "annaehrerung": _("annaehrerung"),
        },
        set(),
        {(179, 180)},
    ),
    (
        ParametersMain.konzept,
        {"Führung": _("Führung"), "führung": _("führung"), "fuehrung": _("fuehrung")},
        set(),
        {(173, 174)},
    ),
    (
        ParametersMain.konzept,
        {
            "Durchleuchten": _("Durchleuchten"),
            "durchleuchten": _("durchleuchten"),
            "erleuchten": _("erleuchten"),
        },
        set(),
        {(177, 178)},
    ),
    (
        ParametersMain.konzept,
        {
            "Fördern_Sensiblisieren_und_Gedeihen": _(
                "Fördern_Sensiblisieren_und_Gedeihen"
            ),
            "foerdern": _("foerdern"),
            "fördern": _("fördern"),
            "begrenzen": _("begrenzen"),
            "sensibilisieren": _("sensibilisieren"),
            "gedeihen": _("gedeihen"),
            "verderben": _("verderben"),
        },
        set(),
        {(175, 176)},
    ),
    (
        ParametersMain.konzept,
        {
            "Überheblichkeit": _("Überheblichkeit"),
            "überheblich": _("überheblich"),
            "ueberheblichkeit": _("ueberheblichkeit"),
            "ueberheblich": _("ueberheblich"),
            "überheblichkeit": _("überheblichkeit"),
        },
        set(),
        {(171, 172)},
    ),
    (
        ParametersMain.konzept,
        {
            "Polung_der_Liebe": _("Polung_der_Liebe"),
            "liebepolung": _("liebepolung"),
        },
        set(),
        {(121, 122)},
    ),
    (
        ParametersMain.konzept,
        {
            "Egoismus_vs_Altruismus": _("Egoismus_vs_Altruismus"),
            "egoismus": _("egoismus"),
            "altruismus": _("altruismus"),
            "egoist": _("egoist"),
            "altruist": _("altruist"),
        },
        {136},
        {(66, 67)},
    ),
    (
        ParametersMain.konzept,
        {"kausal": _("kausal"), "geltung": _("geltung"), "genese": _("genese")},
        set(),
        {(110, 111)},
    ),
    (
        ParametersMain.konzept,
        {"Gleichheit": _("Gleichheit"), "gleich": _("gleich")},
        set(),
        {(192, 193)},
    ),
    (
        ParametersMain.konzept,
        {"Überleben": _("Überleben"), "ueberleben": _("ueberleben")},
        set(),
        {(194, 195)},
    ),
    (ParametersMain.inkrementieren, set(), {43, 54, 74, 95}),
    (ParametersMain.inkrementieren, {"um1": _("um1")}, {155}),
    (ParametersMain.inkrementieren, {"um2": _("um2")}, {156}),
    (ParametersMain.inkrementieren, {"um3": _("um3")}, {157}),
    (
        ParametersMain.inkrementieren,
        {
            "warum_Transzendentalie_=_Strukturgroesse_=_Charakter": _(
                "warum_Transzendentalie_=_Strukturgroesse_=_Charakter"
            ),
            "warumtranszendentaliezustrukturgroesseundcharakter": _(
                "warumtranszendentaliezustrukturgroesseundcharakter"
            ),
        },
        {4, 54, 5, 165},
    ),
    (
        ParametersMain.inkrementieren,
        {
            "warum_Transzendentalie_=_Komplexität_von_Michael_Commons": _(
                "warum_Transzendentalie_=_Komplexität_von_Michael_Commons"
            ),
            "warumtranszendentaliegleichkomplexitaet": _(
                "warumtranszendentaliegleichkomplexitaet"
            ),
        },
        {65, 5, 166},
    ),
    (
        ParametersMain.primvielfache,
        {"Rahmen-Bedingungen": _("Rahmen-Bedingungen"), "rahmen": _("rahmen")},
        {226},
    ),
    (
        ParametersMain.primvielfache,
        {
            "Motive_gleichförmige_Polygone": _("Motive_gleichförmige_Polygone"),
            "motivgleichfoermig": _("motivgleichfoermig"),
        },
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
        {
            "Struktur_gleichförmige_Polygone": _("Struktur_gleichförmige_Polygone"),
            "strukturgleichfoermig": _("strukturgleichfoermig"),
        },
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
        {
            "Motive_Sternpolygone": _("Motive_Sternpolygone"),
            "motivstern": _("motivstern"),
        },
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
        {
            "Struktur_Sternpolygone": _("Struktur_Sternpolygone"),
            "strukturstern": _("strukturstern"),
        },
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
        {
            "Motiv_Sternpolygon_gebrochen-rational": _(
                "Motiv_Sternpolygon_gebrochen-rational"
            ),
            "motivgebrstern": _("motivgebrstern"),
        },
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
        {
            "Struktur_Sternpolyon_gebrochen-rational": _(
                "Struktur_Sternpolyon_gebrochen-rational"
            ),
            "strukgebrstern": _("strukgebrstern"),
        },
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
        {
            "Motiv_gleichförmige_Polygone_gebrochen-rational": _(
                "Motiv_gleichförmige_Polygone_gebrochen-rational"
            ),
            "motivgebrgleichf": _("motivgebrgleichf"),
        },
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
        {
            "Struktur_gleichförmige_Polygone_gebrochen-rational": _(
                "Struktur_gleichförmige_Polygone_gebrochen-rational"
            ),
            "strukgebrgleichf": _("strukgebrgleichf"),
        },
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
        {"beschrieben": _("beschrieben")},
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

kombiParaNdataMatrix: OrderedDict[int, tuple[str]] = OrderedDict(
    {
        1: {
            "Lebewesen": _("Lebewesen"),
            "tiere": _("tiere"),
            "tier": _("tier"),
            "lebewesen": _("lebewesen"),
        },
        2: {"Berufe": _("Berufe"), "berufe": _("berufe"), "beruf": _("beruf")},
        3: {
            "Kreativität_und_Intelligenz": _("Kreativität_und_Intelligenz"),
            "kreativität": _("kreativität"),
            "intelligenz": _("intelligenz"),
            "kreativitaet": _("kreativitaet"),
        },
        4: {
            "Liebe": _("Liebe"),
            "liebe": _("liebe"),
        },
        7: {
            "Männer": _("Männer"),
            "männer": _("männer"),
            "maenner": _("maenner"),
            "frauen": _("frauen"),
        },
        8: {
            "Persönlichkeit_evolutionär_erwerben": _(
                "Persönlichkeit_evolutionär_erwerben"
            ),
            "evolution": _("evolution"),
            "erwerben": _("erwerben"),
            "persoenlichkeit": _("persoenlichkeit"),
            "persönlichkeit": _("persönlichkeit"),
        },
        9: {
            "Religion": _("Religion"),
            "religion": _("religion"),
            "religionen": _("religionen"),
        },
        10: {
            "Motive_Ziele": _("Motive_Ziele"),
            "motivation": _("motivation"),
            "ziele": _("ziele"),
            "ziel": _("ziel"),
            "motive": _("motive"),
        },
        12: {
            "Emotionen": _("Emotionen"),
            "emotionen": _("emotionen"),
            "gefuehle": _("gefuehle"),
            "emotion": _("emotion"),
            "gefühl": _("gefühl"),
            "gefühle": _("gefühle"),
        },
        13: {
            "Personen": _("Personen"),
            "personen": _("personen"),
            "berühmtheiten": _("berühmtheiten"),
            "beruehmtheiten": _("beruehmtheiten"),
        },
        16: {
            "Wirtschaftssysteme": _("Wirtschaftssysteme"),
            "wirtschaftssystem": _("wirtschaftssystem"),
            "wirtschaftssysteme": _("wirtschaftssysteme"),
            "kombinierteswirtschaftssystem": _("kombinierteswirtschaftssystem"),
            "kombiniertewirtschaftssysteme": _("kombiniertewirtschaftssysteme"),
        },
    }
)

kombiParaNdataMatrix2: OrderedDict[int, tuple[str]] = OrderedDict(
    {
        1: {
            "Lebewesen": _("Lebewesen"),
            "tiere": _("tiere"),
            "tier": _("tier"),
            "lebewesen": _("lebewesen"),
        },
        2: {"Berufe": _("Berufe"), "berufe": _("berufe"), "beruf": _("beruf")},
        # 3: {
        #    "Kreativität_und_Intelligenz": _("Kreativität_und_Intelligenz"),
        #    "kreativität": _("kreativität"),
        #    "intelligenz": _("intelligenz"),
        #    "kreativitaet": _("kreativitaet"),
        # },
        # 4: {
        #    "Liebe": _("Liebe"),
        #    "liebe": _("liebe"),
        # },
        5: {
            "Transzendentalien_Strukturalien": _("Transzendentalien_Strukturalien"),
            "transzendenz": _("transzendenz"),
            "transzendentalien": _("transzendentalien"),
            "strukturalien": _("strukturalien"),
            "alien": _("alien"),
        },
        6: {
            "Primzahlkreuz": _("Primzahlkreuz"),
            "leibnitz": _("leibnitz"),
            "primzahlkreuz": _("primzahlkreuz"),
        },
        # 7: {
        #    "Männer": _("Männer"),
        #    "männer": _("männer"),
        #    "maenner": _("maenner"),
        #    "frauen": _("frauen"),
        # },
        8: {
            "Persönlichkeit_evolutionär_erwerben": _(
                "Persönlichkeit_evolutionär_erwerben"
            ),
            "evolution": _("evolution"),
            "erwerben": _("erwerben"),
            "persoenlichkeit": _("persoenlichkeit"),
            "persönlichkeit": _("persönlichkeit"),
        },
        # 9: {
        #    "Religion": _("Religion"),
        #    "religion": _("religion"),
        #    "religionen": _("religionen"),
        # },
        10: {
            "Motive_Ziele": _("Motive_Ziele"),
            "motivation": _("motivation"),
            "motive": _("motive"),
            "ziele": _("ziele"),
            "ziel": _("ziel"),
        },
        11: {
            "analytische_Ontologie": _("analytische_Ontologie"),
            "analytischeontologie": _("analytischeontologie"),
            "ontologie": _("ontologie"),
        },
        # 12: {
        #    "Emotionen": _("Emotionen"),
        #    "emotionen": _("emotionen"),
        #    "gefuehle": _("gefuehle"),
        #    "gefühle": _("gefühle"),
        #    "emotion": _("emotion"),
        #    "gefühl": _("gefühl"),
        #    "gefühle": _("gefühle"),
        # },
        # 13: {"Personen": _("Personen"), "personen": _("personen"), "berühmtheiten": _("berühmtheiten"), "beruehmtheiten": _("beruehmtheiten")},
        14: {
            "Mechanismen_der_Zuechtung": _("Mechanismen_der_Zuechtung"),
            "mechanismen": _("mechanismen"),
            "wesen": _("wesen"),
            "zuechten": _("zuechten"),
            "züchten": _("züchten"),
        },
        15: {
            "Gegentranszendentalien": _("Gegentranszendentalien"),
            "gegentranszendentalien": _("gegentranszendentalien"),
            "gegenstrukturalien": _("gegenstrukturalien"),
        },
        # 16: {
        #    "Wirtschaftssysteme": _("Wirtschaftssysteme"),
        #    "wirtschaftssystem": _("wirtschaftssystem"),
        #    "wirtschaftssysteme": _("wirtschaftssysteme"),
        #    "kombinierteswirtschaftssystem": _("kombinierteswirtschaftssystem"),
        #    "kombiniertewirtschaftssysteme": _("kombiniertewirtschaftssysteme"),
        # },
        17: {
            "Maschinen": _("Maschinen"),
            "maschinen": _("maschinen"),
            "geräte": _("geräte"),
            "geraete": _("geraete"),
        },
        18: {"Geist": _("Geist"), "geist": _("geist")},
        19: {"Bewusstsein": _("Bewusstsein"), "bewusstsein": _("bewusstsein")},
    }
)


class tableHandling:
    parameterName: dict[str, str] = {"kombination": _("kombination")}
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
    modalA1 = {"modalS": _("modalS")}
    modalA2 = {"vervielfachter": _("vervielfachter")}
    modalA3 = {"i_origS": _("i_origS")}

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
    headline1 = {
        _(
            "Gegen / pro: Nach Rechenregeln auf Primzahlkreuz und Vielfachern von Primzahlen"
        )
    }
    gegen = {"gegen ": _("gegen ")}
    pro = {"pro ": _("pro ")}
    hineinversetzen = {
        " Darin kann sich die ": _(" Darin kann sich die "),
        " am Besten hineinversetzten.": _(" am Besten hineinversetzten."),
    }
    proIst = {
        "pro dieser Zahl sind: _(": _("pro dieser Zahl sind: _("),
        ")pro dieser Zahl ist ": _(")pro dieser Zahl ist "),
    }
    contraIst = {
        " contra dieser Zahl sind: _(": _(" contra dieser Zahl sind: _("),
        ") contra dieser Zahl ist ": _(") contra dieser Zahl ist "),
    }
    hineinversetzenSatz = " - Die Zahlen, die für oder gegen diese Zahlen hier sind, können sich in diese am Besten gedanklich hineinversetzen."
    polygone = {
        "Sternpolygone": _("Sternpolygone"),
        "gleichförmige Polygone": _("gleichförmige Polygone"),
    }

    kombisNamen: dict[str, str] = {
        "Motiv -> Motiv": _("Motiv -> Motiv"),
        "Motiv -> Strukur": _("Motiv -> Strukur"),
        "Struktur -> Motiv": _("Struktur -> Motiv"),
        "Struktur -> Strukur": _("Struktur -> Strukur"),
    }
    kombisNamen2: dict[str, str] = {
        "GalGal": _("GalGal"),
        "GalUni": _("GalUni"),
        "UniGal": _("UniGal"),
        "UniUni": _("UniUni"),
    }

    faktorenbla = {
        ", mit Faktoren aus gebrochen-rationalen Zahlen": _(
            ", mit Faktoren aus gebrochen-rationalen Zahlen"
        )
    }
    genMul = {"generierte Multiplikationen ": _("generierte Multiplikationen ")}
    ausserdem = {", außerdem: ": _(", außerdem: ")}
    Multiplikationen_ = {"Multiplikationen": _("Multiplikationen")}
    nWichtigste = {
        "Wichtigstes_zum_verstehen": _("Wichtigstes_zum_verstehen"),
        "Viertwichtigste": _("Viertwichtigste"),
    }
    metaOrWhat = OrderedDict(
        {
            2: (
                {"Meta-Thema: ": _("Meta-Thema: "), "Konkretes: ": _("Konkretes: ")},
                {"Meta-": _("Meta-"), "Konkret-": _("Konkret-")},
            ),
            3: (
                {"Theorie-Thema: ": _("Theorie-Thema: "), "Praxis: ": _("Praxis: ")},
                {"Theorie-": _("Theorie-"), "Praxis-": _("Praxis-")},
            ),
            4: (
                {
                    "Planungs-Thema: ": _("Planungs-Thema: "),
                    "Umsetzungs-Thema: ": _("Umsetzungs-Thema: "),
                },
                {"Planung-": _("Planung-"), "Umsetzung-": _("Umsetzung-")},
            ),
            5: (
                {
                    "Anlass-Thema: ": _("Anlass-Thema: "),
                    "Wirkungs-Thema: ": _("Wirkungs-Thema: "),
                },
                {"Anlass-": _("Anlass-"), "wirkung-": _("wirkung-")},
            ),
            6: (
                {
                    "Kraft-Gebung: ": _("Kraft-Gebung: "),
                    "Verstärkungs-Thema: ": _("Verstärkungs-Thema: "),
                },
                {"Kraft-geben-": _("Kraft-geben-"), "Verstärkung-": _("Verstärkung-")},
            ),
            7: (
                {
                    "Beherrschung: ": _("Beherrschung: "),
                    "Richtung-Thema: ": _("Richtung-Thema: "),
                },
                {"beherrschend-": _("beherrschend-"), "Richtung-": _("Richtung-")},
            ),
        }
    )
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
            5: {
                "Transzendentalien, Strukturalien, Universum n": _(
                    "Transzendentalien, Strukturalien, Universum n"
                )
            },
            10: {"Galaxie n": _("Galaxie n")},
            42: {"Galaxie 1/n": _("Galaxie 1/n")},
            131: {
                "Transzendentalien, Strukturalien, Universum 1/n": _(
                    "Transzendentalien, Strukturalien, Universum 1/n"
                )
            },
            138: {
                "Dagegen-Gegen-Transzendentalien, Gegen-Strukturalien, Universum n": _(
                    "Dagegen-Gegen-Transzendentalien, Gegen-Strukturalien, Universum n"
                )
            },
            202: {
                "neutrale Gegen-Transzendentalien, Gegen-Strukturalien, Universum n": _(
                    "neutrale Gegen-Transzendentalien, Gegen-Strukturalien, Universum n)"
                )
            },
            None: {"Richtung-Richtung": _("Richtung-Richtung")},
        }
    )

    primRicht = {"Primzahlwirkung (7, Richtung) ": _("Primzahlwirkung (7, Richtung) ")}

    letztEnd = {"] * letztendlich: ": _("] * letztendlich: ")}

    primVielGen = {
        "Primzahlvielfache, nicht generiert": _("Primzahlvielfache, nicht generiert")
    }
    GalOrUniOrFehler = {
        "Fehler": _("Fehler"),
        " Universum": _(" Universum"),
        " Galaxie": _(" Galaxie"),
    }

    multipl = {"Multiplikationen": _("Multiplikationen")}
    notGen = {"Nicht_generiert": _("Nicht_generiert")}


class lib4tables:
    zaehlung = {"zaehlung:": _("zaehlung")}
    nummerier = {"nummerierung": _("nummerierung")}
    alles = {"alles": _("alles")}


class center:
    @classmethod
    def classify(cls, mod):
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


class retapy:

    beschriebenWort = _("beschrieben")
    mainParaCmds: dict = {
        _("zeilen"): 0,
        _("spalten"): 1,
        tableHandling.parameterName["kombination"]: 2,
        _("ausgabe"): 3,
        _("debug"): None,
        _("h"): None,
        _("help"): None,
    }
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
        "".join((", --", spalten["breiten"], " --", spalten["breite"])),
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
        ", --" + spalten["keinenummerierung"],
    )
    galaxieParameter = _("galaxie")
    universumParameter = _("universum")
    kombinationenWort = _("kombinationen")
    cliout5Saetze = (
        _('Die Kombispalte "'),
        _('" existiert so nicht als Befehl. Möglich sind die Parameter für '),
    )
    cliout6Satz = _(
        "".join(
            (
                'kein Unter-Parameter "--',
                kombiMainParas["galaxie"],
                '=" oder "--',
                kombiMainParas["galaxie"],
                '=" angegeben für Hauptparameter -kombination',
            )
        )
    )
    cliout7Saetze = (
        _("Es muss ein Hauptparameter, bzw. der richtige, gesetzt sein, damit ein"),
        _(' Nebenparameter, wie möglicherweise: "'),
        _('" ausgeführt werden kann. Hauptparameter sind: -'),
    )
    breiteParameterWort = _("breite")

    cliout8Satz = _("Versuche Parameter -h")
    zeilenParas = {
        "alles": _("alles"),
        "zeit": _("zeit"),
        "heute": _("heute"),
        "gestern": _("gestern"),
        "morgen": _("morgen"),
        "hoehemaximal": _("hoehemaximal"),
        "typ": _("typ"),
        "sonne": _("sonne"),
        "mond": _("mond"),
        "planet": _("planet"),
        "schwarzesonne": _("schwarzesonne"),
        "potenzenvonzahlen": _("potenzenvonzahlen"),
        "vielfachevonzahlen": _("vielfachevonzahlen"),
        "primzahlvielfache": _("primzahlvielfache"),
        "vorhervonausschnittteiler": _("vorhervonausschnittteiler"),
        "vorhervonausschnitt": _("vorhervonausschnitt"),
        "nachtraeglichneuabzaehlungvielfache": _("nachtraeglichneuabzaehlungvielfache"),
        "nachtraeglichneuabzaehlung": _("nachtraeglichneuabzaehlung"),
    }
    cliout9Saetze = (
        _('Den Neben-Parameter "'),
        _('" gibt es hier nicht für den Hauptparameter "-'),
        _('".'),
        _(" Möglich sind: "),
    )
    cliout10Satze = (
        _('Den Neben-Parameter "'),
        _('" gibt es hier nicht für den Hauptparameter "-'),
    )


class nested:
    galWort = retapy.galaxieParameter
    uniWort = retapy.universumParameter
    artWort = ausgabeParas["art"]
    zeitWort = zeilenParas["zeit"]
    typWort = zeilenParas["typ"]


class retaPrompt:
    befehleBeenden = {_("ende"), _("exit"), _("quit"), _("q"), _(":q")}
    promptModeSatz = _("promptmode vorher: {} , {}")
    out1Satze = (
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
        befehle["e"]: befehle[
            "keineEinZeichenZeilenPlusKeineAusgabeWelcherBefehlEsWar"
        ],
        befehle["a"]: befehle["absicht"],
        befehle["u"]: befehle["universum"],
        befehle["t"]: befehle["thomas"],
        befehle["r"]: befehle["richtung"],
        befehle["v"]: befehle["vielfache"],
        befehle["h"]: befehle["help"],
        befehle["w"]: befehle["teiler"],
        befehle["S"]: befehle["BefehlSpeichernDanach"],
        befehle["s"]: befehle["BefehlSpeichernDavor"],
        befehle["l"]: befehle["BefehlSpeicherungLöschen"],
        befehle["o"]: befehle["BefehlSpeicherungAusgeben"],
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
            """Erlaube Parameter sind
            -""",
            retaPromptParameter["vi"],
            """, für vi mode statt emacs mode,
            -""",
            retaPromptParameter["log"],
            """,  um Logging zu aktivieren,
            -""",
            retaPromptParameter["debug"],
            """, um Debugging-Log-Ausgabe zu aktivieren. Das ist nur für Entwickler gedacht.
            -""",
            retaPromptParameter["befehl"],
            """ bewirkt, dass bis zum letzten Programmparameter retaPrompt Befehl nur ein RetaPrompt-Befehl ausgeführt wird.
            -""",
            retaPromptParameter["e"],
            _(" bewirkt, dass bei allen Befehlen das '"),
            befehle["e"],
            ("' Kommando bzw. '"),
            befehle["keineEinZeichenZeilenPlusKeineAusgabeWelcherBefehlEsWar"],
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
