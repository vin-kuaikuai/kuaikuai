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
parameter=input("parameter is:")
print
filename=input("filename is:")
print
a=extend(parameter,filename)
print(a)
parameter=input("parameter is:")
print
filename=input("filename is:")
print
b=extend(parameter,filename)
print(b)
parameter=input("parameter is:")
print
filename=input("filename is:")
print
c=extend(parameter,filename)
print(c)
