desc = """
        This is a multiline String.
        An should be treated as such.\nComprendre?!
"""
print(desc)

desc_mod = r"""
        This is a multiline String.
        An should be treated as such.\nComprendre?!
"""
print(desc_mod)

a = 5
print(a, "is of type", type(a))

a = 2.0
print(a, "is of type", type(a))

a = 1+2j
print(a, "is complex number?", isinstance(1+2j,complex))

print(isinstance('king', str))