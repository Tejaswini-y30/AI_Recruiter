#0. libraries
import os
import docx2txt
#import pdftotext
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import PyPDF2


#1. load data

#2. store resume in variable
#resume =docx2txt.process("python_resume.docx")
def match():
    pdffileobj=open('media/python_resume12.pdf','rb')
    pdfreader=PyPDF2.PdfFileReader(pdffileobj)
    x=pdfreader.numPages
    pageobj=pdfreader.getPage(x-1)
    resume=pageobj.extractText()

    #3. store job description into variable
    #job_description = docx2txt.process("job_description.docx")
    pdffileobj=open('media/job_description.pdf','rb')
    pdfreader=PyPDF2.PdfFileReader(pdffileobj)
    x=pdfreader.numPages
    pageobj=pdfreader.getPage(x-1)
    job_description=pageobj.extractText()
    text=[resume,job_description]

    cv = CountVectorizer()
    count_matrix =cv.fit_transform(text)

    #4. similarity
    #print("Similarity Scores")
    # print(cosine_similarity(count_matrix))


    #5. match percentage
    matchpercent = cosine_similarity(count_matrix)[0][1]*100
    matchpercent = round(matchpercent, 2) 
    print('Your resume matches about '+ str(matchpercent) +'% of the job description')
    return matchpercent
