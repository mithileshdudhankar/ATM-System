
from tkinter import *
import tkinter as tk
from tkinter import messagebox 


root=tk.Tk()
root.title('ATM')
root.attributes('-fullscreen',True)
root.configure(bg='white')

heading_label = tk.Label(root,text='BANK OF NAGPUR',font=('times new roman',50),foreground='white',background='#f5007a')
heading_label.place(x=0,y=0,width=1400,height=100)

fot = tk.Label(root,background='#f5007a')
fot.place(x=0,y=730,width=1400,height=20)

global balance
balance = 500

# FOR ENGLISH 

def Withdrawl():
    def With():
        global balance
        balD11 = int(inpw.get())
        balance = balance - balD11
        messagebox.showinfo("showinfo",f"The amount is {balD11} successful withdrawl")
        rootW.withdraw()
        Balance()
    rootW=Tk()
    rootW.geometry('1300x1100')
    rootW.attributes('-fullscreen',True)
    rootW.configure(bg='white')
    
    heading_labelW = tk.Label(rootW,text='BANK OF NAGPUR',font=('times new roman',50),foreground='white',background='#f5007a')
    heading_labelW.place(x=0,y=0,width=1400,height=150)
        
    lbw= tk.Label(rootW,text="Enter the Withdrawl Amount",font=('times new roman',30),foreground='#f5007a',background='white')
    lbw.place(x=470,y=250)
        
    inpw=tk.Entry(rootW,borderwidth=8)
    inpw.place(x=480,y=350,height=40,width=400)
        
    sub1=tk.Button(rootW,text="Submit",font=('times new roman',15),fg='#f5007a',bg='white',command=With)
    sub1.place(x=630,y=450)

    fotE = tk.Label(rootW,background='#f5007a')
    fotE.place(x=0,y=730,width=1400,height=20)
    
def Deposit():
    global balance

    def Depo():
        global balance
        balD11 = int(inpd.get())
        balance = balance + balD11
        messagebox.showinfo("showinfo",f"The amount is {balD11} succesfully deposited")
        rootD.withdraw()
        Balance()

    rootD=Tk()
    rootD.geometry('1300x1100')
    rootD.attributes('-fullscreen',True)
    rootD.configure(bg='white')
    
    heading_labelD = tk.Label(rootD,text='BANK  OF NAGPUR',font=('times new roman',50),foreground='white',background='#f5007a')
    heading_labelD.place(x=0,y=0,width=1400,height=100)
        
    lbd= tk.Label(rootD,text="Enter the Deposit Amount",font=('times new roman',30),foreground='#f5007a',background='white')
    lbd.place(x=470,y=250)
        
    inpd=tk.Entry(rootD,borderwidth=8)
    inpd.place(x=480,y=350,height=40,width=400)
        
    sub2=tk.Button(rootD,text="Submit",font=('times new roman',15),fg='#f5007a',bg='white',command=Depo)
    sub2.place(x=630,y=450)

    fotm = tk.Label(rootD,background='#f5007a')
    fotm.place(x=0,y=730,width=1400,height=20)
    
def Balance():
    global balance
    rootB=Tk()
    rootB.attributes('-fullscreen',True)
    rootB.configure(bg='white')
    
    heading_labelB = tk.Label(rootB,text='BANK OF NAGPUR',font=('times new roman',50),foreground='white',background='#f5007a')
    heading_labelB.place(x=0,y=0,width=1400,height=100)
    
    lbb= tk.Label(rootB,text="Your Balance",font=('times new roman',30),foreground='#f5007a',background='white')
    lbb.place(x=570,y=250)

    lbb1= tk.Label(rootB,text=balance,font=('times new roman',30),bg='white')
    lbb1.place(x=470,y=350,height=40,width=400)

    bbtn= tk.Button(rootB,text="Main Menu",font=('times new roman',15),bg='white',fg='#f5007a',command=Main)
    bbtn.place(x=620,y=450)

    fotcP = tk.Label(rootB,background='#f5007a')
    fotcP.place(x=0,y=730,width=1400,height=20)
    
def Exit():
    msg = messagebox.askquestion("CONFIRM","ARE YOU SURE YOU WANT TO EXIT?", icon='warning')
    if msg == "yes":
        root.deiconify()   
    else:
        msg2=messagebox.showinfo("Okay","Okay")   
         
def Main():
    rootMain=Tk()
    rootMain.attributes('-fullscreen',True)
    rootMain.configure(bg='WHITE')
    
    heading_labelM = tk.Label(rootMain,text='BANK OF NAGUR',font=('times new roman',50),foreground='white',background='#f5007a')
    heading_labelM.place(x=0,y=0,width=1400,height=100)
    
    lb= tk.Label(rootMain,text="Please Make a Selection",font=('times new roman',30),foreground='#f5007a',background='white')
    lb.place(x=520,y=250)
    
    btn1=tk.Button(rootMain,text='Withdrawl',font=("times new roman",15),bg="#f5007a",fg='white',width=15,height=2,command=Withdrawl)
    btn1.place(x=200,y=380)
    
    btn2=tk.Button(rootMain,text='Deposite',font=("times new roman",15),bg="#f5007a",fg='white',width=15,height=2,command=Deposit)
    btn2.place(x=200,y=530)
    
    btn3=tk.Button(rootMain,text='Balance',font=("times new roman",15),bg="#f5007a",fg='white',width=15,height=2,command=Balance)
    btn3.place(x=940,y=380)
    
    btn4=tk.Button(rootMain,text='Exit',font=("times new roman",15),bg="#f5007a",fg='white',width=15,height=2,command=Exit)
    btn4.place(x=940,y=530)

    fotmW = tk.Label(rootMain,background='#f5007a')
    fotmW.place(x=0,y=730,width=1400,height=20)
        
def english():
    Main()
        
# FOR HINDI
  
def Withdrawlh():
    def With():
        global balance
        balD11 = int(inpw.get())
        balance = balance - balD11
        messagebox.showinfo("जानकारी",f"राशि {balD11} सफल निकासी है ")
        rootW.withdraw()
        Balanceh()


    rootW=Tk()
    rootW.geometry('1300x1100')
    rootW.attributes('-fullscreen',True)
    rootW.configure(bg='white')

    heading_labelWh = tk.Label(rootW,text='बैंक ऑफ़ नागपुर',font=('times new roman',50),foreground='white',background='#f5007a')
    heading_labelWh.place(x=0,y=0,width=1400,height=100)
       
    lbw= tk.Label(rootW,text="निकासी राशि दर्ज करें",font=('times new roman',30),foreground='#f5007a',background='white')
    lbw.place(x=530,y=250)
        
    inpw=tk.Entry(rootW,borderwidth=8)
    inpw.place(x=500,y=350,height=40,width=400)
        
    sub1=tk.Button(rootW,text="सबमिट ",font=('times new roman',15),fg='#f5007a',bg='white',command=With)
    sub1.place(x=650,y=450)
        
def Deposith():
    global balance

    def Depo():
        global balance
        balD11 = int(inpd.get())
        balance = balance + balD11
        messagebox.showinfo("जानकारी",f"राशि {balD11} सफलतापूर्वक जमा कर दी गई है")
        rootD.withdraw()
        Balanceh()

    rootD=Tk()
    rootD.geometry('1300x1100')
    rootD.attributes('-fullscreen',True)
    rootD.configure(bg='white')

    heading_labelDh = tk.Label(rootD,text='बैंक ऑफ़ नागपुर',font=('times new roman',50),foreground='white',background='#f5007a')
    heading_labelDh.place(x=0,y=0,width=1400,height=100)
    
    lbd= tk.Label(rootD,text="जमा राशि दर्ज करें",font=('times new roman',30),foreground='#f5007a',background='white')
    lbd.place(x=530,y=250)
        
    inpd=tk.Entry(rootD,borderwidth=8)
    inpd.place(x=500,y=350,height=40,width=400)
        
    sub2=tk.Button(rootD,text="सबमिट",font=('times new roman',15),fg='#f5007a',bg='white',command=Depo)
    sub2.place(x=650,y=450)

    fotmr = tk.Label(rootD,background='#f5007a')
    fotmr.place(x=0,y=730,width=1400,height=20)
    
def Balanceh():

    global balance
    rootB=Tk()
    rootB.attributes('-fullscreen',True)
    rootB.configure(bg='white')

    heading_labelBh = tk.Label(rootB,text='बैंक ऑफ़ नागपुर',font=('times new roman',50),foreground='white',background='#f5007a')
    heading_labelBh.place(x=0,y=0,width=1400,height=100)

    lbb= tk.Label(rootB,text="जमा धनराशि",font=('times new roman',30),foreground='#f5007a',background='white')
    lbb.place(x=570,y=250)

    lbb1= tk.Label(rootB,text=balance,font=('times new roman',30),bg='white')
    lbb1.place(x=470,y=350,height=40,width=400)

    bbtn= tk.Button(rootB,text="मुख्य मेन्यू",font=('times new roman',15),bg='white',fg='#f5007a',command=Mainh)
    bbtn.place(x=630,y=450)

    fotc = tk.Label(rootB,background='#f5007a')
    fotc.place(x=0,y=730,width=1400,height=20)
    
def Exith():
    msg = messagebox.askquestion("पुष्टि करें","क्या आप वाकई बाहर निकलना चाहते हैं?", icon='warning')
    if msg == "yes":
        root.deiconify()   
    else:
        msg2=messagebox.showinfo("ठीक है, ठीक है")
       

def Mainh():
 
    root.withdraw()
    rootMain=Tk()
    rootMain.attributes('-fullscreen',True)
    rootMain.configure(bg='white')

    heading_labelMh = tk.Label(rootMain,text='बैंक ऑफ़ नागपुर ',font=('times new roman',50),foreground='white',background='#f5007a')
    heading_labelMh.place(x=0,y=0,width=1400,height=100)
    
    lb= tk.Label(rootMain,text="कृपया चयन करें",font=('times new roman',30),foreground='#f5007a',background='white')
    lb.place(x=520,y=250)
    
    btn1=tk.Button(rootMain,text='निकासी',font=("times new roman",15),bg="#f5007a",fg='white',width=15,height=2,command=Withdrawlh)
    btn1.place(x=200,y=380)
    
    btn2=tk.Button(rootMain,text='जमा',font=("times new roman",15),bg="#f5007a",fg='white',width=15,height=2,command=Deposith)
    btn2.place(x=200,y=530)
    
    btn3=tk.Button(rootMain,text='शेष',font=("times new roman",15),bg="#f5007a",fg='white',width=15,height=2,command=Balanceh)
    btn3.place(x=940,y=380)
    
    btn4=tk.Button(rootMain,text='बाहर',font=("times new roman",15),bg="#f5007a",fg='white',width=15,height=2,command=Exith)
    btn4.place(x=940,y=530)

    fotm = tk.Label(rootMain,background='#f5007a')
    fotm.place(x=0,y=730,width=1400,height=20)
           
def hindi():
    Mainh()

# FOR MARATHI

def Withdrawlm():
        
    def With():
        global balance
        balD11 = int(inpw.get())
        balance = balance - balD11
        messagebox.showinfo("माहिती",f"रक्कम {balD11} यशस्वीपणे काढली आहे")
        rootW.withdraw()
        Balancem()

    rootW=Tk()
    rootW.geometry('1300x1100')
    rootW.attributes('-fullscreen',True)
    rootW.configure(bg='white')
    heading_labelWm = tk.Label(rootW,text='बैंक ऑफ़ नागपुर ',font=('times new roman',50),foreground='white',background='#f5007a')
    heading_labelWm.place(x=0,y=0,width=1300,height=150)
        
    lbw= tk.Label(rootW,text="पैसे काढण्याची रक्कम प्रविष्ट करा",font=('times new roman',30),foreground='#f5007a',background='white')
    lbw.place(x=450,y=250)
        
    inpw=tk.Entry(rootW,borderwidth=8)
    inpw.place(x=500,y=350,height=40,width=400)
        
    sub1=tk.Button(rootW,text="सबमिट",font=('times new roman',15),fg='#f5007a',bg='white',command=With)
    sub1.place(x=650,y=450)
    
    fotd = tk.Label(rootW,background='#f5007a')
    fotd.place(x=0,y=730,width=1400,height=20)

def Depositm():
    global balance

    def Depo():
        global balance
        balD11 = int(inpd.get())
        balance = balance + balD11
        messagebox.showinfo("माहिती",f"रक्कम {balD11} यशस्वीरित्या जमा केली आहे")
        rootD.withdraw()
        Balancem()

    rootD=Tk()
    rootD.geometry('1300x1100')
    rootD.attributes('-fullscreen',True)
    rootD.configure(bg='white')

    heading_labelDm = tk.Label(rootD,text='बैंक ऑफ़ नागपुर ',font=('times new roman',50),foreground='white',background='#f5007a')
    heading_labelDm.place(x=0,y=0,width=1400,height=100)
        
    lbd= tk.Label(rootD,text="रक्कम ठेव",font=('times new roman',30),fg='#f5007a',bg='white')
    lbd.place(x=600,y=250)
        
    inpd=tk.Entry(rootD,borderwidth=8)
    inpd.place(x=500,y=350,height=40,width=400)
        
    sub2=tk.Button(rootD,text="सबमिट",font=('times new roman',15),fg='#f5007a',bg='white',command=Depo)
    sub2.place(x=650,y=450)

    fotd = tk.Label(rootD,background='#f5007a')
    fotd.place(x=0,y=730,width=1400,height=20)
    
def Balancem():
    global balance
    rootB=Tk()
    rootB.attributes('-fullscreen',True)
    rootB.configure(bg='white')
    heading_labelBm = tk.Label(rootB,text='बैंक ऑफ़ नागपुर ',font=('times new roman',50),foreground='white',background='#f5007a')
    heading_labelBm.place(x=0,y=0,width=1400,height=100)
    
    lbb= tk.Label(rootB,text=" तुमच्या खात्यातील शिल्लक रक्कम ",font=('times new roman',30),fg='#f5007a',bg='white')
    lbb.place(x=430,y=300)
    lbb1= tk.Label(rootB,text=balance,font=('times new roman',30),bg='white')
    lbb1.place(x=650,y=380)
    bbtn= tk.Button(rootB,text="मुख्य मेनू",font=('times new roman',15),bg='white',fg='#f5007a',command=MainM)
    bbtn.place(x=647,y=450)
    
    fotb = tk.Label(rootB,background='#f5007a')
    fotb.place(x=0,y=730,width=1400,height=20)

def Exitm():
    msg = messagebox.askquestion("पुष्टी करा","तुम्हाला खात्री आहे की तुम्ही बाहेर पडू इच्छिता?", icon='warning')
    if msg == "yes":
        root.deiconify()   
    else:
        msg2=messagebox.showinfo("Okay","Okay")    
        
def MainM():
     
        root.withdraw()
        rootMain=Tk()
        rootMain.attributes('-fullscreen',True)
        rootMain.configure(bg='white')

        heading_labelMm = tk.Label(rootMain,text='बैंक ऑफ़ नागपुर ',font=('times new roman',50),foreground='white',background='#f5007a')
        heading_labelMm.place(x=0,y=0,width=1400,height=100)
        
        lb= tk.Label(rootMain,text="कृपया एक निवड करा",font=('times new roman',30),foreground='#f5007a',background='white')
        lb.place(x=520,y=250)
        
        btn1=tk.Button(rootMain,text='पैसे काढणे',font=("times new roman",15),bg="#f5007a",fg='white',width=15,height=2,command=Withdrawlm)
        btn1.place(x=200,y=380)
    
        btn2=tk.Button(rootMain,text='रकम जमा',font=("times new roman",15),bg="#f5007a",fg='white',width=15,height=2,command=Depositm)
        btn2.place(x=200,y=530)
    
        btn3=tk.Button(rootMain,text='शिल्लक',font=("times new roman",15),bg="#f5007a",fg='white',width=15,height=2,command=Balancem)
        btn3.place(x=940,y=380)
    
        btn4=tk.Button(rootMain,text='बाहेर ',font=("times new roman",15),bg="#f5007a",fg='white',width=15,height=2,command=Exitm)
        btn4.place(x=940,y=530)

        fotm = tk.Label(rootMain,background='#f5007a')
        fotm.place(x=0,y=730,width=1400,height=20)

def marathi():
    MainM()
 

# FOR LANGUAGE SELECTION 

def Second():
    rootSecond=Tk()
    rootSecond.attributes('-fullscreen',True)
    rootSecond.configure(bg='white')

    hes = tk.Label(rootSecond,text='BANK OF NAGPUR',font=('times new roman',50),foreground='white',background='#f5007a')
    hes.place(x=0,y=0,width=1400,height=100)
     
    lb= tk.Label(rootSecond,text="SELECT  THE  LANGUAGE",font=("times new roman",30),fg='#f5007a',bg="white")
    lb.place(x=450,y=300)
    
    btn1=tk.Button(rootSecond,text='English',font=("times new roman",15),bg="#f5007a",fg='white',width=15,height=2,command=english)
    btn1.place(x=320,y=500)

    btn2=tk.Button(rootSecond,text='Hindi',font=("times new roman",15),bg="#f5007a",fg='white',width=15,height=2,command=hindi)
    btn2.place(x=630,y=500)

    btn3=tk.Button(rootSecond,text='Marathi',font=("times new roman",15),bg="#f5007a",fg='white',width=15,height=2,command=marathi)
    btn3.place(x=950,y=500)
    
    fots = tk.Label(rootSecond,background='#f5007a')
    fots.place(x=0,y=730,width=1400,height=20)

    

# FOR TYPE OF ACCOUNT 

def First():
    root.withdraw()
    rootFirst=Tk()
    rootFirst.attributes('-fullscreen',True)
    rootFirst.configure(bg='white')
    
    hef = tk.Label(rootFirst,text='BANK OF NAGPUR',font=('times new roman',50),foreground='white',background='#f5007a')
    hef.place(x=0,y=0,width=1400,height=100)

    lb= tk.Label(rootFirst,text="SELECT TYPE OF ACCOUNT",font=('times new roman',30),bg='white',fg='#f5007a')
    lb.place(x=420,y=300)
    
    btn1=tk.Button(rootFirst,text='Saving',font=('times new roman',15),bg="#f5007a",fg='white',width=15,height=2,command=Second)
    btn1.place(x=430,y=500)
    
    btn2=tk.Button(rootFirst,text='Current',font=('times new roman',15),bg="#f5007a",fg='white',width=15,height=2,command=Second)
    btn2.place(x=750,y=500)

    fotf = tk.Label(rootFirst,background='#f5007a')
    fotf.place(x=0,y=730,width=1400,height=20)

    
#  FOR PASSWORD 
    
pz=tk.IntVar()

def AtmMain():
    
    pin=123
    getp=pz.get()
      
    if(getp==pin):
        First()
    else:
        messagebox.showerror("Incorrect Password","Please Enter Correct Password")
   
        
def Pin():
    
    lb= tk.Label(root,text="ENTER YOUR PIN",font=('times new roman',30),bg='white',fg='#f5007a')
    lb.place(x=480,y=300)

    
    inp=tk.Entry(root,textvariable=pz,borderwidth=8)
    inp.place(x=450,y=400,height=40,width=400)
    inp.configure(fg='black',show='*')
    sub=tk.Button(root,text="Enter",font=('times new roman',20),bg="#f5007a",fg="white",command=AtmMain)
    sub.place(x=580,y=480,height=40,width=150)

Pin()
root.mainloop()