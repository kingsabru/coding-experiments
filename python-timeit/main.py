from timeit import timeit, repeat

setup_code = """
name = "Kingsley"
result_list = []
"""

for_loop_code = """
for char in name:
    result_list.append(char)
"""

list_comprehension_code = """
result_list = [char for char in name]
"""

t1 = timeit(setup=setup_code, stmt=for_loop_code, number=10000)
t2 = timeit(setup=setup_code, stmt=list_comprehension_code, number=10000)

print(f'For loop: {t1}')
print(f'List comprehension: {t2}')

t3 = repeat(setup=setup_code, stmt=for_loop_code, repeat=3, number=10000)
t4 = repeat(setup=setup_code, stmt=list_comprehension_code, repeat=3, number=10000)

print(f'For loop: {t3}')
print(f'List comprehension: {t4}')