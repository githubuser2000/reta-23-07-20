"""
Nestedcompleter for completion of hierarchical data structures.
"""
from typing import Any, Dict, Iterable, Mapping, Optional, Set, Union

from prompt_toolkit.completion import CompleteEvent, Completer, Completion
from prompt_toolkit.completion.word_completer import WordCompleter
from prompt_toolkit.document import Document

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
        ignore_case: bool = True,
        already: set[str, Optional[Completer]] = {},
    ) -> None:

        self.options = options
        self.ignore_case = ignore_case
        self.already = already

    def __repr__(self) -> str:
        return "NestedCompleter(%r, ignore_case=%r)" % (self.options, self.ignore_case)

    # @classmethod
    def from_nested_dict(self, data: NestedDict, already: set) -> "NestedCompleter":
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

        def setAufgeloestes(dic, key, value):
            self.already[(key, value.keys())] = dic[key]

        def setDict(key, value):
            if type(value) is dict:
                if type(self.already) is not dict:
                    self.already = {}
                try:
                    if self.already[(key, value.keys())] is not None:
                        return key, value, self.already[(key, value.keys())]
                    else:
                        return key, value, None
                except KeyError:
                    self.already[(key, value.keys())] = None
                    return key, value, None

            elif type(value) is Completer:
                if type(self.already) is not dict:
                    self.already = {}
                if (key, value.keys()) not in self.already:
                    self.already[(key, value)] = None
                    return key, value, None
                elif self.already[(key, value)] is not None:
                    return key, value, self.already[(key, value.keys())]
                else:
                    pass
            # for first, second in self.already:
            #     pass

        options: Dict[str, Optional[Completer]] = {}
        for key, value in data.items():
            if isinstance(value, Completer):
                key, value = setDict(self.already, key, value)
                options[key] = value
            elif isinstance(value, dict):
                key, value = setDict(self.already, key, value)
                options[key] = self.from_nested_dict(value)
                setAufgeloestes(options, key, value)
            elif isinstance(value, set):
                key, value = setDict(self.already, key, {item: None for item in value})
                options[key] = self.from_nested_dict({item: None for item in value})
            else:
                assert value is None
                options[key] = None

        return NestedCompleter(options, already=self.already)

    def get_completions(
        self, document: Document, complete_event: CompleteEvent
    ) -> Iterable[Completion]:
        # Split document.
        text = document.text_before_cursor.lstrip()
        stripped_len = len(document.text_before_cursor) - len(text)

        # If there is a space, check for the first term, and use a
        # subcompleter.
        if " " in text:
            first_term = text.split()[0]
            completer = self.options.get(first_term)

            # If we have a sub completer, use this for the completions.
            if completer is not None:
                remaining_text = text[len(first_term) :].lstrip()
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