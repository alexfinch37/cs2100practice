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

        # "stuff" for next level of recursion
        next_level = level + 1
        next_path = Folder._make_path(
            path,
            self.name
        )

        # add this folder
        lines.append(
            Folder._bullet(
                level,
                next_path
            )
        )

        # add any files in this folder
        for fi in self._files:
            lines.append(
                type(self)._bullet(
                    next_level,
                    Folder._make_path(
                        next_path,
                        fi
                    )
                )
            )

        # recursively add any folders
        # (with their hierarchy)
        for fo in self._subfolders:
            lines += fo._str_helper(
                next_level,
                next_path
            )

        # accumulated lines
        return lines

    def __str__(self) -> str:
        """
        What's the view from this folder down?
        """

        return "\n".join(self._str_helper(0, ""))

    @property
    def num_folders(self) -> int:
        """
        How many folders are in this folder
        (including this one)?
        """

        # accumulator
        # (initial value includes this folder!)
        total: int = 1

        # add recursively from sub-folders
        for fo in self._subfolders:
            total += fo.num_folders

        # accumulation complete!
        return total

    def has_file(self, query_name: str) -> bool:
        """
        Can the file name be found
        in this or any subfolders?
        """

        # base case: found locally
        in_this_folder = query_name in self._files

        return in_this_folder or any(
            # recursively try in
            # sub-folders
            fo.has_file(query_name)
            for fo in self._subfolders
        )


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

    def test_num_folders(self) -> None:
        """folder.num_folders"""

        self.assertEqual(applications.num_folders, 1)
        self.assertEqual(root.num_folders, 5)

    def test_has_file(self) -> None:
        """folder.has_file()"""

        self.assertTrue(root.has_file("defying_gravity.mp3"))
        self.assertFalse(root.has_file("api_key.txt"))
        self.assertTrue(root.has_file("code.py"))
        self.assertFalse(student_downloads.has_file("code.py"))

if __name__ == "__main__":
    print("== subfolder ==")
    print(users_student)
    print()

    print("== root ==")
    print(root)
    print()

    unittest.main()
