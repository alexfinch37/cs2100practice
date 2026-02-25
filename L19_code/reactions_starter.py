"""
🙂
"""

# Hint, Hint!
# from collections.abc import Sized, Container

import unittest

###

# TODO: Reactions class

###

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
