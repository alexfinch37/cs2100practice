"""
Practice problems
before quiz 2
"""

from typing import Any

import unittest

##################################################

# 1. Design & test create_email, which...
#    needs a recipient email (raise a ValueError
#    if it's left blank), and optionally a subject
#    (otherwise use "No Subject") and a sender
#    (otherwise use "noreply@northeastern.edu")
#    and produces the following (each on their
#    own line)...
# 
#    From: noreply@northeastern.edu
#    To: student@northeastern.edu
#    Subject: Subject

def create_email(
    recipient: str,
    subject: str = "No Subject",
    sender: str = "noreply@northeastern.edu"
) -> str:
    """
    Provides an email header

    Parameters
    ==========
    recipient: str
        email address to send to (required)

    subject: str
        optional, the email subject line
        (default = "No Subject)

    sender: str
        email address from which it is sent
        (default = "noreply@northeastern.edu")

    Returns
    =======
    str
        formatted email string with linebreaks, like...
        
        From: noreply@northeastern.edu
        To: student@northeastern.edu
        Subject: Subject

    Raises
    ======
    ValueError
        empty recipient
    """

    if not recipient:
        raise ValueError

    return "\n".join([
        f"From: {sender}",
        f"To: {recipient}",
        f"Subject: {subject}"
    ])

# 2. Design and test find_common,
#    which identifies the elements
#    that exist in both supplied lists

def find_common(lst1: list[Any], lst2: list[Any]) -> set[Any]:
    """
    Produces the set of elements that
    exist within both lists

    Parameters
    ==========
    lst1: list[Any]
        first list

    lst2: list[Any]
        second list

    Returns
    =======
    set[Any]
        items that exist in both
    """

    return set(lst1) & set(lst2)

# 3. Design and test swap_pairs,
#    which takes a list of pairs
#    and produces a new list where
#    the coordinates have been swapped

def swap_pairs(pairs: list[tuple[Any, Any]]) -> list[tuple[Any, Any]]:
    """
    Swaps the coordinates of the supplied
    list of pairs

    Parameters
    ==========
    pairs: list[tuple[Any, Any]]
        pairs to be swapped

    Returns
    =======
    list[tuple[Any, Any]]
        values swapped positions
        in each supplied pair
    """

    return [(b, a) for (a, b) in pairs]

# 4. Design and test second_connections,
#    which takes a person and a dictionary
#    describing person -> direct connections and
#    produces the set of 2nd-level
#    connections: those available via 1 hop
#    that are NOT direct connections (and not the person); 
#    if the person does not exist in connections,
#    ValueError!

def second_connections(person: str, connections: dict[str, set[str]]) -> set[str]:
    """
    Produces 2nd-level connections
    
    Parameters
    ==========
    person: str
        name for which to produce 2nd level

    connections: dict[str, set[str]]
        association between a person
        and their direct connections

    Returns
    =======
    set[str]
        2nd level connections

    Raises
    ======
    ValueError
        person not in connections
    """
    if person not in connections:
        raise ValueError 
    result: set[str] = set()
    directs: set[str] = connections[person]
    for direct in directs:
        for indirect in connections[direct]:
            if (indirect != person) and (indirect not in directs):
                result.add(indirect)
    return result


# 5. Design and test a Book class that represents
#    a vacation read. Each such book should have a title
#    (please provide a reasonable default) and pages read
#    (starting at 0). The book should have a method
#    to read (taking in the number of pages). Finally,
#    implement the __str__ method to provide the name
#    of the book and how many pages have thus far been read.

class Book:
    """Finally some fun reading!!""" 

    def __init__(self, title: str = "Joy") -> None:
        """
        Initializes the book

        Parameters
        ==========
        title: str
            provides the book's title
            ("Joy" if none given)
        """

        self._title: str = title
        self._pages_in: int = 0

    def read(self, pages: int) -> None:
        """
        Read some number of pages

        Parameters
        ==========
        pages: int
            how many pages read
            in this sitting
        """

        self._pages_in += pages

    def __str__(self) -> str:
        """
        Human-readable representation
        of the book

        Returns
        =======
        str
            "{title}: {#} page(s) in!"
        """

        return f"{self._title}: {self._pages_in} page(s) in!"

##################################################

class PracticeTest(unittest.TestCase):
    """Tests for the practice problems"""

    def test_create_email(self) -> None:
        "tests create_email"

        with self.assertRaises(ValueError):
            create_email("")

        self.assertEqual(
            create_email("student@northeastern.edu"),
            "From: noreply@northeastern.edu\nTo: student@northeastern.edu\nSubject: No Subject"
        )

        self.assertEqual(
            create_email("student@northeastern.edu", sender="president@northeastern.edu"),
            "From: president@northeastern.edu\nTo: student@northeastern.edu\nSubject: No Subject"
        )

        self.assertEqual(
            create_email("student@northeastern.edu", subject="Surprise!"),
            "From: noreply@northeastern.edu\nTo: student@northeastern.edu\nSubject: Surprise!"
        )

        self.assertEqual(
            create_email("ceo@google.com", sender="example@me.com", subject="Howdy"),
            "From: example@me.com\nTo: ceo@google.com\nSubject: Howdy"
        )

    def test_find_common(self) -> None:
        """Tests find_common"""

        self.assertEqual(find_common([], ['a', 'b', 'c', 1, 2, 3]), set())
        self.assertEqual(find_common(['a', 'b', 'c', 1, 2, 3], []), set())
        self.assertEqual(find_common(['a', 'b', 'c', 1, 2, 3], {'howdy'}), set())

        self.assertEqual(find_common(['a', 'b', 'c', 1, 2, 3], ['a', 1]), {'a', 1})

    def test_swappairs(self) -> None:
        """Tests swap_pairs"""

        self.assertEqual(swap_pairs([]), [])
        self.assertEqual(
            swap_pairs([('a', 1), (2, 'b')]),
            [(1, 'a'), ('b', 2)]
        )

    def test_second_connections(self) -> None:
        """Tests second_connections"""

        connections = {
            'alice': {'bob', 'chris'},
            'bob': {'alice', 'dan'},
            'chris': set(),
            'dan': {'bob', 'e'},
            'e': set()
        }

        with self.assertRaises(ValueError):
            second_connections('fred', connections)

        self.assertEqual(
            second_connections('alice', connections),
            {'dan',},
        )

        self.assertEqual(
            second_connections('bob', connections),
            {'chris', 'e'},
        )

        self.assertEqual(
            second_connections('chris', connections),
            set(),
        )

        self.assertEqual(
            second_connections('dan', connections),
            {'alice',},
        )

        self.assertEqual(
            second_connections('e', connections),
            set(),
        )

    def test_book(self) -> None:
        """Tests for the Book class"""

        b1 = Book()

        self.assertEqual(
            str(b1),
            "Joy: 0 page(s) in!"
        )

        b1.read(10)

        self.assertEqual(
            str(b1),
            "Joy: 10 page(s) in!"
        )

        #

        b1 = Book("Dune")

        self.assertEqual(
            str(b1),
            "Dune: 0 page(s) in!"
        )

        b1.read(1)

        self.assertEqual(
            str(b1),
            "Dune: 1 page(s) in!"
        )


##################################################

def main() -> None:
    """Let's get going!"""
    unittest.main()

if __name__ == "__main__":
    main()
