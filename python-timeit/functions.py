from timeit import timeit

def for_loop(seq, result_list=[]):
    for char in seq:
        result_list.append(char)
    return result_list

def list_comprehension(seq):
    return [char for char in seq]
  
for_loop_setup = """
from __main__ import for_loop
seq = "Kingsley"
"""

list_comprehension_setup = """
from __main__ import list_comprehension
seq = "Kingsley"
"""

print(f'For loop: {timeit(setup=for_loop_setup, stmt="for_loop(seq)", number=10000)}')
print(f'List comprehension: {timeit(setup=list_comprehension_setup, stmt="list_comprehension(seq)", number=10000)}')