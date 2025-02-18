import os.path
import random
import string
from pprint import pprint
#note the directory of the dictionarty file
ficdic="C:/Users/ASUS/OneDrive/Documents/words_alpha.txt"

strenc=ficdic.encode("ascii","ignore")
strdec=strenc.decode()
if os.path.exists(strdec):
    handle=open(strdec)
    words=handle.readlines()
    handle.close()
    words=[random.choice(words).upper().replace("'","").strip()\
           for _ in range (10)]
    grid_size=20
    #now making the 20x20 grid
    grid=[["_"for _ in range(grid_size)] for _ in range(grid_size) ]
    def print_grid():
        for x in range (grid_size):
            print("\t"*7+" ".join(grid[x]))

    #lets create the orientation of the grid
    orientations=["leftright","updown","diagonalup","diagonaldown"]
    #lets put in the words
    for word in words:
        word_length=len(word)
        print(word)
        #lets add in a boolean checker to keep track of space within the grid
        placed=False
        while not placed:
            orientation=random.choice(orientations)
            #lets create directions in which the text will be added to the grid

            if orientation=="leftright":
                step_x=1
                step_y=0
            if orientation=="updown":
                step_x=0
                step_y=1
            if orientation=="diagonalup":
                step_x=1
                step_y=-1
            if orientation=="diagonaldown":
                step_x=1
                step_y=1
            #lets set a starting place for the cursor which will be randomly generated by the programm
            x_position=random.randint(0,grid_size)
            y_position=random.randint(0,grid_size)
            #checking if the word can fit into the space anotated by the cursor on the grid
            ending_x=x_position+word_length*step_x
            ending_y=y_position+word_length*step_y
            if ending_x<0 or ending_x>=grid_size:
                continue
            if ending_y<0 or ending_y>=grid_size:
                continue
            #if we run out of space on the grid the program should be able to look for a new orientationn and statrt again
            #otherwise we place the word in the grid
            failed=False
            for i in range(word_length):
                character=word[i]
                #placing the characters ob the grid by anotating the new position of x and y of the cursor
                new_position_x=x_position+i*step_x
                new_position_y=y_position+i*step_y

                character_at_new_position = grid[new_position_x][new_position_y]
                if character_at_new_position != "_":
                    if character_at_new_position==character:
                        continue
                    else:
                      failed=True
                      break
            if failed:
              continue
            else:
              for i in range(word_length):
                  character = word[i]
                  new_position_x = x_position + i * step_x
                  new_position_y = y_position + i * step_y
                  grid[new_position_x][new_position_y] = character
              placed = True
                #now weve finished putting the words that we want
                #time to fill the grid with random characeters
    for x in range(grid_size):
        for y in range(grid_size):
            if (grid[x][y])=="_":#this means that space hasnt been ocupied yet
                grid[x][y]=random.choice(string.ascii_uppercase)

    print_grid()
    print("wHAT WORDS HAVE U Identified")
    x=0
    j=1
    while True:
        a=input()
        if a in words:
            print("Correct",(10-j),"remainig")
            j+=1
            if j==10:
                print("Congradulations Wouve Won ")
                break
        else:
            print("Icorrect try again please")
            x+=1
            if x==10:
                print('10 incorrect guesses do you wish to quit??'," yes or no")
                if input()=="yes":
                    pprint(words)
                    break
                elif input()=="no":
                    x=0
                    continue
                else:
                    print("invalid response received")
                    break
else:
    print("Invalid File Received")