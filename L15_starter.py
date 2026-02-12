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


# 2. Design and test find_common,
#    which identifies the elements
#    that exist in both supplied lists

def find_common(lst1: list[Any], lst2: list[Any]) -> list[Any]:
    """
    Docstring for find_common
    
    :param lst1: Description
    :type lst1: List[Any]
    :param lst2: Description
    :type lst2: List[Any]
    """
    
    union_list = []
    for item in lst1:
        if item in lst2:
            union_list.append(item)
    return union_list


# 3. Design and test swap_pairs,
#    which takes a list of pairs
#    and produces a new list where
#    the coordinates have been swapped

def swap_pairs(lst: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """
    Docstring for swap_pairs
    
    :param lst: Description
    :type lst: list[tuple]
    :return: Description
    :rtype: list[tuple]
    """

    new_pairs: list[tuple[int, int]] = []
    for pair in lst:
        new_pairs.append((pair[1], pair[0]))
    return new_pairs


# 4. Design and test second_connections,
#    which takes a person and a dictionary
#    describing person -> direct connections and
#    produces the set of 2nd-level
#    connections: those available via 1 hop
#    that are NOT direct connections (and not the person); 
#    if the person does not exist in connections,
#    ValueError!

#{person: connect1, connect2, connect3}
#{connect: connect4, connect5, connect6}
#second_connections(person, dict)
#result = (connect4, connect5, connect6)
def second_connections(person: str, connects: dict[str, list[str]]) -> set:
    """
    Docstring for second_connections
    
    :param person: Description
    :type person: str
    :param connects: Description
    :type connects: dict[str, str]
    :return: Description
    :rtype: set
    """
    first_connects = connects.get(person, [])
    second_connects = set()
    
    for friend in first_connects:
        # Get friends of each first-degree connection
        friends_of_friend = connects.get(friend, [])
        for second_degree in friends_of_friend:
            # Exclude the original person and direct friends
            if second_degree != person and second_degree not in first_connects:
                second_connects.add(second_degree)
    
    return second_connects
    




# 5. Design and test a Book class that represents
#    a vacation read. Each such book should have a title
#    (please provide a reasonable default) and pages read
#    (starting at 0). The book should have a method
#    to read (taking in the number of pages). Finally,
#    implement the __str__ method to provide the name
#    of the book and how many pages have thus far been read.

class Book:
    """book class"""
    def __init__(self, title: str = "No Name", pages_read: int = 0):
        """
        Docstring for __init__
        
        :param self: Description
        :param title: Description
        :type title: str
        :param pages_read: Description
        :type pages_read: int
        """
        self.title = title
        self.pages_read = pages_read

    def read(self, added_pages: int) -> None:
        """
        Docstring for read
        
        :param self: Description
        :param added_pages: Description
        :type added_pages: int
        """
        self.pages_read += added_pages

    def __str__(self) -> str:
        """nice readable version"""
        return f"Title: {self.title}\nPages Read: {self.pages_read}"

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

def get_friends(name: str, enemies: dict[str, list[str]]) -> list[str]:
    """Returns a list of friends of the person with the given name.
    A friend is defined as an enemy of an enemy.
    For example, if A is an enemy of B, and B is an enemy of C,
    then A and C are friends.
    Args:
    name (str): The name of the person whose friends are to be found
    enemies (dict[str, list[str]]): A dictionary mapping person names
    to a list of their enemy names
    Returns:
    A list of names of friends. May contain repeated names.
    """

    enemies = {
    'Mini': ['Mega', 'Micro'],
    'Mega': ['Mini', 'Giga', 'Micro'],
    'Micro': ['Mini', 'Micro'], # Yes, Micro is Micro's own enemy
    'Giga': ['Mega']}
    if name not in enemies:
        return []
    friends: list[str] = []
    for enemy_name in enemies[name]:
        for friend_name in enemies[enemy_name]:
            friends.append(friend_name)
    return friends
    

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

    def test_common_list_valid(self) -> None:
        """testing longer list with valid input"""
        first_list = ["hello", "testing", "1", "2", "3"]
        second_list = ["hello", "1", "3", "4"]
        result = find_common(first_list, second_list)
        self.assertEqual(result, ["hello", "1", "3"])

    def test_common_list_valid_mixed(self) -> None:
        """testing longer list with valid input"""
        first_list: list[Any] = ["hello","testing", "1", "2", 3]
        second_list: list[Any] = ["hello", "1", 3, "4"]
        result = find_common(first_list, second_list)
        self.assertEqual(result, ["hello", "1", 3])

    def test_common_list_valid_longer_second(self) -> None:
        """testing longer list with valid input"""
        first_list: list[Any] = ["hello","testing", "1", "2", 3, "17"]
        second_list: list[Any] = ["hello", "1", 3, "4", "5", "17", "testing"]
        result = find_common(first_list, second_list)
        self.assertEqual(result, ["hello", "testing", "1", 3, "17",])

    def test_str_with_defaults(self) -> None:
        """Test string representation with default values."""
        book = Book()
        expected = "Title: No Name\nPages Read: 0"
        self.assertEqual(str(book), expected)
    
    def test_str_with_title(self) -> None:
        """Test string representation with custom title."""
        book = Book("Brave New World")
        expected = "Title: Brave New World\nPages Read: 0"
        self.assertEqual(str(book), expected)
    
    def test_str_with_pages_read(self) -> None:
        """Test string representation after reading pages."""
        book = Book("Fahrenheit 451")
        book.read(75)
        expected = "Title: Fahrenheit 451\nPages Read: 75"
        self.assertEqual(str(book), expected)
    
    def test_str_with_initial_pages(self) -> None:
        """Test string representation with initial pages_read."""
        book = Book("Catch-22", 200)
        expected = "Title: Catch-22\nPages Read: 200"
        self.assertEqual(str(book), expected)
    
    # Edge cases and integration tests
    
    def test_multiple_books_independent(self) -> None:
        """Test that multiple book objects are independent."""
        book1 = Book("Book 1")
        book2 = Book("Book 2")
        book1.read(50)
        book2.read(30)
        self.assertEqual(book1.pages_read, 50)
        self.assertEqual(book2.pages_read, 30)
    
    def test_title_with_special_characters(self) -> None:
        """Test book title with special characters."""
        book = Book("The Hitchhiker's Guide to the Galaxy")
        self.assertEqual(book.title, "The Hitchhiker's Guide to the Galaxy")
    
    def test_empty_string_title(self) -> None:
        """Test book with empty string as title."""
        book = Book("")
        self.assertEqual(book.title, "")
        self.assertEqual(str(book), "Title: \nPages Read: 0")
    
    def test_large_number_of_pages(self) -> None:
        """Test reading a very large number of pages."""
        book = Book("War and Peace")
        book.read(1000000)
        self.assertEqual(book.pages_read, 1000000)

##################################################

def main() -> None:
    """Let's get going!"""
    unittest.main()

if __name__ == "__main__":
    main()
