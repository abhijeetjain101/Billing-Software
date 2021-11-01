from tkinter import*
import math,random
from tkinter import messagebox
import os

class Bill_App:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x760+0+0")
        self.root.title("Billing Software")
        bg_color = '#3f4540'
        title = Label(self.root, text="Billing Software",bd=12,relief=GROOVE, bg=bg_color,
                      font=("times new roman", 30, "bold"),fg='white', pady=2).pack(fill=X)

        #================Variables=================

        #=============Cosmetics=================
        self.soap = IntVar()
        self.face_cream = IntVar()
        self.face_wash = IntVar()
        self.spray = IntVar()
        self.gel = IntVar()
        self.lotion = IntVar()

        #================Grocery================
        self.rice = IntVar()
        self.food_oil = IntVar()
        self.daal = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        self.tea = IntVar()

        #==================Cold Drinks================
        self.maaza = IntVar()
        self.cocacola = IntVar()
        self.frooti = IntVar()
        self.thumsup = IntVar()
        self.limca = IntVar()
        self.sprite = IntVar()

        #=========Total Product Price and Tax Variable
        self.cosmetic_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_drink_price = StringVar()

        self.cosmetic_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drink_tax = StringVar()

        self.billed_products = StringVar()
        self.billed_tax = StringVar()
        #=============Customer===========
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()

        # ===============Customer Detail Frame============
        F1 = LabelFrame(self.root,bd=10,relief=GROOVE, text="Customer Details",font =("times new roman", 15, "bold"),
                        fg="white", bg=bg_color)
        F1.place(x=0, y=80, relwidth=1)
        cname_lbl = Label(F1, text="Customer Name",bg=bg_color, font=("times new roman", 18, "bold"), fg="white").grid(row=0,
                                                                                               column=0,padx=20,pady=5)
        cname_txt = Entry(F1,width=15,textvariable = self.c_name,font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=1, pady=5, padx=10)



        cphn_lbl = Label(F1, text="Phone No.",bg=bg_color, font=("times new roman", 18, "bold"), fg="white").grid(row=0,
                                                                                                                       column=2,padx=20,pady=5)
        cphn_txt = Entry(F1,width=15,font="arial 15",textvariable = self.c_phone, bd=7, relief=SUNKEN).grid(row=0, column=3, pady=5, padx=10)


        c_bill_lbl = Label(F1, text="Bill No.",bg=bg_color, font=("times new roman", 18, "bold"), fg="white").grid(row=0,
                                                                                                                       column=4,padx=20,pady=5)
        c_bill_txt = Entry(F1,width=15,font="arial 15",textvariable = self.search_bill, bd=7, relief=SUNKEN).grid(row=0, column=5, pady=5, padx=10)

        bill_btn = Button(F1, text="Search",command = self.find_bill, width=10, bd=7, font="arial 12 bold").grid(row=0, column=6, pady=5, padx=10)

        #=======Cosmetics Frame==========
        F2 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Cosmetics", font=("times new roman", 15, "bold"), bg=bg_color, fg="white")
        F2.place(x=5, y=180, width=325, height=380)

        bath_lbl = Label(F2, text = "Bath Soap", font= ("times new roman",16,"bold"), bg=bg_color, fg="lightsalmon").grid(row=0,
                                                                                                                         column=0,
                                                                                                                         padx =10,
                                                                                                                          pady =10,
                                                                                                                          sticky='w')
        bath_txt = Entry(F2,width=10,textvariable=self.soap,font=("times new roman",16,"bold"), bd=5, relief=SUNKEN).grid(row=0,column=1, padx=10,pady=10)




        Face_cream_lbl = Label(F2, text = "Face Cream", font= ("times new roman",16,"bold"), bg=bg_color, fg="lightsalmon").grid(row=1,
                                                                                                                          column=0,
                                                                                                                          padx =10,
                                                                                                                          pady =10,
                                                                                                                          sticky='w')
        Face_cream_txt = Entry(F2,width=10,textvariable=self.face_cream,font=("times new roman",16,"bold"), bd=5, relief=SUNKEN).grid(row=1,column=1, padx=10,pady=10)



        Face_w_lbl = Label(F2, text = "Face Wash", font= ("times new roman",16,"bold"), bg=bg_color, fg="lightsalmon").grid(row=2,
                                                                                                                          column=0,
                                                                                                                          padx =10,
                                                                                                                          pady =10,
                                                                                                                          sticky='w')
        Face_w_txt = Entry(F2,width=10,textvariable=self.face_wash,font=("times new roman",16,"bold"), bd=5, relief=SUNKEN).grid(row=2,column=1, padx=10,pady=10)



        Hair_s_lbl = Label(F2, text = "Hair Spray", font= ("times new roman",16,"bold"), bg=bg_color, fg="lightsalmon").grid(row=3,
                                                                                                                          column=0,
                                                                                                                          padx =10,
                                                                                                                          pady =10,
                                                                                                                          sticky='w')
        Hair_s_txt = Entry(F2,width=10,textvariable = self.spray,font=("times new roman",16,"bold"), bd=5, relief=SUNKEN).grid(row=3,column=1, padx=10,pady=10)


        Hair_g_lbl = Label(F2, text = "Hair Gel", font= ("times new roman",16,"bold"), bg=bg_color, fg="lightsalmon").grid(row=4,
                                                                                                                          column=0,
                                                                                                                          padx =10,
                                                                                                                          pady =10,
                                                                                                                          sticky='w')
        Hair_g_txt = Entry(F2,width=10,textvariable = self.gel,font=("times new roman",16,"bold"), bd=5, relief=SUNKEN).grid(row=4,column=1, padx=10,pady=10)



        body_l_lbl = Label(F2, text = "Body Lotion", font= ("times new roman",16,"bold"), bg=bg_color, fg="lightsalmon").grid(row=5,
                                                                                                                          column=0,
                                                                                                                          padx =10,
                                                                                                                          pady =10,
                                                                                                                          sticky='w')
        body_l_txt = Entry(F2,width=10,textvariable=self.lotion,font=("times new roman",16,"bold"), bd=5, relief=SUNKEN).grid(row=5,column=1, padx=10,pady=10)



        #=======Grocery Frame==========
        F3 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Grocery", font=("times new roman", 15, "bold"), bg=bg_color, fg="white")
        F3.place(x=340, y=180, width=325, height=380)

        g1_lbl = Label(F3, text = "Rice", font= ("times new roman",16,"bold"), bg=bg_color, fg="lightsalmon").grid(row=0,
                                                                                                                          column=0,
                                                                                                                          padx =10,
                                                                                                                          pady =10,
                                                                                                                          sticky='w')
        g1_txt = Entry(F3,width=10,textvariable = self.rice,font=("times new roman",16,"bold"), bd=5, relief=SUNKEN).grid(row=0,column=1, padx=10,pady=10)




        g2_cream_lbl = Label(F3, text = "Food Oil", font= ("times new roman",16,"bold"), bg=bg_color, fg="lightsalmon").grid(row=1,
                                                                                                                                 column=0,
                                                                                                                                 padx =10,
                                                                                                                                 pady =10,
                                                                                                                                 sticky='w')
        g2_txt = Entry(F3,width=10,textvariable=self.food_oil,font=("times new roman",16,"bold"), bd=5, relief=SUNKEN).grid(row=1,column=1, padx=10,pady=10)



        g3_lbl = Label(F3, text = "Daal", font= ("times new roman",16,"bold"), bg=bg_color, fg="lightsalmon").grid(row=2,
                                                                                                                            column=0,
                                                                                                                            padx =10,
                                                                                                                            pady =10,
                                                                                                                            sticky='w')
        g3_txt = Entry(F3,width=10,textvariable=self.daal,font=("times new roman",16,"bold"), bd=5, relief=SUNKEN).grid(row=2,column=1, padx=10,pady=10)



        g4_lbl = Label(F3, text = "Wheat", font= ("times new roman",16,"bold"), bg=bg_color, fg="lightsalmon").grid(row=3,
                                                                                                                             column=0,
                                                                                                                             padx =10,
                                                                                                                             pady =10,
                                                                                                                             sticky='w')
        g4_txt = Entry(F3,width=10,textvariable=self.wheat,font=("times new roman",16,"bold"), bd=5, relief=SUNKEN).grid(row=3,column=1, padx=10,pady=10)


        g5_lbl = Label(F3, text = "Sugar", font= ("times new roman",16,"bold"), bg=bg_color, fg="lightsalmon").grid(row=4,
                                                                                                                           column=0,
                                                                                                                           padx =10,
                                                                                                                           pady =10,
                                                                                                                           sticky='w')
        g5_txt = Entry(F3,width=10,textvariable=self.sugar,font=("times new roman",16,"bold"), bd=5, relief=SUNKEN).grid(row=4,column=1, padx=10,pady=10)



        g6_lbl = Label(F3, text = "Tea", font= ("times new roman",16,"bold"), bg=bg_color, fg="lightsalmon").grid(row=5,
                                                                                                                              column=0,
                                                                                                                              padx =10,
                                                                                                                              pady =10,
                                                                                                                              sticky='w')
        g6_txt = Entry(F3,width=10,textvariable=self.tea,font=("times new roman",16,"bold"), bd=5, relief=SUNKEN).grid(row=5,column=1, padx=10,pady=10)


        #=======Coldrink Frame==========
        F4 = LabelFrame(self.root, bd=10, relief=GROOVE, text="ColdDrinks", font=("times new roman", 15, "bold"), bg=bg_color, fg="white")
        F4.place(x=675, y=180, width=325, height=380)

        c1_lbl = Label(F4, text = "Maaza", font= ("times new roman",16,"bold"), bg=bg_color, fg="lightsalmon").grid(row=0,
                                                                                                                   column=0,
                                                                                                                   padx =10,
                                                                                                                   pady =10,
                                                                                                                   sticky='w')
        c1_txt = Entry(F4,width=10,textvariable=self.maaza,font=("times new roman",16,"bold"), bd=5, relief=SUNKEN).grid(row=0,column=1, padx=10,pady=10)




        g2_cream_lbl = Label(F4, text = "Cocacola", font= ("times new roman",16,"bold"), bg=bg_color, fg="lightsalmon").grid(row=1,
                                                                                                                             column=0,
                                                                                                                             padx =10,
                                                                                                                             pady =10,
                                                                                                                             sticky='w')
        g2_txt = Entry(F4,width=10,textvariable=self.cocacola,font=("times new roman",16,"bold"), bd=5, relief=SUNKEN).grid(row=1,column=1, padx=10,pady=10)



        g3_lbl = Label(F4, text = "Frooti", font= ("times new roman",16,"bold"), bg=bg_color, fg="lightsalmon").grid(row=2,
                                                                                                                   column=0,
                                                                                                                   padx =10,
                                                                                                                   pady =10,
                                                                                                                   sticky='w')
        g3_txt = Entry(F4,width=10,textvariable=self.frooti,font=("times new roman",16,"bold"), bd=5, relief=SUNKEN).grid(row=2,column=1, padx=10,pady=10)



        g4_lbl = Label(F4, text = "Thums Up", font= ("times new roman",16,"bold"), bg=bg_color, fg="lightsalmon").grid(row=3,
                                                                                                                    column=0,
                                                                                                                    padx =10,
                                                                                                                    pady =10,
                                                                                                                    sticky='w')
        g4_txt = Entry(F4,width=10,textvariable=self.thumsup,font=("times new roman",16,"bold"), bd=5, relief=SUNKEN).grid(row=3,column=1, padx=10,pady=10)


        g5_lbl = Label(F4, text = "Limca", font= ("times new roman",16,"bold"), bg=bg_color, fg="lightsalmon").grid(row=4,
                                                                                                                    column=0,
                                                                                                                    padx =10,
                                                                                                                    pady =10,
                                                                                                                    sticky='w')
        g5_txt = Entry(F4,width=10,textvariable=self.limca,font=("times new roman",16,"bold"), bd=5, relief=SUNKEN).grid(row=4,column=1, padx=10,pady=10)



        g6_lbl = Label(F4, text = "Sprite", font= ("times new roman",16,"bold"), bg=bg_color, fg="lightsalmon").grid(row=5,
                                                                                                                  column=0,
                                                                                                                  padx =10,
                                                                                                                  pady =10,
                                                                                                                  sticky='w')
        g6_txt = Entry(F4,width=10,textvariable=self.sprite,font=("times new roman",16,"bold"), bd=5, relief=SUNKEN).grid(row=5,column=1, padx=10,pady=10)




        #===========Bill Area============
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1010, y=180, width=340, height=380)
        bill_title = Label(F5, text="Bill Area", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)
        scrool_y = Scrollbar(F5, orient= VERTICAL)
        self.txtarea = Text(F5, yscrollcommand = scrool_y.set)
        scrool_y.pack(side=RIGHT, fill=Y)
        scrool_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill = BOTH, expand=1)


        #=========Button Frame=============
        F6 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Bill Menu", font=("times new roman", 15, "bold"), bg=bg_color, fg="white")
        F6.place(x=0, y=560, relwidth=1, height=200)

        m1_lbl = Label(F6, text = 'Total Cosmetic Price', font = ('times new roman', 14, 'bold'), bg=bg_color, fg='white').grid(row=0, column=0, padx=20, pady=1,
                                                                                                   sticky='w')
        m1_txt = Entry(F6, width=18, textvariable=self.cosmetic_price,font=('arial',10,'bold'), bd=7, relief=SUNKEN).grid(row=0, column=1,padx=10,pady=1)

        m2_lbl = Label(F6, text = 'Total Grocery Price', font = ('times new roman', 14, 'bold'), bg=bg_color, fg='white').grid(row=1, column=0, padx=20, pady=1,
                                                                                                                                sticky='w')
        m2_txt = Entry(F6, width=18, textvariable=self.grocery_price,font=('arial',10,'bold'), bd=7, relief=SUNKEN).grid(row=1, column=1,padx=10,pady=1)

        m3_lbl = Label(F6, text = 'Total Coldrink Price', font = ('times new roman', 14, 'bold'), bg=bg_color, fg='white').grid(row=2, column=0, padx=20, pady=1,
                                                                                                                               sticky='w')
        m3_txt = Entry(F6, width=18,textvariable=self.cold_drink_price, font=('arial',10,'bold'), bd=7, relief=SUNKEN).grid(row=2, column=1,padx=10,pady=1)

        m4_lbl = Label(F6, text= "Total Billed", font = ('times new roman', 14, 'bold'), bg=bg_color, fg='white').grid(row=3,column=0,padx=20, pady=20,sticky='w')
        m4_txt = Entry(F6, width=18, textvariable=self.billed_products, font=('arial',10,'bold'), relief=SUNKEN).grid(row=3, column=1,padx=10,pady=1)




        c1_lbl = Label(F6, text = 'Cosmetic Tax', font = ('times new roman', 14, 'bold'), bg=bg_color, fg='white').grid(row=0, column=2, padx=20, pady=1,
                                                                                                                                sticky='w')
        c1_txt = Entry(F6, width=18, textvariable=self.cosmetic_tax,font=('arial',10,'bold'), bd=7, relief=SUNKEN).grid(row=0, column=3,padx=10,pady=1)

        c2_lbl = Label(F6, text = 'Grocery Tax', font = ('times new roman', 14, 'bold'), bg=bg_color, fg='white').grid(row=1, column=2, padx=20, pady=1,
                                                                                                                           sticky='w')
        c2_txt = Entry(F6, width=18, textvariable=self.grocery_tax,font=('arial',10,'bold'), bd=7, relief=SUNKEN).grid(row=1, column=3,padx=10,pady=1)

        c3_lbl = Label(F6, text = 'Coldrink Tax', font = ('times new roman', 14, 'bold'), bg=bg_color, fg='white').grid(row=2, column=2, padx=20, pady=1,
                                                                                                                            sticky='w')
        c3_txt = Entry(F6, width=18, textvariable=self.cold_drink_tax,font=('arial',10,'bold'), bd=7, relief=SUNKEN).grid(row=2, column=3,padx=10,pady=1)

        c4_lbl = Label(F6, text= "Total Tax", font = ('times new roman', 14, 'bold'), bg=bg_color, fg='white').grid(row=3,column=2,padx=20, pady=20,sticky='w')
        c4_txt = Entry(F6, width=18, textvariable=self.billed_tax, font=('arial',10,'bold'), relief=SUNKEN).grid(row=3, column=3,padx=10,pady=1)


        btn_F = Frame(F6, bd=7, relief=GROOVE)
        btn_F.place(x = 740, width = 585, height = 105)

        total_btn = Button(btn_F, command = self.total, text="Total", bg="cadetblue", fg="white", bd=2, pady=15, width =10 , font='arial 15 bold').grid(row=0, column=0, padx=5, pady=5)
        gbill_btn = Button(btn_F, command = self.bill_area, text="Generate Bill", bg="cadetblue", fg="white", bd=2, pady=15, width =10, font='arial 15 bold').grid(row=0, column=1, padx=5, pady=5)
        clear_btn = Button(btn_F, text="Clear",command = self.clear_data, bg="cadetblue", fg="white", bd=2, pady=15, width =10, font='arial 15 bold').grid(row=0, column=2, padx=5, pady=5)
        exit_btn = Button(btn_F, text="Exit",command = self.Exit_app, bg="cadetblue", fg="white", bd=2, pady=15, width =10, font='arial 15 bold').grid(row=0, column=3, padx=5, pady=5)
        self.welcome_bill()



    def total(self):

        self.c_s_p = (self.soap.get()*40)
        self.fc_p = (self.face_cream.get()*120)
        self.fw_p = (self.face_wash.get()*60)
        self.s_p = (self.spray.get()*180)
        self.g_p = (self.gel.get()*140)
        self.l_p =  (self.lotion.get()*180)

        self.total_cosmetic_price = float(
            self.c_s_p +
            self.fc_p +
            self.fw_p +
            self.s_p +
            self.g_p +
            self.l_p
        )

        self.cosmetic_price.set('Rs. ' + str(self.total_cosmetic_price))
        self.c_tax = round((self.total_cosmetic_price * 0.05), 2)
        self.cosmetic_tax.set('Rs. ' + str(self.c_tax))

        self.r_p = (self.rice.get()*80)
        self.f_p = (self.food_oil.get()*180)
        self.d_p = (self.daal.get()*60)
        self.w_p = (self.wheat.get()*240)
        self.su_p = (self.sugar.get()*45)
        self.t_p = (self.tea.get()*150)

        self.total_grocery_price = float(
            self.r_p +
            self.f_p +
            self.d_p +
            self.w_p +
            self.su_p +
            self.t_p
        )

        self.grocery_price.set('Rs. ' + str(self.total_grocery_price))
        self.g_tax = round((self.total_grocery_price * 0.1), 2)
        self.grocery_tax.set('Rs. ' + str(self.g_tax))

        self.m_p = (self.maaza.get()*60)
        self.c_p = (self.cocacola.get()*60)
        self.fr_p = (self.frooti.get()*50)
        self.th_p = (self.thumsup.get()*45)
        self.li_p = (self.limca.get()*40)
        self.sp_p = (self.sprite.get()*60)


        self.total_drinks_price = float(
            self.m_p +
            self.c_p +
            self.fr_p +
            self.th_p +
            self.li_p +
            self.sp_p
        )

        self.cold_drink_price.set('Rs. ' + str(self.total_drinks_price))
        self.d_tax = round((self.total_drinks_price * 0.05), 2)
        self.cold_drink_tax.set('Rs. ' + str(self.d_tax))

        self.total_bill = float(self.total_cosmetic_price +
                                self.total_grocery_price +
                                self.total_drinks_price +
                                self.c_tax +
                                self.g_tax +
                                self.d_tax)


        #Total of Billed Products and Total of tax
        self.total_billed_products= float(self.total_cosmetic_price +
                                          self.total_grocery_price +
                                          self.total_drinks_price)
        self.billed_products.set('Rs. ' + str(self.total_billed_products))



        self.total_billed_tax = float(self.c_tax + self.g_tax + self.d_tax)
        self.billed_tax.set('Rs. ' + str(self.total_billed_tax))




    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\t Welcome To Retail Mart \n")
        self.txtarea.insert(END,f"\n Bill Number : {self.bill_no.get()}")
        self.txtarea.insert(END,f"\n Customer Name : {self.c_name.get()}")
        self.txtarea.insert(END,f"\n Phone Number : {self.c_phone.get()}")
        self.txtarea.insert(END,f"\n=====================================")
        self.txtarea.insert(END,f"\n Products\t\tQty\t    Price")
        self.txtarea.insert(END,f"\n=====================================")

    def bill_area(self):
        if self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror("Error", "Customer details are must")
        elif self.cosmetic_price.get() == "Rs. 0.0" and self.grocery_price.get() == "Rs. 0.0" and self.cold_drink_price.get() == "Rs. 0.0":
            messagebox.showerror("Error", "No Products Purchsed")
        else:
            self.welcome_bill()
            # == Cosmetics ==
            if self.soap.get()!= 0:
                self.txtarea.insert(END,f"\n Bath Soap\t\t{self.soap.get()}\t   Rs.{self.c_s_p}")
            if self.face_cream.get()!= 0:
                self.txtarea.insert(END,f"\n Face Cream\t\t{self.face_cream.get()}\t   Rs.{self.fc_p}")
            if self.face_wash.get()!= 0:
                self.txtarea.insert(END,f"\n Face Wash\t\t{self.face_wash.get()}\t   Rs.{self.fw_p}")
            if self.spray.get()!=0:
                self.txtarea.insert(END,f"\n Hair Spray\t\t{self.spray.get()}\t   Rs.{self.s_p}")
            if self.gel.get()!= 0:
                self.txtarea.insert(END,f"\n Hair Gel\t\t{self.gel.get()}\t   Rs.{self.g_p}")
            if self.lotion.get()!= 0:
                self.txtarea.insert(END,f"\n Body Lotion\t\t{self.lotion.get()}\t   Rs.{self.l_p}")

            # == Grocery ==
            if self.rice.get()!= 0:
                self.txtarea.insert(END,f"\n Rice\t\t{self.rice.get()}\t   Rs.{self.r_p}")
            if self.food_oil.get()!= 0:
                self.txtarea.insert(END,f"\n Food Oil\t\t{self.food_oil.get()}\t   Rs.{self.f_p}")
            if self.daal.get()!= 0:
                self.txtarea.insert(END,f"\n Daal\t\t{self.daal.get()}\t   Rs.{self.d_p}")
            if self.wheat.get()!= 0:
                self.txtarea.insert(END,f"\n Wheat\t\t{self.wheat.get()}\t   Rs.{self.w_p}")
            if self.sugar.get()!= 0:
                self.txtarea.insert(END,f"\n Sugar\t\t{self.sugar.get()}\t   Rs.{self.su_p}")
            if self.tea.get()!= 0:
                self.txtarea.insert(END,f"\n Tea\t\t{self.tea.get()}\t   Rs.{self.t_p}")

            # == ColdDrinks ==
            if self.maaza.get()!= 0:
                self.txtarea.insert(END,f"\n Maaza\t\t{self.maaza.get()}\t   Rs.{self.m_p}")
            if self.cocacola.get()!= 0:
                self.txtarea.insert(END,f"\n Cocacola\t\t{self.cocacola.get()}\t   Rs.{self.c_p}")
            if self.frooti.get()!= 0:
                self.txtarea.insert(END,f"\n Frooti\t\t{self.frooti.get()}\t   Rs.{self.fr_p}")
            if self.thumsup.get()!= 0:
                self.txtarea.insert(END,f"\n ThumsUp\t\t{self.thumsup.get()}\t   Rs.{self.th_p}")
            if self.limca.get()!= 0:
                self.txtarea.insert(END,f"\n Limca\t\t{self.limca.get()}\t   Rs.{self.li_p}")
            if self.sprite.get()!= 0:
                self.txtarea.insert(END,f"\n Sprite\t\t{self.sprite.get()}\t   Rs.{self.sp_p}")
            pass

            self.txtarea.insert(END,f"\n-------------------------------------")
            if self.cosmetic_tax.get()!= "Rs. 0.0":
                self.txtarea.insert(END,f"\n Cosmetic Tax\t\t\t   {self.cosmetic_tax.get()}")

            if self.grocery_tax.get()!= "Rs. 0.0":
                self.txtarea.insert(END,f"\n Grocery Tax\t\t\t   {self.grocery_tax.get()}")

            if self.cold_drink_tax.get()!= "Rs. 0.0":
                self.txtarea.insert(END,f"\n ColdDrink Tax\t\t\t   {self.cold_drink_tax.get()}")
            self.txtarea.insert(END,f"\n-------------------------------------")

            self.txtarea.insert(END,f"\n Total Bill: \t\t\t{self.total_bill}")
            self.txtarea.insert(END,f"\n-------------------------------------")
            self.save_bill()

    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save bill ?")
        if op > 0 :
            self.bill_data = self.txtarea.get('1.0', END)
            f1 = open("bills/" + str(self.bill_no.get()) + ".csv","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved", f"Bill no. {self.bill_no.get()} Saved Successfully")
        else:
            return

    def find_bill(self):
        present = "no"
        for i in os.listdir("bills/"):
            if i.split('.')[0] == self.search_bill.get():
                f1 = open(f"bills/{i}","r")
                self.txtarea.delete('1.0', END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present = 'yes'
        if present == "no":
            messagebox.showerror("Error", "Invalid Bill No.")

    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you really want to Clear data ?")
        if op > 0:

        #=============Cosmetics=================
            self.soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.spray.set(0)
            self.gel.set(0)
            self.lotion.set(0)

            #================Grocery================
            self.rice.set(0)
            self.food_oil.set(0)
            self.daal.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)

            #==================Cold Drinks================
            self.maaza.set(0)
            self.cocacola.set(0)
            self.frooti.set(0)
            self.thumsup.set(0)
            self.limca.set(0)
            self.sprite.set(0)

            #=========Total Product Price and Tax Variable
            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.cold_drink_price.set("")

            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.cold_drink_tax.set("")
    
            self.billed_products.set("")
            self.billed_tax.set("")
            #=============Customer===========
            self.c_name.set("")
            self.c_phone.set("")
            self.bill_no.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")

            self.welcome_bill()


    def Exit_app(self):
        op = messagebox.askyesno("Exit", "Do you really want to exit ?")
        if op > 0:
            self.root.destroy()






root = Tk()
obj = Bill_App(root)
root.mainloop()