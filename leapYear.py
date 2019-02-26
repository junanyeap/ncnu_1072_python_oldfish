#學號：104213070
#姓名：葉潤安

def leapYearJudge(year):
    # 依傳遞來的year，做下面兩項判斷來計算是否爲閏年
    # 其中一項符合，即是閏年
    # 是---則return true，否---則return false
    return (year%4==0 and year%100!=0) or (year%400 == 0 and year % 3200 !=0)

def main():
    # [WRONG] 宣告變數year，存儲使用者輸入的年份
    # define and link year with input()
    # int()目的在於改變輸入值的形態，由預設的str改成int
    year = int(input("Please input a year to judge if leapyear : "))
    
    # 依據呼叫class的回傳結果，印出相對應文字
    # print(leapYearJudge(year))
    if leapYearJudge(year) == True:
        print("加薪!!")
    else :
        print("沒有加薪QQ")

# 呼叫主class
main()