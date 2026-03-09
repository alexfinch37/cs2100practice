"""
Learning about performance
tradeoffs when searching
"""

from collections.abc import Container, Iterable

import time

import array as arr

###

NUM_NUMS: int = 50_000_000
samples: int = 10

#

print(f"Building big array ({samples} times)...")

start_time = time.perf_counter()
for _ in range(samples):
    big_arr = mynums = arr.array('i', range(NUM_NUMS))
end_time = time.perf_counter()

print(f"Done (size={len(big_arr):,})")
print(f"Operation took {(end_time - start_time)/samples:.4f} seconds")
print()

#

print("Building big set ({samples} times)...")

start_time = time.perf_counter()
for _ in range(samples):
    big_set = set(range(NUM_NUMS))
end_time = time.perf_counter()

print(f"Done (size={len(big_set):,})")
print(f"Operation took {(end_time - start_time)/samples:.4f} seconds")
print()

#

its: list[Iterable[int]] = [big_arr, big_set]
it_sum: int

for i in its:
    print(f"Iterating big {type(i).__name__}...")
    it_sum = 0
    start_time = time.perf_counter()
    for n in i:
        it_sum += n
    end_time = time.perf_counter()
    print(f"{it_sum=} in {((end_time - start_time)/samples):.4f} seconds")
print()

#

vals_to_find: list[int] = [0, NUM_NUMS // 2, NUM_NUMS-1, NUM_NUMS*2]
within: list[Container[int]] = [big_arr, big_set]

for c in within:
    print(f"Searching big {type(c).__name__}...")
    for v in vals_to_find:
        start_time = time.perf_counter()
        for _ in range(samples):
            found = v in c
        end_time = time.perf_counter()
        print(f"{v:,}) {found=} in {((end_time - start_time)/samples):.4f} seconds")
    print()
