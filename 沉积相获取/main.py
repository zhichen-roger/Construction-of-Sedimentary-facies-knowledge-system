import docx
from docx import Document
def run():


    doc = Document('docxtest.docx')
    sections = doc.paragraphs
    print(len(sections))
    for i in sections:
        print("1234",i.text)

    return

if __name__ == '__main__':
    run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
