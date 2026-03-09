"""
Sometimes I feel the need,
the need for speed!
"""

from typing import Callable, Optional, Sequence, TypeVar

import array as arr

###

mynums = arr.array('i', [1, 2, 3, 4, 5])
memloc: Callable[[object], str] = lambda o: hex(id(o))

first_loc = memloc(mynums[0])
print(f"{first_loc=}")

for i in range(1, 5):
    prior_loc = id(mynums[i-1])
    my_loc = id(mynums[i])

    print(f"Element[{i}] = {mynums[i]} @ {memloc(mynums[i])} (diff={my_loc - prior_loc})")
    # print(mynums.itemsize * 8) # 8 bits in a byte

# TODO #1
# What is the location of element n?

# def predict_loc(start: int, offset: int, size: int) -> int:
#     return 0

# assert predict_loc(
#     id(mynums[0]),
#     4,
#     32
# ) == id(mynums[4])
print()


# true of lists, why?
# listnums = [1, 'two', 3.0, None]
# listnums.append([])

# first_list_loc = memloc(listnums[0])
# print(f"{first_list_loc=}")

# for i in range(1, 5):
#     prior_loc = id(listnums[i-1])
#     my_loc = id(listnums[i])

#     print(f"Element[{i}] @ {memloc(listnums[i])} (diff={my_loc - prior_loc})")


# TODO #2
# Assuming a large array of n items,
# how long does it take to get the
# element at index 0, 1, 100, ... n-1?


# TODO #3
# Assuming a large array has n items,
# how long does it take to determine if
# it *contains* a particular value?
# (Consider that it might be at location
# 0, 1, 100, n-1, or not at all!)

# T = TypeVar('T')

# def seq_contains(a: Sequence[T], val: T) -> Optional[int]:
#     """Where is val in a"""

#     idx: int
#     num: T

#     for idx, num in enumerate(a):
#         if num == val:
#             return idx

#     return None

# assert seq_contains(mynums, 1) == 0
# assert seq_contains(mynums, 5) == 4
# assert seq_contains(mynums, 0) is None


# Can we do better?
# What if we had a way of
# converting each value into a number
# in the range [0, array.size)?

# def magic(val: object) -> int:
#     return hocus_pocus(val)

# for num in mynums:
#     magictable[magic(num)] = num


# TODO #4: How long would it take to see if
# a value was in the table?

# def magic_lookup(val: object) -> bool:
#     return magictable[magic(val)] == val


# TODO #5: What if I have more values than
# spots in the table?


# :: dramatic effect ::
# magic = hash
print()

# and this is why sets/dictionaries...
# * REQUIRE hashable values +
# * are WAY faster than lists for
#   answering containment queries

# == RULES ==
# 1. hash(obj) cannot change for same obj
#    -> what does this imply about what in obj
#       is used to calculate hash(obj)?

# 2. if obj1 == obj2 then hash(obj1) == hash(obj2)
#    -> reverse?

# == would be nice ==
# a) if obj1 != obj2 then hash(obj1) != hash(obj2)
#    -> why?

# b) hash(obj) is FAST to compute
#    -> why?


# == General approach for a class ==
# * Identify immutable attributes
#   (iattr1, iattr2, ...)
# * __hash__ = hash((iattr1, iattr2, ...))
# * __eq__   = check equality of at least
#              immutable attributes
#
# * Unless you have a VERY good reason,
#   and know what you are doing...
#   do NOT implement your own hash()

# from typing import Hashable

# class CourseAtLoc(Hashable):
#     """Course at a location"""

#     def __init__(self, subj: str, num: int, loc: str) -> None:
#         self._subj = subj
#         self._num = num
#         self._loc = loc

#     def _impt(self) -> tuple[str, int, str]:
#         return (self._subj, self._num, self._loc)

#     def __eq__(self, other: object) -> bool:
#         if not isinstance(other, CourseAtLoc):
#             return NotImplemented

#         return self._impt() == other._impt()

#     def __hash__(self) -> int:
#         return hash(self._impt())

#     def __str__(self) -> str:
#         return f"{self._subj} {self._num} ({self._loc})"

#     def __repr__(self) -> str:
#         classname = self.__class__.__name__
#         subj_q = repr(self._subj)
#         num = self._num
#         loc_q = repr(self._loc)

#         return f"{classname}({subj_q}, {num}, {loc_q})"

# strange_2100 = CourseAtLoc('CS', 2100, 'Boston')
# derbinsky_2100 = CourseAtLoc('CS', 2100, 'Boston')
# bhalerao_2100 = CourseAtLoc('CS', 2100, 'Oakland')

# print(strange_2100 == derbinsky_2100)
# print(derbinsky_2100 == bhalerao_2100)
# print(hash(strange_2100))
# print(hash(derbinsky_2100))
# print(hash(bhalerao_2100))

# spring26: set[CourseAtLoc] = set()
# spring26.add(strange_2100)

# print(derbinsky_2100 in spring26)
# print(bhalerao_2100 in spring26)
