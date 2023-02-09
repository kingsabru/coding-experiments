def outer_func():
    b = 20
    a = 20 
    
    def inner_func():
        global a
        nonlocal b
        c = 30
        b = 30
        a = 30
        print(f'a (inner_func) = {a}')
        print(f'b (inner_func) = {b}')
        print(f'c (inner_func) = {c}')
        
    inner_func()
    print(f'a (outer_func) = {a}')
    print(f'b (outer_func) = {b}')

a = 10
outer_func()
print(f'a = {a}')