"""
TODO: A very useful temperature-conversion app.
"""

THRESHOLD_TEMP_F: float = 68

def greet_person() -> None:
    """
    Gets the name of a person
    from the keyboard
    and greets them
    """
    your_name: str = input("What is your name? ")
    print(f'howdy {your_name}')

def is_cold_f(temp_f: float) -> bool:
    """
    Determines if the supplied 
    temperature in F is below 
    our agreed upon temp

    Parameters
    =========
    temp_f: float
        supplied temp in F

    Returns
    ========
    bool
        True means below the
        agreed upon threshold
    """

    return temp_f < THRESHOLD_TEMP_F

def main() -> None:
    pass

if __name__ == "__main__":
    main()
