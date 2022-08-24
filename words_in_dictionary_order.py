#Write a python script to print two given words in dictionary order

word_1=input('Enter First World : ')
word_2=input('Enter Second World : ')

print(word_2,word_1,sep='\n') if word_1>word_2 else print(word_1,word_2,sep='\n')