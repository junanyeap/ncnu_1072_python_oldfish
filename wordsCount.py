# 持續讀入資料一直到檔案結束（ctrl d in command line）
# 以空格分割line，找出所有的字串
# 計算所有字的出現次數
# sample input
# hello world this is my first sentence
# A test line is seperated to many word by spaces
# sample output
# is 2
# A 1
# ......
wordDict = {}
def printResult():
    print(wordDict)

def count(words):
    for i in range(len(words)):
        if (words[i] in wordDict) == False :
            wordDict[words[i]] = 1
        else :
            tempCount = wordDict[words[i]] + 1
            wordDict[words[i]] = tempCount

def main():
    while True:
        try :
            words = input().split()
            count(words)
        except :
            printResult()
            break
main() 