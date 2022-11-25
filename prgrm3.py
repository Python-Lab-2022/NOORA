string="Woodchuck How much wood would a woodchuck chuck if a woodchuck could chuck Wood ?"
# converting the string into uppercase
string=string.lower()
# Whenever we encounter a space, break the string
string=string.split(" ")
# Initializing a dictionary to store the frequency of words
frequency={}
for i in string:
     # If the word is already in the keys, increment its frequency
        if i in frequency:
            frequency[i]+=1
             
    # It means that this is the first occurence of the word
        else:
            frequency[i]=1
print(frequency)
