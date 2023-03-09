import os, pandas
from bs4 import BeautifulSoup as BX

tags = ['dhEmi', 'nNF', 'vLiq', 'chNFe']

myfiles_path = r"/Users/rtakaoka/Codes/NFs Two/Notas Fiscais - Two February"

def parse_xml(xmlfile):
    with open(xmlfile, 'r') as fd:
        doc = fd.read()
    soup = BX(doc, 'lxml-xml')
    mydata = {}
    for tag in tags:
        value = soup.find(tag)
        if value:
            mydata[tag] = value.text
        else:
            mydata[tag] = None
    return mydata

all_data = {}

xmlfiles = os.listdir(myfiles_path)

for i, file in enumerate(xmlfiles, start=1):
    print(i, "/", len(xmlfiles))
    file_path = os.path.join(myfiles_path, file)
    all_data[file] = parse_xml(file_path)

df = pandas.DataFrame.from_dict(all_data)
df_transposed = df.transpose()
df_transposed.to_csv('output.csv')