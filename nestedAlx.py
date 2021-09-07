"""
Nestedcompleter for completion of hierarchical data structures.
"""
from typing import Any, Dict, Iterable, Mapping, Optional, Set, Union

# from baseAlx import WordCompleter
# from completionAlx import Completion
from prompt_toolkit.completion import CompleteEvent, Completer, Completion
from prompt_toolkit.document import Document
# from prompt_toolkit.completion.word_completer import WordCompleter
from word_completerAlx import WordCompleter

__all__ = ["NestedCompleter"]

# NestedDict = Mapping[str, Union['NestedDict', Set[str], None, Completer]]
NestedDict = Mapping[str, Union[Any, Set[str], None, Completer]]


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
        ignore_case: bool = True,
    ) -> None:

        self.options = options
        self.ignore_case = ignore_case
        self.notParameterValues = notParameterValues
        self.ExOptions: dict = {}

    def __repr__(self) -> str:
        return "NestedCompleter(%r, ignore_case=%r)" % (self.options, self.ignore_case)

    completers: set = set()

    def __eq__(self, obj) -> bool:
        return self.options.keys() == obj.options.keys()

    def __hash__(self):
        return hash(str(self.options.keys()))

    @classmethod
    def from_nested_dict(
        cls, data: NestedDict, notParameterValues
    ) -> "NestedCompleter":
        """
        Create a `NestedCompleter`, starting from a nested dictionary data
        structure, like this:

        .. code::

            data = {
                'show': {
                    'version': None,
                    'interfaces': None,
                    'clock': None,
                    'ip': {'interface': {'brief'}}
                },
                'exit': None
                'enable': None
            }

        The value should be `None` if there is no further completion at some
        point. If all values in the dictionary are None, it is also possible to
        use a set instead.

        Values in this data structure can be a completers as well.
        """
        # print(str(notParameterValues))
        options: Dict[str, Optional[Completer]] = {}
        for key, value in data.items():
            if (
                isinstance(value, Completer)
                and Completer not in NestedCompleter.completers
            ):
                options[key] = value
                NestedCompleter.completers |= value
                print(str(len(NestedCompleter.completers)))
            elif isinstance(value, dict) and len(value) != 0:
                options[key] = cls.from_nested_dict(
                    value, notParameterValues=notParameterValues
                )
            elif isinstance(value, set) and len(value) != 0:
                options[key] = cls.from_nested_dict(
                    {item: None for item in value},
                    notParameterValues=notParameterValues,
                )
            else:
                assert value is None or value in ({}, set())
                options[key] = None

        return cls(options, notParameterValues)

    def matchTextAlx(self, first_term: str) -> Optional[Completer]:
        result = None
        for i in range(len(first_term), -1, -1):
            result = self.options.get(first_term[:i])
            if result is not None:
                break

        return result

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
                if "=" not in text and len(completer.ExOptions) != 0:
                    for key, val in completer.ExOptions.items():
                        completer.options[key] = val
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
            completer = self.matchTextAlx(first_term)
            # print(str(type(completer)))

            # If we have a sub completer, use this for the completions.
            # print(str(self.notParameterValues))
            if completer is not None:
                for notParaVal in self.notParameterValues:
                    # print(notParaVal)
                    if notParaVal in completer.options:
                        completer.ExOptions[notParaVal] = completer.options.pop(
                            notParaVal, None
                        )
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
            completer = WordCompleter(
                list(self.options.keys()), ignore_case=self.ignore_case
            )
            for c in completer.get_completions(document, complete_event):
                yield c
