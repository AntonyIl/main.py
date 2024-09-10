def print_params(a=1, b='what', c=True):
    print(a, b, c)


print_params()

print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [1, "tha ", True]
values_dict = {"a": 5, "b": False, 'c': "shit"}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [10.0, "the"]
print_params(*values_list_2, 42)
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
