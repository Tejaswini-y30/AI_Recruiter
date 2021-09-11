#0. libraries
import random
from textblob import TextBlob
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
#1. name and converstation
def chat():
    print("Hello human what is your name?")
    name=input()


    #2. greetings 
    greetings =[
        'How are you today '+ name +'?',
        'How are you feeeling today '+ name +' ?',
        'How are things going on ' + name +' ?',
        'Hope you doing good tell me about you '+ name +' ?'
    ]
    print(random.choice(greetings))
    ans=input()
    blob=TextBlob(ans)

    if blob.polarity>0:
        print('Glad your doing well')
    else:
        print('Sorry to hear that')


    #3. random topics
    topics=[
        'html ',
        'java ',
        'c++ ',
        'python ',
        'computer networks '
    ]

    questions=[
        'How much you know about ',
        'Can You tell me about ',
        'Explain me about ',
        'Give a short explaination on ',
    ]
    for i1 in range(0,random.randint(3,4)):
        question=random.choice(questions)
        questions.remove(question)
        topic=random.choice(topics)
        topics.remove(topic)
        print(question+topic+'?')
        ans=input()
        blob=TextBlob(ans)

        if blob.polarity>0.5:
            print('ok great')
        elif blob.polarity>0.1:
            print('quiet right')
        elif blob.polarity<-0.5:
            print('Sorry u miss something')
        elif blob.polarity<-0.1:
            print('Sorry u miss few things')
        else:
            print('good')

        if blob.subjectivity >0.6:
            print("nuteral")
        elif blob.subjectivity >0.3:
            print("not so")
        else:
            print("obj")
    #4. goodbyes

htmlans="Stands for Hypertext Markup Language.HTML is the language used to create webpages. Hypertext refers to the hyperlinks that an HTML page may contain. Markup language refers to the way tags are used to define the page layout and elements within the page.The first line defines what type of contents the document contains. <!doctype html> means the page is written in HTML5. Properly formatted HTML pages should include <html>, <head>, and <body> tags, which are all included in the example above. The page title, metadata, and links to referenced files are placed between the <head> tags. The actual contents of the page go between the <body> tags.The web has gone through many changes over the past few decades, but HTML has always been the fundamental language used to develop webpages. Interestingly, while websites have become more advanced and interactive, HTML has actually gotten simpler. If you compare the source of an HTML5 page with a similar page written in HTML 4.01 or XHTML 1.0, the HTML5 page would probably contain less code. This is because modern HTML relies on cascading style sheets or JavaScript to format nearly all the elements within a page."
def rate(ans):
    avg=0
    blob=TextBlob(ans)
    text=[ans,htmlans]
    cv = CountVectorizer()
    count_matrix =cv.fit_transform(text)
    matchpercent = cosine_similarity(count_matrix)[0][1]*100
    matchpercent = round(matchpercent, 2) 
    if blob.polarity>0.5:
        avg=90
    elif blob.polarity>0.1:
        avg=70
    elif blob.polarity<-0.5:
        avg=60
    elif blob.polarity<-0.1:
        avg=50
    else:
        avg=40

    avg= (avg+matchpercent)/2
    return avg

pythonans="Python is a widely used general-purpose, high level programming language. It was created by Guido van Rossum in 1991 and further developed by the Python Software Foundation. It was designed with an emphasis on code readability, and its syntax allows programmers to express their concepts in fewer lines of code.Python is a programming language that lets you work quickly and integrate systems more efficiently.To print something on the console, print() function is used. This function also adds a newline after our message is printed(unlike in C). Note that in Python 2, “print” is not a function but a keyword and therefore can be used without parentheses. However, in Python 3, it is a function and must be invoked with parentheses.Python is a high level, interpreted and general purpose dynamic programming language that focuses on code readability.It has fewer steps when compared to Java and C.It was founded in 1991 by developer Guido Van Rossum.It is used in many organizations as it supports multiple programming paradigms.It also performs automatic memory management."
def rate1(ans):
    avg=0
    blob=TextBlob(ans)
    text=[ans,pythonans]
    cv = CountVectorizer()
    count_matrix =cv.fit_transform(text)
    matchpercent = cosine_similarity(count_matrix)[0][1]*100
    matchpercent = round(matchpercent, 2) 
    if blob.polarity>0.5:
        avg=90
    elif blob.polarity>0.1:
        avg=70
    elif blob.polarity<-0.5:
        avg=60
    elif blob.polarity<-0.1:
        avg=50
    else:
        avg=40

    avg= (avg+matchpercent)/2
    return avg

cppans="C++ is a general-purpose object-oriented programming language developed by Bjarne Stroustrup of Bell Labs in 1979. C++ was originally called ‘C with classes,’ and was built as an extension of the C language. Its name reflects its origins; C++ literally means ‘increment C by 1.’C++ is considered a mid-level programming language, combining some elements of low-level programming languages, such as the need to learn memory management, with high-level features. Because of this, C++ is considered quite a complex language — in comparison to languages such as Python you need to know quite a bit more before you can create your first truly useful programs.C++ is a multi-paradigm coding language. This means that it supports other styles such as procedural programming, in addition to object-oriented programming. These paradigms are essentially different ways of looking at and solving a coding problem; two different C++ coders could look at and solve the same coding problem in different ways. Paradigms can also be combined to get the most efficient result."
def rate2(ans):
    avg=0
    blob=TextBlob(ans)
    text=[ans,cppans]
    cv = CountVectorizer()
    count_matrix =cv.fit_transform(text)
    matchpercent = cosine_similarity(count_matrix)[0][1]*100
    matchpercent = round(matchpercent, 2) 
    if blob.polarity>0.5:
        avg=90
    elif blob.polarity>0.1:
        avg=70
    elif blob.polarity<-0.5:
        avg=60
    elif blob.polarity<-0.1:
        avg=50
    else:
        avg=40

    avg= (avg+matchpercent)/2
    return avg