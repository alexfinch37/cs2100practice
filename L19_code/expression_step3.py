"""
🎭🎨
"""

# let's get help using
# the Abstract Base Class
from abc import ABC, abstractmethod

###

class Expressive(ABC):
    """
    A contract for what it means
    to be expressive
    """

    @abstractmethod
    def express_yourself(self) -> None:
        """A class MUST implement this method"""
        pass

###

# Now makes more sense: 
# CS2100Student can-do express_yourself
# (is-a Student might make more sense)
class CS2100Student(Expressive):
    def express_yourself(self) -> None:
        print("🐍 rocks!!")

# Now makes more sense: 
# Lion can-do express_yourself
# (is-a Cat might make more sense)
class Lion(Expressive):
    def express_yourself(self) -> None:
        print("ROAR")

# Not adhering to the contract!!
# class Rock(Expressive):
class Rock:
    def contemplate(self) -> None:
        print("👀")

# Now makes more sense: 
# CharlesWrightFan can-do express_yourself
# (is-a Fan might make more sense)
class CharlesWrightFan(Expressive):
    def express_yourself(self) -> None:
        print("\n".join((
            "🎶",
            "It's not what you look like",
            "When you're doin' what you're doin'",
            "It's what you're doin' when you're doin'",
            "What you look like you're doin' 🎶",
        )))

def main() -> None:
    happy_coder = CS2100Student()
    simba = Lion()
    evelyn = Rock()
    watts103_num1 = CharlesWrightFan()

    peeps = [
        happy_coder,
        simba,
        evelyn,
        watts103_num1,

        # it's abstract,
        # (meaning has at least
        # one abstract method)
        # so can't instantiate!!
        # Expressive()
    ]

    #

    # this will totally work!!
    # commit message: please please please 🙏
    for p in [p for p in peeps if isinstance(p, Expressive)]:
        print(f"{type(p).__name__}: ", end="")
        p.express_yourself()


if __name__ == "__main__":
    main()
