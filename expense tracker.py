
# from datetime import date
# from calendar import day_name
# import speech_recognition as sr


# while True:


#     def pur(a):
#         return a


#     def da(b):

#         return b
#     def day(c):
#         return c

#     print("============================")
#     print("  -=--=-=--= | Expense Tracker |-=-=-=-=-=-  ")
#     print("=========================================================== ")
#     print("1. Enter your purchased item")
#     print("2. Enter the date of purchase")
#     print("3. Enter the the day of purchase")


#     ff=int(input('enter your choice from (1-3):'))
#     # print(date.today())

#     ad=0
#     if ff==1:
#         r=sr.Recognizer()
#         with sr.Microphone() as source:

#             a=('What did you purchase?:')
#             print(a)
#             audio=r.listen(source)

#             try:
#                 text=r.recognize_google(audio)
#                 print('You said: {}',format(text))
#             except:
#                 print("sorry couldn't recognize")

#         f = open('pbks.txt', 'w')
#         f.writelines(  format(text))
#         f.close()
#         ad=pur(a)
#     elif ff==2:
#         b=0
#         print(date.today())
#         f = open('pbks.txt', 'a+')
#         f.write(str(date.today()))
#         f.close()

#         ad=da(b)
#     elif ff==3:
#         r = sr.Recognizer()
#         with sr.Microphone() as source:

#             c= ('On which day did you purchase?: ')
#             print(c)
#             audio = r.listen(source)

#             try:
#                 text = r.recognize_google(audio)
#                 print('You said: {}', format(text))
#             except:
#                 print("sorry couldn't recognize")
#             f = open('pbks.txt', 'a+')
#             f.write(   format(text))
#             f.close()

#         ad=day(c)
#     else:
#         print('Sorry wrong input number')

#     choice=input('Do you want to continue{y/n}')
#     if choice !='y':
#         print('Bye! have a great time')

#         break


from tkinter import *
import tkinter.messagebox as tmsg


root = Tk()
root.geometry("800x500")
def order():
    tmsg.showinfo("Order received!",f"We have received your order for {var.get()}.Thanks for ordering!")
var = StringVar()
var.set("Radio")

Label(root,text="Welcome to Valhalla Cuisine",font="lucida 19 bold",justify=LEFT,padx=14.).grid()
radio=Radiobutton(root,text="Chicken Cheese Burger (300)",padx=14,variable=var,value="Chicken Cheese Burger").grid()
radio=Radiobutton(root,text="Grilled chicken Burger (350)",padx=14,variable=var,value="Grilled chicken Burger").grid()
radio=Radiobutton(root,text="Jumbo Ham Burger (360)",padx=14,variable=var,value="Jumbo Ham Burger").grid()
radio=Radiobutton(root,text="Tuna Pizza (1200)",padx=14,variable=var,value="Tuna Pizza").grid()
radio=Radiobutton(root,text="Margarita Pizza (1000)",padx=14,variable=var,value="Margarita Pizza").grid()
radio=Radiobutton(root,text="Salami Pizza (950)",padx=14,variable=var,value="Salami Pizza").grid()
radio=Radiobutton(root,text="French Fries with coke (400)",padx=14,variable=var,value="French Fries with coke").grid()
Button(text='Order now',command=order).grid()


def getvals():
    print("Tracking my expense")

    print(f"{nameval.get(), phonenumbervalue.get(), genderval.get(), dateofpurchase.get(), paymentmodeval.get(), foodserviceval.get()} ")



    with open("records.txt", "a") as f:
        f.write(f"{nameval.get(), phonenumbervalue.get(), genderval.get(), dateofpurchase.get(), paymentmodeval.get(), foodserviceval.get()}\n ")




#Heading
Label(root, text="Your details", font="comicsansms 13 bold", pady=15).grid(row=0, column=3)

#Text for our form
name = Label(root, text="Name")
number = Label(root, text="Phone Number")
gender = Label(root, text="Gender")
Dateofpurchase = Label(root, text="Date of Purchase")
paymentmode = Label(root, text="Payment Mode")

#Pack text for our form
name.grid(row=1, column=2)
number.grid(row=2, column=2)
gender.grid(row=3, column=2)
Dateofpurchase.grid(row=4, column=2)
paymentmode.grid(row=5, column=2)

# Tkinter variable for storing entries
nameval = StringVar()
phonenumbervalue = StringVar()
genderval = StringVar()
dateofpurchase = StringVar()
paymentmodeval = StringVar()
foodserviceval = IntVar()


#Entries for our form
nameentry = Entry(root, textvariable=nameval)
amountentry = Entry(root, textvariable=phonenumbervalue)
genderentry = Entry(root, textvariable=genderval)
dateofpurchaseentry = Entry(root, textvariable=dateofpurchase)
paymentmodeentry = Entry(root, textvariable=paymentmodeval)

# Packing the Entries
nameentry.grid(row=1, column=3)
amountentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
dateofpurchaseentry.grid(row=4, column=3)
paymentmodeentry.grid(row=5, column=3)

#Checkbox & Packing it
foodservice = Checkbutton(text="Want to order for home?", variable = foodserviceval)
foodservice.grid(row=6, column=3)

#Button & packing it and assigning it a command
Button(text="Submit to Valhalla Cuisine", command=getvals).grid(row=7, column=3)


root.mainloop()

