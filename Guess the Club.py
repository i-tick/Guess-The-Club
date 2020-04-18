import random
movies = ["EMOTICA","AVC","SOULS","VIBRANZ","PICXELS"]
pp1 = 10

def create_question(movie):
    n=len(movie)
    letters=list(movie)
    temp=[]
    for i in range(n):
        if letters[i]==' ':
            temp.append(' ')
        else:
            temp.append('*')
    qn="".join(str(x) for x in temp)
    return qn

def is_present(letter,movie):
    c=movie.count(letter)
    if c==0:
        return False
    else:
        return True
    
def unlock(qn,movie,letter):
    global pp1
    ref=list(movie)
    qn_list=list(qn)
    n=len(movie)
    temp=[];
    for i in range(n):
        if ref[i]==letter:
            temp.append(letter)
        else:
            temp.append(qn_list[i])
    qn_new="".join(str(x) for x in temp)   
    return qn_new

def play():
    turn=0
    #willing=True
    #player 1
    picked_movie=random.choice(movies)
    qn=create_question(picked_movie)
    print(qn)
    movies1 = ["performs theatricals.","where writings are turned into cinema.","speaks through music.","makes music alive.","It freezes the  memories for us"]
    index = movies.index(picked_movie)
    print(movies1[index])
    print()
    modified_qn=qn
    global pp1
    temp_movie = picked_movie
    not_said=True
    print("1. Wnat to guess whole name")
    print("2. Wnat to guess letter")
    choice = int(input())
    print(qn)
    print("score: "+str(pp1))
    print()
    if choice == 1:
        while(not_said):
            club_name = input("guess the word: ")
            if club_name.upper() == picked_movie:
                pp1+=5
                print("correct guess")
                print("score: ",pp1)
                print()
                print("you win")
                break
            else:
                pp1-=3
                print("incorrect guess")
                print("score: ",pp1)
                print()
                if(pp1<=0):
                    print("you lose")
                    break
    elif choice == 2:
        while(not_said):
            letter=input("guess a letter: ")
            if letter =="":
                print("enter a character")
            elif(is_present(letter.upper(),temp_movie)):
                temp_movie = picked_movie.replace(letter.upper(),"")
                pp1+=3
                print("correct guess")
                print("score: ",pp1)
                print()
                modified_qn=unlock(modified_qn,picked_movie,letter)
                print(modified_qn)
                if(modified_qn == picked_movie):
                    print("you won")
                    break
            else:
                print("incorrect guess")
                print(modified_qn)
                pp1=pp1-2
                print("score",pp1)
                print()
                if(pp1<=0):
                    print("you lose")
                    break
    else:
        print("incorrect choice, restart")
    
        print()
play()
