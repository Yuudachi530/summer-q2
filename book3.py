file_book = open("Alice's Adventures in wonderland.txt","r")
file_word = open("vocabulary file.txt","r")
file_book = file_book.readlines()
file_word_list = file_word.readlines()
list_file_book = []
list_list_word = []
list_list_word_split = []



for line in file_book:
    list_file_book_split = line.split()
    for word in list_file_book_split:
        list_file_book.append(word)

for line in file_word_list:
    list_list_word_split = line.split()
    for word in list_list_word_split:
        list_list_word.append(word)

for word in list_file_book:
    for symbol in ',.?!":;':
        word.replace(symbol,'')


            
                
    

def search_linear(list_library_1, string_target):
    for i in list_library_1:
        if i == string_target:
            return True


def search_word_notrecommended(list_library_1,list_library_2):
    list_word_choosed = []
    for x in list_library_2:
        if search_linear(list_library_1, x) != True:
            list_word_choosed.append(x)
    list_word_choosed = list(set(list_word_choosed))
    return len(list_word_choosed)

            
            
a = search_word_notrecommended(list_file_book, list_list_word)
print(a)














