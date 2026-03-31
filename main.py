#import tkinter library
from tkinter import *
from tkinter import messagebox
import  random,os,tempfile,smtplib
#function part

def clear():
    # Clear Taxes
    cosmetictaxEntry.delete(0, END)
    groceryTaxEntry.delete(0, END)
    drinktaxEntry.delete(0, END)

    # Clear Prices
    cosmeticpriceEntry.delete(0, END)
    grocerypriceEntry.delete(0, END)
    drinkpriceEntry.delete(0, END)

    # Cosmetics
    bathsoapEntry.delete(0, END)
    bathsoapEntry.insert(0, "0")

    facecreamEntry.delete(0, END)
    facecreamEntry.insert(0, "0")

    facewashEntry.delete(0, END)
    facewashEntry.insert(0, "0")

    hairsprayEntry.delete(0, END)
    hairsprayEntry.insert(0, "0")

    hairgelEntry.delete(0, END)
    hairgelEntry.insert(0, "0")

    bodylotionEntry.delete(0, END)
    bodylotionEntry.insert(0, "0")

    # Grocery
    riceEntry.delete(0, END)
    riceEntry.insert(0, "0")

    oilEntry.delete(0, END)
    oilEntry.insert(0, "0")

    daalEntry.delete(0, END)
    daalEntry.insert(0, "0")

    wheatEntry.delete(0, END)
    wheatEntry.insert(0, "0")

    sugarEntry.delete(0, END)
    sugarEntry.insert(0, "0")

    teaEntry.delete(0, END)
    teaEntry.insert(0, "0")

    # Cold Drinks
    maazaEntry.delete(0, END)
    maazaEntry.insert(0, "0")

    papsiEntry.delete(0, END)
    papsiEntry.insert(0, "0")

    SpriteEntry.delete(0, END)
    SpriteEntry.insert(0, "0")

    dewEntry.delete(0, END)
    dewEntry.insert(0, "0")

    frootiEntry.delete(0, END)
    frootiEntry.insert(0, "0")

    cocacolaEntry.delete(0, END)
    cocacolaEntry.insert(0, "0")

    # Customer Details
    nameEntry.delete(0, END)
    phoneEntry.delete(0, END)
    billnumberEntry.delete(0, END)

    # Clear Bill Area
    textarea.delete(1.0, END)

def send_email():
    def send_gmail():
        try:
            obj= smtplib.SMTP('smtp.gmail.com',587)
            obj.starttls()
            obj.login(senderEntry.get(),passwordEntry.get())
            message=email_textarea.get(1.0,END)
            obj.sendmail(senderEntry.get(),recieverEntry.get(),message)
            obj.quit()
            messagebox.showinfo('Success', 'Email sent successfully',parent=root1)
            root1.destroy()
        except:
            messagebox.showerror('Error','Something went wrong, please try agin',parent=root1)



    if textarea.get(1.0,END) == '\n':
        messagebox.showerror('bill is empty','bill is empty')
    else:
        root1=Toplevel()
        root1.grab_set()
        root1.title('send gmail')
        root1.configure(bg='gray20')
        root1.resizable(0,0)


    senderFrame=LabelFrame(root1,text='Sender',font=('arial',16,'bold'),bd=6,fg='white',bg='gray20')
    senderFrame.grid(row=0,column=0,padx=40,pady=20)

    senderLabel=Label(senderFrame,text='Senders gmail',font=('arial',14,'bold'),bg='gray20',fg='white')
    senderLabel.grid(row=0,column=0,padx=10,pady=8)

    senderEntry=Entry(senderFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
    senderEntry.grid(row=0,column=1,padx=10,pady=8)

    passwordLabel = Label(senderFrame, text='password', font=('arial', 14, 'bold'), bg='gray20', fg='white')
    passwordLabel.grid(row=1, column=0, padx=10, pady=8)

    passwordEntry = Entry(senderFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE,show='*')
    passwordEntry.grid(row=1, column=1, padx=10, pady=8)

    recipientFrame = LabelFrame(root1, text='RECIPIENT', font=('arial', 16, 'bold'), bd=6, fg='white', bg='gray20')
    recipientFrame.grid(row=1, column=0, padx=40, pady=20)

    recieverLabel = Label(recipientFrame, text='Email Address', font=('arial', 14, 'bold'), bg='gray20', fg='white')
    recieverLabel.grid(row=0, column=0, padx=10, pady=8)

    recieverEntry = Entry(recipientFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE)
    recieverEntry.grid(row=0, column=1, padx=10, pady=8)

    messageLabel = Label(recipientFrame, text='Message', font=('arial', 14, 'bold'), bg='gray20', fg='white')
    messageLabel.grid(row=1, column=0, padx=10, pady=8)

    email_textarea=Text(recipientFrame,font=('arial',14,'bold'),bd=2,relief=SUNKEN,width=42,height=11)
    email_textarea.grid(row=2,column=0,columnspan=2)
    email_textarea.delete(1.0,END)
    email_textarea.insert(END,textarea.get(1.0,END).replace('=','').replace('-','').replace('\t\t\t','\t\t'))

    sendButton=Button(root1,text='SEND',font=('arial',14,'bold'),width=15,command=send_gmail)
    sendButton.grid(row=2,column=0,padx=10,pady=20)
    root1.mainloop()

def print_bill():
    if textarea.get(1.0,END) == '\n':
        messagebox.showerror('Error','Bill is empty')
    else:
        file=tempfile.mktemp('.txt')
        open(file,'w').write(textarea.get(1.0,END))
        os.startfile(file,'print')


def search_bill():
    bill_no = billnumberEntry.get().strip()

    if bill_no == "":
        messagebox.showerror("Error", "Please enter bill number")
        return

    found = False

    for i in os.listdir('bills/'):
        if i.split('.')[0] == bill_no:
            with open(f'bills/{i}', 'r') as f:
                textarea.delete(1.0, END)
                textarea.insert(END, f.read())
            found = True
            break

    if not found:
        messagebox.showerror('Error', 'Invalid Bill Number')


if not os.path.exists('bills'):
    os.mkdir('bills')

def save_bill():
    global billnumber
    result=messagebox.askyesno('Confirmation', 'Do you wish to save bill?')
    if(result):
        bill_content=textarea.get(1.0,END)
        file=open(f'bills/{billnumber}.txt','w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Sucess',f'bill number {billnumber}Bill Saved sucessfully')
        billnumber=random.randint(500,1000)

billnumber=random.randint(500,1000)
def bill_area():
    if nameEntry.get() == '' or phoneEntry.get() == '':
        messagebox.showerror('Error','Customer Details is Are required')
    elif cosmeticpriceEntry.get() == '' and grocerypriceEntry.get() == '' and drinkpriceEntry.get() == '':
        messagebox.showerror('Error', ' no products are selected ')
    elif cosmeticpriceEntry.get() == '0 Rs' and grocerypriceEntry.get() == '0 Rs' and drinkpriceEntry.get() == '0 Rs':
       messagebox.showerror('Error', ' no products are selected ')
    textarea.delete('1.0', END)

    name = nameEntry.get().strip()
    phone = phoneEntry.get().strip()

    # Validate name
    if not name.replace(" ", "").isalpha():
        messagebox.showerror("Invalid Name", "Name must contain only letters!")
        return

    # Validate phone number
    if not phone.isdigit() or len(phone) != 10:
        messagebox.showerror("Invalid Phone", "Phone number must be 10 digits!")
        return

    # If valid → insert into textarea
    textarea.insert(END, '\t\t**Welcome Customer**\n')
    textarea.insert(END, f'\nBill Number: {billnumber}\n')
    textarea.insert(END, f'\nCustomer Name: {name}\n')
    textarea.insert(END, f'\nCustomer Phone Number: {phone}\n')
    textarea.insert(END, '\n==================================================')
    textarea.insert(END, '\tProdect\t\tQuantity\t\tPrice')
    textarea.insert(END, '\n==================================================')

    if bathsoapEntry.get()!='0':
        textarea.insert(END,f'\nBath Soap\t\t{bathsoapEntry.get()}\t\t{soapprice} Rs')
    if hairsprayEntry.get() != '0':
            textarea.insert(END, f'\nHair Spary\t\t{hairsprayEntry.get()}\t\t{hairsparyprice} Rs')
    if hairgelEntry.get() != '0':
            textarea.insert(END, f'\nHair Gel\t\t{hairgelEntry.get()}\t\t{hairgelprice} Rs')
    if facecreamEntry.get() != '0':
           textarea.insert(END, f'\nFace Cream\t\t{facecreamEntry.get()}\t\t{facecreamprice} Rs')
    if facewashEntry.get() != '0':
             textarea.insert(END, f'\nFace Wash\t\t{facewashEntry.get()}\t\t{facewashprice} Rs')
    if bodylotionEntry.get() != '0':
            textarea.insert(END, f'\nBody Lotion\t\t{bodylotionEntry.get()}\t\t{bodylotionprice} Rs')



    if riceEntry.get() != '0':
            textarea.insert(END, f'\nRice \t\t{riceEntry.get()}\t\t{riceprice} Rs')
    if daalEntry.get() != '0':
            textarea.insert(END, f'\nDaal \t\t{daalEntry.get()}\t\t{daalprice} Rs')
    if oilEntry.get() != '0':
            textarea.insert(END, f'\nOil \t\t{oilEntry.get()}\t\t{oilprice} Rs')
    if sugarEntry.get() != '0':
            textarea.insert(END, f'\nSugar \t\t{sugarEntry.get()}\t\t{sugarprice} Rs')
    if teaEntry.get() != '0':
            textarea.insert(END, f'\nTea_powder\t\t{teaEntry.get()}\t\t{teaprice} Rs')
    if wheatEntry.get() != '0':
            textarea.insert(END, f'\nWheat \t\t{wheatEntry.get()}\t\t{wheatprice} Rs')

    if maazaEntry.get() != '0':
            textarea.insert(END, f'\nMaaza \t\t{maazaEntry.get()}\t\t{maazaprice} Rs')
    if frootiEntry.get() != '0':
            textarea.insert(END, f'\nFrooti \t\t{frootiEntry.get()}\t\t{frooitprice} Rs')
    if papsiEntry.get() != '0':
            textarea.insert(END, f'\npepsi \t\t{papsiEntry.get()}\t\t{papsiprice} Rs')
    if dewEntry.get() != '0':
            textarea.insert(END, f'\nDew \t\t{dewEntry.get()}\t\t{dewprice} Rs')
    if SpriteEntry.get() != '0':
            textarea.insert(END, f'\nSprite \t\t{SpriteEntry.get()}\t\t{spriteprice} Rs')
    if cocacolaEntry.get() != '0':
            textarea.insert(END, f'\nCoca cola \t\t{cocacolaEntry.get()}\t\t{cocacloprice} Rs')
            textarea.insert(END, '\n==================================================')

    if cosmetictaxEntry.get() != '0.0':
            textarea.insert(END, f'\nCosmetic Tax \t\t\t{cosmetictaxEntry.get()} ')
    if groceryTaxEntry.get() != '0.0':
            textarea.insert(END, f'\nGrocery Tax \t\t\t{groceryTaxEntry.get()} ')
    if drinktaxEntry.get() != '0.0':
            textarea.insert(END, f'\nDrink Tax \t\t\t{drinktaxEntry.get()} ')
            textarea.insert(END,f'\n\nTotal Bill\t\t\t\t{totalbill}')
            textarea.insert(END, '\n==================================================')
            save_bill()


def total():
    global soapprice,hairsparyprice,hairgelprice,facecreamprice,bodylotionprice,facewashprice
    global riceprice,daalprice,oilprice,sugarprice,teaprice,wheatprice
    global maazaprice,frooitprice,pepsiprice,dewprice,papsiprice,spriteprice,cocacloprice
    global totalbill

    soapprice=int(bathsoapEntry.get())*20
    facecreamprice=int(facecreamEntry.get())*50
    facewashprice=int(facewashEntry.get())*100
    hairsparyprice=int(hairsprayEntry.get())*120
    hairgelprice=int(hairsprayEntry.get())*60
    bodylotionprice=int(bodylotionEntry.get())*40

    totalcosmeticprice=soapprice+facecreamprice+facewashprice+hairsparyprice+hairgelprice+bodylotionprice
    cosmeticpriceEntry.delete(0,'end')
    cosmeticpriceEntry.insert(0,str(totalcosmeticprice)+ ' Rs')
    cosmatictax=totalcosmeticprice*0.08
    cosmetictaxEntry.delete(0, 'end')
    cosmetictaxEntry.insert(0,str(cosmatictax)+ ' Rs')

    #geocery price calculate
    riceprice=int(riceEntry.get())*30
    daalprice = int(daalEntry.get()) *80
    oilprice = int(oilEntry.get()) *100
    sugarprice = int(sugarEntry.get()) *40
    teaprice = int(teaEntry.get()) *120
    wheatprice = int(wheatEntry.get()) *60

    totalgroceryprice=riceprice+daalprice+oilprice+sugarprice+teaprice+wheatprice
    grocerypriceEntry.delete(0, 'end')
    grocerypriceEntry.insert(0,str(totalgroceryprice)+ ' Rs')
    grocerytax =totalgroceryprice * 0.05
    groceryTaxEntry.delete(0, 'end')
    groceryTaxEntry.insert(0, str(grocerytax) + ' Rs')

    maazaprice=int(maazaEntry.get())*50
    frooitprice = int(frootiEntry.get()) * 20
    dewprice = int(dewEntry.get()) * 30
    papsiprice = int(papsiEntry.get()) * 20
    spriteprice = int(SpriteEntry.get()) * 45
    cocacloprice = int(cocacolaEntry.get()) * 90

    totaldrinkprice=maazaprice+frooitprice+dewprice+papsiprice+spriteprice+cocacloprice
    drinkpriceEntry.delete(0, 'end')
    drinkpriceEntry.insert(0, str(totaldrinkprice) + ' Rs')
    drinkstax=totaldrinkprice * 0.08
    drinktaxEntry.delete(0, 'end')
    drinktaxEntry.insert(0, str(drinkstax) + ' Rs')

    totalbill=totalcosmeticprice+totalgroceryprice+totaldrinkprice+cosmatictax+grocerytax+drinkstax

#GUI PART
root=Tk()
root.title('Reatial Billing Systeam')
root.geometry("1270x685")
root.iconbitmap('icon1.ico')
headingLabel=Label(root,text='Reatial Billing System',font=('times new roman',18,'bold'),
                   bg='gray20',fg='gold',bd=12,relief=GROOVE)
headingLabel.pack(fill=X)

customer_details_frame=LabelFrame(root,text='Customer Details',font=('times new roman',18,'bold')
                                  ,fg='gold',bd=8,relief=GROOVE,bg='gray20',)
customer_details_frame.pack(fill=X)

nameLabel=Label(customer_details_frame,text='Name:-',font=('times new roman',17,'bold'),bg='gray20',fg='white')
nameLabel.grid(row=0,column=0,padx=20)

nameEntry=Entry(customer_details_frame,font=('arial',17),bd=5,width=18)
nameEntry.grid(row=0,column=1,padx=8)

phoneLabel=Label(customer_details_frame,text='phone Number:-',font=('times new roman',17,'bold'),bg='gray20',fg='white')
phoneLabel.grid(row=0,column=2,padx=20,pady=2)

phoneEntry=Entry(customer_details_frame,font=('arial',17),bd=5,width=18)
phoneEntry.grid(row=0,column=3,padx=8)

billnumberLabel=Label(customer_details_frame,text='Bill Number:-',font=('times new roman',17,'bold'),bg='gray20',fg='white')
billnumberLabel.grid(row=0,column=4,padx=20,pady=2)

billnumberEntry=Entry(customer_details_frame,font=('arial',17),bd=5,width=18)
billnumberEntry.grid(row=0,column=5,padx=8)

searchButton=Button(customer_details_frame,text='SEARCH',font=('arial',18,'bold'),bd=10,command=search_bill)
searchButton.grid(row=0,column=6,padx=20,pady=15)

productsFrame=Frame(root)
productsFrame.pack()

cosmeticsFrame=LabelFrame(productsFrame,text='Cosmetics',font=('times new roman',18,'bold'),
                          fg='gold',bd=8,relief=GROOVE,bg='gray20')
cosmeticsFrame.grid(row=0,column=0)

bathsoapLabel=Label(cosmeticsFrame,text='Bath Soap',font=('times new roman',17,'bold'),bg='gray20',fg='white')
bathsoapLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

bathsoapEntry=Entry(cosmeticsFrame,font=('times new roman',20,'bold'),width=10,bd=5)
bathsoapEntry.grid(row=0,column=1,pady=9,padx=10,sticky='w')
bathsoapEntry.insert(0,'0')

facecreamLabel=Label(cosmeticsFrame,text='Face Cream',font=('times new roman',17,'bold'),bg='gray20',fg='white')
facecreamLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

facecreamEntry=Entry(cosmeticsFrame,font=('times new roman',20,'bold'),width=10,bd=5)
facecreamEntry.grid(row=1,column=1,pady=9,padx=10,sticky='w')
facecreamEntry.insert(0,'0')

facewashLabel=Label(cosmeticsFrame,text='Face Wash',font=('times new roman',17,'bold'),bg='gray20',fg='white')
facewashLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

facewashEntry=Entry(cosmeticsFrame,font=('times new roman',20,'bold'),width=10,bd=5)
facewashEntry.grid(row=2,column=1,pady=9,padx=10)
facewashEntry.insert(0,'0')

hairsprayLabel=Label(cosmeticsFrame,text='Hair Spray',font=('times new roman',17,'bold'),bg='gray20',fg='white')
hairsprayLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')

hairsprayEntry=Entry(cosmeticsFrame,font=('times new roman',20,'bold'),width=10,bd=5)
hairsprayEntry.grid(row=3,column=1,pady=9,padx=10)
hairsprayEntry.insert(0,'0')

hairgelLabel=Label(cosmeticsFrame,text='Hair Gel',font=('times new roman',17,'bold'),bg='gray20',fg='white')
hairgelLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

hairgelEntry=Entry(cosmeticsFrame,font=('times new roman',20,'bold'),width=10,bd=5)
hairgelEntry.grid(row=4,column=1,pady=9,padx=10)
hairgelEntry.insert(0,'0')

bodylotionLabel=Label(cosmeticsFrame,text='Body Lotion',font=('times new roman',17,'bold'),bg='gray20',fg='white')
bodylotionLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

bodylotionEntry=Entry(cosmeticsFrame,font=('times new roman',20,'bold'),width=10,bd=5)
bodylotionEntry.grid(row=5,column=1,pady=9,padx=10)
bodylotionEntry.insert(0,'0')

groceryFrame=LabelFrame(productsFrame,text='Grocery',font=('times new roman',18,'bold'),
                          fg='gold',bd=8,relief=GROOVE,bg='gray20')
groceryFrame.grid(row=0,column=1)

riceLabel=Label(groceryFrame,text='Rice (kg)',font=('times new roman',17,'bold'),bg='gray20',fg='white')
riceLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

riceEntry=Entry(groceryFrame,font=('times new roman',20,'bold'),width=10,bd=5)
riceEntry.grid(row=0,column=1,pady=9,padx=10)
riceEntry.insert(0,'0')

oilLabel=Label(groceryFrame,text='Oil (Li)',font=('times new roman',17,'bold'),bg='gray20',fg='white')
oilLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

oilEntry=Entry(groceryFrame,font=('times new roman',20,'bold'),width=10,bd=5)
oilEntry.grid(row=1,column=1,pady=9,padx=10)
oilEntry.insert(0,'0')

daalLabel=Label(groceryFrame,text='Daal (kg)',font=('times new roman',17,'bold'),bg='gray20',fg='white')
daalLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

daalEntry=Entry(groceryFrame,font=('times new roman',20,'bold'),width=10,bd=5)
daalEntry.grid(row=2,column=1,pady=9,padx=10)
daalEntry.insert(0,'0')

wheatLabel=Label(groceryFrame,text='wheat (kg)',font=('times new roman',17,'bold'),bg='gray20',fg='white')
wheatLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')

wheatEntry=Entry(groceryFrame,font=('times new roman',20,'bold'),width=10,bd=5)
wheatEntry.grid(row=3,column=1,pady=9,padx=10)
wheatEntry.insert(0,'0')

sugarLabel=Label(groceryFrame,text='Sugar (kg)',font=('times new roman',17,'bold'),bg='gray20',fg='white')
sugarLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

sugarEntry=Entry(groceryFrame,font=('times new roman',20,'bold'),width=10,bd=5)
sugarEntry.grid(row=4,column=1,pady=9,padx=10)
sugarEntry.insert(0,'0')

teaLabel=Label(groceryFrame,text='Tea_powder(kg)',font=('times new roman',17,'bold'),bg='gray20',fg='white')
teaLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

teaEntry=Entry(groceryFrame,font=('times new roman',20,'bold'),width=10,bd=5)
teaEntry.grid(row=5,column=1,pady=9,padx=10)
teaEntry.insert(0,'0')


drinkFrame=LabelFrame(productsFrame,text='Cold Drinks',font=('times new roman',18,'bold'),
                          fg='gold',bd=8,relief=GROOVE,bg='gray20')
drinkFrame.grid(row=0,column=2)

maazaLabel=Label(drinkFrame,text='Maaza (Li)',font=('times new roman',17,'bold'),bg='gray20',fg='white')
maazaLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

maazaEntry=Entry(drinkFrame,font=('times new roman',20,'bold'),width=10,bd=5)
maazaEntry.grid(row=0,column=2,pady=9,padx=10)
maazaEntry.insert(0,'0')

papsiLabel=Label(drinkFrame,text='Pepsi (Li)',font=('times new roman',17,'bold'),bg='gray20',fg='white')
papsiLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

papsiEntry=Entry(drinkFrame,font=('times new roman',20,'bold'),width=10,bd=5)
papsiEntry.grid(row=1,column=2,pady=9,padx=10)
papsiEntry.insert(0,'0')

spriteLabel=Label(drinkFrame,text='Sprite (Li)',font=('times new roman',17,'bold'),bg='gray20',fg='white')
spriteLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

SpriteEntry=Entry(drinkFrame,font=('times new roman',20,'bold'),width=10,bd=5)
SpriteEntry.grid(row=2,column=2,pady=9,padx=10)
SpriteEntry.insert(0,'0')

dewLabel=Label(drinkFrame,text='Dew (Li)',font=('times new roman',17,'bold'),bg='gray20',fg='white')
dewLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')

dewEntry=Entry(drinkFrame,font=('times new roman',20,'bold'),width=10,bd=5)
dewEntry.grid(row=3,column=2,pady=9,padx=10)
dewEntry.insert(0,'0')

frootiLabel=Label(drinkFrame,text='Frooti (Li)',font=('times new roman',17,'bold'),bg='gray20',fg='white')
frootiLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

frootiEntry=Entry(drinkFrame,font=('times new roman',20,'bold'),width=10,bd=5)
frootiEntry.grid(row=4,column=2,pady=9,padx=10)
frootiEntry.insert(0,'0')

cocacolaLabel=Label(drinkFrame,text='Coca Cola (Li)',font=('times new roman',17,'bold'),bg='gray20',fg='white')
cocacolaLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

cocacolaEntry=Entry(drinkFrame,font=('times new roman',20,'bold'),width=10,bd=5)
cocacolaEntry.grid(row=5,column=2,pady=9,padx=10)
cocacolaEntry.insert(0,'0')

billframe=Frame(productsFrame,bd=8,relief=GROOVE)
billframe.grid(row=0,column=3,padx=10)

billareaLabel=Label(billframe,text='Label Area',font=('times new roman',17,'bold'))
billareaLabel.pack(fill=X)
scrollbar=Scrollbar(billframe,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)

textarea=Text( billframe,height=20,width=50,yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

billmenuFrame=LabelFrame(root,text='Bill menu',font=('times new roman',18,'bold'),
                          fg='gold',bd=8,relief=GROOVE,bg='gray20')
billmenuFrame.pack()

cosmeticpriceLabel=Label(billmenuFrame,text='Cosmetic Price',font=('times new roman',18,'bold'),bg='gray20',fg='white')
cosmeticpriceLabel.grid(row=0,column=0,pady=10,padx=15,sticky='w')

cosmeticpriceEntry=Entry(billmenuFrame,font=('times new roman',18,'bold'),width=10,bd=5)
cosmeticpriceEntry.grid(row=0,column=1,pady=10,padx=15)

grocerypriceLabel=Label(billmenuFrame,text='Grocery Price',font=('times new roman',18,'bold'),bg='gray20',fg='white')
grocerypriceLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

grocerypriceEntry=Entry(billmenuFrame,font=('times new roman',18,'bold'),width=10,bd=5)
grocerypriceEntry.grid(row=1,column=1,pady=9,padx=10)

drinkpriceLabel=Label(billmenuFrame,text='Drink Price',font=('times new roman',18,'bold'),bg='gray20',fg='white')
drinkpriceLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

drinkpriceEntry=Entry(billmenuFrame,font=('times new roman',18,'bold'),width=10,bd=5)
drinkpriceEntry.grid(row=2,column=1,pady=9,padx=10)

cosmetictaxLabel=Label(billmenuFrame,text='Cosmetic Tax',font=('times new roman',18,'bold'),bg='gray20',fg='white')
cosmetictaxLabel.grid(row=0,column=2,pady=9,padx=10,sticky='w')

cosmetictaxEntry=Entry(billmenuFrame,font=('times new roman',18,'bold'),width=10,bd=5)
cosmetictaxEntry.grid(row=0,column=3,pady=9,padx=10)

grocerytaxLabel=Label(billmenuFrame,text='Grocery Tax',font=('times new roman',18,'bold'),bg='gray20',fg='white')
grocerytaxLabel.grid(row=1,column=2,pady=9,padx=10,sticky='w')

groceryTaxEntry=Entry(billmenuFrame,font=('times new roman',18,'bold'),width=10,bd=5)
groceryTaxEntry.grid(row=1,column=3,pady=9,padx=10)

drinktaxLabel=Label(billmenuFrame,text='Drink tax',font=('times new roman',18,'bold'),bg='gray20',fg='white')
drinktaxLabel.grid(row=2,column=2,pady=9,padx=10,sticky='w')

drinktaxEntry=Entry(billmenuFrame,font=('times new roman',18,'bold'),width=10,bd=5)
drinktaxEntry.grid(row=2,column=3,pady=9,padx=10)

buttonFrame=Frame(billmenuFrame,bd=8,relief=GROOVE)
buttonFrame.grid(row=0,column=4,rowspan=3)

totalButton=Button(buttonFrame,text='Total',font=('arial',18,'bold'),bg='gray20',fg='white',bd=5,width=9,pady=10
                   ,command=total)
totalButton.grid(row=0,column=0,padx=4,pady=20)

billButton=Button(buttonFrame,text='Bill',font=('arial',18,'bold'),bg='gray20',fg='white',bd=5,width=9,pady=10
                  ,command=bill_area)
billButton.grid(row=0,column=1,padx=4,pady=20)

emailButton=Button(buttonFrame,text='Email',font=('arial',18,'bold'),bg='gray20',fg='white',bd=5,width=9,pady=10,command=send_email)
emailButton.grid(row=0,column=2,padx=4,pady=20)

printButton=Button(buttonFrame,text='Print',font=('arial',18,'bold'),bg='gray20',fg='white',bd=5,width=9,pady=10,command=print_bill)
printButton.grid(row=0,column=3,padx=4,pady=20)

clearButton=Button(buttonFrame,text='Clear',font=('arial',18,'bold'),bg='gray20',fg='white',bd=5,width=9,pady=10,command=clear)
clearButton.grid(row=0,column=4,padx=4,pady=20)
root.mainloop()