def triangle_type(a, b, c):
    if a==b==c:
        print("равностранен")
        return
    if a==b or b==c or c==a:
        print("равнобедрен")
        return
    else:
        print("разностранен")
        return


def is_anagram(word1, word2):
    word1=word1.lower()
    word2=word2.lower()
    if sorted(word1)==sorted(word2):
        print("ANAGRAMS")
    else:
        print("NOT ANAGRAMS")
    return

def evens_count(list_of_nums):
    count = 0
    for i in list_of_nums:
        if i % 2 == 0:
            count+=1
    print("Number of even number: ",count)
    return

def word_counter(list_of_words, word):
    count = 0
    ammount = len(list_of_words)
    for i in range(ammount):
        if list_of_words[i] == word:
            count+=1
    return count

##############Fixed################
#In babababa example the code returns 3 instead of 2 because
# `baba`**** == baba 1
# **`baba`ba == baba 2
# ****`baba` == baba 3
##############Fixed################
def count_substrings(sentence, sub):
    count = 0
    len_of_sent = len(sentence)
    len_of_sub = len(sub)
    i = 0
    while i < len_of_sent:
        if sentence[i:i+len_of_sub] == sub:
            i=i+3
            #possible solution for the babababa problem?
            count+=1
            continue
        i+=1
    print(count)
    return count

###############overly complicated...################
############### UNUSED ################
def dictionary_generator(start, end):
    diff = end - start
    diff = abs(diff)
    key_list = []
    dic = ""
    for i in range(diff+1):
        value = 5%(i+start)
        temp_key = i+start
        temp_value = int(round(value))
        temp_dic = str(temp_key)+":"+str(temp_value)
        if dic == "":
            dic = temp_dic
            continue
        dic = dic+", "+temp_dic
    key_list.append(dic)
### How do I convert key_list(list) -> key_list(dic)
### ['3:2, 4:1, 5:0'] -> {3:2, 4:1, 5:0}
    final_dic = {str(key_list[0])}
### Fixed by simply creating a dic
### and filling it with the value of the list key_list[0]

### doesn't work as it counts the whole str as 1 key
    print(final_dic)
############### UNUSED ################


def new_dict_generator(start, end):
    dict_final= ""
    diff = end - start
    diff = abs(diff)
    list_of_keys = []
    for i in range(diff+1):
        temp_key = i+start
        list_of_keys.append(temp_key)

    dict_final = dict.fromkeys(list_of_keys, 0)

    for i in range(diff+1):
        value = 5%(i+start)
        temp_key = i+start
        temp_value = int(round(value))
        temp_update = {temp_key:temp_value}
        dict_final.update(temp_update)
    print(dict_final)

import books
a = input("Value of a: ")
b = input("Value of b: ")
c = input("Value of c: ")
triangle_type(a,b,c)

word1 = input("First word:")
word2 = input("Second word:")
is_anagram(word1, word2)

nums = [1,2,3,4,5,1,2,9,4,5]
evens_count(nums)

print("Number of times the word ""word"" is repeated: ", word_counter(['list','python','word',], 'word'))

print("Sub strings This is this and that is this. ~this~")
count_substrings("This is this and that is this", "this")

print("Key/Value between 3 and 5: ")
new_dict_generator(3,5)