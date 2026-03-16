"""
Recursion, huh?
"""

# Sometimes you encounter data or problems
# where the "bigger" looks a LOT like the
# "smaller", such as...

# * Toys: https://en.wikipedia.org/wiki/Matryoshka_doll


# * In a math class: factorial (exponents as well in notes)
#
#   3! = 3 * 2 * 1
#
#   look at it like...
#
#   3! = 3 x 2! = 3 x 2 = 6
#   2! = 2 x 1! = 2 x 1 = 2
#   1! = 1 x 0! = 1 x 1 = 1
#   0! = 1
#
#   meaning the "recursive" definition
#   (for a non-negative integer) is...
#
#   n! = n x (n-1)!
#   0! = 1


# * In data science/programming: sequences (e.g., string, list)
#   are often composed of OTHER sequences (that can) be then
#   processed likewise, so if we consider length/size (||)...
#
#   |"abc"| = 1 + |"abc"[1:]| = 1 + 2 = 3
#   |"bc"|  = 1 + |"bc"[1:]| = 1 + 1 = 2
#   |"c"|   = 1 + |""| = 1 + 0 = 1
#   |""|    = 0


# * Hierarchical data (e.g., many org charts)
#
#   Let's define a "team" as a group of
#   employees working on a task;
#   if a member of the team is the manager,
#   often times that looks like another team!
#
#   * Aoun (President)
#     * Winkelstein (Provost)
#       * Brodley (Dean)
#       * Mynatt (Dean)
#         * Mislove (Sen Assoc Dean)
#           * Jamieson (Assoc Dean)
#             * Strange (Director)
#             * Derbinsky (peon)
#         * Hescott (Sen Assoc Dean)
#     * Henderson (Chancellor)
#
#   Or a file system that has folders that
#   each may contain files... or other
#   folders!!
#
#   * /
#     * /Users
#       * /Users/student
#         * /Users/student/code.py
#         * /Users/student/Downloads
#           * /Users/student/Downloads/defying_gravity.mp3
#     * /Applications
























# In each case, to build up your data/problem, you
# typically start with the small and perform a common
# operation to build up something bigger...
#
# SO, recursion is an approach to problem-solving
# in code (or mathematics) that uses this structure
# in reverse - start with the bigger, and while breaking
# into smaller versions compute useful info.

# So consider that your recursive problem/data has one
# or more "base cases" (i.e., can't get smaller), then...


def recursive_func_simple(problem):
    if is_base_case1(problem):
        return simple_answer
    # possibly check for others

    subresult = recursive_func_simple(
        make_recursively_smaller(problem)
    )
    # possibly for multiple subproblems
    # (either individually or via loop)

    return combine_results(
        simple_piece_of(problem),
        subresult
    )


# Note: sometimes your function needs some
#       "stuff" to get it going (ala accumulator
#       pattern, in which case...


def _recursive_helper(problem, stuff):
    if is_base_case1(problem):
        return simple_answer
    # possibly check for others

    subresult = _recursive_helper(
        make_recursively_smaller(problem),
        make_next_stuff(stuff)
    )
    # possibly for multiple subproblems
    # (either individually or via loop)

    return combine_results(
        simple_piece_of(problem),
        subresult,
        stuff
    )

def recursive_function(problem):
    return _recursive_helper(
        problem,
        initial_stuff
    )



















# Example: factorial
# * (single) base case = 0! -> 1
# * make smaller = reduce n by 1
# * combine = n x factorial(smaller)
# * no "stuff" necessary!

def recursive_factorial(n: int) -> int:
    """Recursive n!"""

    # quick input check
    if n < 0:
        raise ValueError

    # base case
    if n == 0:
        return 1

    smaller = n - 1
    subresult = recursive_factorial(smaller)

    return n * subresult


assert recursive_factorial(0) == 1

# recursive_factorial(2) = 2 * recursive_factorial(1) = 2 * 1 = 2
# recursive_factorial(1) = 1 * recursive_factorial(0) = 1 * 1 = 1
# recursive_factorial(0) = 1
assert recursive_factorial(2) == 2

# recursive_factorial(3) = 3 * recursive_factorial(2) = 3 * 2 = 6
# recursive_factorial(2) = 2 * recursive_factorial(1) = 2 * 1 = 2
# recursive_factorial(1) = 1 * recursive_factorial(0) = 1 * 1 = 1
# recursive_factorial(0) = 1
assert recursive_factorial(3) == 6















# Example: sequence length (|seq|)
# * (single) base case = |empty| = 0
# * make smaller = remove the first element
# * combine = 1 + |smaller|
# * no "stuff" necessary!
#   (other than knowing the meaning 
#    of empty for a particular sequence)

from typing import Sequence, TypeVar

T = TypeVar("T")

def recursive_len(seq: Sequence[T], empty: Sequence[T]) -> int:
    """|seq|"""

    if seq == empty:
        return 0

    return 1 + recursive_len(seq[1:], empty)

def recursive_str_len(s: str) -> int:
    """|string|"""

    return recursive_len(s, "")

def recursive_list_len(l: list[T]) -> int:
    """|list|"""

    mt_list: list[T] = []

    return recursive_len(l, mt_list)


assert recursive_str_len("") == len("")
assert recursive_str_len("abc") == len("abc")

assert recursive_list_len([]) == len([])
assert recursive_list_len([1, 2, 3, 4, 5]) == len([1, 2, 3, 4, 5])






















# == Analysis ==
# * Is it correct?
# * Will it always stop executing

# == Why ==
# * Sometimes the most direct way of representing/solving
#   a problem (e.g., hierarchical data above)
# * Can produce very clean, understandable code

# == Why NOT ==
# * Can be less efficient
#   -> May have problems dealing with bigger problems
#      via all the function calls

# Compare...

from math import factorial

def imperative_factorial(n: int) -> int:
    # quick input check
    if n < 0:
        raise ValueError

    result: int = 1

    for i in range(1, n+1):
        result *= i

    return result

assert factorial(100) == imperative_factorial(100)
assert factorial(100) == recursive_factorial(100)

# but...

assert factorial(1000) == imperative_factorial(1000)
# recursive_factorial(1000) # 💥
