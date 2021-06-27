import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

dbcon = mysql.connector.connect(host='localhost',
        user='vvcupdateuser',
        password='password',
        database='vvc')

dbselect = dbcon.cursor(dictionary=True)
dbins = dbcon.cursor()

root = Tk()
root.title("Update VVC Data")

myusername = StringVar(value='')
myfullname = StringVar(value='')
myoffice = StringVar(value='')
myorg = StringVar(value='')
myphone = StringVar(value='')
mymobile = StringVar(value='')
myemail = StringVar(value='')
mywebsite = StringVar(value='')
myaddress = StringVar(value='')
res_username = StringVar(value='')
res_fullname = StringVar(value='')
res_office = StringVar(value='')
res_org = StringVar(value='')
res_phone = StringVar(value='')
res_mobile = StringVar(value='')
res_email = StringVar(value='')
res_website = StringVar(value='')
res_address = StringVar(value='')
res_rownum = StringVar(value='')

def select():
    query = ("SELECT * FROM report WHERE myusername = %s")
    dbselect.execute(query,(myusername.get(),))
    res = dbselect.fetchall()
    res_username.set(res[0]['myusername'].decode("utf-8"))
    res_fullname.set(res[0]['myfullname'].decode("utf-8"))
    res_office.set(res[0]['myoffice'].decode("utf-8"))
    res_org.set(res[0]['myorg'].decode("utf-8"))
    res_phone.set(res[0]['myphone'].decode("utf-8"))
    res_mobile.set(res[0]['mymobile'].decode("utf-8"))
    res_email.set(res[0]['myemail'].decode("utf-8"))
    res_website.set(res[0]['mywebsite'].decode("utf-8"))
    res_address.set(res[0]['myaddress'].decode("utf-8"))
    
#

def insert():
    
    query = ("INSERT INTO report (runindex, myusername, myfullname, myoffice, myorg, myphone, mymobile, \
        myemail, mywebsite, myaddress) VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
    vals = (myusername.get(), myfullname.get(), myoffice.get(), myorg.get(), myphone.get(), mymobile.get(),
    myemail.get(), mywebsite.get(), myaddress.get())
    dbins.execute(query,vals)

    dbcon.commit()

    res_rownum.set(dbins.rowcount)
#

def update():
    
    args = dict()
    vals = []

    if myfullname.get() != '':
        args['myfullname'] = myfullname.get()
    #

    if myoffice.get() != '':
        args['myoffice'] = myoffice.get()
    #

    if myorg.get() != '':
        args['myorg'] = myorg.get()
    #

    if myphone.get() != '':
        args['myphone'] = myphone.get()
    #

    if mymobile.get() != '':
        args['mymobile'] = mymobile.get()
    #

    if myemail.get() != '':
        args['myemail'] = myemail.get()
    #

    if mywebsite.get() != '':
        args['mywebsite'] = mywebsite.get()
    #

    if myaddress.get() != '':
        args['myaddress'] = myaddress.get()
    #

    query = "UPDATE report SET "
    
    for key in args:
        query += key + '= %s, '
        vals.append(args[key])
    #

    query = query[:len(query)-2]

    #print(query)

    query += " WHERE myusername = %s"
 
    vals.append(myusername.get())

    dbins.execute(query,vals)

    dbcon.commit()

    res_rownum.set(dbins.rowcount)
#

def deleterec():
    ans = messagebox.askokcancel(title = "Delete", message = "Delete User?")
    
    if ans == True:
        query = "DELETE FROM report WHERE myusername = %s"
        
        vals = myusername.get()

        dbins.execute(query,(vals,))

        dbcon.commit()

        res_rownum.set(dbins.rowcount)
    else:
        pass
    #
#

def clearall():
    myusername.set('')
    myfullname.set('')
    myoffice.set('')
    myorg.set('')
    myphone.set('')
    mymobile.set('')
    myemail.set('')
    mywebsite.set('')
    myaddress.set('')
#

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(mainframe, text="Query Name").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Full Name").grid(column=1, row=2, sticky=W)
ttk.Label(mainframe, text="Occupation").grid(column=1, row=3, sticky=W)
ttk.Label(mainframe, text="Organization").grid(column=1, row=4, sticky=W)
ttk.Label(mainframe, text="Phone").grid(column=1, row=5, sticky=W)
ttk.Label(mainframe, text="Cellphone").grid(column=1, row=6, sticky=W)
ttk.Label(mainframe, text="Email").grid(column=1, row=7, sticky=W)
ttk.Label(mainframe, text="Website").grid(column=1, row=8, sticky=W)
ttk.Label(mainframe, text="Address").grid(column=1, row=9, sticky=W)

ttk.Label(mainframe, textvariable=res_username).grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, textvariable=res_fullname).grid(column=3, row=2, sticky=W)
ttk.Label(mainframe, textvariable=res_office).grid(column=3, row=3, sticky=W)
ttk.Label(mainframe, textvariable=res_org).grid(column=3, row=4, sticky=W)
ttk.Label(mainframe, textvariable=res_phone).grid(column=3, row=5, sticky=W)
ttk.Label(mainframe, textvariable=res_mobile).grid(column=3, row=6, sticky=W)
ttk.Label(mainframe, textvariable=res_email).grid(column=3, row=7, sticky=W)
ttk.Label(mainframe, textvariable=res_website).grid(column=3, row=8, sticky=W)
ttk.Label(mainframe, textvariable=res_address).grid(column=3, row=9, sticky=W)

ttk.Entry(mainframe, width=7, textvariable=myusername).grid(column=2, row=1, sticky=(W, E))
ttk.Entry(mainframe, width=20, textvariable=myfullname).grid(column=2, row=2, sticky=(W, E))
ttk.Entry(mainframe, width=7, textvariable=myoffice).grid(column=2, row=3, sticky=(W, E))
ttk.Entry(mainframe, width=10, textvariable=myorg).grid(column=2, row=4, sticky=(W, E))
ttk.Entry(mainframe, width=10, textvariable=myphone).grid(column=2, row=5, sticky=(W, E))
ttk.Entry(mainframe, width=10, textvariable=mymobile).grid(column=2, row=6, sticky=(W, E))
ttk.Entry(mainframe, width=20, textvariable=myemail).grid(column=2, row=7, sticky=(W, E))
ttk.Entry(mainframe, width=10, textvariable=mywebsite).grid(column=2, row=8, sticky=(W, E))
ttk.Entry(mainframe, width=30, textvariable=myaddress).grid(column=2, row=9, sticky=(W, E))

ttk.Button(mainframe, text="Select", command=select).grid(column=4, row=1, sticky=W)
ttk.Button(mainframe, text="Insert", command=insert).grid(column=4, row=2, sticky=W)
ttk.Button(mainframe, text="Update", command=update).grid(column=4, row=3, sticky=W)
ttk.Button(mainframe, text="Delete", command=deleterec).grid(column=4, row=4, sticky=W)
ttk.Button(mainframe, text="Clear", command=clearall).grid(column=4, row=5, sticky=W)

ttk.Label(mainframe, textvariable=res_rownum).grid(column=4, row=6, sticky=E)

root.mainloop()
dbcon.close()
