"""
🙂
"""

from collections.abc import Sized, Container

import unittest

###

class Reactions(Sized, Container[str]):
    """Keeps track of reactions"""

    def __init__(self) -> None:
        self.__reactions: list[str] = []

    def send_reaction(self, s: str) -> None:
        """
        Adds a reaction

        Parameters
        ==========
        s: str
            reaction to add
        """
        self.__reactions.append(s)

    def __len__(self) -> int:
        """
        Gets number of reactions sent

        Returns
        =======
        int
            Number of reactions
        """

        return len(self.__reactions)
    
    def __contains__(self, reaction: object) -> bool:
        """
        Determines if the supplied
        reaction had been sent

        Parameters
        ==========
        reaction: object
            reaction to find

        Returns
        =======
        bool
            True if the reaction had been sent
        """

        return reaction in self.__reactions
    
    def __str__(self) -> str:
        """
        Concatenation of all sent reactions

        Returns
        =======
        str
            reactions sent in order
        """

        return "".join(self.__reactions)

class TestL8(unittest.TestCase):

    def test_admin(self) -> None:
        """Test the admin video"""

        vid: Reactions = Reactions()

        vid.send_reaction("🔥")
        vid.send_reaction("👏")
        vid.send_reaction("❤️")
        vid.send_reaction("👍")
        vid.send_reaction("👍")

        self.assertEqual(str(vid), "🔥👏❤️👍👍")
        self.assertEqual(len(vid), 5)
        
        self.assertTrue("🔥" in vid)
        self.assertTrue("👏" in vid)
        self.assertTrue("❤️" in vid)
        self.assertTrue("👍" in vid)
        self.assertFalse("🙌" in vid)

    def test_oo_testing(self) -> None:
        """Test the oo_testing video"""

        vid: Reactions = Reactions()

        vid.send_reaction("👍")

        self.assertEqual(str(vid), "👍")
        self.assertEqual(len(vid), 1)
        
        self.assertFalse("🔥" in vid)
        self.assertFalse("👏" in vid)
        self.assertFalse("❤️" in vid)
        self.assertTrue("👍" in vid)
        self.assertFalse("🙌" in vid)

    def test_memory_mutability_testing(self) -> None:
        """Test the memory_mutability_testing video"""

        vid: Reactions = Reactions()

        vid.send_reaction("❤️")
        vid.send_reaction("👍")

        self.assertEqual(str(vid), "❤️👍")
        self.assertEqual(len(vid), 2)
        
        self.assertFalse("🔥" in vid)
        self.assertFalse("👏" in vid)
        self.assertTrue("❤️" in vid)
        self.assertTrue("👍" in vid)
        self.assertFalse("🙌" in vid)

    def test_new(self) -> None:
        """Test a new video"""

        vid: Reactions = Reactions()

        self.assertEqual(str(vid), "")
        self.assertEqual(len(vid), 0)
        
        self.assertFalse("🔥" in vid)
        self.assertFalse("👏" in vid)
        self.assertFalse("❤️" in vid)
        self.assertFalse("👍" in vid)
        self.assertFalse("🙌" in vid)

if __name__ == "__main__":
    unittest.main()
