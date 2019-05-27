# cats 貓清單
# photonum 要幾隻來拍照
# troublelis 那幾隻貓互看不順眼

def findPhoto(cats,photoNum,troubleList):
# cats 貓清單
# totalCast 一共有幾隻貓
# pos 清單内哪個位置之後可選
# photoNum 要幾隻拍照
    myFind(cats,len(cats),photoNum,troubleList,0)

def myFind(cats,totalCats,photoNum,troubleList,pos):
    if photoNum == pos :
        for i in range(pos):
            print(cats[i],end=' ')
        print()
        return
    for i in range(pos,totalCats):
        # ((非第一次) and (前一隻貓) 都在troublelist) 和 (此貓是否是troublelist)
        if (pos != 0 and cats[pos-1] in troubleList) and (cats[i] in troubleList):
            continue
        cats[i],cats[pos] = cats[pos],cats[i]
        myFind(cats,totalCats,photoNum,troubleList,pos+1)
        cats[i],cats[pos] = cats[pos],cats[i]

def main():
    cats = input().split()
    photoNum = int(input())
    troubleList = input().split()
    findPhoto(cats,photoNum,troubleList)

main()