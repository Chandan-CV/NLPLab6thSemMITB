'''# Greedy Tokenizer

text = "shesellsseashellslol"
vocab = ["she", "sells", "sea", "shells", "he"]
vocab.sort(key= lambda x: len(x), reverse= True)
ans =[]
while text:
    print(text)
    for x in vocab:
        if(len(text)<len(x)):
            continue
        if(text[:len(x)]==x):
            ans.append(x)
            text = text[len(x):]
            break
# someone please add a condition to quit the loop when the remaining token is not int the vocab plz
print(ans)
'''

# bro experiment 5 is something else what are you doing lol 

# WRITE A PROGRAM TO REMOVE DIGITS FROM A GIVEN SENTENCE USING GREEDY TOKENIZER.
import re
text= input("your string")
print(re.sub(r"/d+",'',text)

# additional 5.1
print(len(re.findall(r"\d", text)))
# additional 5.2
print(re.findall(r"\d+", text))

# too lazy to do 5.3 lol someone pls put that
    
