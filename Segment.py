#學號：104213070
#姓名：葉潤安

lenghtSum = 0

def sort(data):
    # sort a 2D list element by his first-"D" element
    data = sorted(data, key=lambda x: x[0])
    print(data)
    return data 

def calcSegment(xylist):
    xylist=sort(xylist)
    global lenghtSum
    start, end = xylist[0][0], xylist[0][1]
    i = 1
    lenghtSum = end - start
    # print("init lenghtSum : ",lenghtSum)
    for i in range(len(xylist)):
        if xylist[i][0] <= end :

            # next line is all inside current line, combine it
            if xylist[i][1] < end:
                lenghtSum = lenghtSum
            #  next line is half inside current line, extends
            elif xylist[i][1] > end :
                lenghtSum = lenghtSum + xylist[i][1] - end
                # print("e",lenghtSum)
                end = xylist[i][1]
        elif xylist[i][0] > end :
            lenghtSum = lenghtSum + xylist[i][1] - xylist[i][0]
            # print("e",lenghtSum)
            end = xylist[i][1]            

    # print(start,end)
    print(lenghtSum)


def main():
    i = 0
    global lenghtSum
    xylist = []
    print("APCS 線段長度計算")
    # built in testData to skip step of input 
    # xylist = [
    #     [160,180],
    #     [150,200],
    #     [280,300],
    #     [300,330],
    #     [190,210]
    # ]
    # xylist = [
    #     [120,120]
    # ]
    n = int(input("input a n : "))
    for i in range(n):
        rawInput = input()
        x,y = rawInput.split()
        xylist.append([int(x),int(y)])

    calcSegment(xylist)
main()
