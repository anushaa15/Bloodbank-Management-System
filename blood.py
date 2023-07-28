

from tkinter import *
from tkinter import ttk
import tkinter as tk
from sqlalchemy import create_engine

from cs50 import SQL

my_conn = create_engine("sqlite:///bloodbank.db")
window_size = '700x500+350+150'

db=SQL("sqlite:///bloodbank.db")
table = ""
def view_data():

    def view_donor():
        view_DWindow=Tk()
        view_DWindow.geometry(window_size)
        view_DWindow.title("INSTRUCTION")
        view_DWindow.config(bg = "#000000")
        img= PhotoImage(file="photo10.gif", master= view_DWindow)
        img_label= Label(view_DWindow,image=img)
        lable3=Label(view_DWindow, text = "DONOR DATA" , bg="#ff0022", fg = "white", font =("calbiri", 25))
        lable3.place(x=250, y=10)
        img_label.place(x=0, y=0)
        trv = ttk.Treeview(view_DWindow, selectmode ='browse')
        trv.grid(row=1,column=1,padx=20,pady=80)
        trv["columns"] = ("1", "2", "3","4","5","6", "7","8","9")
        trv['show'] = 'headings'
        trv.column("1", width = 30, anchor ='c')
        trv.column("2", width = 70, anchor ='c')
        trv.column("3", width = 30, anchor ='c')
        trv.column("4", width = 60, anchor ='c')
        trv.column("5", width = 80, anchor ='c')
        trv.column("6", width = 100, anchor ='c')
        trv.column("7", width = 90, anchor ='c')
        trv.column("8", width = 100, anchor ='c')
        trv.column("9", width = 100, anchor ='c')


        trv.heading("1", text ="id")
        trv.heading("2", text ="Name")
        trv.heading("3", text ="age")
        trv.heading("4", text ="gender")  
        trv.heading("5", text ="blood_id")
        trv.heading("6", text ="haemoglobin")
        trv.heading("7", text ="donation_date")
        trv.heading("8", text ="phone_no")
        trv.heading("9", text ="is_eligible")


        r_set=my_conn.execute('SELECT * from donor LIMIT 0,11')
        for dt in r_set: 
            trv.insert("", 'end',iid=dt[0], text=dt[0],
            values =(dt[0],dt[1],dt[2],dt[3],dt[4], dt[5],dt[6], dt[7], dt[8]))
        view_DWindow.mainloop()

        print("view donor clicked")

    def view_patient():
        view_PWindow=Tk()
        view_PWindow.geometry(window_size)
        view_PWindow.title("INSTRUCTION")
        view_PWindow.config(bg = "#000000")
        img= PhotoImage(file="photo10.gif", master= view_PWindow)
        img_label= Label(view_PWindow,image=img)
        img_label.place(x=0, y=0)
        lable3=Label(view_PWindow, text = "PATIENT DATA" , bg="#ff0022", fg = "white", font =("calbiri", 25))
        lable3.place(x=250, y=10)
        trv = ttk.Treeview(view_PWindow, selectmode ='browse')
        trv.grid(row=1,column=1,padx=20,pady=80)
        trv["columns"] = ("1", "2", "3","4","5","6", "7","8","9")
        trv['show'] = 'headings'
        trv.column("1", width = 30, anchor ='c')
        trv.column("2", width = 60, anchor ='c')
        trv.column("3", width = 60, anchor ='c')
        trv.column("4", width = 80, anchor ='c')
        trv.column("5", width = 80, anchor ='c')
        trv.column("6", width = 80, anchor ='c')
        trv.column("7", width = 120, anchor ='c')
        trv.column("8", width = 80, anchor ='c')
        trv.column("9", width = 80, anchor ='c')

        trv.heading("1", text ="id")
        trv.heading("2", text ="Name")
        trv.heading("3", text ="age")
        trv.heading("4", text ="gender")  
        trv.heading("5", text ="blood_id")
        trv.heading("6", text ="haemoglobin")
        trv.heading("7", text ="registration_date")
        trv.heading("8", text ="phone_no")
        trv.heading("9", text ="address")


        r_set=my_conn.execute('''SELECT * from patient LIMIT 0,10''')
        for dt in r_set: 
            trv.insert("", 'end',iid=dt[0], text=dt[0],
            values =(dt[0],dt[1],dt[2],dt[3],dt[4], dt[5],dt[6], dt[7], dt[8]))

        view_PWindow.mainloop()
        print("view patient clicked")


    def view_bloodBank():
        view_BloodBankWindow=Tk()
        view_BloodBankWindow.geometry(window_size)
        view_BloodBankWindow.title("INSTRUCTION")
        view_BloodBankWindow.config(bg = "#000000")
        img= PhotoImage(file="photo10.gif", master= view_BloodBankWindow)
        img_label= Label(view_BloodBankWindow,image=img)
        img_label.place(x=0, y=0)
        lable3=Label(view_BloodBankWindow, text = "BLOOD BANK  DATA" , bg="#ff0022", fg = "white", font =("calbiri", 25))
        lable3.place(x=220, y=10)

        trv = ttk.Treeview(view_BloodBankWindow, selectmode ='browse')
        trv.grid(row=1,column=1,padx=240,pady=80)
        trv["columns"] = ("1", "2", "3","4")
        trv['show'] = 'headings'
        trv.column("1", width = 30, anchor ='c')
        trv.column("2", width = 80, anchor ='c')
        trv.column("3", width = 80, anchor ='c')
        trv.column("4", width = 80, anchor ='c')
    

        trv.heading("1", text ="id")
        trv.heading("2", text ="Name")
        trv.heading("3", text ="Quantity")
        trv.heading("4", text ="Cost")  
 
        r_set=my_conn.execute('''SELECT * from blood_bank LIMIT 0,10''')
        for dt in r_set: 
            trv.insert("", 'end',iid=dt[0], text=dt[0],
            values =(dt[0],dt[1],dt[2],dt[3]))

        view_BloodBankWindow.mainloop()
        print("view bloodbank clicked")




    def view_campSchedule():
        view_campScheduleWindow=Tk()
        view_campScheduleWindow.geometry(window_size)
        view_campScheduleWindow.title("INSTRUCTION")
        view_campScheduleWindow.config(bg = "#000000")
        img= PhotoImage(file="photo10.gif", master= view_campScheduleWindow)
        img_label= Label(view_campScheduleWindow,image=img)
        img_label.place(x=0, y=0)
        lable3=Label(view_campScheduleWindow, text = "CAMP SCHEDULE" , bg="#ff0022", fg = "white", font =("calbiri", 25))
        lable3.place(x=220, y=10)
        trv = ttk.Treeview(view_campScheduleWindow, selectmode ='browse')
        trv.grid(row=1,column=1,padx=80,pady=80)
        trv["columns"] = ("1", "2", "3","4","5")
        trv['show'] = 'headings'
        trv.column("1", width = 100, anchor ='c')
        trv.column("2", width = 100, anchor ='c')
        trv.column("3", width = 120, anchor ='c')
        trv.column("4", width = 100, anchor ='c')
        trv.column("5", width = 100, anchor ='c')


        trv.heading("1", text ="camp_id")
        trv.heading("2", text ="schedule_date")
        trv.heading("3", text ="no_of_donation")
        trv.heading("4", text ="head_id")  
        trv.heading("5", text ="location")



        r_set=my_conn.execute('''SELECT * from camp_schedule LIMIT 0,10''')
        for dt in r_set: 
            trv.insert("", 'end',iid=dt[0], text=dt[0],
            values =(dt[0],dt[1],dt[2],dt[3],dt[4]))

        view_campScheduleWindow.mainloop()
        print("view campschedule clicked")


    def view_demand():
        view_DemandWindow=Tk()
        view_DemandWindow.geometry(window_size)
        view_DemandWindow.title("INSTRUCTION")
        view_DemandWindow.config(bg = "#000000")
        img= PhotoImage(file="photo10.gif", master= view_DemandWindow)
        img_label= Label(view_DemandWindow,image=img)
        img_label.place(x=0, y=0)
        lable3=Label(view_DemandWindow, text = "DEMAND" , bg="#ff0022", fg = "white", font =("calbiri", 25))
        lable3.place(x=270, y=10)
        
        trv = ttk.Treeview(view_DemandWindow, selectmode ='browse')
        trv.grid(row=1,column=1,padx=220,pady=80)
        trv["columns"] = ("1", "2", "3",)
        trv['show'] = 'headings'
        trv.column("1", width = 80, anchor ='c')
        trv.column("2", width = 80, anchor ='c')
        trv.column("3", width = 80, anchor ='c')

    

        trv.heading("1", text ="blood_id")
        trv.heading("2", text ="hospital_id")
        trv.heading("3", text ="qty")
 
 
        r_set=my_conn.execute('''SELECT * from demand LIMIT 0,10''')
        for dt in r_set: 
            trv.insert("", 'end',iid=dt[0], text=dt[0],
            values =(dt[0],dt[1],dt[2]))

        view_DemandWindow.mainloop()
        print("view demand clicked")


    def view_collectedBlood():
        view_collectedBloodWindow=Tk()
        view_collectedBloodWindow.geometry(window_size)
        view_collectedBloodWindow.title("INSTRUCTION")
        view_collectedBloodWindow.config(bg = "#000000")
        img= PhotoImage(file="photo10.gif", master= view_collectedBloodWindow)
        img_label= Label(view_collectedBloodWindow,image=img)
        img_label.place(x=0, y=0)
        lable3=Label(view_collectedBloodWindow, text = "COLLECTED BLOOD DATA" , bg="#ff0022", fg = "white", font =("calbiri", 25))
        lable3.place(x=160, y=10)

        trv = ttk.Treeview(view_collectedBloodWindow, selectmode ='browse')
        trv.grid(row=1,column=1,padx=220,pady=80)
        trv["columns"] = ("1", "2", "3",)
        trv['show'] = 'headings'
        trv.column("1", width = 80, anchor ='c')
        trv.column("2", width = 80, anchor ='c')
        trv.column("3", width = 80, anchor ='c')

    

        trv.heading("1", text ="blood_id")
        trv.heading("2", text ="camp_id")
        trv.heading("3", text ="qty")
 
 
        r_set=my_conn.execute('''SELECT * from blood_collected LIMIT 0,10''')
        for dt in r_set: 
            trv.insert("", 'end',iid=dt[0], text=dt[0],
            values =(dt[0],dt[1],dt[2]))

        view_collectedBloodWindow.mainloop()
        print("view collectedblood  clicked")
  

    def view_staff():
        view_staffWindow=Tk()
        view_staffWindow.geometry(window_size)
        view_staffWindow.title("INSTRUCTION")
        view_staffWindow.config(bg = "#000000")
        img= PhotoImage(file="photo10.gif", master= view_staffWindow)
        img_label= Label(view_staffWindow,image=img)
        img_label.place(x=0, y=0)
        lable3=Label(view_staffWindow, text = " STAFF DATA" , bg="#ff0022", fg = "white", font =("calbiri", 25))
        lable3.place(x=220, y=10)
        trv = ttk.Treeview(view_staffWindow, selectmode ='browse')
        trv.grid(row=1,column=1,padx=80,pady=80)
        trv["columns"] = ("1", "2", "3","4","5", "6","7")
        trv['show'] = 'headings'
        trv.column("1", width = 40, anchor ='c')
        trv.column("2", width = 60, anchor ='c')
        trv.column("3", width = 60, anchor ='c')
        trv.column("4", width = 120, anchor ='c')
        trv.column("5", width = 40, anchor ='c')
        trv.column("6", width = 120, anchor ='c')
        trv.column("7", width = 80, anchor ='c')


        trv.heading("1", text ="id")
        trv.heading("2", text ="name")
        trv.heading("3", text ="age")
        trv.heading("4", text ="qualification")  
        trv.heading("5", text ="post")
        trv.heading("6", text ="hospital_id")
        trv.heading("7", text ="gender")



        r_set=my_conn.execute('''SELECT * from staff LIMIT 0,10''')
        for dt in r_set: 
            trv.insert("", 'end',iid=dt[0], text=dt[0],
            values =(dt[0],dt[1],dt[2],dt[3],dt[4], dt[5], dt[6]))

        view_staffWindow.mainloop()
        print("view staff clicked")
        
        


    def view_hospital():
        view_hospitalWindow=Tk()
        view_hospitalWindow.geometry(window_size)
        view_hospitalWindow.title("INSTRUCTION")
        view_hospitalWindow.config(bg = "#000000")
        img= PhotoImage(file="photo10.gif", master= view_hospitalWindow)
        img_label= Label(view_hospitalWindow,image=img)
        img_label.place(x=0, y=0)
        lable3=Label(view_hospitalWindow, text = " HOSPITAL DATA" , bg="#ff0022", fg = "white", font =("calbiri", 25))
        lable3.place(x=220, y=10)
        trv = ttk.Treeview(view_hospitalWindow, selectmode ='browse')
        trv.grid(row=1,column=1,padx=180,pady=80)
        trv["columns"] = ("1", "2", "3","4")
        trv['show'] = 'headings'
        trv.column("1", width = 30, anchor ='c')
        trv.column("2", width = 80, anchor ='c')
        trv.column("3", width = 120, anchor ='c')
        trv.column("4", width = 140, anchor ='c')
    

        trv.heading("1", text ="id")
        trv.heading("2", text ="Name")
        trv.heading("3", text ="location")
        trv.heading("4", text ="doctor_id")  
 
        r_set=my_conn.execute('''SELECT * from hospital LIMIT 0,10''')
        for dt in r_set: 
            trv.insert("", 'end',iid=dt[0], text=dt[0],
            values =(dt[0],dt[1],dt[2],dt[3]))

        view_hospitalWindow.mainloop()
        print("view bloodbank clicked")

    


    
    view_window=Tk()
    view_window.geometry(window_size)
    view_window.title("INSTRUCTION")
    view_window.config(bg = "#000000")
    img= PhotoImage(file="photo02.gif", master= view_window)
    img_label= Label(view_window,image=img)
    img_label.place(x=0, y=0)
    lable2=Label(view_window, text = "Please choose any one option " , bg="#ff0022", fg = "white", font =("calbiri", 25))
    lable2.place(x=120, y=10)
    button3=Button(view_window, text = "DONOR", bg="#5B2C6F", fg = "white", font =("calbiri", 15), command=view_donor)
    button3.config(height = 2, width=18)
    button3.place(x=100, y=100)

    button4=Button(view_window, text = "PATIENT", bg="#5B2C6F", fg = "white", font =("calbiri", 15),  command=view_patient)
    button4.config(height = 2, width=18)
    button4.place(x=400, y=100)
 
    button5=Button(view_window, text = "BLOOD BANK", bg="#5B2C6F", fg = "white", font =("calbiri", 15), command=view_bloodBank)
    button5.config(height = 2, width=18)
    button5.place(x=100, y=200)

    button6=Button(view_window, text = "CAMP SCHEDULE", bg="#5B2C6F", fg = "white", font =("calbiri", 15), command= view_campSchedule)
    button6.config(height = 2, width=18)
    button6.place(x=400, y=200)

    button7=Button(view_window, text = "DEMAND", bg="#5B2C6F", fg = "white", font =("calbiri", 15), command=view_demand)
    button7.config(height = 2, width=18)
    button7.place(x=100, y=300)

    button8=Button(view_window, text = "COLLECTED BLOOD", bg="#5B2C6F", fg = "white", font =("calbiri", 15), command=view_collectedBlood)
    button8.config(height = 2, width=18)
    button8.place(x=400, y=300)

    button9=Button(view_window, text = "STAFF", bg="#5B2C6F", fg = "white", font =("calbiri", 15), command=view_staff)
    button9.config(height = 2, width=18)
    button9.place(x=100, y=400)

    button10=Button(view_window, text = "HOSPITAL", bg="#5B2C6F", fg = "white", font =("calbiri", 15), command=view_hospital)
    button10.config(height = 2, width=18)
    button10.place(x=400, y=400)
    view_window.mainloop()
    

def edit_data():

    def edit_donor():
        global table
        table = "donor"

        def add_donor():


            def add_DData():

                # try:
                   
                    donor_id= id_dat.get()
                    name = name_dat.get()
                    age = age_dat.get()
                    gender= gender_dat.get()
                    haemoglobin = haemoglobin_dat.get()
                   
                    disease = diseaseName_dat.get()
                    d_id = db.execute(f"SELECT * from disease where disease_name in (?)", disease)
                    print('here')
                    

                    

                    donationDate = donationDate_dat.get()
                    phone = phoneNo_dat.get()
                    blood = b_g_dat.get()

                    res = db.execute(f"select blood_id from blood_bank where blood_group is ?", blood)

                    blood_id = res[0]['blood_id']               
                    eligible = "yes"
                    if int(haemoglobin) < 13:
                        eligible = "no"
                    db.execute(f"INSERT INTO donor VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)",  donor_id, name, age, gender, blood_id, haemoglobin, donationDate, phone, eligible)
                    print("DONE")
                    if  not d_id:
                        dis = db.execute("INSERT INTO disease (disease_name) VALUES (?)",disease) 
                        print(f"INSERT INTO sick_donor VALUES (?, ?)", donor_id, dis)
                        db.execute("INSERT INTO sick_donor VALUES (?, ?)", donor_id, dis)
                        print("in1")
                    else:
                        print("in2")
                        db.execute("INSERT INTO sick_donor VALUES (?, ?)", donor_id, d_id[0]['id'])



                # except:
                #     print("Invalid data")
                

            edit_addDWindow=Tk()
            edit_addDWindow.geometry(window_size)
            edit_addDWindow.title("BLOOD BANK MANAGEMENT")
            edit_addDWindow.config(bg = "#000000")

            img= PhotoImage(file="photo10.gif", master= edit_addDWindow)
            img_label= Label(edit_addDWindow,image=img)
            img_label.place(x=0, y=0)

            label2 = Label(edit_addDWindow , text = "Please fill the following credentials." , bg = "#CCCCFF" , fg = "black" , font = ("Bookman Old Style" , 20))
            label2.place(x= 120 , y = 20)

            label3 = Label(edit_addDWindow , text = "id" , bg = "#003366" , fg = "white" , font = ("Bookman Old Style" , 15))
            label3.place(x = 180, y = 80)

            id_dat = Entry(edit_addDWindow)                                           
            id_dat.place(x = 400 , y = 90)  

            label4 = Label(edit_addDWindow , text = "name " , bg = "#003366" , fg = "white" , font = ("Bookman Old Style" , 15))
            label4.place(x = 180, y = 120)

            name_dat = Entry(edit_addDWindow)                                           
            name_dat.place(x = 400 , y = 125)

            label5 = Label(edit_addDWindow , text = "age " , bg = "#003366" , fg = "white" , font = ("Bookman Old Style" , 15))
            label5.place(x = 180, y = 160)

            age_dat = Entry(edit_addDWindow)                                           
            age_dat.place(x = 400 , y = 170) 

            label6 = Label(edit_addDWindow , text = "gender " , bg = "#003366" , fg = "white" , font = ("Bookman Old Style" , 15))
            label6.place(x = 180, y = 200)

            gender_dat = Entry(edit_addDWindow)                                           
            gender_dat.place(x = 400 , y = 205) 

            label7 = Label(edit_addDWindow , text = "haemoglobin " , bg = "#003366" , fg = "white" , font = ("Bookman Old Style" , 15))
            label7.place(x = 180, y = 240)

            haemoglobin_dat = Entry(edit_addDWindow)                                           
            haemoglobin_dat.place(x = 400 , y = 240) 

            label8 = Label(edit_addDWindow , text = "donation date" , bg = "#003366" , fg = "white" , font = ("Bookman Old Style" , 15))
            label8.place(x = 180, y = 280)

            donationDate_dat = Entry(edit_addDWindow)                                           
            donationDate_dat.place(x = 400 , y = 280) 

            label9 = Label(edit_addDWindow , text = "phone_no" , bg = "#003366" , fg = "white" , font = ("Bookman Old Style" , 15))
            label9.place(x = 180, y = 320)

            phoneNo_dat = Entry(edit_addDWindow)                                           
            phoneNo_dat.place(x = 400 , y = 320) 

            labe20 = Label(edit_addDWindow , text = "blood_group" , bg = "#003366" , fg = "white" , font = ("Bookman Old Style" , 15))
            labe20.place(x = 180, y = 360)

            b_g_dat = Entry(edit_addDWindow)                                           
            b_g_dat.place(x = 400 , y = 360) 

            labe21 = Label(edit_addDWindow , text = "Disease Name" , bg = "#003366" , fg = "white" , font = ("Bookman Old Style" , 15))
            labe21.place(x = 180, y = 400)

            diseaseName_dat = Entry(edit_addDWindow)                                           
            diseaseName_dat.place(x = 400 , y = 400) 


            submit = Button(edit_addDWindow , text = "OK" , bg = "#99FFFF" , fg = "blue" , font = ("calibri" , 10), command=add_DData)
            submit.config(width = 10 , height = 1)
            submit.place(x=330, y=430)
                    
            edit_addDWindow.mainloop()


        def delete_donor():

            def delete_DData():
                id = id_dat.get()
                
                db.execute(f"DELETE FROM donor WHERE id IN (?)", id)
            
            edit_deleteDWindow=Tk()
            edit_deleteDWindow.geometry(window_size)
            edit_deleteDWindow.title("BLOOD BANK MANAGEMENT")
            edit_deleteDWindow.config(bg = "#000000")
            img= PhotoImage(file="photo10.gif", master= edit_deleteDWindow)
            img_label= Label(edit_deleteDWindow,image=img)
            img_label.place(x=0, y=0)
            label2 = Label(edit_deleteDWindow , text = "Please fill the id to delete the data" , bg = "#CCCCFF" , fg = "black" , font = ("Bookman Old Style" , 20))
            label2.place(x= 120 , y = 20)

            label3 = Label(edit_deleteDWindow , text = "id" , bg = "#003366" , fg = "white" , font = ("Bookman Old Style" , 15))
            label3.place(x = 300, y = 80)

            id_dat = Entry(edit_deleteDWindow)                                           
            id_dat.place(x = 350 , y = 80)  

            submit = Button(edit_deleteDWindow , text = "OK" , bg = "#99FFFF" , fg = "blue" , font = ("calibri" , 10), command=delete_DData)
            submit.config(width = 10 , height = 1)
            submit.place(x=330, y=150)
                    
            edit_deleteDWindow.mainloop()




        edit_DWindow=Tk()
        edit_DWindow.geometry(window_size)
        edit_DWindow.title("BLOOD BANK MANAGEMENT")
        edit_DWindow.config(bg = "#000000")
        img= PhotoImage(file="photo09.gif", master= edit_DWindow)
        img_label= Label(edit_DWindow,image=img)
        img_label.place(x=0, y=0)
        lable2=Label(edit_DWindow, text = "DONOR DATA" , bg="#3B001D", fg = "white", font =("calbiri", 25))
        lable2.place(x=210, y=10)
        button19=Button(edit_DWindow, text = "ADD DATA", bg="#0A003B", fg = "white", font =("calbiri", 15), command=add_donor)
        button19.config(height = 2, width=18)
        button19.place(x=220, y=150)


        button21=Button(edit_DWindow, text = "DELETE DATA", bg="#0A003B", fg = "white", font =("calbiri", 15), command=delete_donor)
        button21.config(height = 2, width=18)
        button21.place(x=220, y=250)
        edit_DWindow.mainloop()


    def edit_patient():

        def add_patient():

            def add_PData():
                try:
                    patient_id= id_dat.get()
                    name = name_dat.get()
                    age = age_dat.get()
                    gender= gender_dat.get()
                    haemoglobin = haemoglobin_dat.get()

                    disease = diseaseName_dat.get()


                    regis_Date = regis_Date_dat.get()
                    phone = phoneNo_dat.get()
                    add = add_dat.get()
                    blood = b_g_dat.get()

                    res = db.execute(f"select blood_id from blood_bank where blood_group is ?", blood)

                    blood_id = res[0]['blood_id']               
                    db.execute(f"INSERT INTO patient VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)",  patient_id, name, age, gender, blood_id, haemoglobin, regis_Date, phone, add)
                    
                    d_id = db.execute(f"SELECT * from disease where disease_name in (?)", disease)

                    if  not d_id:
                        dis = db.execute("INSERT INTO disease (disease_name) VALUES (?)",disease) 
                        db.execute("INSERT INTO sick_patient VALUES (?, ?)", patient_id, dis)
                    else:
                        db.execute("INSERT INTO sick_patient VALUES (?, ?)", patient_id, d_id[0]['id'])
                except:
                    "Invalid data"

            edit_addPWindow=Tk()
            edit_addPWindow.geometry(window_size)
            edit_addPWindow.title("BLOOD BANK MANAGEMENT")
            edit_addPWindow.config(bg = "#000000")
            img= PhotoImage(file="photo10.gif", master= edit_addPWindow)
            img_label= Label(edit_addPWindow,image=img)
            img_label.place(x=0, y=0)

            label2 = Label(edit_addPWindow , text = "Please fill the following credentials." , bg = "#CCCCFF" , fg = "black" , font = ("Bookman Old Style" , 20))
            label2.place(x= 120 , y = 20)

            label3 = Label(edit_addPWindow , text = "id" , bg = "#003366" , fg = "white" , font = ("Bookman Old Style" , 15))
            label3.place(x = 180, y = 80)

            id_dat = Entry(edit_addPWindow)                                           
            id_dat.place(x = 400 , y = 80)  

            label4 = Label(edit_addPWindow , text = "name " , bg = "#003366" , fg = "white" , font = ("Bookman Old Style" , 15))
            label4.place(x = 180, y = 120)

            name_dat = Entry(edit_addPWindow)                                           
            name_dat.place(x = 400 , y = 120)

            label5 = Label(edit_addPWindow , text = "age " , bg = "#003366" , fg = "white" , font = ("Bookman Old Style" , 15))
            label5.place(x = 180, y = 160)

            age_dat = Entry(edit_addPWindow)                                           
            age_dat.place(x = 400 , y = 160) 

            label6 = Label(edit_addPWindow , text = "gender " , bg = "#003366" , fg = "white" , font = ("Bookman Old Style" , 15))
            label6.place(x = 180, y = 200)

            gender_dat = Entry(edit_addPWindow)                                           
            gender_dat.place(x = 400 , y = 200) 

            label7 = Label(edit_addPWindow , text = "haemoglobin " , bg = "#003366" , fg = "white" , font = ("Bookman Old Style" , 15))
            label7.place(x = 180, y = 240)

            haemoglobin_dat = Entry(edit_addPWindow)                                           
            haemoglobin_dat.place(x = 400 , y = 240) 

            label8 = Label(edit_addPWindow , text = "registration date" , bg = "#003366" , fg = "white" , font = ("Bookman Old Style" , 15))
            label8.place(x = 180, y = 280)

            regis_Date_dat = Entry(edit_addPWindow)                                           
            regis_Date_dat.place(x = 400 , y = 280) 

            label9 = Label(edit_addPWindow , text = "phone No" , bg = "#003366" , fg = "white" , font = ("Bookman Old Style" , 15))
            label9.place(x = 180, y = 320)

            phoneNo_dat = Entry(edit_addPWindow)                                           
            phoneNo_dat.place(x = 400 , y = 320)

            label10 = Label(edit_addPWindow , text = "Address" , bg = "#003366" , fg = "white" , font = ("Bookman Old Style" , 15))
            label10.place(x = 180, y = 360)

            add_dat = Entry(edit_addPWindow)                                           
            add_dat.place(x = 400 , y = 360) 

            labe20 = Label(edit_addPWindow , text = "blood_group" , bg = "#003366" , fg = "white" , font = ("Bookman Old Style" , 15))
            labe20.place(x = 180, y = 400)

            b_g_dat = Entry(edit_addPWindow)                                           
            b_g_dat.place(x = 400 , y = 400) 

            labe21 = Label(edit_addPWindow , text = "Disease Name" , bg = "#003366" , fg = "white" , font = ("Bookman Old Style" , 15))
            labe21.place(x = 180, y = 440)

            diseaseName_dat = Entry(edit_addPWindow)                                           
            diseaseName_dat.place(x = 400 , y = 440) 

            submit = Button(edit_addPWindow , text = "OK" , bg = "#99FFFF" , fg = "blue" , font = ("calibri" , 10), command=add_PData)
            submit.config(width = 10 , height = 1)
            submit.place(x=330, y=460)
                    
            edit_addPWindow.mainloop()

        def delete_patient():
            def delete_p():
                id = id_dat.get()
                
                db.execute(f"DELETE FROM patient WHERE id IN (?)", id)

            edit_deletePWindow=Tk()
            edit_deletePWindow.geometry(window_size)
            edit_deletePWindow.title("BLOOD BANK MANAGEMENT")
            edit_deletePWindow.config(bg = "#000000")
            img= PhotoImage(file="photo10.gif", master= edit_deletePWindow)
            img_label= Label(edit_deletePWindow,image=img)
            img_label.place(x=0, y=0)

            label2 = Label(edit_deletePWindow , text = "Please fill the id to delete the data" , bg = "#CCCCFF" , fg = "black" , font = ("Bookman Old Style" , 20))
            label2.place(x= 120 , y = 20)

            label3 = Label(edit_deletePWindow , text = "id" , bg = "#003366" , fg = "white" , font = ("Bookman Old Style" , 15))
            label3.place(x = 300, y = 80)

            id_dat = Entry(edit_deletePWindow)                                           
            id_dat.place(x = 350 , y = 90)  

            submit = Button(edit_deletePWindow , text = "OK" , bg = "#99FFFF" , fg = "blue" , font = ("calibri" , 10), command=delete_p)
            submit.config(width = 10 , height = 1)
            submit.place(x=330, y=150)
                    
            edit_deletePWindow.mainloop()


        edit_DWindow=Tk()
        edit_DWindow.geometry(window_size)
        edit_DWindow.title("BLOOD BANK MANAGEMENT")
        edit_DWindow.config(bg = "#000000")

        img= PhotoImage(file="photo09.gif", master= edit_DWindow)
        img_label= Label(edit_DWindow,image=img)
        img_label.place(x=0, y=0)

        lable2=Label(edit_DWindow, text = "PATIENT DATA" , bg="#3B001D", fg = "white", font =("calbiri", 25))
        lable2.place(x=210, y=10)

        button19=Button(edit_DWindow, text = "ADD DATA", bg="#0A003B", fg = "white", font =("calbiri", 15), command=add_patient)
        button19.config(height = 2, width=18)
        button19.place(x=220, y=150)

        button21=Button(edit_DWindow, text = "DELETE DATA", bg="#0A003B", fg = "white", font =("calbiri", 15), command= delete_patient)
        button21.config(height = 2, width=18)
        button21.place(x=220, y=250)
        edit_DWindow.mainloop()

    def custom_query():
        cust_query = query.get()
        db.execute(cust_query)
        edit_Window()
        

    edit_Window=Tk()
    edit_Window.geometry(window_size)
    edit_Window.title("BLOOD BANK MANAGEMENT")
    edit_Window.config(bg = "#000000")

    img= PhotoImage(file="photo02.gif", master= edit_Window)
    img_label= Label(edit_Window,image=img)
    img_label.place(x=0, y=0)

    lable3=Label(edit_Window, text = "Please choose any one option " , bg="#ff0022", fg = "white", font =("calbiri", 25))
    lable3.place(x=120, y=10)

    button11=Button(edit_Window, text = "DONOR", bg="#5B2C6F", fg = "white", font =("calbiri", 15), command=edit_donor)
    button11.config(height = 2, width=18)
    button11.place(x=250, y=150)

    button12=Button(edit_Window, text = "PATIENT", bg="#5B2C6F", fg = "white", font =("calbiri", 15),  command=edit_patient)
    button12.config(height = 2, width=18)
    button12.place(x=250, y=250)

    lable3=Label(edit_Window, text = "Write your query " , bg="#ff0022", fg = "white", font =("calbiri", 18))
    lable3.place(x=250, y=350)
    
    query = Entry(edit_Window)                                               #used to give a entry field on the GUI
    query.place(x = 280 , y = 400)


    button34=Button(edit_Window, text = "EXECUTE", bg="#0A003B", fg = "white", font =("calbiri", 15), command=custom_query)
    button34.config(height=1, width=18)
    button34.place(x=250, y=430)

    edit_Window.mainloop()



main_window=Tk()
main_window.geometry(window_size)
main_window.title("BLOOD BANK MANAGEMENT")
main_window.config(bg = "#000000")
img= PhotoImage(file="photo01.gif", master= main_window)
img_label= Label(main_window,image=img)
img_label.place(x=0, y=0)
lable1=Label(main_window, text = "BLOOD BANK MANAGEMENT" , bg="#ff0022", fg = "white", font =("calbiri", 25))
lable1.place(x=120, y=10)

button1=Button(main_window, text = "VIEW DATA", bg="#5B2C6F", fg = "white", font =("calbiri", 15), command=view_data)
button1.config(height = 2, width=20)
button1.place(x=220, y=150)

   
button2=Button(main_window, text = "EDIT DATA", bg="#5B2C6F", fg = "white", font =("calbiri", 15), command=edit_data)
button2.config(height = 2, width=20)
button2.place(x=220, y=250)
main_window.mainloop()
