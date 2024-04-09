immutable_var = 1, 2, True, "Hello"
print(immutable_var)
# immutable_var[0] = 10   # будет ошибка. Кортеж является неизменяемым
mutable_list = [1, 2, True, "Hello"]
print(mutable_list)
mutable_list[1] = 10
print(mutable_list)
