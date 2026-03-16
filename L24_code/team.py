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

        # accumulator
        # (initialized to include me!)
        total: int = 1

        if not self._team:
            return total

        return total + sum(
            h.team_size
            for h in self._team
        )

        # same as...
        # for h in self._team:
        #     total += h.team_size
        # return total

    @property
    def team_depth(self) -> int:
        """
        How deep does it go?
        Each human counts as a level
        (including this one)
        """

        me: int = 1

        if not self._team:
            return me

        depths_below = [
            h.team_depth
            for h in self._team
        ]

        return me + max(depths_below)

        # same as...
        # from typing import Optional, cast

        # deepest_so_far: Optional[int] = None

        # for h in self._team:
        #     h_depth = h.team_depth
        #     if (deepest_so_far is None) or (h_depth > deepest_so_far):
        #         deepest_so_far = h_depth
        
        # return me + cast(int, deepest_so_far)
                


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

        lines: list[str] = [
            Human._bullet(level, str(self)),
        ]

        next_level = level + 1

        for h in self._team:
            lines += h._org_helper(next_level)

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

    def test_team_size(self) -> None:
        "human.team_size"

        self.assertEqual(derbinsky.team_size, 1)
        self.assertEqual(jamieson.team_size, 3)
        self.assertEqual(mislove.team_size, 4)
        self.assertEqual(mynatt.team_size, 6)
        self.assertEqual(winkelstein.team_size, 8)
        self.assertEqual(aoun.team_size, 10)

    def test_team_depth(self) -> None:
        "human.team_depth"

        self.assertEqual(derbinsky.team_depth, 1)
        self.assertEqual(jamieson.team_depth, 2)
        self.assertEqual(mislove.team_depth, 3)
        self.assertEqual(mynatt.team_depth, 4)
        self.assertEqual(winkelstein.team_depth, 5)
        self.assertEqual(aoun.team_depth, 6)

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
