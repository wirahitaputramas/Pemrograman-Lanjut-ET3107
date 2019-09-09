word=input("masukkan kata atau kalimat: ")
vocals=['a','e','i','o','u']
for ch in word.lower():
    if ch in vocals:
        word=word.replace(ch,"")
print (word)
