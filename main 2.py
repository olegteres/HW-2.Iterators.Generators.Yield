nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]

for i in nested_list[:]:
    for x in i: nested_list.append(x)
    nested_list.remove(i)
print(nested_list)