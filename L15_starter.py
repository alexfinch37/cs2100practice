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

def create_email(recipient: str, sender: str, subject: str) -> str:
    """
    Docstring for create_email
    
    :param recipient: Description
    :type recipient: str
    :param sender: Description
    :type sender: str
    :param subject: Description
    :type subject: str
    :return: Description
    :rtype: str
    """

    if recipient is None:
        raise ValueError("Need a recipient")
    if sender is None:
        sender = "noreply@northeastern.edu"
    if subject is None:
        subject = "No Subject"
    
    return f"From: {sender}\nTo: {recipient}\nSubject: {subject}"

class TestCreateEmail(unittest.TestCase):
    """tests for create email"""
    def test_create_email_valid(self) -> None:
        """testing with all valid imports"""
        result = create_email("arnav@gmail.com", "alex@finch.com", "arnav is lame")
        self.assertEqual(result, "From: alex@finch.com\nTo: arnav@gmail.com\nSubject: arnav is lame")

    def test_create_email_invalid(self) -> None:
        """testing with all bad parameters"""
        self.assertRaises(ValueError, create_email, None, "arnav@gmail.com", "Hello")

    def test_some_parameters(self) -> None:
        """testing with some of the parameters"""
        result = create_email("arnav@gmail.com", None, None)
        self.assertEqual(result, "From: noreply@northeastern.edu\nTo: arnav@gmail.com\nSubject: No Subject")


# 2. Design and test find_common,
#    which identifies the elements
#    that exist in both supplied lists

# TODO: find_common


# 3. Design and test swap_pairs,
#    which takes a list of pairs
#    and produces a new list where
#    the coordinates have been swapped

# TODO: swap_pairs


# 4. Design and test second_connections,
#    which takes a person and a dictionary
#    describing person -> direct connections and
#    produces the set of 2nd-level
#    connections: those available via 1 hop
#    that are NOT direct connections (and not the person); 
#    if the person does not exist in connections,
#    ValueError!

# TODO: second_connections


# 5. Design and test a Book class that represents
#    a vacation read. Each such book should have a title
#    (please provide a reasonable default) and pages read
#    (starting at 0). The book should have a method
#    to read (taking in the number of pages). Finally,
#    implement the __str__ method to provide the name
#    of the book and how many pages have thus far been read.

# TODO: Book


##################################################

class PracticeTest(unittest.TestCase):
    """Tests for the practice problems"""

    def test_create_email(self) -> None:
        "tests create_email"

        # with self.assertRaises(ValueError):
        #     create_email("")

        # self.assertEqual(
        #     create_email("student@northeastern.edu"),
        #     "From: noreply@northeastern.edu\nTo: student@northeastern.edu\nSubject: No Subject"
        # )

        # TODO: more testing!


    def test_find_common(self) -> None:
        """Tests find_common"""

        # self.assertEqual(find_common({'a', 'b', 'c', 1, 2, 3}, {'a', 1}), {'a', 1})
        # TODO: more testing!


    def test_swappairs(self) -> None:
        """Tests swap_pairs"""

        # self.assertEqual(
        #     swap_pairs([('a', 1), (2, 'b')]),
        #     [(1, 'a'), ('b', 2)]
        # )
        # TODO: more testing!


    def test_second_connections(self) -> None:
        """Tests second_connections"""

        # connections = {
        #     'alice': {'bob', 'chris'},
        #     'bob': {'alice', 'dan'},
        #     'chris': set(),
        #     'dan': {'bob', 'e'},
        #     'e': set()
        # }

        # with self.assertRaises(ValueError):
        #     second_connections('fred', connections)

        # self.assertEqual(
        #     second_connections('alice', connections),
        #     {'dan',},
        # )

        # self.assertEqual(
        #     second_connections('bob', connections),
        #     {'chris', 'e'},
        # )

        # self.assertEqual(
        #     second_connections('chris', connections),
        #     set(),
        # )

        # self.assertEqual(
        #     second_connections('dan', connections),
        #     {'alice',},
        # )

        # self.assertEqual(
        #     second_connections('e', connections),
        #     set(),
        # )


    def test_book(self) -> None:
        """Tests for the Book class"""

        # b1 = Book()

        # self.assertEqual(
        #     str(b1),
        #     "Joy: 0 page(s) in!"
        # )

        # b1.read(10)

        # self.assertEqual(
        #     str(b1),
        #     "Joy: 10 page(s) in!"
        # )

        # #

        # b1 = Book("Dune")

        # self.assertEqual(
        #     str(b1),
        #     "Dune: 0 page(s) in!"
        # )

        # b1.read(1)

        # self.assertEqual(
        #     str(b1),
        #     "Dune: 1 page(s) in!"
        # )


##################################################

def main() -> None:
    """Let's get going!"""
    unittest.main()

if __name__ == "__main__":
    main()
