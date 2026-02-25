"""
🎭🎨
"""

class CS2100Student:
    def express_yourself(self) -> None:
        print("🐍 rocks!!")

class Lion:
    def express_yourself(self) -> None:
        print("ROAR")

class Rock:
    def contemplate(self) -> None:
        print("👀")

class CharlesWrightFan:
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
        watts103_num1
    ]

    #

    # this will totally work!!
    # for p in peeps:
    #     print(f"{type(p).__name__}: ", end="")
    #     p.express_yourself()

    # ok maybe not...
    # better??
    # for p in peeps:
    #     print(f"{type(p).__name__}: ", end="")

    #     try:
    #         p.express_yourself()
    #     except:
    #         print('\033[31m' + 'has other plans :(' + '\033[0m')

    # how about detection?
    # what happens when we add a new
    # expressive class... or 100!?
    # feels like coupling is afoot 🤮
    # for p in peeps:
    #     if isinstance(p, CS2100Student) or \
    #        isinstance(p, Lion) or \
    #        isinstance(p, CharlesWrightFan):
    #         print(f"{type(p).__name__}: ", end="")
    #         p.express_yourself()


if __name__ == "__main__":
    main()
