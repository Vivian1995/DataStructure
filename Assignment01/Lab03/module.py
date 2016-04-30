def htmlChecker(htmlString):
    s = Stack()
    balanced = True
    index = 0
    opens = ['html>', 'title>', 'body>', 'head>', 'h1>']            #開頭符號
    closers = ['/html>', '/title>', '/body>', '/head>', '/h1>']     #結尾符號
    htmltag= htmlString.split('<')                                  #將輸入字串以符號<為分界，拆成一個list
    while index < len(htmltag) and balanced:
        tag = htmltag[index]
        if tag in opens:                                            #比對的符號與開頭符號相符＝＞加入堆疊
            s.push(tag)
        elif tag in closers:
            if s.isEmpty():                                         #比對的符號與結尾符號相符且堆疊是空的＝＞不對稱
                balanced = False
            else:                                                   #比對的符號與結尾符號相符且堆疊不是空的
                top = s.pop()
                if not matches(top, tag):                           #比對堆疊對上層符號與比對的符號是否對稱
                       balanced = False
        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open,close):                                            #檢查開頭與結尾符號是否為同一對
    opens = ['html>', 'title>', 'body>', 'head>', 'h1>']
    closers = ['/html>', '/title>', '/body>', '/head>', '/h1>']
    return opens.index(open) == closers.index(close)



class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)