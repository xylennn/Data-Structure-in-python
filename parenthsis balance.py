class stack():
    def __init__(self):
        self.item = []

    def push(self, data):
        return self.item.append(data)

    def pop(self):
        return self.item.pop()

    def get_stack(self):
        return self.item

    def is_empty(self):
        return self.item == []

    def peak(self):
        return self.item[-1]

def not_match(p1,p2):
    if p1=='(' and p2 ==')':
        return True
    elif p1 == '{' and p2 == '}':
        return True
    elif p1=='[' and p2 ==']':
        return True
    else:
        return False


def paren_balanced(paren_str):
    s=stack()
    is_balanced=True
    index=0
    while is_balanced == True and index<len(paren_str):
            paren=paren_str[index]
            if paren in '({[':
                s.push(paren)
            else:
                if s.is_empty():
                    is_balanced=False
                else:
                    top=s.pop()
                    if not not_match(top,paren):
                        is_balanced=False
            index+=1
    if s.is_empty() and is_balanced==True:
        return True
    else:
        return False
