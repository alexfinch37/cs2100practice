"""
Practice with OOP
"""

class CoffeeBag:
    """
    Data type for bags of coffee
    """
    
    def __init__(self, roast_level: str, grams: int) -> None:
        """
        Intiailizes the bag
        """

        self.roast_level: str = roast_level
        self.grams: int = grams

    def __str__(self) -> str:
        """
        Nice readable version of the bag
        """

        return f"A {self.roast_level} roast with {self.grams} grams left."
    
    def brew(self, how_many_grams: int) -> None:
        """
        Reduces the available coffee in the bag

        Parameters
        ==========
        how_many_grams: int
            indicates how much to reduce
            the overall grams in the bag
        """
        if how_many_grams > self.grams:
            print("Sorry not enough coffee here")
        else:
            self.grams -= how_many_grams


        


def main() -> None:
    "Running the coffee app"
    
    current_bag: CoffeeBag = CoffeeBag("dark", 284)
    fav_bag: CoffeeBag = CoffeeBag("light", 150)

    print(f"Current: {current_bag}")
    print(f"Favorite: {fav_bag}")

    print("brew a cup")
    current_bag.brew(15)
    print(f"Current: {current_bag}")

if __name__ == "__main__":
    main()
