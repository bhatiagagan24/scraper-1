from bs4 import BeautifulSoup
import requests
import pymongo

import json

myclient = pymongo.MongoClient("mongodb+srv://gdb101:gaganonmongodb100@cluster0.xcgis.mongodb.net/questionBank?retryWrites=true&w=majority")
mydb = myclient["learncbse"]
mycol = mydb["class_9th"]

url = ["https://www.learncbse.in/ncert-solutions-for-class-9-english-moments-weathering-the-storm-in-ersama/", 
        "https://www.learncbse.in/ncert-solutions-for-class-9-english-moments-the-last-leaf/",
        "https://www.ncertbooks.guru/ncert-solutions-for-class-9-english-moments-chapter-8-a-house-is-not-a-home/amp/",
        "https://www.learncbse.in/ncert-solutions-for-class-9-english-moments-the-accidental-tourist/",
        "https://www.learncbse.in/ncert-solutions-for-class-9-english-moments-the-beggar/"]


topics = [ "Chapter 6 Weathering the Storm in Ersama","Chapter 7 The Last Leaf", "Chapter 8 A House is not a Home", "Chapter 9 The Accidental Tourist", "Chapter 10 The Beggar"]


cbse_class = "Class 9"

subject = "English Moments"

params = ["class" , "subject" , "url", "topics", "QuestionAnswers"]

qna = []

for u in range(0, len(url)):
    qna_temp = []
    qna_temp.append(cbse_class)
    qna_temp.append(subject)
    qna_temp.append(url[u])
    qna_temp.append(topics[u])
    html_content = requests.get(url[u])
    soup = BeautifulSoup(html_content.content, 'html.parser')
    one = []
    m = soup.findAll('p')
    for g in m:
        if(g.strong) or (g.time):
            continue
        elif "Filed Under:" in g.text:
            continue
        elif "Learn CBSE" in g.text:
            continue
        elif "NCERT Solutions for Class 6, 7, 8, 9, 10, 11 and 12" in g:
            continue
        elif "Filed Under: CBSE Tagged With: NCERT Solutions for Class 9," in g:
            continue
        elif "drop a comment below and we will get back to you at the earliest.'" in g:
            continue
        elif "We hope the NCERT" in g:
            continue
        # elif "\u00a0" in g:
            # continue
        else:
            # print(g.text)
            one.append(g.text)
    qna_temp.append(one)
    qna.append(dict(zip(params, qna_temp)))
print(qna)
print()
print("--------------------------------------------------------")
print()

temp1 = open('chap6-10-eng-class9.json', 'a')
# temp1.write(str(qna))
# temp1.close()
json.dump(qna, temp1)


# res1 = dict(zip(qna, url))

# Inserting into MongoDB
print(type(qna))
# db_upload = mycol.insert_many(qna)
# print(db_upload)
print()

# print(qna)