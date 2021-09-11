from textblob import TextBlob

def analysis(ans):
    rate=0
    blob=TextBlob(ans)

    if blob.polarity>0.5:
        rate=80
    elif blob.polarity>0.1:
        rate=70
    elif blob.polarity<-0.5:
        rate=30
    elif blob.polarity<-0.1:
        rate=40
    else:
        rate=50

    if blob.subjectivity >0.6:
        rate=rate+7
    elif blob.subjectivity >0.3:
        rate=rate+10
    else:
        rate=rate+5
    
    return rate