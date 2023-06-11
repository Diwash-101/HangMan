import time
import hello
import random
import words
hello.hanger()
word=random.choice(words.b)
ans=['_ ']*len(word)
errcnt=0
running=True
preverrcnt=0


def isvalid(b):
    #check whether the input is 1 letter alphabet
    while b.isalpha()!=True or len(b)!=1:
        b=input('enter a valid letter: ')
        b=b.lower()
    return b



def main():
    global running
    global errcnt
    global preverrcnt
    b=input('enter a letter: ')
    #To exit when user inputs exit TODO:doesnot work
    if b=="exit":
        running=False

    b=isvalid(b)




    NoOfB=word.count(b)
    pos=-1
    prevPos=0
    #the letter is not in the word
    if NoOfB==0:
        errcnt+=1
    if preverrcnt!=errcnt:
        hello.call_function(errcnt)
        preverrcnt=errcnt
    print(errcnt)

    #finding positon of multiple letters
    while NoOfB>0:
        pos=word[pos+1:].index(b)
        NoOfB-=1
        actualPos=prevPos+pos
        prevPos=pos+1
        ans[actualPos]=b


    print(ans)

    #gameover
    if errcnt>=6:
        running=False
    elif ans==word:
        running=False

def gameloop():
    while running:
        main()
        time.sleep(0.1)
    print('Bye Bye. :)')


if __name__=="__main__":
    gameloop()

