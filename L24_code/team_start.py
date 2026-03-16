"""
Org charts!!
"""

from __future__ import annotations

from typing import Iterable

import unittest

###

class Human:
    """🧍"""

    def __init__(self, name: str, role: str) -> None:
        """A peep with a fresh team"""

        self._name = name
        self._role = role
        self._team: list[Human] = []

    def __str__(self) -> str:
        """Name tag?"""

        return f"{self._name} ({self._role})"

    def add_team_member(self, *peeps: Human) -> None:
        """Adds humans to the team!"""

        for h in peeps:
            self._team.append(h)

    @property
    def team_size(self) -> int:
        """
        How many humans?
        (including this one)
        """

        # TODO #1a: base case here!
        # how many humans do you have
        # if you have no one in your team?

        # TODO #1b: the "smaller" set of
        # humans is found via each member
        # of your direct team - how many
        # humans do each of them contribute
        # to the total?

        # TODO #1c: make sure to return!

        # TODO #1d: uncomment the test below 🧐

    @property
    def team_depth(self) -> int:
        """
        How deep does it go?
        Each human counts as a level
        (including this one)
        """

        # TODO #2a: base case here!
        # what is the depth if you have
        # no one on your team?

        # TODO #2b: the "smaller" set of
        # humans is found via each member
        # of your direct team - if you had
        # the depth of their teams, how do
        # you find the depth of your own?
        # start by getting those depths...

        # TODO #2c: now combine + return!

        # TODO #2d: uncomment the test below 🤓


    @staticmethod
    def _bullet(level: int, thing: str) -> str:
        """
        Produces consistent spacing for
        bulleted lists
        """

        space_before = 2 * level * " "

        return f"{space_before}* {thing}"

    def _org_helper(self, level: int) -> Iterable[str]:
        """Produce lines of bulleted humans"""

        # TODO 3a: producing a bulleted picture
        # (like below) involves keeping track of
        # "stuff" (i.e., the level you are on within
        # the hierarchy) - so examine the initialization
        # below from org_chart.

        lines: list[str] = []

        # Your job is to populate this list
        # with lines, and you have help!

        # TODO 3b: let's start with the "base" case...
        # even if there's no one on the team, you'll
        # add yourself - use _bullet above to add this
        # string to the lines

        # TODO 3c: now let's figure out the level
        # for the team members?

        # TODO 3d: lastly, recursively get the lines
        # for each team member and combine their lines
        # with what you already have

        # Now the prints in main should be pretty :)

        return lines

    def org_chart(self) -> str:
        """Picture time!"""

        return "\n".join(self._org_helper(0))

#   * Aoun (President)
#     * Winkelstein (Provost)
#       * Brodley (Dean)
#       * Mynatt (Dean)
#         * Mislove (Sr Assoc Dean)
#           * Jamieson (Assoc Dean)
#             * Strange (Director)
#             * Derbinsky (peon)
#         * Hescott (Sr Assoc Dean)
#     * Henderson (Chancellor)

aoun = Human("Aoun", "President")

winkelstein = Human("Winkelstein", "Provost")
henderson = Human("Henderson", "Chancellor")

brodley = Human("Brodley", "Dean")
mynatt = Human("Mynatt", "Dean")

mislove = Human("Mislove", "Sr Assoc Dean")
hescott = Human("Hescott", "Sr Assoc Dean")

jamieson = Human("Jamieson", "Assoc Dean")

strange = Human("Strange", "Director")

derbinsky = Human("Derbinsky", "peon")

aoun.add_team_member(winkelstein, henderson)
winkelstein.add_team_member(brodley, mynatt)
mynatt.add_team_member(mislove, hescott)
mislove.add_team_member(jamieson)
jamieson.add_team_member(strange, derbinsky)

#

class TeamTest(unittest.TestCase):
    """Testing team stats"""

    # def test_team_size(self) -> None:
    #     "human.team_size"

    #     self.assertEqual(derbinsky.team_size, 1)
    #     self.assertEqual(jamieson.team_size, 3)
    #     self.assertEqual(mislove.team_size, 4)
    #     self.assertEqual(mynatt.team_size, 6)
    #     self.assertEqual(winkelstein.team_size, 8)
    #     self.assertEqual(aoun.team_size, 10)

    # def test_team_depth(self) -> None:
    #     "human.team_depth"

    #     self.assertEqual(derbinsky.team_depth, 1)
    #     self.assertEqual(jamieson.team_depth, 2)
    #     self.assertEqual(mislove.team_depth, 3)
    #     self.assertEqual(mynatt.team_depth, 4)
    #     self.assertEqual(winkelstein.team_depth, 5)
    #     self.assertEqual(aoun.team_depth, 6)

if __name__ == "__main__":
    print("== university ==")
    print(aoun.org_chart())
    print()

    print("== college ==")
    print(mynatt.org_chart())
    print()

    print("== classroom ==")
    print(derbinsky.org_chart())
    print()

    unittest.main()
