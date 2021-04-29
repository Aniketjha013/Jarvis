
from datetime import date
from calendar import day_name
import speech_recognition as sr


while True:


    def pur(a):
        return a


    def da(b):

        return b
    def day(c):
        return c

    print("============================")
    print("  -=--=-=--= | Expense Tracker |-=-=-=-=-=-  ")
    print("=========================================================== ")
    print("1. Enter your purchased item")
    print("2. Enter the date of purchase")
    print("3. Enter the the day of purchase")


    ff=int(input('enter your choice from (1-3):'))
    # print(date.today())

    ad=0
    if ff==1:
        r=sr.Recognizer()
        with sr.Microphone() as source:

            a=('What did you purchase?:')
            print(a)
            audio=r.listen(source)

            try:
                text=r.recognize_google(audio)
                print('You said: {}',format(text))
            except:
                print("sorry couldn't recognize")

        f = open('pbks.txt', 'w')
        f.writelines(  format(text))
        f.close()
        ad=pur(a)
    elif ff==2:
        b=0
        print(date.today())
        f = open('pbks.txt', 'a+')
        f.write(str(date.today()))
        f.close()

        ad=da(b)
    elif ff==3:
        r = sr.Recognizer()
        with sr.Microphone() as source:

            c= ('On which day did you purchase?: ')
            print(c)
            audio = r.listen(source)

            try:
                text = r.recognize_google(audio)
                print('You said: {}', format(text))
            except:
                print("sorry couldn't recognize")
            f = open('pbks.txt', 'a+')
            f.write(   format(text))
            f.close()

        ad=day(c)
    else:
        print('Sorry wrong input number')

    choice=input('Do you want to continue{y/n}')
    if choice !='y':
        print('Bye! have a great time')

        break



