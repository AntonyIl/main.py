my_dict = {'Anton' : 1995 , 'Evgeniy' : 1997 , 'Bogdan' : 1996 , 'Geor' : 1995}
print(my_dict)
print(my_dict['Anton'])
my_dict.update({'Denis' : 2001 ,
                'Mihail' : 1008})
print(my_dict)
my_set = (1 , 15 , 1 , 8 , 'string' , 'string' , 2.0)
my_set = set(my_set)
print(my_set)
print(set(my_set))
my_set.update(['Anton' , 7])
my_set.discard(0)
print(my_set)