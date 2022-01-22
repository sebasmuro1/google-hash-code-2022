#local simulator written on python to test your submissions to google hash code's practice round 2022
#by Sebastian Muro Sanchez https://github.com/sebasmuro1

#Fvec is the string you would normally submit to the google hash code platform, e.g. 4 cheese mushrooms tomatoes peppers
Fvec = list(input().split())
#then you should input the sample from google hash code
#C is the number of potential clients
C = int(input())
#CC is the score counter
CC = 0
while C > 0:
#L is the list of ingredients each potiential client likes
    L = list(input().split())
#D is the list of ingredients each potiential client dislikes
    D = list(input().split())
    C -= 1
    iC = 0
    dC = 0
    i = 1
    j = 1
#this cycle checks that none of the ingredients each potential client dislikes is in the pizza submission
    while j < len(D):
        if D[j] in Fvec:
            j = len(D)
        else:
            j += 1
            dC += 1
#if there is none of the ingredients each potential client dislikes, the next cycle checks if there are all the ingredients the client likes
    if dC == (len(D)-1):
        while i < len(L):
            if L[i] in Fvec:
                i += 1
                iC += 1
            else:
                i = len(L)
#if both conditions are encountered, then it counts it as a client
        if iC == (len(L)-1):
            CC += 1
#the final number of clients is printed
print(CC)
