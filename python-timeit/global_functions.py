from timeit import timeit

def for_loop(seq, result_list=[]):
    for char in seq:
        result_list.append(char)
    return result_list

def list_comprehension(seq):
    return [char for char in seq]
  

t1 = timeit(setup="seq='Kingsley'", stmt="for_loop(seq)", number=10000, globals=globals())
t2 = timeit(setup="seq='Kingsley'", stmt="list_comprehension(seq)", number=10000, globals=globals())

print(f'For loop: {t1}')
print(f'List comprehension: {t2}')