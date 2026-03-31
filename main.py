# AIM: Develop a Python program that reads a text file and 
# prints words of specified lengths (e.g., three, four, 
# five, etc.) found within the file.
# Coder:REHAN AKHTAR ALI SHAIKH

# Date:11/02/26

#print("--- Extracting Words from Text File ---\n")
num = int(input("enter word length: "))
words =[]
with open("story.txt", "r") as file:
    content = file.read().split()
    for i in content:
        if len(i) == num:
            words.append(i)
words=set(words)
words=list(words)
words.sort()
print(words)    
