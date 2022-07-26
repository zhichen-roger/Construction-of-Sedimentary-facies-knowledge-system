import docx
from docx import Document
from  reforsinglegainian import  regurlar
from  judge2 import judgesection,judgechpter,judgejie
def run():
    doc = Document('docxtest.docx')
    sections = doc.paragraphs
    print(len(sections))
    k=0
    c=0
    j=0
    ktext=''
    ctext=''
    jtext=''
    for i in sections:

        if judgesection(i.text)==True:
            k=k+1
            c=0
            ktext=i.text
            for cc in ['一','二','三','四','五','六','七','八','第','部分',":"," "]:
                ktext= ktext.replace(cc, "")

        else:
            if judgechpter(i.text) == True:
                c = c+1
                j = 0
                print(i.text)
                jtext=i.text
                for cc in ['一', '二', '三', '四', '五', '六', '七', '八', '第', '章', ":", " ","	"]:
                    jtext = jtext.replace(cc, "")
            else:
                if judgejie(i.text) == True:
                    j = j + 1
                    ctext=i.text
                    for cc in ['一', '二', '三', '四', '五', '六', '七', '八', '第', '节', ":", " ", "	"]:
                        ctext = ctext.replace(cc, "")

                else:
                     strtext=i.text.split("。")
                     for ccc in strtext:
                        strtextlist = ccc.split("，")

                        for jj in strtextlist:
                            regurlar(jj,ktext,ctext,jtext)
    return

if __name__ == '__main__':
    run()