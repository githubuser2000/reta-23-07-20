import sys
from collections import OrderedDict, namedtuple
from typing import Optional, Union

try:
    from orderedset import OrderedSet
except:
    OrderedSet = set

sys.path.insert(1, "./..")
from center import Multiplikationen, Primzahlkreuz_pro_contra_strs

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

gebrochenSpaltenMaximumPlus1 = 21
spalten: dict = {}
spalten |= {
    "--breite=": "--breite=",
    "--breiten=": "--breiten=",
    "--keinenummerierung": "--keinenummerierung",
}

zeilenTypen = {
    "sonne": "sonne",
    "mond": "mond",
    "planet": "planet",
    "schwarzesonne": "schwarzesonne",
}
zeilenZeit = {"heute": "heute", "gestern": "gestern", "morgen": "morgen"}

ausgabeParas = {
    "--nocolor": "--nocolor",
    "--justtext": "--justtext",
    "--art=": "--art=",
    "--onetable": "--onetable",
    "--spaltenreihenfolgeundnurdiese=": "--spaltenreihenfolgeundnurdiese=",
    "--endlessscreen": "--endlessscreen",
    "--endless": "--endless",
    "--dontwrap": "--dontwrap",
    "--breite=": "--breite=",
    "--breiten=": "--breiten=",
    "--keineleereninhalte": "--keineleereninhalte",
    "--keinenummerierung": "--keinenummerierung",
    "--keineueberschriften": "--keineueberschriften",
}
kombiMainParas = {"--galaxie=": "--galaxie=", "--universum=": "--universum="}
zeilenParas = {
    "--zeit=": "--zeit=",
    "--zaehlung=": "--zaehlung=",
    "--vorhervonausschnitt=": "--vorhervonausschnitt=",
    "--vorhervonausschnittteiler": "--vorhervonausschnittteiler",
    "--primzahlvielfache=": "--primzahlvielfache=",
    "--nachtraeglichneuabzaehlung=": "--nachtraeglichneuabzaehlung=",
    "--nachtraeglichneuabzaehlungvielfache=": "--nachtraeglichneuabzaehlungvielfache=",
    "--alles": "--alles",
    "--potenzenvonzahlen=": "--potenzenvonzahlen=",
    "--typ=": "--typ=",
    "--vielfachevonzahlen=": "--vielfachevonzahlen=",
    "--oberesmaximum=": "--oberesmaximum=",
}

hauptForNeben = {
    "-zeilen": "-zeilen",
    "-spalten": "-spalten",
    "-kombination": "-kombination",
    "-ausgabe": "-ausgabe",
    "-h": "-h",
    "-help": "-help",
}

ausgabeArt = {
    "bbcode": "bbcode",
    "html": "html",
    "csv": "csv",
    "shell": "shell",
    "markdown": "markdown",
    "emacs": "emacs",
}


wahl15Words = {
    "Strukturalien_bzw_Meta-Paradigmen_bzw_Transzendentalien_(15),Geist_(15),Model_of_Hierarchical_Complexity,"
    + Primzahlkreuz_pro_contra_strs[
        1
    ]: "Strukturalien_bzw_Meta-Paradigmen_bzw_Transzendentalien_(15),Geist_(15),Model_of_Hierarchical_Complexity,"
    + Primzahlkreuz_pro_contra_strs[1],
    "Konkreta_und_Focus_(2)": "Konkreta_und_Focus_(2)",
    "Impulse_(5)": "Impulse_(5)",
    "Gefühle_(7)": "Gefühle_(7)",
    "Modus_und_Sein_(8)": "Modus_und_Sein_(8)",
    "Wirklichkeiten_Wahrheit_Wahrnehmung_(10)": "Wirklichkeiten_Wahrheit_Wahrnehmung_(10)",
    "Meta-Systeme_(12),Ordnung_und_Filterung_12_und_1pro12": "Meta-Systeme_(12),Ordnung_und_Filterung_12_und_1pro12",
    "Paradigmen_sind_Absichten_(13)": "Paradigmen_sind_Absichten_(13)",
    "Gedanken_sind_Positionen_(17)": "Gedanken_sind_Positionen_(17)",
    "Verbundenheiten_(18)": "Verbundenheiten_(18)",
    "Triebe_und_Bedürfnisse_(6)": "Triebe_und_Bedürfnisse_(6)",
    "Lust_(9)": "Lust_(9)",
    "Reflexe_(3),Existenzialien_(3)": "Reflexe_(3),Existenzialien_(3)",
    "Absicht_6_ist_Vorteilsmaximierung": "Absicht_6_ist_Vorteilsmaximierung",
    "Absicht_7_ist_Selbstlosigkeit": "Absicht_7_ist_Selbstlosigkeit",
    "Absicht_10_ist_Wirklichkeit_erkennen": "Absicht_10_ist_Wirklichkeit_erkennen",
    "Absicht_17_ist_zu_meinen": "Absicht_17_ist_zu_meinen",
    "Zeit_(4)_als_Wirklichkeit": "Zeit_(4)_als_Wirklichkeit",
    "Funktionen_Vorstellungen_(16)": "Funktionen_Vorstellungen_(16)",
    "Achtung_(4)": "Achtung_(4)",
    "Absicht_1/8": "Absicht_1/8",
    "Absicht_1/6_ist_Reinigung_und_Klarheit": "Absicht_1/6_ist_Reinigung_und_Klarheit",
    "Reflektion_und_Kategorien_(1/15)": "Reflektion_und_Kategorien_(1/15)",
    "Regungen_(1)": "Regungen_(1)",
    "Energie_und_universelle_Eigenschaften_(30)": "Energie_und_universelle_Eigenschaften_(30)",
    "Stimmungen_Kombinationen_(14)": "Stimmungen_Kombinationen_(14)",
    "Klassen_(20)": "Klassen_(20)",
    "Empathie_(37)": "Empathie_(37)",
    "Garben_und_Verhalten_nachfühlen(31)": "Garben_und_Verhalten_nachfühlen(31)",
    "Verhalten_(11)": "Verhalten_(11)",
    "Bedeutung_(10)": "Bedeutung_(10)",
    "Themen_(6)": "Themen_(6)",
    "Optimierung_(10)": "Optimierung_(10)",
    "Attraktionen_(36)": "Attraktionen_(36)",
    "Absicht_16_ist_zu_genügen": "Absicht_16_ist_zu_genügen",
    "Liebe_(7)": "Liebe_(7)",
    "Koalitionen_(10)": "Koalitionen_(10)",
    "Ansichten_Standpunkte_(18_17)": "Ansichten_Standpunkte_(18_17)",
    "Prinzipien(1/8)": "Prinzipien(1/8)",
    "Bestrebungen(1/5)": "Bestrebungen(1/5)",
    "Bedingung_und_Auslöser_(1/3)": "Bedingung_und_Auslöser_(1/3)",
    "relativer_Zeit-Betrag_(15_10_4_18_6)": "relativer_Zeit-Betrag_(15_10_4_18_6)",
    "Zahlenvergleich_(15_18_6)": "Zahlenvergleich_(15_18_6)",
    "Leidenschaften_(21)": "Leidenschaften_(21)",
    "Erwartungshaltungen_(26)": "Erwartungshaltungen_(26)",
    "Extremalien_(19),Ziele_(19)": "Extremalien_(19),Ziele_(19)",
    "universeller_Komperativ_(18→15)": "universeller_Komperativ_(18→15)",
    "Relation_zueinander_reziprok_Universellen_(18→n_vs._1/n)": "Relation_zueinander_reziprok_Universellen_(18→n_vs._1/n)",
    "Sollen_Frage_Vorgehensweise_(1/13)": "Sollen_Frage_Vorgehensweise_(1/13)",
    "Fundament_(1/19)": "Fundament_(1/19)",
    "abhängige_Verbundenheit_(90)": "abhängige_Verbundenheit_(90)",
    "Absicht_13_ist_Helfen": "Absicht_13_ist_Helfen",
    "Karte_Filter_und_Unterscheidung_(1/12)": "Karte_Filter_und_Unterscheidung_(1/12)",
}
wahl15 = {
    #    "_": "Strukturalien_bzw_Meta-Paradigmen_bzw_Transzendentalien_(15),Geist_(15)",
    "_15": "Strukturalien_bzw_Meta-Paradigmen_bzw_Transzendentalien_(15),Geist_(15),Model_of_Hierarchical_Complexity,"
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

befehle = {"15" + a: "15" + a for a in wahl15.keys()} | {
    "mond": "mond",
    "reta": "reta",
    "absicht": "absicht",
    "motiv": "motiv",
    "thomas": "thomas",
    "universum": "universum",
    "motive": "motive",
    "absichten": "absichten",
    "vielfache": "vielfache",
    "einzeln": "einzeln",
    "multis": "multis",
    "modulo": "modulo",
    "prim": "prim",
    "primfaktorzerlegung": "primfaktorzerlegung",
    "procontra": "procontra",
    "prim24": "prim24",
    "primfaktorzerlegungModulo24": "primfaktorzerlegungModulo24",
    "help": "help",
    "hilfe": "hilfe",
    "abc": "abc",
    "abcd": "abcd",
    "alles": "alles",
    "a": "a",
    "u": "u",
    "befehle": "befehle",
    "t": "t",
    "richtung": "richtung",
    "r": "r",
    "v": "v",
    "h": "h",
    "p": "p",
    "mo": "mo",
    "mu": "mu",
    "primzahlkreuz": "primzahlkreuz",
    "ende": "ende",
    "exit": "exit",
    "quit": "quit",
    "q": "q",
    ":q": ":q",
    "shell": "shell",
    "s": "s",
    "math": "math",
    "loggen": "loggen",
    "nichtloggen": "nichtloggen",
    "mulpri": "mulpri",
    "python": "python",
    "w": "w",
    "teiler": "teiler",
    "BefehlSpeichernDanach": "BefehlSpeichernDanach",
    "S": "S",
    "BefehlSpeicherungLöschen": "BefehlSpeicherungLöschen",
    "l": "l",
    "BefehlSpeicherungAusgeben": "BefehlSpeicherungAusgeben",
    "o": "o",
    # "BefehlsSpeicherungsModusAus": "BefehlsSpeicherungsModusAus",
    # "x": "x",
    "BefehlSpeichernDavor": "BefehlSpeichernDavor",
    "keineEinZeichenZeilenPlusKeineAusgabeWelcherBefehlEsWar": "keineEinZeichenZeilenPlusKeineAusgabeWelcherBefehlEsWar",
}

ParametersMain1: namedtuple = namedtuple(
    "ParametersMain",
    "wichtigste wichtigste2 religionen galaxie strukturgroesse universum wirtschaft menschliches procontra licht bedeutung symbole Multiplikationen konzept konzept2 inkrementieren operationen universummetakonkret primzahlwirkung gebrochenuniversum gebrochengalaxie primvielfache planet strukturenkleinere grundstrukturen alles",
)

ParametersMain = ParametersMain1(
    {
        "Wichtigstes_zum_verstehen": "Wichtigstes_zum_verstehen",
        "wichtigsteverstehen": "wichtigsteverstehen",
    },
    {
        "Wichtigstes_zum_gedanklich_einordnen": "Wichtigstes_zum_gedanklich_einordnen",
        "wichtigsteeinordnen": "wichtigsteeinordnen",
    },
    {
        "Religionen": "Religionen",
        "religionen": "religionen",
        "religion": "religion",
    },
    {
        "Galaxie": "Galaxie",
        "galaxie": "galaxie",
        "alteschriften": "alteschriften",
        "kreis": "kreis",
        "galaxien": "galaxien",
        "kreise": "kreise",
    },
    {
        "Größenordnung": "Größenordnung",
        "groessenordnung": "groessenordnung",
        "strukturgroesse": "strukturgroesse",
        "strukturgroeße": "strukturgroeße",
        "strukturgrösse": "strukturgrösse",
        "strukturgröße": "strukturgröße",
        "groesse": "groesse",
        "stufe": "stufe",
        "organisationen": "organisationen",
    },
    {
        "Universum": "Universum",
        "universum": "universum",
        "transzendentalien": "transzendentalien",
        "strukturalien": "strukturalien",
        "kugel": "kugel",
        "kugeln": "kugeln",
        "ball": "ball",
        "baelle": "baelle",
        "bälle": "bälle",
    },
    {"Wirtschaft": "Wirtschaft", "wirtschaft": "wirtschaft"},
    {
        "Menschliches": "Menschliches",
        "menschliches": "menschliches",
    },
    {
        "Pro_Contra": "Pro_Contra",
        "procontra": "procontra",
        "dagegendafuer": "dagegendafuer",
    },
    {
        "Licht": "Licht",
        "licht": "licht",
    },
    {
        "Bedeutung": "Bedeutung",
        "bedeutung": "bedeutung",
    },
    {
        "Symbole": "Symbole",
        "symbole": "symbole",
    },
    {a[0]: a[0] for a in Multiplikationen},
    {
        "Eigenschaften_n": "Eigenschaften_n",
        "eigenschaften": "eigenschaften",
        "eigenschaft": "eigenschaft",
        "konzept": "konzept",
        "konzepte": "konzepte",
    },
    {
        "Eigenschaften_1/n": "Eigenschaften_1/n",
        "konzept2": "konzept2",
        "konzepte2": "konzepte2",
    },
    {
        "Inkrementieren": "Inkrementieren",
        "inkrementieren": "inkrementieren",
    },
    {
        "Operationen": "Operationen",
        "operationen": "operationen",
    },
    {
        "Meta_vs_Konkret_{Universum}": "Meta_vs_Konkret_{Universum}",
        "universummetakonkret": "universummetakonkret",
    },
    {
        "Primzahlwirkung": "Primzahlwirkung",
        "primzahlwirkung": "primzahlwirkung",
    },
    {"gebrochenuniversum": "gebrochenuniversum"},
    {"gebrochengalaxie": "gebrochengalaxie"},
    {"Multiplikationen": "Multiplikationen", "multiplikationen": "multiplikationen"},
    {"Planet_{10_und_oder_12}": "Planet_{10_und_oder_12}", "planet": "planet"},
    {
        "Strukturen_1_bis_9": "Strukturen_1_bis_9",
        "strukturkleinerzehn": "strukturkleinerzehn",
    },
    {"Grundstrukturen": "Grundstrukturen", "grundstrukturen": "grundstrukturen"},
    {"alles": "alles"},
)


paraNdataMatrix: list[
    tuple[
        tuple[str],
        set[int],
        set[tuple[int]],
        set,
        set,
        set[tuple[Optional[int], Optional[int]]],
        set,
        set[list[str]],
        set[str],
    ]
] = [
    (
        ParametersMain.wichtigste,
        {
            "Wichtigste": "Wichtigste",
            "wichtigste": "wichtigste",
        },
        {10, 5, 4, 8},
    ),
    (
        ParametersMain.menschliches,
        {
            "Mensch-zu-Tier": "Mensch-zu-Tier",
            "menschtier": "menschtier",
            "tiermensch": "tiermensch",
        },
        {314},
    ),
    (
        ParametersMain.menschliches,
        {
            "Ansichten_Standpunkte_(18_17)": "Ansichten_Standpunkte_(18_17)",
            "ansichten": "ansichten",
        },
        {240, 346},
    ),
    (
        ParametersMain.menschliches,
        {
            "(politische)_Richtungen_(7)": "(politische)_Richtungen_(7)",
            "richtungen": "richtungen",
            "politische": "politische",
        },
        {235},
    ),
    (
        ParametersMain.planet,
        {
            "Wirklichkeiten_(10)": "Wirklichkeiten_(10)",
            "wirklichkeit": "wirklichkeit",
            "wirklichkeiten": "wirklichkeiten",
        },
        {233, 265, 268, 322},
    ),
    (
        ParametersMain.planet,
        {
            "Meta-Systeme_(12)": "Meta-Systeme_(12)",
            "metasysteme": "metasysteme",
            "metasystem": "metasystem",
            "meta-systeme": "meta-systeme",
            "meta-system": "meta-system",
        },
        {232, 288, 334},
    ),
    (
        ParametersMain.planet,
        {"Intelligenz": "Intelligenz", "intelligenz": "intelligenz"},
        {214},
    ),
    (
        ParametersMain.planet,
        {
            "Gleichheit_Freiheit_Ordnung": "Gleichheit_Freiheit_Ordnung",
            "gleichheit": "gleichheit",
            "freiheit": "freiheit",
            "ordnung": "ordnung",
        },
        {132, 324, 328, 79, 80, 331, 335},
    ),
    (
        ParametersMain.planet,
        {
            "Komplexität": "Komplexität",
            "komplexität": "komplexität",
            "komplexitaet": "komplexitaet",
        },
        {213},
    ),
    (
        ParametersMain.planet,
        {
            "Mechanismen": "Mechanismen",
            "mechanismen": "mechanismen",
            "mechanismus": "mechanismus",
        },
        {107},
    ),
    (
        ParametersMain.wichtigste,
        {
            "Zweitwichtigste": "Zweitwichtigste",
            "zweitwichtigste": "zweitwichtigste",
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
            "Drittwichtigste": "Drittwichtigste",
            "drittwichtigste": "drittwichtigste",
        },
        {64},
    ),
    (
        ParametersMain.wichtigste,
        {
            "Motive_Sternpolygone": "Motive_Sternpolygone",
            "viertwichtigste": "viertwichtigste",
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
        {"Wichtigste": "Wichtigste", "wichtigstes": "wichtigstes"},
        {0, 1, 2, 36, 37, 207},
    ),
    (
        ParametersMain.wichtigste2,
        {"Zweitwichtigste": "Zweitwichtigste", "zweitwichtigste": "zweitwichtigste"},
        {30},
    ),
    (
        ParametersMain.operationen,
        {
            "Halbierung": "Halbierung",
            "halbierung": "halbierung",
            "halbierungen": "halbierungen",
        },
        {86},
    ),
    (
        ParametersMain.religionen,
        {
            "Religions-Gründer-Typ": "Religions-Gründer-Typ",
            "religionsgründertyp": "religionsgründertyp",
            "prophet": "prophet",
            "archon": "archon",
            "religionsgruendertyp": "religionsgruendertyp",
        },
        {72},
    ),
    (
        ParametersMain.religionen,
        {"Hinduismus": "Hinduismus", "hinduismus": "hinduismus"},
        {217},
    ),
    (
        ParametersMain.religionen,
        {"Sternpolygon": "Sternpolygon", "sternpolygon": "sternpolygon"},
        {0, 6, 36},
    ),
    (
        ParametersMain.religionen,
        {
            "der_Tierkreiszeichen": "der_Tierkreiszeichen",
            "dertierkreiszeichen": "dertierkreiszeichen",
            "babylon": "babylon",
        },
        {0, 36, 207},
    ),
    (
        ParametersMain.religionen,
        {
            "Sternpolygon_vs_gleichförmiges": "Sternpolygon_vs_gleichförmiges",
            "vergleich": "vergleich",
            "sternpolygonvsgleichfoermiges": "sternpolygonvsgleichfoermiges",
            "vergleichnvs1divn": "vergleichnvs1divn",
        },
        {87},
    ),
    (
        ParametersMain.religionen,
        {
            "Messias": "Messias",
            "messias": "messias",
            "heptagramm": "heptagramm",
            "hund": "hund",
            "messiase": "messiase",
            "messiasse": "messiasse",
        },
        {7},
    ),
    (
        ParametersMain.religionen,
        {
            "gleichförmiges_Polygon": "gleichförmiges_Polygon",
            "gleichförmigespolygon": "gleichförmigespolygon",
            "gleichfoermigespolygon": "gleichfoermigespolygon",
            "nichtsternpolygon": "nichtsternpolygon",
            "polygon": "polygon",
        },
        {16, 37},
    ),
    (
        ParametersMain.religionen,
        {
            "Vertreter_höherer_Konzepte": "Vertreter_höherer_Konzepte",
            "vertreterhoehererkonzepte": "vertreterhoehererkonzepte",
            "galaxien": "galaxien",
            "galaxie": "galaxie",
            "schwarzesonne": "schwarzesonne",
            "schwarzesonnen": "schwarzesonnen",
            "universum": "universum",
            "universen": "universen",
            "kreis": "kreis",
            "kreise": "kreise",
            "kugel": "kugel",
            "kugeln": "kugeln",
        },
        {23},
    ),
    (
        ParametersMain.galaxie,
        {
            "Offenbarung_des_Johannes": "Offenbarung_des_Johannes",
            "offenbarung": "offenbarung",
            "offenbarungdesjohannes": "offenbarungdesjohannes",
            "johannes": "johannes",
            "bibel": "bibel",
            "offenbarungjohannes": "offenbarungjohannes",
        },
        {90},
    ),
    (
        ParametersMain.inkrementieren,
        {
            "Teilchen-Meta-Physik": "Teilchen-Meta-Physik",
            "addition": "addition",
            "identitaet": "identitaet",
            "Identität": "Identität",
        },
        {219, 223, 307, 308, 333},
    ),
    (
        ParametersMain.galaxie,
        {
            "Hochzüchten": "Hochzüchten",
            "hochzüchten": "hochzüchten",
            "hochzuechten": "hochzuechten",
        },
        {318, 319},
    ),
    (
        ParametersMain.universum,
        {
            "Universelles_Verhältnis_gleicher_Zahlen": "Universelles_Verhältnis_gleicher_Zahlen",
            "verhaeltnisgleicherzahl": "verhaeltnisgleicherzahl",
        },
        {383},
    ),
    (
        ParametersMain.universum,
        {"universelles_Recht": "universelles_Recht", "recht": "recht", "jura": "jura"},
        {382, 34, 65},
    ),
    (
        ParametersMain.universum,
        {
            "sowas_wie_Kombinieren_Verknüpfen": "sowas_wie_Kombinieren_Verknüpfen",
            "kombinierenetc": "kombinierenetc",
        },
        {320},
    ),
    (
        ParametersMain.universum,
        {
            "Hochzüchten": "Hochzüchten",
            "hochzüchten": "hochzüchten",
            "hochzuechten": "hochzuechten",
        },
        {318, 319},
    ),
    (
        ParametersMain.universum,
        {
            "Teilchen-Meta-Physik": "Teilchen-Meta-Physik",
            "addition": "addition",
            "identitaet": "identitaet",
            "Identität": "Identität",
        },
        {219, 223, 307, 308, 333},
    ),
    (
        ParametersMain.universum,
        {
            "keine_Nur-Paradigma-Religionen": "keine_Nur-Paradigma-Religionen",
            "metaparadigmareligion": "metaparadigmareligion",
        },
        {190, 191, 196},
    ),
    (
        ParametersMain.universum,
        {
            "Kugeln_Kreise": "Kugeln_Kreise",
            "kugelnkreise": "kugelnkreise",
            "kugeln": "kugeln",
            "kreise": "kreise",
        },
        {77, 145},
    ),
    (
        ParametersMain.galaxie,
        {
            "Kugeln_Kreise": "Kugeln_Kreise",
            "kugelnkreise": "kugelnkreise",
            "kugeln": "kugeln",
            "kreise": "kreise",
        },
        {77, 145},
    ),
    (
        ParametersMain.galaxie,
        {
            "chinesisches_Horoskop": "chinesisches_Horoskop",
            "chinesischeshoroskop": "chinesischeshoroskop",
            "china": "china",
        },
        {91},
    ),
    (
        ParametersMain.galaxie,
        {
            "babylonische_Tierkreiszeichen": "babylonische_Tierkreiszeichen",
            "tierkreiszeichen": "tierkreiszeichen",
            "babylon": "babylon",
        },
        {1, 2},
    ),
    (
        ParametersMain.galaxie,
        {
            "Thomasevangelium": "Thomasevangelium",
            "thomasevangelium": "thomasevangelium",
            "thomas": "thomas",
        },
        {0, 3, 303},
    ),
    (
        ParametersMain.galaxie,
        {
            "analytische_Ontologie": "analytische_Ontologie",
            "analytischeontologie": "analytischeontologie",
            "ontologie": "ontologie",
        },
        {84},
    ),
    (
        ParametersMain.galaxie,
        {
            "Transzendentalien_innen_außen": "Transzendentalien_innen_außen",
            "innenaussenstrukur": "innenaussenstrukur",
            "strukturalieninnenaußen": "strukturalieninnenaußen",
            "strukturalieninnenaussen": "strukturalieninnenaussen",
            "innenaußenstrukur": "innenaußenstrukur",
            "transzendentalieninnenaußen": "transzendentalieninnenaußen",
            "transzendentalieninnenaussen": "transzendentalieninnenaussen",
        },
        {149},
    ),
    (
        ParametersMain.galaxie,
        {
            "Modallogik": "Modallogik",
            "modallogik": "modallogik",
        },
        {148},
    ),
    (
        ParametersMain.operationen,
        {
            "5": "5",
            "fünf": "fünf",
            "fünfer": "fünfer",
            "fünferstruktur": "fünferstruktur",
            "fuenf": "fuenf",
            "fuenfer": "fuenfer",
            "fuenferstruktur": "fuenferstruktur",
        },
        {96},
    ),
    (
        ParametersMain.operationen,
        {
            "9": "9",
            "neun": "neun",
            "neuner": "neuner",
            "neunerstruktur": "neunerstruktur",
        },
        {94},
    ),
    (
        ParametersMain.operationen,
        {
            "3": "3",
            "drei": "drei",
            "dreier": "dreier",
            "dreierstruktur": "dreierstruktur",
        },
        {92, 93, 315, 316},
    ),
    (
        ParametersMain.strukturgroesse,
        {
            "Licht": "Licht",
            "licht": "licht",
        },
        {20, 27, 313},
    ),
    (
        ParametersMain.strukturgroesse,
        {
            "Strukturgrösse": "Strukturgrösse",
            "größe": "größe",
            "groesse": "groesse",
            "gross": "gross",
            "strukturgroesse": "strukturgroesse",
            "strukturgroeße": "strukturgroeße",
            "strukturgrösse": "strukturgrösse",
            "strukturgröße": "strukturgröße",
        },
        {4, 21, 54, 197},
    ),
    (
        ParametersMain.strukturgroesse,
        {
            "Organisationen": "Organisationen",
            "organisationen": "organisationen",
            "organisation": "organisation",
        },
        {30, 82},
    ),
    (
        ParametersMain.strukturgroesse,
        {
            "politische_Systeme": "politische_Systeme",
            "politischesysteme": "politischesysteme",
            "politik": "politik",
        },
        {83},
    ),
    (
        ParametersMain.universummetakonkret,
        {"meta": "meta"},
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
        {"konkret": "konkret"},
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
        {"Theorie": "Theorie", "theorie": "theorie"},
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
        {"Praxis": "Praxis", "praxis": "praxis"},
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
            "Management": "Management",
            "management": "management",
            "stau": "stau",
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
            "verändernd": "verändernd",
            "veraendernd": "veraendernd",
            "fluss": "fluss",
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
            "ganzheitlich": "ganzheitlich",
            "mathematisch_diskret": "mathematisch_diskret",
            "diskret": "diskret",
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
            "darüber_hinausgehend": "darüber_hinausgehend",
            "hinausgehend": "hinausgehend",
            "kontinuierlich": "kontinuierlich",
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
            "Universum_Strukturalien_Transzendentalien": "Universum_Strukturalien_Transzendentalien",
            "universum": "universum",
            "strukturalie": "strukturalie",
            "strukturalien": "strukturalien",
            "transzendentalien": "transzendentalien",
            "transzendentalie": "transzendentalie",
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
            "Richtung_als_Richtung": "Richtung_als_Richtung",
            "richtungrichtung": "richtungrichtung",
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
            "Galaxieabsicht": "Galaxieabsicht",
            "absichtgalaxie": "absichtgalaxie",
            "absicht": "absicht",
            "motive": "motive",
            "motiv": "motiv",
            "absichten": "absichten",
            "galaxie": "galaxie",
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
            "Absicht_Reziproke_Galaxie": "Absicht_Reziproke_Galaxie",
            "absichtgalaxiereziproke": "absichtgalaxiereziproke",
            "absichtreziproke": "absichtreziproke",
            "motivereziproke": "motivereziproke",
            "motivreziproke": "motivreziproke",
            "absichtenreziproke": "absichtenreziproke",
            "galaxiereziproke": "galaxiereziproke",
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
            "Universum_Reziproke": "Universum_Reziproke",
            "universumreziproke": "universumreziproke",
            "strukturaliereziproke": "strukturaliereziproke",
            "strukturalienreziproke": "strukturalienreziproke",
            "transzendentalienreziproke": "transzendentalienreziproke",
            "transzendentaliereziproke": "transzendentaliereziproke",
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
            "Dagegen-Gegentranszendentalie": "Dagegen-Gegentranszendentalie",
            "dagegengegentranszendentalie": "dagegengegentranszendentalie",
            "dagegengegentranszendentalien": "dagegengegentranszendentalien",
            "dagegengegenstrukturalien": "dagegengegenstrukturalien",
            "dagegengegenstrukturalie": "dagegengegenstrukturalie",
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
            "neutrale_Gegentranszendentalie": "neutrale_Gegentranszendentalie",
            "neutralegegentranszendentalie": "neutralegegentranszendentalie",
            "neutralegegentranszendentalien": "neutralegegentranszendentalien",
            "neutralegegenstrukturalien": "neutralegegenstrukturalien",
            "neutralegegenstrukturalie": "neutralegegenstrukturalie",
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
            "Unternehmung_Geschäft": "Unternehmung_Geschäft",
            "unternehmen": "unternehmen",
            "unternehmung": "unternehmung",
            "geschaeft": "geschaeft",
            "geschäft": "geschäft",
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
        {"wertvoll": "wertvoll", "wert": "wert"},
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
            "Beherrschen": "Beherrschen",
            "regieren": "regieren",
            "beherrschen": "beherrschen",
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
            "Richtung": "Richtung",
            "richtung": "richtung",
            "gut": "gut",
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
            "analytische_Ontologie": "analytische_Ontologie",
            "analytischeontologie": "analytischeontologie",
            "ontologie": "ontologie",
        },
        {84},
    ),
    (
        ParametersMain.universum,
        {
            "Gegentranszendentalien": "Gegentranszendentalien",
            "gegentranszendentalien": "gegentranszendentalien",
            "gegentranszendentalie": "gegentranszendentalie",
            "gegenstrukturalien": "gegenstrukturalien",
            "gegenalien": "gegenalien",
            "gegenuniversalien": "gegenuniversalien",
        },
        {138, 202},
    ),
    (
        ParametersMain.universum,
        {"Systemsachen": "Systemsachen", "systemsachen": "systemsachen"},
        {
            150,
        },
    ),
    (
        ParametersMain.universum,
        {
            "Transzendentalien": "Transzendentalien",
            "transzendentalien": "transzendentalien",
            "transzendentalie": "transzendentalie",
            "strukturalien": "strukturalien",
            "alien": "alien",
            "universalien": "universalien",
        },
        {5, 54, 55, 198},
    ),
    (
        ParametersMain.universum,
        {
            "Reziproke_von_Transzendentalien": "Reziproke_von_Transzendentalien",
            "transzendentalienreziproke": "transzendentalienreziproke",
            "transzendentaliereziproke": "transzendentaliereziproke",
            "strukturalienreziproke": "strukturalienreziproke",
            "alienreziproke": "alienreziproke",
            "universalienreziproke": "universalienreziproke",
        },
        {131, 201},
    ),
    (
        ParametersMain.universum,
        {"Netzwerk": "Netzwerk", "netzwerk": "netzwerk"},
        {25},
    ),
    (
        ParametersMain.universum,
        {
            "warum_Transzendentalie_=_Strukturgroesse_=_Charakter": "warum_Transzendentalie_=_Strukturgroesse_=_Charakter",
            "warumtranszendentaliezustrukturgroesseundcharakter": "warumtranszendentaliezustrukturgroesseundcharakter",
        },
        {4, 54, 5, 165},
    ),
    (
        ParametersMain.universum,
        {"Kategorie": "Kategorie", "kategorie": "kategorie"},
        {204, 205, 281},
    ),
    (
        ParametersMain.universum,
        {"Raum-Missionen": "Raum-Missionen", "weltall": "weltall"},
        {218},
    ),
    (
        ParametersMain.universum,
        {
            "Programmier-Paradigmen": "Programmier-Paradigmen",
            "programmierparadigmen": "programmierparadigmen",
        },
        {351},
    ),
    (
        ParametersMain.galaxie,
        {"Raum-Missionen": "Raum-Missionen", "weltall": "weltall"},
        {218},
    ),
    (
        ParametersMain.universum,
        {"Geist__(15)": "Geist__(15)", "geist": "geist"},
        {242},
    ),
    (
        ParametersMain.universum,
        {
            "warum_Transzendentalie_=_Komplexität_von_Michael_Commons": "warum_Transzendentalie_=_Komplexität_von_Michael_Commons",
            "warumtranszendentaliegleichkomplexitaet": "warumtranszendentaliegleichkomplexitaet",
        },
        {65, 5, 166},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Model_of_Hierarchical_Complexity": "Model_of_Hierarchical_Complexity",
            "modelofhierarchicalcomplexity": "modelofhierarchicalcomplexity",
            "komplex": "komplex",
            "komplexität": "komplexität",
            "komplexitaet": "komplexitaet",
            "complexity": "complexity",
            "model": "model",
            "abstraktion": "abstraktion",
        },
        {65, 75, 203},
    ),
    (
        ParametersMain.universum,
        {
            "Model_of_Hierarchical_Complexity": "Model_of_Hierarchical_Complexity",
            "modelofhierarchicalcomplexity": "modelofhierarchicalcomplexity",
            "komplex": "komplex",
            "komplexität": "komplexität",
            "komplexitaet": "komplexitaet",
            "complexity": "complexity",
            "model": "model",
            "abstraktion": "abstraktion",
        },
        {65, 75, 203},
    ),
    (
        ParametersMain.operationen,
        {
            "2": "2",
            "zwei": "zwei",
            "gerade": "gerade",
            "ungerade": "ungerade",
            "alternierung": "alternierung",
            "alternierend": "alternierend",
            "zweierstruktur": "zweierstruktur",
        },
        {78, 79, 80, 331},
    ),
    (
        ParametersMain.operationen,
        {
            "Multiplikation": "Multiplikation",
            "multiplikation": "multiplikation",
        },
        {158},
    ),
    (
        ParametersMain.operationen,
        {
            "4": "4",
            "vier": "vier",
            "viererstruktur": "viererstruktur",
            "viererabfolgen": "viererabfolgen",
        },
        {76, 77, 81, 104, 145},
    ),
    (
        ParametersMain.menschliches,
        {
            "Gesellschaftsschicht": "Gesellschaftsschicht",
            "klasse": "klasse",
            "klassen": "klassen",
        },
        {241},
    ),
    (
        ParametersMain.menschliches,
        {"Moral": "Moral", "moral": "moral", "warummoral": "warummoral"},
        {215, 216},
        {(216, 221)},
    ),
    (
        ParametersMain.menschliches,
        {
            "Fachgebiete": "Fachgebiete",
            "fachgebiete": "fachgebiete",
            "fachbereiche": "fachbereiche",
            "themen": "themen",
        },
        {183},
    ),
    (
        ParametersMain.wirtschaft,
        {
            "Fachgebiete": "Fachgebiete",
            "fachgebiete": "fachgebiete",
            "fachbereiche": "fachbereiche",
            "themen": "themen",
        },
        {183},
    ),
    (
        ParametersMain.wirtschaft,
        {
            "Pflanzen": "Pflanzen",
            "pflanzen": "pflanzen",
        },
        {113},
    ),
    (
        ParametersMain.wirtschaft,
        {
            "Maschinen": "Maschinen",
            "maschinen": "maschinen",
            "maschine": "maschine",
            "gerät": "gerät",
            "geräte": "geräte",
            "geraete": "geraete",
            "geraet": "geraet",
        },
        {89},
    ),
    (
        ParametersMain.wirtschaft,
        {
            "Organisationsform": "Organisationsform",
            "organisationsform": "organisationsform",
            "organisationsart": "organisationsart",
            "firma": "firma",
            "verein": "verein",
        },
        {99},
    ),
    (
        ParametersMain.wirtschaft,
        {
            "System": "System",
            "system": "system",
        },
        {
            69,
        },
    ),
    (
        ParametersMain.wirtschaft,
        {
            "realistisch": "realistisch",
            "funktioniert": "funktioniert",
        },
        {70},
    ),
    (
        ParametersMain.wirtschaft,
        {
            "Erklärung": "Erklärung",
            "erklärung": "erklärung",
            "erklaerung": "erklaerung",
        },
        {71},
    ),
    (
        ParametersMain.wirtschaft,
        {
            "BWL": "BWL",
            "bwl": "bwl",
        },
        {109},
    ),
    (
        ParametersMain.menschliches,
        {
            "Sinn_des_Lebens": "Sinn_des_Lebens",
            "sinndeslebens": "sinndeslebens",
            "lebenssinn": "lebenssinn",
            "sinn": "sinn",
            "sinnsuche": "sinnsuche",
        },
        {88, 189},
        {(181, 182)},
    ),
    (
        ParametersMain.menschliches,
        {
            "Intelligenzprobleme": "Intelligenzprobleme",
            "intelligenzprobleme": "intelligenzprobleme",
            "intelligenzmaengel": "intelligenzmaengel",
            "intelligenzmängel": "intelligenzmängel",
        },
        {147},
    ),
    (
        ParametersMain.menschliches,
        {
            "Denkweise_von_Lebewesen": "Denkweise_von_Lebewesen",
            "lebewesendenkweise": "lebewesendenkweise",
            "denkweise": "denkweise",
        },
        {146},
    ),
    (
        ParametersMain.menschliches,
        {
            "Gegentranszendentalien": "Gegentranszendentalien",
            "gegentranszendentalien": "gegentranszendentalien",
            "gegenstrukturalien": "gegenstrukturalien",
        },
        {138, 139, 202},
    ),
    (
        ParametersMain.menschliches,
        {
            "Gleichheit_Freiheit": "Gleichheit_Freiheit",
            "gleichheitfreiheit": "gleichheitfreiheit",
            "ungleichheit": "ungleichheit",
            "dominieren": "dominieren",
            "gleichheit": "gleichheit",
            "freiheit": "freiheit",
        },
        {132, 328, 331, 335},
    ),
    (
        ParametersMain.menschliches,
        {
            "Gefühle": "Gefühle",
            "emotionen": "emotionen",
            "gefuehle": "gefuehle",
            "gefuehle": "gefuehle",
            "emotion": "emotion",
            "gefühl": "gefühl",
            "gefuehl": "gefuehl",
        },
        {105, 230, 243, 283, 284, 285, 286, 305},
    ),
    (
        ParametersMain.menschliches,
        {
            "Egoismus": "Egoismus",
            "egoismus": "egoismus",
            "altruismus": "altruismus",
            "selbstlosigkeit": "selbstlosigkeit",
        },
        {136},
        {(66, 67)},
    ),
    (
        ParametersMain.menschliches,
        {
            "Wirkung": "Wirkung",
            "wirkung": "wirkung",
        },
        {135},
    ),
    (
        ParametersMain.menschliches,
        {
            "INCELs": "INCELs",
            "incel": "incel",
            "incels": "incels",
        },
        {68},
    ),
    (
        ParametersMain.menschliches,
        {
            "irrationale_Zahlen_durch_Wurzelbildung": "irrationale_Zahlen_durch_Wurzelbildung",
            "irrationalezahlendurchwurzelbildung": "irrationalezahlendurchwurzelbildung",
            "ausgangslage": "ausgangslage",
        },
        {73},
    ),
    (
        ParametersMain.menschliches,
        {
            "dominierendes_Geschlecht": "dominierendes_Geschlecht",
            "dominierendesgeschlecht": "dominierendesgeschlecht",
            "maennlich": "maennlich",
            "männlich": "männlich",
            "weiblich": "weiblich",
        },
        {51},
    ),
    (
        ParametersMain.menschliches,
        {
            "Liebe": "Liebe",
            "liebe": "liebe",
            "ethik": "ethik",
        },
        {8, 9, 28, 208, 330},
        {(121, 122)},
    ),
    (
        ParametersMain.menschliches,
        {
            "Glaube_Erkenntnis": "Glaube_Erkenntnis",
            "glauben": "glauben",
            "erkenntnis": "erkenntnis",
            "glaube": "glaube",
        },
        {59},
    ),
    (
        ParametersMain.menschliches,
        {
            "Angreifbarkeit": "Angreifbarkeit",
            "angreifbarkeit": "angreifbarkeit",
            "angreifbar": "angreifbar",
        },
        {58, 57},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Strukturalien_bzw_Meta-Paradigmen_bzw_Transzendentalien_(15)": "Strukturalien_bzw_Meta-Paradigmen_bzw_Transzendentalien_(15)",
            "Transzendentalien": "Transzendentalien",
            "transzendentalien": "transzendentalien",
            "transzendentalie": "transzendentalie",
            "strukturalien": "strukturalien",
            "alien": "alien",
            "universalien": "universalien",
            "meta-paradigmen": "meta-paradigmen",
        },
        {5, 229, 131},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Bedingung_und_Auslöser_(1/3)": "Bedingung_und_Auslöser_(1/3)",
            "bedingung": "bedingung",
            "bedingungen": "bedingungen",
            "auslöser": "auslöser",
            "ausloeser": "ausloeser",
        },
        {338},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Relation_zueinander_reziprok_Universellen_(18→n_vs._1/n)": "Relation_zueinander_reziprok_Universellen_(18→n_vs._1/n)",
            "relativreziprokuniversell": "relativreziprokuniversell",
        },
        {350},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "universeller_Komperativ_(18→15)": "universeller_Komperativ_(18→15)",
            "universellerkomperativ": "universellerkomperativ",
        },
        {349},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Existenzialien_(3)": "Existenzialien_(3)",
            "existenzialien": "existenzialien",
        },
        {348},
    ),
    (
        ParametersMain.grundstrukturen,
        {"Extremalien_(19)": "Extremalien_(19)", "extremalien": "extremalien"},
        {347, 352},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Erwartungshaltungen_(26)": "Erwartungshaltungen_(26)",
            "erwartungen": "erwartungen",
            "erwartungshaltungen": "erwartungshaltungen",
        },
        {344},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Leidenschaften_(21)": "Leidenschaften_(21)",
            "leidenschaft": "leidenschaft",
            "leidenschaften": "leidenschaften",
        },
        {343},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "relativer_Zeit-Betrag_(15_10_4_18_6)": "relativer_Zeit-Betrag_(15_10_4_18_6)",
            "relativerzeitbetrag": "relativerzeitbetrag",
        },
        {339},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Zahlenvergleich_(15_18_6)": "Zahlenvergleich_(15_18_6)",
            "zahlenvergleich": "zahlenvergleich",
        },
        {340},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Bestrebungen(1/5)": "Bestrebungen(1/5)",
            "bestrebung": "bestrebung",
            "bestrebungen": "bestrebungen",
        },
        {332},
    ),
    (
        ParametersMain.grundstrukturen,
        {"Prinzipien(1/8)": "Prinzipien(1/8)", "prinzipien": "prinzipien"},
        {329, 378},
    ),
    (
        ParametersMain.grundstrukturen,
        {"Attraktionen_(36)": "Attraktionen_(36)", "attraktionen": "attraktionen"},
        {311},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Optimierung_(10)": "Optimierung_(10)",
            "optimierung": "optimierung",
        },
        {310},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Themen_(6)": "Themen_(6)",
            "themen": "themen",
            "thema": "thema",
        },
        {309},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Bedeutung_(10)": "Bedeutung_(10)",
            "bedeutung": "bedeutung",
        },
        {306},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Reziprokes": "Reziprokes",
            "reziproke": "reziproke",
            "reziprokes": "reziprokes",
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
        {"Achtung_(4)": "Achtung_(4)", "achtung": "achtung", "achten": "achten"},
        {270},
    ),
    (
        ParametersMain.grundstrukturen,
        {"Zeit_(4)_als_Wirklichkeit": "Zeit_(4)_als_Wirklichkeit", "zeit": "zeit"},
        {266, 267},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Absicht_16_ist_zu_genügen": "Absicht_16_ist_zu_genügen",
            "absicht16": "absicht16",
        },
        {312},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Absicht_17_ist_zu_meinen": "Absicht_17_ist_zu_meinen",
            "absicht17": "absicht17",
        },
        {263},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Absicht_6_ist_Vorteilsmaximierung": "Absicht_6_ist_Vorteilsmaximierung",
            "absicht6": "absicht6",
        },
        {262},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Absicht_7_ist_Selbstlosigkeit": "Absicht_7_ist_Selbstlosigkeit",
            "absicht7": "absicht7",
        },
        {261},
    ),
    (
        ParametersMain.grundstrukturen,
        {"Regungen_(1)": "Regungen_(1)", "regung": "regung", "regungen": "regungen"},
        {282},
    ),
    (
        ParametersMain.grundstrukturen,
        {"Verhalten_(11)": "Verhalten_(11)", "verhalten": "verhalten"},
        {301, 302},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Energie_und_universelle_Eigenschaften_(30)": "Energie_und_universelle_Eigenschaften_(30)",
            "energie": "energie",
            "universelleeigenschaften": "universelleeigenschaften",
            "lebensenergie": "lebensenergie",
        },
        {287, 293},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Garben_und_Verhalten_nachfühlen(31)": "Garben_und_Verhalten_nachfühlen(31)",
            "garben": "garben",
            "verhaltenfuehlen": "verhaltenfuehlen",
            "verhaltenfühlen": "verhaltenfühlen",
        },
        {295},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            Primzahlkreuz_pro_contra_strs[1]: Primzahlkreuz_pro_contra_strs[1],
            "nachvollziehen": "nachvollziehen",
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
            "Empathie_(37)": "Empathie_(37)",
            "empathie": "empathie",
            "mitgefuehl": "mitgefuehl",
        },
        {294},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Absicht_1/6_ist_Reinigung_und_Klarheit": "Absicht_1/6_ist_Reinigung_und_Klarheit",
            "absicht1/6": "absicht1/6",
            "absicht1pro6": "absicht1pro6",
        },
        {298},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Absicht_10_ist_Wirklichkeit_erkennen": "Absicht_10_ist_Wirklichkeit_erkennen",
            "absicht10": "absicht10",
        },
        {260},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Geist_(15)": "Geist_(15)",
            "geist": "geist",
            "bewusstsein": "bewusstsein",
        },
        {229, 231, 242, 273, 297, 304},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Reflexe_(3)": "Reflexe_(3)",
            "reflex": "reflex",
            "reflexe": "reflexe",
        },
        {256},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Lust_(9)": "Lust_(9)",
            "lust": "lust",
        },
        {255},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Paradigmen_sind_Absichten_(13)": "Paradigmen_sind_Absichten_(13)",
            "paradigmen": "paradigmen",
            "absichten": "absichten",
        },
        {10, 42},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Wirklichkeiten_Wahrheit_Wahrnehmung_(10)": "Wirklichkeiten_Wahrheit_Wahrnehmung_(10)",
            "wirklichkeit": "wirklichkeit",
            "wirklichkeiten": "wirklichkeiten",
            "wahrheit": "wahrheit",
            "wahrnehmung": "wahrnehmung",
        },
        {233, 265, 268, 322, 342},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Stimmungen_Kombinationen_(14)": "Stimmungen_Kombinationen_(14)",
            "stimmung": "stimmung",
            "stimmungen": "stimmungen",
            "kombination": "kombination",
            "kombinationen": "kombinationen",
        },
        {290, 296, 325, 326, 327},
    ),
    (
        ParametersMain.grundstrukturen,
        {"Klassen_(20)": "Klassen_(20)", "klasse": "klasse", "klassen": "klassen"},
        {241, 289},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Ordnung_und_Filterung_12_und_1pro12": "Ordnung_und_Filterung_12_und_1pro12",
            "ordnen": "ordnen",
            "ordnenundfiltern": "ordnenundfiltern",
            "filtern": "filtern",
        },
        {132, 328, 331, 335},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Meta-Systeme_(12)": "Meta-Systeme_(12)",
            "metasysteme": "metasysteme",
            "metasystem": "metasystem",
            "meta-systeme": "meta-systeme",
            "meta-system": "meta-system",
            "menge": "menge",
            "mengen": "mengen",
        },
        {232, 288, 334},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Absicht_1/8": "Absicht_1/8",
            "absicht1pro8": "absicht1pro8",
            "absicht1/8": "absicht1/8",
        },
        {272, 379},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Ziele_(19)": "Ziele_(19)",
            "ziele": "ziele",
            "maxima": "maxima",
            "höhenvorstellungen": "höhenvorstellungen",
        },
        {271},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Konkreta_und_Focus_(2)": "Konkreta_und_Focus_(2)",
            "konkreta": "konkreta",
            "focus": "focus",
            "fokus": "fokus",
        },
        {250, 269},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Gefühle_(7)": "Gefühle_(7)",
            "gefuehle": "gefuehle",
            "emotionen": "emotionen",
            "gefühle": "gefühle",
        },
        {243, 283, 284, 285, 286, 305},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "abhängige_Verbundenheit_(90)": "abhängige_Verbundenheit_(90)",
            "abhaengigkeit": "abhaengigkeit",
            "abhängigkeit": "abhängigkeit",
        },
        {357},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Karte_Filter_und_Unterscheidung_(1/12)": "Karte_Filter_und_Unterscheidung_(1/12)",
            "karte": "karte",
            "filter": "filter",
            "unterscheidung": "unterscheidung",
        },
        {377},
    ),
    (
        ParametersMain.grundstrukturen,
        {"Fundament_(1/19)": "Fundament_(1/19)", "fundament": "fundament"},
        {356},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Gedanken_sind_Positionen_(17)": "Gedanken_sind_Positionen_(17)",
            "positionen": "positionen",
            "gedanken": "gedanken",
        },
        {249, 317, 323},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Funktionen_Vorstellungen_(16)": "Funktionen_Vorstellungen_(16)",
            "vorstellungen": "vorstellungen",
            "vorstellung": "vorstellung",
            "funktionen": "funktionen",
        },
        {345, 264},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Sollen_Frage_Vorgehensweise_(1/13)": "Sollen_Frage_Vorgehensweise_(1/13)",
            "sollen": "sollen",
            "frage": "frage",
            "vorgehensweise": "vorgehensweise",
        },
        {353, 354},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Ansichten_Standpunkte_(18_17)": "Ansichten_Standpunkte_(18_17)",
            "ansichten": "ansichten",
        },
        {240, 346},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Verbundenheiten_(18)": "Verbundenheiten_(18)",
            "verbundenheiten": "verbundenheiten",
        },
        {252, 299, 300, 336},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Absicht_13_ist_Helfen": "Absicht_13_ist_Helfen",
            "absicht13": "absicht13",
            "helfen": "helfen",
        },
        {370},
    ),
    (
        ParametersMain.grundstrukturen,
        {"Liebe_(7)": "Liebe_(7)", "liebe": "liebe"},
        {8, 9, 28, 208, 221, 330},
        {(121, 122)},
    ),
    (
        ParametersMain.grundstrukturen,
        {"Koalitionen_(10)": "Koalitionen_(10)", "koalitionen": "koalitionen"},
        {321},
    ),
    (
        ParametersMain.grundstrukturen,
        {"Impulse_(5)": "Impulse_(5)", "impulse": "impulse"},
        {251, 253, 257, 341},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Triebe_und_Bedürfnisse_(6)": "Triebe_und_Bedürfnisse_(6)",
            "trieb": "trieb",
            "triebe": "triebe",
            "bedürfnis": "bedürfnis",
            "bedürfnisse": "bedürfnisse",
        },
        {254},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Reflektion_und_Kategorien_(1/15)": "Reflektion_und_Kategorien_(1/15)",
            "reflektion": "reflektion",
            "kategorien": "kategorien",
        },
        {204, 205, 281},
    ),
    (
        ParametersMain.grundstrukturen,
        {
            "Modus_und_Sein_(8)": "Modus_und_Sein_(8)",
            "zustaende": "zustaende",
            "zustände": "zustände",
            "modus": "modus",
            "modi": "modi",
            "sein": "sein",
        },
        {234, 337},
    ),
    (
        ParametersMain.menschliches,
        {
            "Motive": "Motive",
            "motive": "motive",
            "motivation": "motivation",
            "motiv": "motiv",
            "absicht": "absicht",
            "absichten": "absichten",
        },
        {10, 18, 42, 167, 168, 149, 229, 230},
    ),
    (
        ParametersMain.menschliches,
        {
            "Gedanken_sind_Positionen_(17)": "Gedanken_sind_Positionen_(17)",
            "positionen": "positionen",
            "gedanken": "gedanken",
        },
        {249, 276},
    ),
    (
        ParametersMain.menschliches,
        {
            "Bewusstsein_und_Wahrnehmung": "Bewusstsein_und_Wahrnehmung",
            "bewusstsein": "bewusstsein",
            "wahrnehmung": "wahrnehmung",
        },
        {265, 229, 231, 281, 304, 342},
    ),
    (
        ParametersMain.menschliches,
        {
            "Errungenschaften": "Errungenschaften",
            "errungenschaften": "errungenschaften",
            "ziele": "ziele",
            "erhalten": "erhalten",
        },
        {11, 257, 251},
    ),
    (
        ParametersMain.menschliches,
        {
            "evolutionär_erwerben_und_Intelligenz_Kreativität": "evolutionär_erwerben_und_Intelligenz_Kreativität",
            "evolutionärerwerbenundintelligenz": "evolutionärerwerbenundintelligenz",
            "intelligenz": "intelligenz",
            "erwerben": "erwerben",
            "erlernen": "erlernen",
            "lernen": "lernen",
            "evolutionaer": "evolutionaer",
            "evolutionär": "evolutionär",
            "kreativität": "kreativität",
            "kreativitaet": "kreativitaet",
            "kreativ": "kreativ",
        },
        {12, 47, 27, 13, 32},
    ),
    (
        ParametersMain.menschliches,
        {
            "brauchen": "brauchen",
            "benoetigen": "benoetigen",
            "benötigen": "benötigen",
            "notwendig": "notwendig",
        },
        {13, 14},
    ),
    (
        ParametersMain.menschliches,
        {
            "Krankheit": "Krankheit",
            "krankheit": "krankheit",
            "krankheiten": "krankheiten",
            "pathologisch": "pathologisch",
            "pathologie": "pathologie",
            "psychiatrisch": "psychiatrisch",
        },
        {24},
    ),
    (
        ParametersMain.menschliches,
        {
            "alpha_beta": "alpha_beta",
            "alphabeta": "alphabeta",
            "alpha": "alpha",
            "beta": "beta",
            "omega": "omega",
            "sigma": "sigma",
        },
        {46},
    ),
    (
        ParametersMain.menschliches,
        {
            "Anführer": "Anführer",
            "anfuehrer": "anfuehrer",
            "chef": "chef",
        },
        {29, 170},
    ),
    (
        ParametersMain.menschliches,
        {
            "Manipulation": "Manipulation",
            "manipulation": "manipulation",
        },
        {153},
    ),
    (
        ParametersMain.menschliches,
        {
            "Berufe": "Berufe",
            "berufe": "berufe",
            "beruf": "beruf",
        },
        {30},
    ),
    (
        ParametersMain.menschliches,
        {
            "Lösungen": "Lösungen",
            "lösungen": "lösungen",
            "loesungen": "loesungen",
            "loesung": "loesung",
            "lösungen": "lösungen",
        },
        {31},
    ),
    (ParametersMain.menschliches, {"Musik": "Musik", "musik": "musik"}, {33}),
    (
        ParametersMain.procontra,
        {
            "ergibt_Sinn": "ergibt_Sinn",
            "ergibtsinn": "ergibtsinn",
            "machtsinn": "machtsinn",
            "sinn": "sinn",
        },
        {140},
    ),
    (
        ParametersMain.procontra,
        {
            "Veränderung": "Veränderung",
            "veraenderung": "veraenderung",
            "veraendern": "veraendern",
            "veränderung": "veränderung",
            "verändern": "verändern",
        },
        {142},
    ),
    (
        ParametersMain.procontra,
        {
            "bändigen_kontrollieren": "bändigen_kontrollieren",
            "baendigenkontrollieren": "baendigenkontrollieren",
            "kontrollieren": "kontrollieren",
            "baendigen": "baendigen",
            "bändigen": "bändigen",
        },
        {143},
    ),
    (
        ParametersMain.procontra,
        {
            "vereinen": "vereinen",
            "einheit": "einheit",
        },
        {144},
    ),
    (
        ParametersMain.procontra,
        {
            "Vorteile": "Vorteile",
            "vorteile": "vorteile",
            "veraenderungnutzen": "veraenderungnutzen",
        },
        {141},
    ),
    (
        ParametersMain.procontra,
        {
            "Gegenspieler": "Gegenspieler",
            "gegenspieler": "gegenspieler",
            "antagonist": "antagonist",
        },
        {137},
    ),
    (
        ParametersMain.procontra,
        {"nervig": "nervig"},
        {120},
    ),
    (
        ParametersMain.procontra,
        {
            "pro_nutzen": "pro_nutzen",
            "pronutzen": "pronutzen",
        },
        {117},
    ),
    (
        ParametersMain.procontra,
        {
            "Gegenposition": "Gegenposition",
            "gegenposition": "gegenposition",
        },
        {116},
    ),
    (
        ParametersMain.procontra,
        {
            "Hilfe_erhalten": "Hilfe_erhalten",
            "hilfeerhalten": "hilfeerhalten",
        },
        {114},
    ),
    (
        ParametersMain.procontra,
        {
            "Helfen": "Helfen",
            "helfen": "helfen",
            "hilfe": "hilfe",
        },
        {115},
    ),
    (
        ParametersMain.procontra,
        {
            "Pro": "Pro",
            "pro": "pro",
            "dafür": "dafür",
            "dafuer": "dafuer",
        },
        {17, 48},
    ),
    (
        ParametersMain.procontra,
        {
            "nicht_miteinander_auskommen": "nicht_miteinander_auskommen",
            "nichtauskommen": "nichtauskommen",
        },
        {123},
    ),
    (
        ParametersMain.procontra,
        {
            "nicht_dagegen": "nicht_dagegen",
            "nichtdagegen": "nichtdagegen",
        },
        {124},
    ),
    (
        ParametersMain.procontra,
        {
            "kein_Gegenteil": "kein_Gegenteil",
            "keingegenteil": "keingegenteil",
        },
        {125},
    ),
    (
        ParametersMain.procontra,
        {
            "nicht_dafür": "nicht_dafür",
            "nichtdafuer": "nichtdafuer",
        },
        {126},
    ),
    (
        ParametersMain.procontra,
        {
            "Hilfe_nicht_gebrauchen": "Hilfe_nicht_gebrauchen",
            "hilfenichtgebrauchen": "hilfenichtgebrauchen",
        },
        {127},
    ),
    (
        ParametersMain.procontra,
        {
            "nicht_helfen_können": "nicht_helfen_können",
            "nichthelfenkoennen": "nichthelfenkoennen",
        },
        {128},
    ),
    (
        ParametersMain.procontra,
        {
            "nicht_abgeneigt": "nicht_abgeneigt",
            "nichtabgeneigt": "nichtabgeneigt",
        },
        {129},
    ),
    (
        ParametersMain.procontra,
        {"unmotivierbar": "unmotivierbar"},
        {130},
    ),
    (
        ParametersMain.procontra,
        {
            "contra": "contra",
            "dagegen": "dagegen",
        },
        {15, 26},
    ),
    (
        ParametersMain.procontra,
        {
            "Gegenteil": "Gegenteil",
            "gegenteil": "gegenteil",
        },
        {100, 101, 222},
    ),
    (
        ParametersMain.procontra,
        {
            "Harmonie": "Harmonie",
            "harmonie": "harmonie",
        },
        {102, 103},
    ),
    (ParametersMain.licht, (), {20, 27, 313}),
    (
        ParametersMain.procontra,
        {
            Primzahlkreuz_pro_contra_strs[0]: Primzahlkreuz_pro_contra_strs[0],
            "primzahlkreuz": "primzahlkreuz",
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
            Primzahlkreuz_pro_contra_strs[0]: Primzahlkreuz_pro_contra_strs[0],
            "primzahlkreuz": "primzahlkreuz",
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
            "in_ReTa": "in_ReTa",
            "inreta": "inreta",
        },
        {209, 210},
    ),
    (
        ParametersMain.bedeutung,
        {
            "Vorzeichen": "Vorzeichen",
            "vorzeichen": "vorzeichen",
        },
        {118, 119},
    ),
    (
        ParametersMain.bedeutung,
        {
            "Primzahlen": "Primzahlen",
            "primzahlen": "primzahlen",
            "vielfache": "vielfache",
            "vielfacher": "vielfacher",
        },
        {19},
    ),
    (
        ParametersMain.bedeutung,
        {
            "Anwendung_der_Sonnen_und_Monde": "Anwendung_der_Sonnen_und_Monde",
            "anwendungdersonnenundmonde": "anwendungdersonnenundmonde",
            "anwendungdersonnen": "anwendungdersonnen",
            "anwendungenfuermonde": "anwendungenfuermonde",
        },
        {22},
    ),
    (
        ParametersMain.bedeutung,
        {
            "Zählungen": "Zählungen",
            "zählungen": "zählungen",
            "zaehlung": "zaehlung",
            "zaehlungen": "zaehlungen",
            "zählung": "zählung",
        },
        {25, 45, 169, 188},
    ),
    (
        ParametersMain.bedeutung,
        {
            "Jura": "Jura",
            "jura": "jura",
            "gesetzeslehre": "gesetzeslehre",
            "recht": "recht",
        },
        {34},
    ),
    (
        ParametersMain.bedeutung,
        {
            "Vollkommenheit_des_Geistes": "Vollkommenheit_des_Geistes",
            "vollkommenheit": "vollkommenheit",
            "geist": "geist",
        },
        {35},
    ),
    (
        ParametersMain.bedeutung,
        {
            "Gestirn": "Gestirn",
            "gestirn": "gestirn",
            "mond": "mond",
            "sonne": "sonne",
            "planet": "planet",
        },
        {64, 154},
        set(),
        set(),
        set(),
    ),
    (
        ParametersMain.bedeutung,
        {
            "Konjunktiv_Wurzelbildung": "Konjunktiv_Wurzelbildung",
            "konjunktiv": "konjunktiv",
            "wurzel": "wurzel",
        },
        {106},
    ),
    (
        ParametersMain.bedeutung,
        {
            "Mechanismen_der_Züchtung": "Mechanismen_der_Züchtung",
            "mechanismen": "mechanismen",
            "wesen": "wesen",
            "zuechtung": "zuechtung",
            "züchtung": "züchtung",
            "züchten": "züchten",
            "zuechten": "zuechten",
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
            "Weisheit_etc": "Weisheit_etc",
            "weisheit": "weisheit",
            "metaweisheit": "metaweisheit",
            "meta-weisheit": "meta-weisheit",
            "idiot": "idiot",
            "weise": "weise",
            "optimal": "optimal",
            "optimum": "optimum",
        },
        {112},
        {(40, 41)},
    ),
    (
        ParametersMain.konzept,
        {
            "Dein_Recht_bekommen": "Dein_Recht_bekommen",
            "rechte": "rechte",
            "recht": "recht",
            "selbstgerecht": "selbstgerecht",
        },
        set(),
        {(291, 292)},
    ),
    (
        ParametersMain.konzept,
        {
            "unterlegen_überlegen": "unterlegen_überlegen",
            "unterlegen": "unterlegen",
            "ueberlegen": "ueberlegen",
        },
        set(),
        {(380, 381)},
    ),
    (
        ParametersMain.konzept,
        {
            "Ehrlichkeit_und_Streit": "Ehrlichkeit_und_Streit",
            "streit": "streit",
            "ehrlichkeit": "ehrlichkeit",
        },
        set(),
        {(375, 376)},
    ),
    (
        ParametersMain.konzept2,
        {"Würdig": "Würdig", "wuerdig": "wuerdig", "würdig": "würdig"},
        set(),
        {(373, 374)},
    ),
    (
        ParametersMain.konzept2,
        {
            "Regel_vs_Ausnahme": "Regel_vs_Ausnahme",
            "regel": "regel",
            "ausnahme": "ausnahme",
        },
        set(),
        {(371, 372)},
    ),
    (
        ParametersMain.konzept2,
        {
            "Filterart_Widrigkeit": "Filterart_Widrigkeit",
            "filterart": "filterart",
            "widrigkeit": "widrigkeit",
        },
        {331, 335},
    ),
    (
        ParametersMain.konzept2,
        {
            "Werte": "Werte",
            "werte": "werte",
        },
        set(),
        {(360, 361)},
    ),
    (
        ParametersMain.konzept2,
        {
            "Gutartigkeits-Egoismus": "Gutartigkeits-Egoismus",
            "position": "position",
            "gutesreziprok": "gutesreziprok",
        },
        set(),
        {(362, 363)},
    ),
    (
        ParametersMain.konzept2,
        {
            "Reflektieren_Erkenntnis-Erkennen": "Reflektieren_Erkenntnis-Erkennen",
            "reflektieren": "reflektieren",
            "erkenntnis": "erkenntnis",
        },
        set(),
        {(364, 365)},
    ),
    (
        ParametersMain.konzept2,
        {"Vertrauen_wollen": "Vertrauen_wollen", "vertrauenwollen": "vertrauenwollen"},
        set(),
        {(366, 367)},
    ),
    (
        ParametersMain.konzept,
        {
            "einklinken_vertrauen_anprangern": "einklinken_vertrauen_anprangern",
            "einklinken": "einklinken",
            "vertrauenerhalten": "vertrauenerhalten",
            "anprangern": "anprangern",
        },
        set(),
        {(368, 369)},
    ),
    (
        ParametersMain.konzept2,
        {
            "Ausrichten_Einrichten": "Ausrichten_Einrichten",
            "einrichten": "einrichten",
            "ausrichten": "ausrichten",
        },
        set(),
        {(358, 359)},
    ),
    (
        ParametersMain.konzept2,
        {
            "Toleranz_Respekt_Akzeptanz_Willkommen": "Toleranz_Respekt_Akzeptanz_Willkommen",
            "toleranz": "toleranz",
            "respekt": "respekt",
            "akzeptanz": "akzeptanz",
            "willkommen": "willkommen",
        },
        set(),
        # {(359, 360)},
        {(62, 63)},
    ),
    (
        ParametersMain.konzept,
        {"familiebrauchen": "familiebrauchen"},
        set(),
        {(279, 280)},
    ),
    (
        ParametersMain.konzept,
        {"ego": "ego", "bescheiden": "bescheiden"},
        set(),
        {(277, 278)},
    ),
    (
        ParametersMain.konzept,
        {
            "Selbstsucht_Ichsucht_etc": "Selbstsucht_Ichsucht_etc",
            "selbstsucht": "selbstsucht",
            "ichsucht": "ichsucht",
        },
        set(),
        {(274, 275)},
    ),
    (
        ParametersMain.konzept,
        {
            "Forschen_Erfinden_Einklinken": "Forschen_Erfinden_Einklinken",
            "wissenschaft": "wissenschaft",
            "forschen": "forschen",
            "einklinken": "einklinken",
            "erfinden": "erfinden",
        },
        set(),
        {(258, 259)},
    ),
    (
        ParametersMain.konzept,
        {
            "Kooperation_vs_Arsch": "Kooperation_vs_Arsch",
            "arschloch": "arschloch",
            "kooperation": "kooperation",
            "arsch": "arsch",
        },
        set(),
        {(245, 246)},
    ),
    (
        ParametersMain.konzept,
        {"Liebe_usw": "Liebe_usw", "liebe": "liebe", "zuneigung": "zuneigung"},
        set(),
        {(247, 248)},
    ),
    (
        ParametersMain.konzept,
        {
            "Selbstlosigkeit_Ichlosigkeit_etc": "Selbstlosigkeit_Ichlosigkeit_etc",
            "selbstlos": "selbstlos",
            "ichlos": "ichlos",
        },
        set(),
        {(238, 239)},
    ),
    (
        ParametersMain.konzept,
        {
            "variationsreich_eintönig": "variationsreich_eintönig",
            "eintönig": "eintönig",
            "eintoenig": "eintoenig",
            "variationsreich": "variationsreich",
        },
        set(),
        {(236, 237)},
    ),
    (
        ParametersMain.konzept,
        {
            "Zuneigung_Abneigung": "Zuneigung_Abneigung",
            "abgeneigt": "abgeneigt",
            "zugewandt": "zugewandt",
            "reserviert": "reserviert",
            "zugeneigt": "zugeneigt",
        },
        set(),
        {(199, 200)},
    ),
    (
        ParametersMain.menschliches,
        {
            "ehrlich vs höflich": "ehrlich vs höflich",
            "ehrlich": "ehrlich",
            "höflich": "höflich",
            "hoeflich": "hoeflich",
        },
        set(),
        {(224, 225)},
    ),
    # (
    #    ParametersMain.konzept,
    #    {"delegieren": "delegieren", "ansammlung": "ansammlung"},
    #    set(),
    #    {(227, 228)},
    # ),
    (
        ParametersMain.konzept,
        {
            "ehrlich vs höflich": "ehrlich vs höflich",
            "ehrlich": "ehrlich",
            "höflich": "höflich",
            "hoeflich": "hoeflich",
        },
        set(),
        {(224, 225)},
    ),
    (
        ParametersMain.konzept,
        {"Tragweite": "Tragweite", "tragweite": "tragweite"},
        set(),
        {(211, 212)},
    ),
    (
        ParametersMain.konzept,
        {"wertvoll": "wertvoll", "wertlos": "wertlos"},
        set(),
        {(186, 187)},
    ),
    (
        ParametersMain.konzept,
        {
            "Götter_Propheten_Familien_Freunde": "Götter_Propheten_Familien_Freunde",
            "familiaer": "familiaer",
            "goettlich": "goettlich",
            "freunde": "freunde",
            "propheten": "propheten",
        },
        set(),
        {(184, 185)},
    ),
    (
        ParametersMain.konzept,
        {
            "sanft_vs_hart": "sanft_vs_hart",
            "sanft": "sanft",
            "hart": "hart",
        },
        set(),
        {(159, 160), (161, 162)},
    ),
    (
        ParametersMain.konzept,
        {
            "vereinen_vs_verbinden": "vereinen_vs_verbinden",
            "vereinenverbinden": "vereinenverbinden",
            "vereinen": "vereinen",
            "verbinden": "verbinden",
            "einheit": "einheit",
            "verbindung": "verbindung",
        },
        set(),
        {(133, 134)},
    ),
    (
        ParametersMain.konzept,
        {
            "ähnlich": "ähnlich",
            "aehnlich": "aehnlich",
        },
        {220},
    ),
    (
        ParametersMain.konzept,
        {
            "gut_böse_lieb_schlecht": "gut_böse_lieb_schlecht",
            "gut": "gut",
            "böse": "böse",
            "boese": "boese",
            "lieb": "lieb",
            "schlecht": "schlecht",
        },
        {52, 53},
        {(38, 39)},
    ),
    (
        ParametersMain.konzept,
        {
            "Sinn_und_Zweck_des_Lebens": "Sinn_und_Zweck_des_Lebens",
            "sinn": "sinn",
            "zweck": "zweck",
            "bedeutung": "bedeutung",
        },
        {88, 189},
        {(181, 182)},
    ),
    (
        ParametersMain.konzept,
        {
            "Zeit_vs_Raum": "Zeit_vs_Raum",
            "zeit": "zeit",
            "raum": "raum",
            "zeitlich": "zeitlich",
            "räumlich": "räumlich",
        },
        set(),
        {(49, 50)},
    ),
    (
        ParametersMain.konzept,
        {
            "egalitär_vs_autoritär": "egalitär_vs_autoritär",
            "egalitaerautoritaer": "egalitaerautoritaer",
            "egalitaer": "egalitaer",
            "autoritaer": "autoritaer",
            "egalitär": "egalitär",
            "autoritär": "autoritär",
        },
        set(),
        {(163, 164)},
    ),
    (
        ParametersMain.konzept,
        {
            "Meinungen_und_Ruf": "Meinungen_und_Ruf",
            "meinungen": "meinungen",
            "anderemenschen": "anderemenschen",
            "ruf": "ruf",
        },
        set(),
        {(60, 61)},
    ),
    (
        ParametersMain.konzept,
        {
            "Meinungsintelligenz": "Meinungsintelligenz",
            "meinungsintelligenz": "meinungsintelligenz",
            "ursprungsintelligenz": "ursprungsintelligenz",
        },
        set(),
        {(151, 152)},
    ),
    (
        ParametersMain.konzept,
        {
            "Sittlichkeit": "Sittlichkeit",
            "sittlichkeit": "sittlichkeit",
            "annaehrerung": "annaehrerung",
        },
        set(),
        {(179, 180)},
    ),
    (
        ParametersMain.konzept,
        {"Führung": "Führung", "führung": "führung", "fuehrung": "fuehrung"},
        set(),
        {(173, 174)},
    ),
    (
        ParametersMain.konzept,
        {
            "Durchleuchten": "Durchleuchten",
            "durchleuchten": "durchleuchten",
            "erleuchten": "erleuchten",
        },
        set(),
        {(177, 178)},
    ),
    (
        ParametersMain.konzept,
        {
            "Fördern_Sensiblisieren_und_Gedeihen": "Fördern_Sensiblisieren_und_Gedeihen",
            "foerdern": "foerdern",
            "fördern": "fördern",
            "begrenzen": "begrenzen",
            "sensibilisieren": "sensibilisieren",
            "gedeihen": "gedeihen",
            "verderben": "verderben",
        },
        set(),
        {(175, 176)},
    ),
    (
        ParametersMain.konzept,
        {
            "Überheblichkeit": "Überheblichkeit",
            "überheblich": "überheblich",
            "ueberheblichkeit": "ueberheblichkeit",
            "ueberheblich": "ueberheblich",
            "überheblichkeit": "überheblichkeit",
        },
        set(),
        {(171, 172)},
    ),
    (
        ParametersMain.konzept,
        {
            "Polung_der_Liebe": "Polung_der_Liebe",
            "liebepolung": "liebepolung",
        },
        set(),
        {(121, 122)},
    ),
    (
        ParametersMain.konzept,
        {
            "Egoismus_vs_Altruismus": "Egoismus_vs_Altruismus",
            "egoismus": "egoismus",
            "altruismus": "altruismus",
            "egoist": "egoist",
            "altruist": "altruist",
        },
        {136},
        {(66, 67)},
    ),
    (
        ParametersMain.konzept,
        {"kausal": "kausal", "geltung": "geltung", "genese": "genese"},
        set(),
        {(110, 111)},
    ),
    (
        ParametersMain.konzept,
        {"Gleichheit": "Gleichheit", "gleich": "gleich"},
        set(),
        {(192, 193)},
    ),
    (
        ParametersMain.konzept,
        {"Überleben": "Überleben", "ueberleben": "ueberleben"},
        set(),
        {(194, 195)},
    ),
    (ParametersMain.inkrementieren, set(), {43, 54, 74, 95}),
    (ParametersMain.inkrementieren, {"um1": "um1"}, {155}),
    (ParametersMain.inkrementieren, {"um2": "um2"}, {156}),
    (ParametersMain.inkrementieren, {"um3": "um3"}, {157}),
    (
        ParametersMain.inkrementieren,
        {
            "warum_Transzendentalie_=_Strukturgroesse_=_Charakter": "warum_Transzendentalie_=_Strukturgroesse_=_Charakter",
            "warumtranszendentaliezustrukturgroesseundcharakter": "warumtranszendentaliezustrukturgroesseundcharakter",
        },
        {4, 54, 5, 165},
    ),
    (
        ParametersMain.inkrementieren,
        {
            "warum_Transzendentalie_=_Komplexität_von_Michael_Commons": "warum_Transzendentalie_=_Komplexität_von_Michael_Commons",
            "warumtranszendentaliegleichkomplexitaet": "warumtranszendentaliegleichkomplexitaet",
        },
        {65, 5, 166},
    ),
    (
        ParametersMain.primvielfache,
        {"Rahmen-Bedingungen": "Rahmen-Bedingungen", "rahmen": "rahmen"},
        {226},
    ),
    (
        ParametersMain.primvielfache,
        {
            "Motive_gleichförmige_Polygone": "Motive_gleichförmige_Polygone",
            "motivgleichfoermig": "motivgleichfoermig",
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
            "Struktur_gleichförmige_Polygone": "Struktur_gleichförmige_Polygone",
            "strukturgleichfoermig": "strukturgleichfoermig",
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
        {"Motive_Sternpolygone": "Motive_Sternpolygone", "motivstern": "motivstern"},
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
            "Struktur_Sternpolygone": "Struktur_Sternpolygone",
            "strukturstern": "strukturstern",
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
            "Motiv_Sternpolygon_gebrochen-rational": "Motiv_Sternpolygon_gebrochen-rational",
            "motivgebrstern": "motivgebrstern",
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
            "Struktur_Sternpolyon_gebrochen-rational": "Struktur_Sternpolyon_gebrochen-rational",
            "strukgebrstern": "strukgebrstern",
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
            "Motiv_gleichförmige_Polygone_gebrochen-rational": "Motiv_gleichförmige_Polygone_gebrochen-rational",
            "motivgebrgleichf": "motivgebrgleichf",
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
            "Struktur_gleichförmige_Polygone_gebrochen-rational": "Struktur_gleichförmige_Polygone_gebrochen-rational",
            "strukgebrgleichf": "strukgebrgleichf",
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
        {"beschrieben": "beschrieben"},
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
            "Lebewesen": "Lebewesen",
            "tiere": "tiere",
            "tier": "tier",
            "lebewesen": "lebewesen",
        },
        2: {"Berufe": "Berufe", "berufe": "berufe", "beruf": "beruf"},
        3: {
            "Kreativität_und_Intelligenz": "Kreativität_und_Intelligenz",
            "kreativität": "kreativität",
            "intelligenz": "intelligenz",
            "kreativitaet": "kreativitaet",
        },
        4: {
            "Liebe": "Liebe",
            "liebe": "liebe",
        },
        7: {
            "Männer": "Männer",
            "männer": "männer",
            "maenner": "maenner",
            "frauen": "frauen",
        },
        8: {
            "Persönlichkeit_evolutionär_erwerben": "Persönlichkeit_evolutionär_erwerben",
            "evolution": "evolution",
            "erwerben": "erwerben",
            "persoenlichkeit": "persoenlichkeit",
            "persönlichkeit": "persönlichkeit",
        },
        9: {
            "Religion": "Religion",
            "religion": "religion",
            "religionen": "religionen",
        },
        10: {
            "Motive_Ziele": "Motive_Ziele",
            "motivation": "motivation",
            "motive": "motive",
            "ziele": "ziele",
            "ziel": "ziel",
            "motive": "motive",
        },
        12: {
            "Emotionen": "Emotionen",
            "emotionen": "emotionen",
            "gefuehle": "gefuehle",
            "gefühle": "gefühle",
            "emotion": "emotion",
            "gefühl": "gefühl",
            "gefühle": "gefühle",
        },
        13: {
            "Personen": "Personen",
            "personen": "personen",
            "berühmtheiten": "berühmtheiten",
            "beruehmtheiten": "beruehmtheiten",
        },
        16: {
            "Wirtschaftssysteme": "Wirtschaftssysteme",
            "wirtschaftssystem": "wirtschaftssystem",
            "wirtschaftssysteme": "wirtschaftssysteme",
            "kombinierteswirtschaftssystem": "kombinierteswirtschaftssystem",
            "kombiniertewirtschaftssysteme": "kombiniertewirtschaftssysteme",
        },
    }
)

kombiParaNdataMatrix2: OrderedDict[int, tuple[str]] = OrderedDict(
    {
        1: {
            "Lebewesen": "Lebewesen",
            "tiere": "tiere",
            "tier": "tier",
            "lebewesen": "lebewesen",
        },
        2: {"Berufe": "Berufe", "berufe": "berufe", "beruf": "beruf"},
        # 3: {
        #    "Kreativität_und_Intelligenz": "Kreativität_und_Intelligenz",
        #    "kreativität": "kreativität",
        #    "intelligenz": "intelligenz",
        #    "kreativitaet": "kreativitaet",
        # },
        # 4: {
        #    "Liebe": "Liebe",
        #    "liebe": "liebe",
        # },
        5: {
            "Transzendentalien_Strukturalien": "Transzendentalien_Strukturalien",
            "transzendenz": "transzendenz",
            "transzendentalien": "transzendentalien",
            "strukturalien": "strukturalien",
            "alien": "alien",
        },
        6: {
            "Primzahlkreuz": "Primzahlkreuz",
            "leibnitz": "leibnitz",
            "primzahlkreuz": "primzahlkreuz",
        },
        # 7: {
        #    "Männer": "Männer",
        #    "männer": "männer",
        #    "maenner": "maenner",
        #    "frauen": "frauen",
        # },
        8: {
            "Persönlichkeit_evolutionär_erwerben": "Persönlichkeit_evolutionär_erwerben",
            "evolution": "evolution",
            "erwerben": "erwerben",
            "persoenlichkeit": "persoenlichkeit",
            "persönlichkeit": "persönlichkeit",
        },
        # 9: {
        #    "Religion": "Religion",
        #    "religion": "religion",
        #    "religionen": "religionen",
        # },
        10: {
            "Motive_Ziele": "Motive_Ziele",
            "motivation": "motivation",
            "motive": "motive",
            "ziele": "ziele",
            "ziel": "ziel",
            "motive": "motive",
        },
        11: {
            "analytische_Ontologie": "analytische_Ontologie",
            "analytischeontologie": "analytischeontologie",
            "ontologie": "ontologie",
        },
        # 12: {
        #    "Emotionen": "Emotionen",
        #    "emotionen": "emotionen",
        #    "gefuehle": "gefuehle",
        #    "gefühle": "gefühle",
        #    "emotion": "emotion",
        #    "gefühl": "gefühl",
        #    "gefühle": "gefühle",
        # },
        # 13: {"Personen": "Personen", "personen": "personen", "berühmtheiten": "berühmtheiten", "beruehmtheiten": "beruehmtheiten"},
        14: {
            "Mechanismen_der_Zuechtung": "Mechanismen_der_Zuechtung",
            "mechanismen": "mechanismen",
            "wesen": "wesen",
            "zuechten": "zuechten",
            "züchten": "züchten",
        },
        15: {
            "Gegentranszendentalien": "Gegentranszendentalien",
            "gegentranszendentalien": "gegentranszendentalien",
            "gegenstrukturalien": "gegenstrukturalien",
        },
        # 16: {
        #    "Wirtschaftssysteme": "Wirtschaftssysteme",
        #    "wirtschaftssystem": "wirtschaftssystem",
        #    "wirtschaftssysteme": "wirtschaftssysteme",
        #    "kombinierteswirtschaftssystem": "kombinierteswirtschaftssystem",
        #    "kombiniertewirtschaftssysteme": "kombiniertewirtschaftssysteme",
        # },
        17: {
            "Maschinen": "Maschinen",
            "maschinen": "maschinen",
            "geräte": "geräte",
            "geraete": "geraete",
        },
        18: {"Geist": "Geist", "geist": "geist"},
        19: {"Bewusstsein": "Bewusstsein", "bewusstsein": "bewusstsein"},
    }
)


class concat:
    polygon1 = " der eigenen Strukturgröße ("
    polygon2 = ") auf dich bei gleichförmigen Polygonen"
    energietopologie1 = (
        "eine Denkart",
        "eine Gefühlsart",
        "total eine Art, etwas geistig zu erzeugen",
        "total eine Art zu erleben",
        "total eine Energie-Art",
        "etwas eine Art zu erleben",
        "etwas eine Art, etwas geistig zu erzeugen",
        "wenig eine Art, etwas geistig zu erzeugen",
        "einigermaßen eine Energie-Art",
        "kaum eine Energie-Art",
        "kaum eine Art, etwas geistig zu erzeugen",
        "eine Denkart",
        "eine Gefühlsart",
        "total eine Art, etwas geistig zu erzeugen",
        "total eine Art zu erleben",
        "total eine Energie-Art",
        "etwas eine Art zu erleben",
        "etwas eine Art, etwas geistig zu erzeugen",
        "wenig eine Art, etwas geistig zu erzeugen",
        "einigermaßen eine Energie-Art",
        "kaum eine Energie-Art",
        "kaum eine Art, etwas geistig zu erzeugen",
    )
    ausgabeString = (
        "Energie oder Denkart oder Gefühlsart oder Materie-Art oder Topologie-Art"
    )
    kreaZahl = (
        "Evolutions-Züchtungs-Kreativität",
        "0. Primzahl 1",
        "1. Primzahl und Sonnenzahl",
        "2. Sonnenzahl, aber keine Primzahl",
        "3. Mondzahl",
    )
    mondExpLog1 = (
        "Mond-Typ eines Sternpolygons",
        "Mond-Typ eines gleichförmigen Polygons",
    )

    mondExpLog2 = "kein Mond"
    # wohl nich nötig zu übersetzen modalA_
    modalA1 = "modalS"
    modalA2 = "vervielfachter"
    modalA3 = "i_origS"

    modalB = (
        "mittelstark überdurchschnittlich: ",
        "überdurchschnittlich: ",
        "mittelleicht überdurchschnittlich: ",
        "sehr: ",
        "sehr leicht überdurchschnittlich: ",
    )
    modalC = ("intrinsisch", "zuerst", "extrinsisch", "als zweites")
    modalD = (
        ", nicht: ",
        " (das alles nicht): ",
        "extrinsisch",
        "als zweites",
        "intrinsisch",
        "zuerst",
    )
    generiert = "Generiert: "
    allesNurBezogen = ("Alles nur bezogen auf die selbe Strukturgröße einer ",)
    headline1 = "Gegen / pro: Nach Rechenregeln auf Primzahlkreuz und Vielfachern von Primzahlen"
    gegen = "gegen "
    pro = "pro "
    hineinversetzen = (
        " Darin kann sich die ",
        " am Besten hineinversetzten.",
    )
    proIst = ("pro dieser Zahl sind: ", "pro dieser Zahl ist ")
    contraIst = (" contra dieser Zahl sind: ", " contra dieser Zahl ist ")
    hineinversetzen = " - Die Zahlen, die für oder gegen diese Zahlen hier sind, können sich in diese am Besten gedanklich hineinversetzen."
    polygone = ("Sternpolygone", "gleichförmige Polygone")

    kombisNamen: tuple = (
        "Motiv -> Motiv",
        "Motiv -> Strukur",
        "Struktur -> Motiv",
        "Struktur -> Strukur",
    )
    kombisNamen2: tuple = (
        "GalGal",
        "GalUni",
        "UniGal",
        "UniUni",
    )

    faktorenbla = ", mit Faktoren aus gebrochen-rationalen Zahlen"
    genMul = "generierte Multiplikationen "
    ausserdem = ", außerdem: "
    Multiplikationen_ = "Multiplikationen"
    nWichtigste = ("Wichtigstes_zum_verstehen", "Viertwichtigste")
    metaOrWhat = OrderedDict(
        {
            2: (("Meta-Thema: ", "Konkretes: "), ("Meta-", "Konkret-")),
            3: (("Theorie-Thema: ", "Praxis: "), ("Theorie-", "Praxis-")),
            4: (
                ("Planungs-Thema: ", "Umsetzungs-Thema: "),
                ("Planung-", "Umsetzung-"),
            ),
            5: (
                ("Anlass-Thema: ", "Wirkungs-Thema: "),
                ("Anlass-", "wirkung-"),
            ),
            6: (
                ("Kraft-Gebung: ", "Verstärkungs-Thema: "),
                ("Kraft-geben-", "Verstärkung-"),
            ),
            7: (
                ("Beherrschung: ", "Richtung-Thema: "),
                ("beherrschend-", "Richtung-"),
            ),
        }
    )
    metaKonkret = (
        "Meta",
        "Theorie",
        "Management",
        "ganzheitlich",
        "Verwertung, Unternehmung, Geschäft",
        "regieren, beherrschen",
        "Konkretes",
        "Praxis",
        "verändernd",
        "darüber hinaus gehend",
        "wertvoll",
        "Richtung",
        " für 1/n statt n",
        " für n",
    )
    innenAussen = (
        "für innen",
        "für außen",
        '"für seitlich und gegen Schwächlinge innen"',
        '"gegen seitlich und für Schwächlinge innen"',
        "für außen",
    )
    spaltenNamen = OrderedDict(
        {
            5: "Transzendentalien, Strukturalien, Universum n",
            10: "Galaxie n",
            42: "Galaxie 1/n",
            131: "Transzendentalien, Strukturalien, Universum 1/n",
            138: "Dagegen-Gegen-Transzendentalien, Gegen-Strukturalien, Universum n",
            202: "neutrale Gegen-Transzendentalien, Gegen-Strukturalien, Universum n",
            None: "Richtung-Richtung",
        }
    )

    primRicht = "Primzahlwirkung (7, Richtung) "

    letztEnd = "] * letztendlich: "

    primVielGen = "Primzahlvielfache, nicht generiert"
    GalOrUniOrFehler = ("Fehler", " Universum", " Galaxie")

    multipl = "Multiplikationen"
    notGen = "Nicht_generiert"


class lib4tables:
    zaehlung = "zaehlung"
    nummerier = "nummerierung"
    alles = "alles"


class center:
    Primzahlkreuz_pro_contra_strs = (
        "Primzahlkreuz_pro_contra",
        "nachvollziehen_emotional_oder_geistig_durch_Primzahl-Kreuz-Algorithmus_(15)",
    )

    Multiplikationen = [("Multiplikationen", "")]

    @classmethod
    def classify(cls, mod):
        if mod == 0:
            return "ja"
        elif mod == 1:
            return "Gegenteil"
        elif mod == 2:
            return "ähnlich"
        elif mod == 3:
            return "entferntes Gegenteil"
        elif mod == 4:
            return "entfernt ähnlich"


class nested:
    gal = "galaxie"  # eigtl aus reta.py
    uni = "universum"  # eigtl aus reta.py
    typ = "typ"  # eigtl aus reta.py
    zeit = "zeit"  # eigtl aus reta.py
    art = "art"  # eigtl aus reta.py


class retapy:
    beschrieben = "beschrieben"
    mainParaCmds: dict = {
        "zeilen": 0,
        "spalten": 1,
        self.tables.getCombis.parameterName: 2,
        "ausgabe": 3,
        "debug": None,
        "h": None,
        "help": None,
    }
    nichts = "nichts"
    cliout1 = (
        'Der Haupt-Parameter "',
        '" existiert hier nicht als Befehl!',
        " Es ist nur möglich: -",
    )

    keineNum = "keinenummerierung"
    cliout2 = (
        'Der Unter-Paramaeter "--',
        '" existiert, aber nicht mit dem Textwert "',
        '". Mögliche Nebenparameter-Textwerte, für diesen Unter-Parameter, sind: "',
        '". Stattdessen gibt keine Nebenparameter-Textwerte.',
    )
    cliout3 = (
        'Der Unter-Paramaeter "--',
        '" mit dem Textwert "',
        '" existiert hier nicht als Befehl für Haupt-Parameter',
        " -spalten",
        " !",
        " Es ist nur möglich:\n--",
        ", --breiten, --breite",
        "\nmit dem Werten dahinter:\n",
    )
    cliout4 = (
        'Der Unter-Parameter "--',
        '" existiert hier nicht als Befehl für Haupt-Parameter',
        " -spalten",
        ", oder dieser Parameter braucht Werte analog wie: \n--unterParameter=Wert1\n",
        "Es ist nur möglich: --",
        ", --keinenummerierung",
    )
    galaxie = "--galaxie="
    universum = "--universum="
    kombinationen = "kombinationen"
    cliout5 = (
        'Die Kombispalte "',
        '" existiert so nicht als Befehl. Möglich sind die Parameter für ',
    )
    cliout6 = 'kein Unter-Parameter "--galaxie=" oder "--universum=" angegeben für Hauptparameter -kombination'
    cliout7 = (
        "Es muss ein Hauptparameter, bzw. der richtige, gesetzt sein, damit ein",
        ' Nebenparameter, wie möglicherweise: "',
        '" ausgeführt werden kann. Hauptparameter sind: -',
    )
    breite = "--breite"

    cliout8 = "Versuche Parameter -h"
    zeilenParas = {
        "alles": "alles",
        "zeit": "zeit",
        "heute": "heute",
        "gestern": "gestern",
        "morgen": "morgen",
        "hoehemaximal": "hoehemaximal",
        "typ": "typ",
        "sonne": "sonne",
        "mond": "mond",
        "planet": "planet",
        "schwarzesonne": "schwarzesonne",
        "potenzenvonzahlen": "potenzenvonzahlen",
        "vielfachevonzahlen": "vielfachevonzahlen",
        "primzahlvielfache": "primzahlvielfache",
        "vorhervonausschnittteiler": "vorhervonausschnittteiler",
        "vorhervonausschnitt": "vorhervonausschnitt",
        "nachtraeglichneuabzaehlungvielfache": "nachtraeglichneuabzaehlungvielfache",
        "nachtraeglichneuabzaehlung": "nachtraeglichneuabzaehlung",
    }
    cliout9 = (
        'Den Neben-Parameter "',
        '" gibt es hier nicht für den Hauptparameter "-',
        '".',
        " Möglich sind: ",
    )
    cliout10 = (
        'Den Neben-Parameter "',
        '" gibt es hier nicht für den Hauptparameter "-',
    )
