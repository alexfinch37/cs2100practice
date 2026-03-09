"""
Understanding instance
vs class data
"""

class Example:
    """Feeling DRY?"""

    def __init__(self, home: str) -> None:
        """
        Construct an instance

        Parameters
        ==========
        home: str
            where from?
        """
        self.home = home
        self.planet = "Earth"

    def __str__(self) -> str:
        """Where from?"""
        return f"Human from {self.home}, {self.planet}"

def main() -> None:
    """Some instances"""

    for e in (
        Example("Boston, MA, USA"),
        Example("Oakland, CA, USA"),
        Example("London, England, UK"),
        Example("New York, NY, USA"),
    ):
        print(e)

if __name__ == "__main__":
    main()
