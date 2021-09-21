"""
Nestedcompleter for completion of hierarchical data structures.
"""
import difflib
from enum import Enum
from typing import Any, Dict, Iterable, Mapping, Optional, Set, Union

from LibRetaPrompt import (ausgabeArt, ausgabeParas, befehle, befehle2,
                           hauptForNeben, hauptForNebenSet, kombiMainParas,
                           mainParas, notParameterValues, reta, retaProgram,
                           spalten, spaltenDict, zeilenParas)
# from baseAlx import WordCompleter
# from completionAlx import Completion
from prompt_toolkit.completion import (CompleteEvent, Completer, Completion,
                                       FuzzyWordCompleter)
from prompt_toolkit.document import Document
# from prompt_toolkit.completion.word_completer import WordCompleter
from word_completerAlx import WordCompleter

__all__ = ["NestedCompleter"]

# NestedDict = Mapping[str, Union['NestedDict', Set[str], None, Completer]]
NestedDict = Mapping[str, Union[Any, Set[str], None, Completer]]


class ComplSitua(Enum):
    hauptPara = 0
    zeilenPara = 1
    value = 3
    neitherNor = 4
    retaAnfang = 5
    unbekannt = 6
    spaltenPara = 7
    komiPara = 8
    kombiMetaPara = 9
    ausgabePara = 10
    spaltenValPara = 11
    zeilenValPara = 12
    kombiValPara = 13
    ausgabeValPara = 14
    BefehleNichtReta = 15


class NestedCompleter(Completer):
    """
    Completer which wraps around several other completers, and calls any the
    one that corresponds with the first word of the input.

    By combining multiple `NestedCompleter` instances, we can achieve multiple
    hierarchical levels of autocompletion. This is useful when `WordCompleter`
    is not sufficient.

    If you need multiple levels, check out the `from_nested_dict` classmethod.
    """

    def __init__(
        self,
        options: Dict[str, Optional[Completer]],
        notParameterValues,
        optionsStandard: Dict[str, Optional[Completer]],
        situation: ComplSitua,
        lastString: str,
        optionsTypes: Dict[str, Optional[ComplSitua]],
        ignore_case: bool = True,
    ) -> None:
        self.options2 = optionsStandard
        self.options1 = options
        self.options = {**options, **optionsStandard}
        self.ignore_case = ignore_case
        self.notParameterValues = notParameterValues
        self.ExOptions: dict = {}
        self.ifGleichheitszeichen = False
        self.optionsPark: Dict[str, Optional[Completer]] = {}
        self.situationsTyp: Optional[ComplSitua] = situation
        self.lastString: str = lastString
        self.optionsTypes: Dict[str, Optional[ComplSitua]] = optionsTypes
        self.spaltenParaWort: Optional[str] = "  "
        self.kombiParaWort: Optional[str] = "  "
        self.ausgabeParaWort: Optional[str] = "  "
        self.zeilenParaWort: Optional[str] = "  "
        self.nebenParaWort: Optional[str] = "  "

    def optionsSync(
        self,
    ):
        self.options = {**self.options1, **self.options2}

    def __repr__(self) -> str:
        return "NestedCompleter(%r, ignore_case=%r)" % (self.options, self.ignore_case)

    completers: set = set()

    def __eq__(self, obj) -> bool:
        return self.options.keys() == obj.options.keys()

    def __hash__(self):
        return hash(str(self.options.keys()))

    def matchTextAlx(
        self, first_term: str, trennzeichen: str = " "
    ) -> Optional[Completer]:
        result = None
        for i in range(len(first_term), -1, -1):
            result = self.options.get(first_term[:i])
            if result is not None:
                break
        if result is None:
            result = NestedCompleter(
                {}, notParameterValues, {}, self.situationsTyp, first_term, {}
            )
            self.__setOptions(result, first_term, trennzeichen)
        return result

    def __setOptions(
        self, completer: "NestedCompleter", first_term: str, trennzeichen: str
    ):
        gleich = trennzeichen == "=" and self.situationsTyp in (
            ComplSitua.spaltenPara,
            ComplSitua.zeilenPara,
            ComplSitua.komiPara,
            ComplSitua.ausgabePara,
        )
        komma = trennzeichen == "," and self.situationsTyp in (
            ComplSitua.spaltenValPara,
            ComplSitua.zeilenValPara,
            ComplSitua.kombiValPara,
            ComplSitua.ausgabeValPara,
        )
        # print(str(self.nebenParaWort) + "SDT" + trennzeichen + "|" + str(gleich))
        if trennzeichen == " ":
            if (
                "reta" == tuple(self.options.keys())[0]
                and self.situationsTyp == ComplSitua.retaAnfang
            ):
                completer.options = {key: None for key in hauptForNeben}
                completer.optionsTypes = {
                    key: ComplSitua.hauptPara for key in hauptForNeben
                }
                completer.lastString = first_term
                completer.situationsTyp = ComplSitua.hauptPara
            elif (
                (
                    tuple(self.options.keys())[0] in befehle2
                    or tuple(self.options.keys())[0].isnumeric()
                )
                and self.situationsTyp
                in (
                    ComplSitua.retaAnfang,
                    ComplSitua.befehleNichtReta,
                )
                or self.situationsTyp == ComplSitua.befehleNichtReta
            ):
                completer.options = {key: None for key in befehle2}
                completer.optionsTypes = {
                    key: ComplSitua.befehleNichtReta for key in befehle2
                }
                completer.lastString = first_term
                completer.situationsTyp = ComplSitua.befehleNichtReta

            else:
                # elif (
                # self.situationsTyp
                # in (
                # ComplSitua.hauptPara,
                # ComplSitua.retaAnfang,
                # ComplSitua.spaltenPara,
                # ComplSitua.spaltenValPara,
                # )
                # or True
                # ):
                if len({first_term, self.nebenParaWort} & hauptForNebenSet) > 0:
                    if "-zeilen" == first_term:
                        var1, var2 = self.paraZeilen(completer)
                    elif "-spalten" == first_term:
                        var1, var2 = self.paraSpalten(completer)
                    elif "-ausgabe" == first_term:
                        var1, var2 = self.paraAusgabe(completer)
                    elif "-kombination" == first_term:
                        var1, var2 = self.paraKombination(completer)
                    elif "-zeilen" == self.nebenParaWort:
                        var1, var2 = self.paraZeilen(completer)
                    elif "-spalten" == self.nebenParaWort:
                        var1, var2 = self.paraSpalten(completer)
                    elif "-ausgabe" == self.nebenParaWort:
                        var1, var2 = self.paraAusgabe(completer)
                    elif "-kombination" == self.nebenParaWort:
                        var1, var2 = self.paraKombination(completer)

                    completer.options = {key: None for key in var1}
                    completer.optionsTypes = {key: var2 for key in var1}
                    completer.lastString = first_term

                    completer.nebenParaWort = (
                        first_term
                        if first_term in hauptForNeben
                        else self.nebenParaWort
                    )
                    if first_term not in hauptForNeben:
                        completer.options = {
                            **completer.options,
                            **{key: None for key in hauptForNeben},
                        }
                        completer.optionsTypes = {
                            **completer.optionsTypes,
                            **{key: ComplSitua.hauptPara for key in hauptForNeben},
                        }

        elif gleich or komma:
            # print(str(self.nebenParaWort) + "SDG")
            if "-spalten" == first_term:
                var2, var3, var4 = self.gleichKommaSpalten(
                    completer, first_term, gleich, komma
                )
            elif "-zeilen" == first_term:
                var2, var3, var4 = self.gleichKommaZeilen(
                    completer, first_term, gleich, komma
                )
            elif "-kombination" == first_term:
                var2, var3, var4 = self.gleichKommaKombi(
                    completer, first_term, gleich, komma
                )
            elif "-ausgabe" == first_term:
                var2, var3, var4 = self.gleichKommaAusg(
                    completer, first_term, gleich, komma
                )
            elif "-spalten" == self.nebenParaWort:
                var2, var3, var4 = self.gleichKommaSpalten(
                    completer, first_term, gleich, komma
                )
            elif "-zeilen" == self.nebenParaWort:
                var2, var3, var4 = self.gleichKommaZeilen(
                    completer, first_term, gleich, komma
                )
            elif "-kombination" == self.nebenParaWort:
                var2, var3, var4 = self.gleichKommaKombi(
                    completer, first_term, gleich, komma
                )
            elif "-ausgabe" == self.nebenParaWort:
                var2, var3, var4 = self.gleichKommaAusg(
                    completer, first_term, gleich, komma
                )

            if self.situationsTyp != ComplSitua.BefehleNichtReta:
                # print("S" + var3 + "|" + first_term + "|" + self.nebenParaWort)
                suchWort = (
                    first_term[2:]
                    if gleich
                    else var3[2:]
                    if komma and var3 is not None
                    else None
                )
                try:
                    var1 = var4[suchWort]
                except KeyError:
                    var1 = difflib.get_close_matches(suchWort, var4.keys())
                # print(suchWort)
                completer.options = {key: None for key in var1}
                completer.optionsTypes = {key: var2 for key in var1}
                completer.lastString = first_term
                completer.nebenParaWort = self.nebenParaWort

        def gleichKommaKombi(self, completer, first_term, gleich, komma):
            # print(str(self.kombiParaWort) + "_")
            completer.kombiParaWort = (
                first_term if gleich else self.kombiParaWort if komma else None
            )
            var4 = {
                "galaxie": [
                    item
                    for sublist in retaProgram.kombiParaNdataMatrix.values()
                    for item in sublist
                ],
                "universum": [
                    item
                    for sublist in retaProgram.kombiParaNdataMatrix2.values()
                    for item in sublist
                ],
            }
            var2 = ComplSitua.kombiValPara
            var3 = self.kombiParaWort
            completer.situationsTyp = ComplSitua.kombiValPara
            # print(str(var4))
            return var2, var3, var4

    def gleichKommaZeilen(self, completer, first_term, gleich, komma):
        completer.zeilenParaWort = (
            first_term if gleich else self.zeilenParaWort if komma else None
        )
        var4 = {key: [] for key in zeilenParas}
        var2 = ComplSitua.zeilenPara
        var3 = self.zeilenParaWort
        completer.situationsTyp = ComplSitua.zeilenValPara
        return var2, var3, var4

    def gleichKommaAusg(self, completer, first_term, gleich, komma):
        # print(str(self.spaltenParaWort) + "_")
        completer.ausgabeParaWort = (
            first_term if gleich else self.ausgabeParaWort if komma else None
        )
        var4 = {key: [] for key in ausgabeParas}
        var4["art"] = ausgabeArt
        var2 = ComplSitua.ausgabeValPara
        var3 = self.ausgabeParaWort
        # print("|", var3, "|")
        completer.situationsTyp = ComplSitua.ausgabeValPara
        return var2, var3, var4

    def gleichKommaSpalten(self, completer, first_term, gleich, komma):
        # print(str(self.spaltenParaWort) + "_")
        completer.spaltenParaWort = (
            first_term if gleich else self.spaltenParaWort if komma else None
        )
        var4 = spaltenDict
        var2 = ComplSitua.spaltenValPara
        var3 = self.spaltenParaWort
        # print("|", var3, "|")
        completer.situationsTyp = ComplSitua.spaltenValPara
        return var2, var3, var4

    def paraKombination(self, completer):
        var1 = kombiMainParas
        var2 = ComplSitua.kombiValPara
        completer.situationsTyp = ComplSitua.komiPara
        return var1, var2

    def paraAusgabe(self, completer):
        var1 = ausgabeParas
        var2 = ComplSitua.ausgabeValPara
        completer.situationsTyp = ComplSitua.ausgabePara
        return var1, var2

    def paraSpalten(self, completer):
        var1 = spalten
        var2 = ComplSitua.spaltenValPara
        completer.situationsTyp = ComplSitua.spaltenPara
        return var1, var2

    def paraZeilen(self, completer):
        var1 = zeilenParas
        var2 = ComplSitua.zeilenValPara
        completer.situationsTyp = ComplSitua.zeilenPara
        return var1, var2

    def get_completions(
        self, document: Document, complete_event: CompleteEvent
    ) -> Iterable[Completion]:
        # Split document.
        text = document.text_before_cursor.lstrip()
        stripped_len = len(document.text_before_cursor) - len(text)

        # If there is a space, check for the first term, and use a
        # subcompleter.
        gleich: bool = "=" in text
        komma: bool = "," in text
        if " " in text:
            # print(str(type(text)))
            first_term = text.split()[0]
            # print(first_term)
            # completer = self.options.get(first_term)
            completer = self.matchTextAlx(first_term)
            # print(str(type(completer)))

            # If we have a sub completer, use this for the completions.
            if completer is not None:
                # if self.ifGleichheitszeichen:
                #    completer.options = completer.optionsPark
                # self.ifGleichheitszeichen = False
                # if "=" not in text and len(completer.ExOptions) != 0:
                #    for key, val in completer.ExOptions.items():
                #        completer.options[key] = val
                remaining_text = text[len(first_term) :].lstrip()
                move_cursor = len(text) - len(remaining_text) + stripped_len

                new_document = Document(
                    remaining_text,
                    cursor_position=document.cursor_position - move_cursor,
                )

                for c in completer.get_completions(new_document, complete_event):
                    yield c

        elif gleich or komma:
            text = str(text)
            first_term = text.split("=" if gleich else ",")[0]
            # print("|" + first_term + "|")
            # print(str(self.options.keys()))
            # completer = self.options.get(first_term)
            completer = self.matchTextAlx(first_term, "=" if gleich else ",")
            # print(str(type(completer)))

            # If we have a sub completer, use this for the completions.
            # print(str(self.notParameterValues))
            # print("||" + first_term + "|")
            # print(str(type(completer)))
            if completer is not None:
                # self.ifGleichheitszeichen = True
                # completer.optionsPark = completer.options
                # completer.options = completer.options2
                # ES SIND EINFACH ZU VIELE, D.H.: ANDERS LÖSEN!
                # ES GIBT AB SOFORT 2 options DATENSTRUKTUREN!
                # for notParaVal in self.notParameterValues:
                #    # print(notParaVal)
                #    if notParaVal in completer.options:
                #        completer.ExOptions[notParaVal] = completer.options.pop(
                #            notParaVal, None
                #        ||)
                # print("|||" + remaining_text + "|")
                # print(str(completer.options))
                remaining_text = text[len(first_term) + 1 :].lstrip()
                # print("|" + remaining_text + "|")
                move_cursor = len(text) - len(remaining_text) + stripped_len

                new_document = Document(
                    remaining_text,
                    cursor_position=document.cursor_position - move_cursor,
                )

                for c in completer.get_completions(new_document, complete_event):
                    yield c

        # No space in the input: behave exactly like `WordCompleter`.
        else:
            # completer = WordCompleter(
            #    list(self.options.keys()), ignore_case=self.ignore_case
            # )
            completer = FuzzyWordCompleter(list(self.options.keys()))

            document._text = document._text
            if self.ifGleichheitszeichen:
                completer.options = completer.optionsPark
            self.ifGleichheitszeichen = False
            for c in completer.get_completions(document, complete_event):
                yield c
