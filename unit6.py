words = "My goal is to be a professional programmer and pro software engineer by 2022 after i complete my degree program with University of the People"
delimiter = ' '
word_split =  words.split(delimiter)
print(word_split, '\n')
del word_split[6] #removed 'professional' 
print(word_split,'\n')
word_split2 = word_split.pop(6)
print(word_split,'\n')      #removed 'programmer'
word_split.remove('and')
print(word_split,'\n')      #removed 'and'
word_split.sort()
print(word_split,'\n')   #sorted string
word_split.append('Ubah')           
print(word_split,'\n')
new_word = word_split.extend(['Moses']) 
print(word_split,'\n')
word_split.insert(24,'Chukwuemeka')
print(word_split,'\n')
s = ' '
print(s.join(word_split),'\n')




def My_fnc():
    nes_list = [2, 8]
    nested_list = [4, 5, 11, 13, 20]
    join_list = [nes_list] + nested_list #nested list
    print(join_list)
    new_list = nested_list * 2     #The “*” operator 
    print(new_list)
    rem_num = new_list[1:4]    #splice list
    print(rem_num)
    for i in rem_num:
        rem_num = rem_num + [i] #+= operator 
        print(rem_num)
        print(sum(rem_num))
    divisible  = filter(lambda i: i % 2 == 0, nested_list + nes_list)   #list filter with list operator
    print('Numbers divisible by 2 in nested_list + nes_list:',list(divisible))
My_fnc()


