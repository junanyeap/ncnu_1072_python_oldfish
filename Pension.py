# 12(一年) * (每個月提撥金額) * {(1+(年報酬)) + (1+(年報酬))2 + … + (1+(年報酬))m}
# m 為總工作年資
def main():
    start,ryear,rate,roi,expect = map(int,input().split())
    fund = 0
    for age in range(start,ryear):
        if age < ryear:
            fund += rate/100
        else :
            fund -= expert/100
        if fund <= 0:
            print('break at age ',age)
            break;
        fund *= (1+roi/100)
    if fund > 0:
        print('remain ',fund)

main()