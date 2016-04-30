from module import Stack        #和module裡的stack連結，以便後續使用

def infixToPrefix(infixexpr):   #轉換成prefix
    prec = {}
    prec["*"] = 3               #建立每個符號的階級，這樣子之後才可以判斷堆疊適用pop或push
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec[")"] = 1
    opStack = Stack()
    prefixList = []
    tokenList = infixexpr.split()   #split是把字串拆開成list
    tokenList.reverse()             #因為prefix由右至左判斷 所以先把原先postfix的list反相

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            prefixList.append(token)
        elif token == ')':            #處理括號 左右相反 因為prefix由右至左判斷
            opStack.push(token)
        elif token == '(':
            topToken = opStack.pop()
            while topToken != ')':
                prefixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  prefixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        prefixList.append(opStack.pop())
    prefixList.reverse()                #判斷完的結果需要再反向一次才恢復正確的答案
    return " ".join(prefixList)

print(infixToPrefix("A * B + C * D"))
print(infixToPrefix("( A + B ) * C - ( D - E ) * ( F + G )"))
