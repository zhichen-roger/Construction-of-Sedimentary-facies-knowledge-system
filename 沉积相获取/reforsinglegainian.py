# -*- coding: utf-8 -*-
import csv
import re
str1=' 同相位爬生波痕纹理（Climbing ripple laminations in-phase）：后一波痕直接 盖在前一波痕之上，前后波痕在水平方向上的位移很小，向流面和背流面纹层的厚度近于相等。   迁移型爬生波痕纹理（Climbing ripple laminations in-drift）：后一波痕盖在前一波痕之上，但前后波痕在水平方向上有明显的位移，向流面和背流面纹层的厚度不相等。向流面和背流面纹层都发育，称为Ⅰ型；仅背流面纹层保留下来，向流面纹层没有保存下来，称为Ⅱ型。      c) 水平层理（Horizontal Bedding）：由相互平行且近于水平的泥质纹层构成 ，纹层厚 1~2mm   d) 平行层理（Parallel Bedding）：由相互平行且近于水平的沙质纹层构成 ，纹层厚 1~2mm'
str2='正砾岩（Orthoconglomerate)：沙质基质<15%，砾石支撑，牵引流的滚动搬运或浊流搬运，国内一般将这种砾岩简称为砾岩，下面主要讨论这种砾岩。 副砾岩（Paraconglomerate)：基质>15%，多为泥质，基质支撑，砾石漂浮在基质中，因此，这种砾岩也称为砾质泥岩或含砾泥岩（Pebbly mudstone, Conglomeratic mudstone）。这种砾岩多呈块体搬运，如冰川、泥石流等。 '
def regurlar(str1,ktext,ctext,jtext):
    print(str1)
    str1=str1.replace('-','hzc')
    findch = re.compile('(.[\u4E00-\u9FA5]+\s*[（|(]+\s*[\u9FA5_a-zA-Z ]+)')
    cas_part_names = re.findall(findch,str1)
    with open('1.csv','a+',newline='',encoding='gbk') as f:
        w=csv.writer(f)

        for i in cas_part_names:
            print('概念',i.replace("hzc",'-'))
            i=i.replace("⇒", '')
            i=i.replace("hzc", '-')
            alist=i.split("（")
            try:
                w.writerow([ktext, ctext, jtext,alist[0],alist[1]])
            except IndexError:
                w.writerow([ktext, ctext, jtext, alist[0]])
    f.close()
if __name__ == '__main__':
    regurlar(str2)

