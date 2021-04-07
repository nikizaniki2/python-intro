def triangle_type(a, b, c):
    if a==b==c:
        return "равностранен"
    if a==b or b==c or c==a:
        return "равнобедрен"
    else:
        return "разностранен"


def is_anagram(word1, word2):
    word1=word1.lower()
    word2=word2.lower()
    if sorted(word1)==sorted(word2):
        return "ANAGRAMS"
    else:
        return "NOT ANAGRAMS"

def events_count(list_of_nums):
    count = 0
    for i in list_of_nums:
        if i % 2 == 0:
            count+=1
    return count

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
    return count

def dict_generator(start, end):
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
    return dict_final

print(dict_generator(3,5))