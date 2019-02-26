# 103 = 2*50 0 0 3*1
# 1 5 10 50

def printOut(coin1,coin5,coin10,coin50):
    line_title = 'coin  | %4s  %4s  %4s %4s' % ("50", "10", "5", "1")
    line_value = 'value | %4s  %4s  %4s %4s' % (coin50,coin10,coin5,coin1)
    # print("50|10|5|1")
    print(line_title)
    print("-----------------------------")
    print(line_value)
    # print(coin50,coin10,coin5,coin1)


def main():
    changeMoney = int(input())
    leftAmount = changeMoney
    coin1 = 0
    coin5 = 0
    coin10 = 0
    coin50 = 0
    while leftAmount != 0 and leftAmount > 0 :
        # print(leftAmount)
        if leftAmount >= 50:
            coin50 = coin50+1
            leftAmount=leftAmount-50

        elif leftAmount >= 10:
            coin10 = coin10 + 1
            leftAmount=leftAmount-10
        
        elif leftAmount >= 5:
            coin5 = coin5 +5
            leftAmount=leftAmount-5

        elif leftAmount >= 1:
            coin1 = coin1 +1
            leftAmount=leftAmount-1

    printOut(coin1,coin5,coin10,coin50)

main()