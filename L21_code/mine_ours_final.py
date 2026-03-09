"""
Understanding instance
vs class data
"""

from __future__ import annotations

from typing import Optional

#

class Example:
    """Feeling DRY-er :)"""

    _instance_count: int = 0
    GEOCODE_API: str = "http://api.openweathermap.org/geo/1.0/direct"

    def __init__(self, home: str) -> None:
        """
        Creates an instance

        Parameters
        ==========
        home: str
            where from?
        """

        Example._instance_count += 1
        # self.__class__._instance_count += 1

        self._home = home
        self._id = self.num_humans()

    @property
    def home(self) -> str:
        """Where is home?"""

        return self._home

    @classmethod
    def num_humans(cls) -> int:
        """Number of peeps"""

        return cls._instance_count

    @staticmethod
    def home_with_planet(home: str, planet: str = "Earth") -> str:
        """
        Produces home name with planet
        """

        return f"{home} ({planet})"

    @staticmethod
    def geocode_url(q: str, api_key: str, limit: Optional[int] = None) -> str:
        """
        OpenWeather geocode API url

        Parameters
        ==========
        q: str
            location to query

        api_key: str
            api key

        limit: Optional[int]
            up to 5 responses

        Raises
        ======
        ValueError
            invalid limit

        Returns
        =======
        str
            URL for geocode info
        """

        if limit and limit not in range(1, 6):
            raise ValueError("Limit must be in [1, 5]")

        params: dict[str, str] = {
            'q': q,
            'appid': api_key,
        }

        if limit:
            params['limit'] = str(limit)

        param_str: str = '&'.join(
            f"{k}={v}"
            for k,v in params.items()
        )

        return (
            f"{Example.GEOCODE_API}"
            f"?{param_str}"
        )

    @classmethod
    def create_earthly(cls, home: str) -> Example:
        """
        Constructs an instance with
        associated home
        """

        return cls(Example.home_with_planet(home))

    @classmethod
    def create_usa(cls, city: str, state: str) -> Example:
        """
        Constructs an instance with
        associated usa city+state
        """
        return cls.create_earthly(
            f"{city}, {state}, USA"
        )

    def __str__(self) -> str:
        """Where from?"""

        return (
            "Human "
            f"({self._id} of {self.num_humans()}) "
            f"from {self._home}"
        )

def main() -> None:
    """Some instances"""

    print(Example.home_with_planet("Olympus Mons", "Mars"))
    print(Example.home_with_planet("Mount Everest"))
    print()

    # should NEVER have in source or repo!!
    fake_key: str = "abc123"

    print(Example.geocode_url("Boston,MA,USA", fake_key))
    print()

    for e in (
        Example("bed"),
        Example.create_usa("Boston", "MA"),
        Example.create_usa("Oakland", "CA"),
        Example.create_usa("New York", "NY"),
        Example.create_earthly("London, UK"),
    ):
        print(e)

if __name__ == "__main__":
    main()
