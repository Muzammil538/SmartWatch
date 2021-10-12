import datetime

def ShowTime():

    Date = datetime.date.today().strftime("%B %d, %Y")
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    print("Date : ",Date,"\nTime : ",Time)
#ShowTime()

