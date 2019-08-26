def search(keyword) :
    all_words=list()
    all_words.append(keyword)
    for entry in Thesaurus:
        if keyword==entry.word:
            for i in entry.synonyms:
                all_words.append(i)
    output_list=list()
    for word in all_words:
        n=0
        for doc in Corpus:
            for each_word in doc:
                if each_word==word:
                    n+=1
        word_count=(word,n)
        output_list.append(word_count)
   # implement the function here
    


    return output_list
# modify to return a list of tuples

input = "happy"
output = search(input) # invoke the method using a test input
print(output) # prints the output of the function
# do not remove this line!
