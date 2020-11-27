#define function
def basic(parameter,filename):
    with open(filename) as fx:
        Htext=fx.read()
        chars=len(Htext)
        sentence=0
        danci=0
        words= Htext.split()
        danci=len(words)
        for ch in Htext:
            if (ch=='.'):
                sentence=sentence+1
        if parameter=='c':
            return chars
        elif parameter=='w':
            return danci
        elif parameter=='s':
            return sentence
#define function
def extend(parameter,filename):
    with open(filename,'r',encoding='UTF-8') as fy:
        Htext=fy.readlines()
        code_num=0
        blank_num=0
        annotate_num=0
        for content in Htext:
            content = content.strip()
            # 统计空行
            if content == '':
                blank_num += 1
            # 统计注释行
            elif content.startswith('#'):
                annotate_num += 1
            # 统计代码行
            else:
                code_num += 1
        if parameter=='k':
            return blank_num
        elif parameter=='z':
            return annotate_num
        elif parameter=='d':
            return code_num
