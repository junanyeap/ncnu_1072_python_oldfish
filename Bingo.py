import random
def selectNum():
    num = input("input a num:")
    return num

def printPlate(n,plate):
    for key in plate:
        if(key % n == 0):
            print()
        if plate[key] == False:
            print("xx"," ",end="")
        else :
            print(key," ",end="")
def lineCheck(plate,n){
    i = 0
    j = 0
    # left to right
    for i in range(len(plate)/n):
}
def bingo(n):
    count = 0
    line = 0
    plate = {}
    i = 0
    for i in range(n*n):
        plate.update({i:False})
    print(plate)
    random.shuffle(plate)
    
    printPlate(n,plate)
    while line < 5 :
        num = selectNum()
        if num in plate:
            print("got this number ~")
            plate.update({num:True})
            count++
            line = lineCheck(plate,n)
        else:
            print("no number ~")
    print("game over,you guessed %s times.",count)

def main():
    n = int(input("n: "))
    time = bingo(n)

main()