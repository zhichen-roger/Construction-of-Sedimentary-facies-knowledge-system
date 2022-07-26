import re
def judgesection(strtest):
    findch = re.compile('第([\u4E00-\u9FA5])部分')
    cas_part_names = re.findall(findch, strtest)
    if len(cas_part_names)!=0:
        return True
    return False
def judgechpter(strtest):
    findch = re.compile('第([\u4E00-\u9FA5])章')
    cas_part_names = re.findall(findch, strtest)

        #print(i)
    if len(cas_part_names)!=0:
        return True
    return False
def judgejie(strtest):
    findch = re.compile('第([\u4E00-\u9FA5])节')
    cas_part_names = re.findall(findch, strtest)
    if len(cas_part_names)!=0:
        return True
    return False

if __name__ == '__main__':
    str1='第一部分: 分析原理'
    judgesection(str1)

