ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}


try:
    value = "World!"
    ft_list[1] = value
except Exception as e:
    print(e)

try:
    value = "Barcelona!"
    list_tmp = list(ft_tuple)
    list_tmp[1] = value
    ft_tuple = tuple(list_tmp)
except:
    print(e)

try:
    value = "Spain!"
    ft_set.clear()
    ft_set.add("Hello")
    ft_set.add(value)
except Exception as e:
    print(e)

try:
    value = "42Barcelona!"
    ft_dict["Hello"] = value
except Exception as e:
    print(e)


print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
