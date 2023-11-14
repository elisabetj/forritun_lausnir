#!/usr/bin/python3

from io import TextIOWrapper
from typing import Dict, List, Set
from string import punctuation

DOCUMENT_END = "<END OF DOCUMENT>"
SEARCH = "search"
PRINT = "print"
NO_MATCH = "No match"
OPTIONS = {SEARCH, PRINT}


def main() -> None:
    documents = get_documents()
    if documents is None:
        return

    registry = register_words(documents)
    handle_queries(documents, registry)


def get_documents() -> List[str] | None:
    """Retrieves documents from a file specified by the user."""
    file_name = input()
    try:
        with open(file_name) as file:
            return extract_documents(file)
    except FileNotFoundError:
        return None


def extract_documents(file_object: TextIOWrapper) -> List[str]:
    """Reads all documents in the file object into a list and returns it.

    Each list entry is a string representing a document.
    """
    documents = file_object.read().split(DOCUMENT_END)
    assert documents[-1].strip() == ""
    return documents[:-1]


def register_words(documents: List[str]) -> Dict[str, Set[int]]:
    """Returns a dictionary of words and the documents they appear in."""
    document_sets = {}
    for index, document in enumerate(documents):
        for word in document.split():
            word = word.strip(punctuation).lower()
            if word:
                if word not in document_sets:
                    document_sets[word] = set()

                document_sets[word].add(index)

    return document_sets


def handle_queries(documents: List[str], words: Dict[str, Set[int]]) -> None:
    """Enables the user to interact with the documents.

    Repeatedly offers the user a selection of option,
    until the user moves on.

    Currently, there are two options.
      Search:
        The user specifies a number of search words,
        and the program responds by listing the documents
        containing all the specified search terms.
        If no search words are specified, no documents are listed.
      Print:
        The user specifies the number of the document to examine,
        and the program responds by printing the specified document.
    """
    while (action := input()) in OPTIONS:
        query = input()
        if action == SEARCH:
            document_indices = search_documents(words, query)
            print_document_numbers(document_indices)
        else:
            assert action == PRINT
            print_document(documents, query)


def search_documents(documents: Dict[str, Set[int]], query: str) -> Set[int]:
    """Finds which documents contain all the words in the search string."""
    search_words = query.strip().lower().split()
    document_sets = [
        documents[search_word] if search_word in documents else set()
        for search_word in search_words
    ]

    if document_sets:
        return get_intersection(document_sets)
    else:
        # If no search word is entered, no documents should be listed.
        return set()


def get_intersection(sets: List[Set[int]]) -> Set[int]:
    """Returns a set of the elements contained in all sets in the list.

    Assumes the list is nonempty,
    as the empty intersection would have to be some kind of universal set,
    containing all applicable sets as subsets.
    """
    # In this case, no set would be larger than the list of all documents,
    # so that range could be taken as the universal set,
    # but providing that context to this function
    # would mean passing that information down through the function calls,
    # and is not necessary.

    intersection = sets.pop()

    for index_set in sets:
        intersection = intersection & index_set

    return intersection


def print_document_numbers(document_indices: Set[int]) -> None:
    """Prints out document numbers, sorted in ascending order."""
    if not document_indices:
        print(NO_MATCH)
        return

    print("Documents matching search: ", end="")
    for index in sorted(document_indices):
        print(index + 1, end=" ")

    print()


def print_document(documents: List[str], query: str) -> None:
    """Prints out the contents of the requested document."""
    document_number = int(query)
    if 1 <= document_number <= len(documents):
        document = documents[document_number - 1]
        print(f"Document #{document_number}:")
        # There is a new line at the end of each document string.
        # Make sure not to add an extra empty line to the end.
        print(document, end="")
    else:
        print(NO_MATCH)


if __name__ == "__main__":
    main()
