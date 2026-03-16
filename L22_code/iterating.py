"""
Our next protocol relates to iteration!
(fancy word for going through something
one at a time)
"""

from typing import Iterable, Iterator

from enum import StrEnum, auto

###

# I am able to "iterate" over
# each letter in a string bc
# the str class implements
# the "Iterable" protocol by
# implementing the __iter__
# method
myword: Iterable[str] = "abcdefg"

print("== usual ==")
for letter in myword:
    print(letter)
print()


print("== manual ==")
myword_iterator: Iterator[str] = myword.__iter__()

# usually done via function...
# myword_iterator = iter(myword)

while True:
    try:
        letter = myword_iterator.__next__()

        # usually done via function...
        # letter = next(myword_iterator)

        print(letter)

    except StopIteration:
        break
print()



# Now let's try to make classes that can be
# iterated over :)

# TODO 1: Using iterator of a composed attribute
#         (easy!!)

class Weekday(StrEnum):
    """Days of the week!"""

    MONDAY = auto()
    TUESDAY = auto()
    WEDNESDAY = auto()
    THURSDAY = auto()
    FRIDAY = auto()


class LectureSchedule(Iterable[Weekday]):
    """Days when a class has lecture"""

    def __init__(self, *days: Weekday) -> None:
        """Provide any days with lecture"""

        self._days = list(days)

    def __iter__(self) -> Iterator[Weekday]:

        # since _days is a list,
        # and lists already are iterable,
        # and all I want to iterate over
        # is the days in the list...
        return iter(self._days)


taught: dict[str, LectureSchedule] = {
    'cs2500sp26': LectureSchedule(
        Weekday.MONDAY,
        Weekday.WEDNESDAY,
        Weekday.THURSDAY
    ),

    'cs5200sp25': LectureSchedule(
        Weekday.THURSDAY
    )
}

for course,schedule in taught.items():
    print(f"{course}: {", ".join(str(d) for d in schedule)}")
print()


# TODO 2: Building a custom iterator (to make
#         another class iterable)

class PerfectSquares(Iterable[int]):
    """
    Like range, but perfect squares,
    so PerfectSquares(10) = 1, 4, 9
       PerfectSquares(30) = 1, 4, 9, 16, 25
    """

    def __init__(self, limit: int) -> None:
        """How far to go?"""

        self._limit = limit

    def __iter__(self) -> Iterator[int]:
        return PerfectIterator(self._limit)

class PerfectIterator(Iterator[int]):
    """
    Goes to the next perfect square below
    a supplied limit
    """

    def __init__(self, limit: int) -> None:
        """Supply the limit"""

        self._limit = limit
        self._current = 0

    def __next__(self) -> int:
        """Gets the next perfect square"""

        self._current += 1
        squared = self._current ** 2

        if squared < self._limit:
            return squared
        else:
            raise StopIteration


for n in [10, 30]:
    print(f"PerfectSquares({n}) = {", ".join(str(i) for i in PerfectSquares(n))}")
print()
