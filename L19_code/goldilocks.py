"""3 * 🐻"""

from enum import Enum
from typing import Callable

###

# Enumeration is a useful
# way to make types that
# have a fixed set of
# possibile values (name = value)
class Bear(Enum):
    """Represents the three bears"""
    PAPA = 1
    MAMA = 2
    BABY = 3

###

class PorridgeTemperatureException(Exception):
    """🥵🥶"""

    def __init__(self, too_hot: bool) -> None:
        super().__init__(f"Way too {"hot" if too_hot else "cold"}!!!")

def try_porridge(owner: Bear) -> str:
    """
    🥣

    Returns
    =======
    str
        Result of eating a bear's porridge
    
    Raises
    ======
    PorridgeTemperatureException
        Eat fail
    """

    match owner:
        case Bear.PAPA:
            raise PorridgeTemperatureException(too_hot=True)
        
        case Bear.MAMA:
            raise PorridgeTemperatureException(too_hot=False)
        
        case Bear.BABY:
            return "😋"

###

class ChairTooBigException(Exception):
    """Is it a sofa?!"""

    def __init__(self) -> None:
        super().__init__("🛋️")

def try_chair(owner: Bear) -> str:
    """
    🪑

    Returns
    =======
    str
        Result of sitting in a bear's chair
    
    Raises
    ======
    ChairTooBigException
        Sit fail
    """

    match owner:
        case Bear.BABY:
            return "CRACK"
        
        case _:
            raise ChairTooBigException()

###

class BedException(Exception):
    """🪨🪶"""

    def __init__(self, resistance: str) -> None:
        super().__init__(f"Entirely too {resistance}!!!")

def try_bed(owner: Bear) -> str:
    """
    🛌

    Returns
    =======
    str
        Result of sleeping in a bear's bed
    
    Raises
    ======
    BedException
        Sleep fail
    """

    match owner:
        case Bear.PAPA:
            raise BedException("hard")
        
        case Bear.MAMA:
            raise BedException("soft")
        
        case Bear.BABY:
            return "😴"

##

def main() -> None:
    """Story time!!"""

    story: dict[str, Callable[[Bear], str]] = {
        'Porridge': try_porridge,
        'Chair': try_chair,
        'Bed': try_bed,
    }

    print(f"👩‍🦱 and the { len(Bear) * "🐻" }")
    print()

    for name,func in story.items():
        print(f"== {name} ==")
        for b in Bear:
            try:
                print(f"{b.name}: ", end="")
                print(func(b))
            except Exception as e:
                print(e)
        print()

if __name__ == "__main__":
    main()
