"""
Recursion example
on a tree of folders
"""

from __future__ import annotations

from typing import Iterable

import unittest

###

class Folder:
    """A folder!"""

    SEPERATOR: str = "/"

    def __init__(self, name: str) -> None:
        """Creates a new empty folder"""

        self._name = name
        self._files: list[str] = []
        self._subfolders: list[Folder] = [] # recursive structure!

    def add_file(self, fname: str) -> None:
        """Adds a file to the folder"""
        self._files.append(fname)

    def add_subfolder(self, directory: Folder) -> None:
        """Adds a folder as a subfolder"""
        self._subfolders.append(directory)

    @property
    def name(self) -> str:
        """Get my name!"""
        return self._name

    ###

    @property
    def num_folders(self) -> int:
        """
        How many folders are in this folder
        (including this one)?
        """

        # TODO #1: code + uncomment test below

    def has_file(self, query_name: str) -> bool:
        """
        Can the file name be found
        in this or any subfolders?
        """

        # TODO #2: code + uncomment test below

    @staticmethod
    def _bullet(level: int, thing: str) -> str:
        """
        Produces consistent spacing for
        bulleted lists
        """

        space_before = 2 * level * " "

        return f"{space_before}* {thing}"

    @staticmethod
    def _make_path(prefix: str, thing: str) -> str:
        """
        Produces consistent look of
        separated paths

        "" + "after" -> "after"
        "/" + "after" -> "/after"
        "before" + "after" -> "before/after"
        """

        # starting path
        if not prefix:
            return thing

        # root
        if prefix == Folder.SEPERATOR:
            return f"{prefix}{thing}"

        # everything/else/like/this
        return f"{prefix}{Folder.SEPERATOR}{thing}"

    def _str_helper(self, level: int, path: str) -> Iterable[str]:
        """
        Recursively build up
        deeper paths
        """

        # accumulator
        lines: list[str] = []

        # TODO #3: code + see pretty from main :)

        # accumulated lines
        return lines

    def __str__(self) -> str:
        """
        What's the view from this folder down?
        """

        return "\n".join(self._str_helper(0, ""))


#   * /
#     * /Users
#       * /Users/student
#         * /Users/student/code.py
#         * /Users/student/Downloads
#           * /Users/student/Downloads/defying_gravity.mp3
#     * /Applications

root: Folder = Folder("/")
users: Folder = Folder("Users")
applications: Folder = Folder("Applications")
users_student: Folder = Folder("student")
student_downloads: Folder = Folder("Downloads")

root.add_subfolder(users)
root.add_subfolder(applications)
users.add_subfolder(users_student)
users_student.add_subfolder(student_downloads)
users_student.add_file("code.py")
student_downloads.add_file("defying_gravity.mp3")

###

class TestFolder(unittest.TestCase):
    """Testing Folder"""

    # def test_num_folders(self) -> None:
    #     """folder.num_folders"""

    #     self.assertEqual(applications.num_folders, 1)
    #     self.assertEqual(root.num_folders, 5)

    # def test_has_file(self) -> None:
    #     """folder.has_file()"""

    #     self.assertTrue(root.has_file("defying_gravity.mp3"))
    #     self.assertFalse(root.has_file("api_key.txt"))
    #     self.assertTrue(root.has_file("code.py"))
    #     self.assertFalse(student_downloads.has_file("code.py"))

if __name__ == "__main__":
    print("== subfolder ==")
    print(users_student)
    print()

    print("== root ==")
    print(root)
    print()

    unittest.main()
