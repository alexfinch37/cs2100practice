"""
🎭🎨
"""

# How about an "abstract"
# class with an "abstract"
# method?
class Expressive:
    def express_yourself(self) -> None:
        pass

###

# Curious: CS2100Student is-a Expressive? 🤔
class CS2100Student(Expressive):
    def express_yourself(self) -> None:
        print("🐍 rocks!!")

# Curious: Lion is-a Expressive? 🤔
class Lion(Expressive):
    def express_yourself(self) -> None:
        print("ROAR")

# Curious: Rock is-a Expressive? 🤔
class Rock(Expressive):
    def contemplate(self) -> None:
        print("👀")

# Curious: CharlesWrightFan is-a Expressive? 🤔
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
        Expressive()
    ]

    #

    # this will totally work!!
    # what went wrong!? 😭
    for p in [p for p in peeps if isinstance(p, Expressive)]:
        print(f"{type(p).__name__}: ", end="")
        p.express_yourself()


if __name__ == "__main__":
    main()
