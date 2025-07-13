from random import randint
my_list = []
string = 'abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()~`?><,./;:[]'
string[randint(0, len(string)-1)]
for i in range(10):
    my_list.append(string[randint(0, len(string)-1)])
print(''.join(my_list))