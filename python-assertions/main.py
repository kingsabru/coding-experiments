def sum_list(lst: list) -> float:
  assert type(lst) == list, 'Param `lst` must be of type list!'
  assert len(lst), 'The input list is empty!'

  total = 0
  for num in lst:
    total += num

  return total

lst_sum = sum_list(lst={'a':2, 'b':4}) # raises 1st assertionExption
# # lst_sum = sum_list(lst=[]) # raises 2nd assertionException
# lst_sum = sum_list([1.11, 2.21, 3.14])

print(lst_sum)

# NOTE
# 1. You should only do assertions when debugging your code.
#    Do not leave assert statements in a production environment.
# 2. To ignore all assertions, run your python script with the letter -O flag.
#    For example: python -O main.py
# 3. Assertion informs a developer of an unrecoverable error. Thus, the assertion is not
#    intended to point out regular error conditions like “File not found”.
# 4. You should use assertions to declare conditions that should be impossible in your code.
# 5. assert statements can be turned off in Python. So do not rely on assert statements for 
#    data validation. This can lead to big problems as these checks are omitted.

# RESOURCE
# - https://www.codingem.com/python-assert-statements/