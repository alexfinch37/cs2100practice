"""
Another protocol: comparable
"""

# SO, we can do the following
print(5 < 42)
print("pavement" > "dunkin")
print()

# this is done via a set of dunder
# methods that together comprise
# a protocol around comparison

# we've already seen __eq__ (==)
# and now we add...
# * __ne__ (!=)
# * __lt__ (<)
# ...

class MyFaves:
    """Fave things"""

    def __init__(self, *things: str) -> None:
        """Provide fave things, keep distinct"""

        self._faves = set(things)

    def __str__(self) -> str:
        return f"Faves: {str(self._faves)}"

    def __ne__(self, other) -> bool:
        if not isinstance(other, MyFaves):
            return NotImplemented
        
        print("my != check")
        return self._faves != other._faves
    
    # for funsies: change to eq (name and logic)
    #              and then look at outputs

    # for MORE funsies...
    # from functools import total_ordering
    # @total_ordering
    
    def __lt__(self, other) -> bool:
        if not isinstance(other, MyFaves):
            return NotImplemented
        
        print("my < check")
        return len(self._faves) < len(other._faves)

fave_francais = MyFaves("écureuil")
fave_music = MyFaves("raindrops on roses", "whiskers on kittens")
fave_howdy = MyFaves("howdy")
fave_howdyhowdy = MyFaves("howdy", "howdy")

print(fave_francais != fave_music)
print(fave_howdy == fave_howdyhowdy)

print(fave_howdy < fave_howdyhowdy)
print(fave_music > fave_howdy)
print()

# and even more funsies!
# print([str(f) for f in sorted([fave_music, fave_francais, fave_howdyhowdy])])
