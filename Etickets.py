"""
Created on Wednesday 21-11-17 at 15:11:22

author@ Jonathan Estrada
"""

import tkinter as tk
from tkinter import ttk
from pyfiglet import figlet_format
import getpass
import time
import sqlite3
import pandas as pd
from datetime import datetime
import shutil


def rma_frm(sql):
    # RMA FORM --- 

    def submit_rma():
        # SQLITE STORING FORM DATA --- 

        # SQL CURSOR --- 

        rmaSql_curs = sql.cursor()

        # CREATING RMA TABLES --- 

        rma_table = """

        CREATE TABLE RMA(
        DATES DATE,
        RMA_NUMBER TEXT, 
        INVOICE_NUMBER INTEGER,
        QUANITY INTEGER,
        PART_NUMBER TEXT, 
        SERIAL_NUMBER TEXT, 
        NAME_COMPANY TEXT,
        ADDRESS TEXT,
        CITY TEXT,
        STATE TEXT,
        ZIP_CODE INTEGER, 
        EMAIL TEXT,
        PHONE INTEGER, 
        OS TEXT,
        FORMAT TEXT,
        RESIDENT TEXT,
        ISSUE TEXT)

        """

        # EXECUTING SQL TABLE --- 

        try:
            rmaSql_curs.execute(rma_table)

        except:
            time.sleep(.1)

        # GET "DATES" VALUE --- 

        month_value = month_fltr.get()
        day_value = day_fltr.get()
        yr_value = yr_fltr.get()

        date_value = month_value + '/' + day_value + '/' + yr_value

        # GET "RMA NUMBER" VALUE --- 

        rmaNum_value = rma_numEnt.get()
        rma_numEnt.delete(0, 'end')

        # GET "INVOICE NUMBER" VALUE --- 

        invc_value = invc_ent.get()
        invc_ent.delete(0, 'end')

        # GET "QUANITY" VALUE --- 

        quant_value = quant_ent.get()
        quant_ent.delete(0, 'end')

        # GET "PART NUMBER" VALUE --- 

        pn_value = pn_ent.get()
        pn_ent.delete(0, 'end')

        # GET "SERIAL NUMBER" VALUE --- 

        sn_value = sn_ent.get()
        sn_ent.delete(0, 'end')

        # GET "NAME AND COMPANY" DATA VALUE ---

        name_value = name_ttl_ent.get()
        name_ttl_ent.delete(0, 'end')

        # GET "ADDRESS" DATA VALUE --- 

        adrs_value = adrs_ent.get()
        adrs_ent.delete(0, 'end')

        # GET "CITY" DATA VALUE --- 

        city_value = city_ent.get()
        city_ent.delete(0, 'end')

        # GET "STATE" DATA VALUE --- 

        state_value = state_ent.get()
        state_ent.delete(0, 'end')

        # GET "ZIP CODE" DATA VALUE ---

        zip_value = zip_ent.get()
        zip_ent.delete(0, 'end')

        # GET "EMAIL" DATA VALUE --- 

        email_value = email_ent.get()
        email_ent.delete(0, 'end')

        # GET "PHONE" DATA VALUE --- 

        phone_value = phone_ent.get()
        phone_ent.delete(0, 'end')

        # GET QUESTION 1 DATA VALUE --- 

        ques1_value = ques1_fltr.get()

        # GET QUESTION 2 DATA VALUE --- 

        ques2_value = ques2_fltr.get()

        # GET QUESTION 3 DATA VALUE --- 

        ques3_value = ques3_fltr.get()

        # GET "DESCRIPTION" DATA VALUE --- 

        prb_value = prbd_ent.get('1.0', 'end')
        prbd_ent.delete('1.0', 'end')

        # CREATING DATAFRAME --- 

        rma_dict = {

            'DATES': [date_value],
            'RMA_NUMBER': [rmaNum_value],
            'INVOICE_NUMBER': [invc_value],
            'QUANITY': [quant_value],
            'PART_NUMBER': [pn_value],
            'SERIAL_NUMBER': [sn_value],
            'NAME_COMPANY': [name_value],
            'ADDRESS': [adrs_value],
            'CITY': [city_value],
            'STATE': [state_value],
            'ZIP_CODE': [zip_value],
            'EMAIL': [email_value],
            'PHONE': [phone_value],
            'OS': [ques1_value],
            'FORMAT': [ques2_value],
            'RESIDENT': [ques3_value],
            'ISSUE': [prb_value]

        }

        df_rma = pd.DataFrame(rma_dict)

        # INSERT DATAFRAME IN DATABASE --- 

        for i in range(len(df_rma)):
            df_rows = df_rma.iloc[i]
            rmaSql_curs.execute("INSERT INTO RMA VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", df_rows)

        sql.commit()

    def query_rma(sql, tree):
        # FUNCTION TO QUERY INDIVIDUAL VALUES --- 

        def rget(fch, clm):
            # INSERTING RMA VALUES IN TREEVIEW --- 

            global bol

            def rget2():
                qnm = 0

                for q_row in fch:
                    qrw = str(q_row[clm])
                    qrwL = qrw.lower()
                    if qrwL.find(qry_ent.get().lower()) != -1:
                        qnm += 1
                        tree.insert("", "end", values=(qnm, q_row[1], q_row[2], q_row[3], q_row[4],
                                                       q_row[5], q_row[6], q_row[7], q_row[8], q_row[9], q_row[10],
                                                       q_row[11], q_row[12],
                                                       q_row[13], q_row[14], q_row[15], q_row[16], q_row[17]))

            rma_srch = qry_ent.get().lower()
            Rn1 = 0
            Rn2 = 0
            Rls = []
            for s in rma_srch:
                Rn1 += 1
                if s == ' ':
                    n3 = Rn1 - 1
                    Rls.append(rma_srch[Rn2:n3])
                    Rn2 = Rn1
                    bol = True

            try:
                if bol == True:
                    Rls.append(rma_srch[Rn2:len(rma_srch)])
                    Rln = len(Rls)
                    Rn1 = 0
                    qnm2 = 0

                    for Rx in fch:
                        Rxs = Rx[7].lower()
                        for Rl in Rls:
                            if Rxs.find(Rl) != -1:
                                Rn1 += 1
                                if Rln == Rn1:
                                    qnm2 += 1
                                    tree.insert("", "end", values=(qnm2, Rx[1], Rx[2], Rx[3], Rx[4],
                                                                   Rx[5], Rx[6], Rx[7], Rx[8], Rx[9], Rx[10], Rx[11],
                                                                   Rx[12],
                                                                   Rx[13], Rx[14], Rx[15], Rx[16], Rx[17]))

            except:
                bol = False

            if bol == False:
                rget2()

        # QUERY ---

        # DELETING PREVIOS TREEVIEW CONTENT --- 

        for del_ in tree.get_children():
            tree.delete(del_)

        # CREATING COLUMN FOR TREEVIEW --- 

        tree['column'] = ('ROW_ID', 'DATES', 'RMA_NUMBER', 'INVOICE_NUMBER', 'QUANITY', 'PART_NUMBER',
                          'SERIAL_NUMBER', 'NAME_COMPANY', 'ADDRESS', 'CITY', 'STATE', 'ZIP_CODE', 'EMAIL',
                          'PHONE', 'OS', 'FORMAT', 'RESIDENT', 'ISSUE')

        tree["show"] = "headings"

        for columns in tree['column']:
            tree.heading(columns, text=columns)

        # OPENING SQL CURSOR --- 

        qry_cursql = sql.cursor()

        # FETCHING RMA TABLE IN RMA.DB --- 

        qry_fch = qry_cursql.execute("SELECT rowid, * FROM RMA").fetchall()

        # QUERYING SPECIFIC VALUES IN RMA TABLE --- 

        if qryOpt_fltr.get() == 'Name / Company':
            rget(qry_fch, 7)

        elif qryOpt_fltr.get() == 'Address':
            rget(qry_fch, 8)

        elif qryOpt_fltr.get() == 'City':
            rget(qry_fch, 9)

        elif qryOpt_fltr.get() == 'State':
            rget(qry_fch, 10)

        elif qryOpt_fltr.get() == 'Zip Code':
            rget(qry_fch, 11)

        elif qryOpt_fltr.get() == 'Email':
            rget(qry_fch, 12)

        elif qryOpt_fltr.get() == 'Phone':
            rget(qry_fch, 13)

        elif qryOpt_fltr.get() == 'RMA Number':
            rget(qry_fch, 2)

        elif qryOpt_fltr.get() == 'Invoice Number':
            rget(qry_fch, 3)

        elif qryOpt_fltr.get() == 'Part Number':
            rget(qry_fch, 5)

        elif qryOpt_fltr.get() == 'Serial Number':
            rget(qry_fch, 6)

        sql.commit()

    # ROOT RMA WINDOW ---

    rma_tpl = tk.Toplevel()

    rma_tpl.title('RMA Form')
    rma_tpl.geometry("900x700")

    # BACKGROUND INSIDE OF ROOT --- 

    rma_bck_img = tk.PhotoImage(file='rma_bck.png')
    rma_bck = tk.Label(rma_tpl, image=rma_bck_img)
    rma_bck.place(relwidth=1, relheight=1)

    # ROOT FRAME FOR CONTACT INFO AND PRODUCT INFO--- 

    cntp_info = tk.Frame(rma_tpl, bg='#81781C', bd=3)
    cntp_info.place(relx=.02, rely=.07, relwidth=.96, relheight=.35)

    cntp_info2 = tk.Frame(cntp_info, bg='#BF833C', bd=4)
    cntp_info2.place(relwidth=1, relheight=1)

    # TITLE IN ROOT WINDOW --- 

    rma_ttl_frame = tk.Frame(rma_tpl, bg='#A56239', bd=1.5)
    rma_ttl_frame.place(relx=.01, rely=.01, relwidth=.23, relheight=.07)

    rma_ttl_img = tk.PhotoImage(file='image001.png')
    rma_ttl_label = tk.Label(rma_ttl_frame, image=rma_ttl_img)
    rma_ttl_label.place(relwidth=1, relheight=1)

    # THIS IS THE RIDGE FOR THE ADDRESS AND CONTACT INFO --- 

    addrs_rd = tk.Label(cntp_info2, bg='#EBC89F', relief='ridge')
    addrs_rd.place(relwidth=.5, relheight=.45)

    # COMPANY NAME --- 

    name_ttl_lbl = tk.Label(addrs_rd, bg='#EBC89F', relief='ridge')
    name_ttl_lbl.place(relx=.01, rely=.08, relwidth=.4, relheight=.39)

    name_ttl_ent = tk.Entry(name_ttl_lbl, bd=3, relief='sunken')
    name_ttl_ent.place(relx=.02, rely=.25, relwidth=.96, relheight=.65)

    name_ttl = tk.Label(addrs_rd, text='Name / Company', bg='#EBC89F')
    name_ttl.config(font=('Calibri', 10))
    name_ttl.place(relx=.03, rely=.03, relheight=.13)

    # ADDRESS ---

    adrs_lbl = tk.Label(addrs_rd, bg='#EBC89F', relief='ridge')
    adrs_lbl.place(relx=.01, rely=.57, relwidth=.4, relheight=.39)

    adrs_ent = tk.Entry(adrs_lbl, bd=3, relief='sunken')
    adrs_ent.place(relx=.02, rely=.25, relwidth=.96, relheight=.65)

    adrs_ttl = tk.Label(addrs_rd, text='Address', bg='#EBC89F')
    adrs_ttl.place(relx=.03, rely=.5, relheight=.1)

    # CITY --- 

    city_lbl = tk.Label(addrs_rd, bg='#EBC89F', relief='ridge')
    city_lbl.place(relx=.45, rely=.07, relwidth=.3, relheight=.39)

    city_ent = tk.Entry(city_lbl, bd=3, relief='sunken')
    city_ent.place(relx=.04, rely=.25, relwidth=.93, relheight=.65)

    city_ttl = tk.Label(addrs_rd, text='City', bg='#EBC89F')
    city_ttl.place(relx=.47, rely=.02, relheight=.13)

    # STATE --- 

    state_lbl = tk.Label(addrs_rd, bg='#EBC89F', relief='ridge')
    state_lbl.place(relx=.45, rely=.57, relwidth=.1, relheight=.39)

    state_ent = tk.Entry(state_lbl, bd=3, relief='sunken')
    state_ent.place(relx=.1, rely=.25, relwidth=.8, relheight=.65)

    state_ttl = tk.Label(addrs_rd, text='State', bg='#EBC89F')
    state_ttl.place(relx=.46, rely=.5, relwidth=.07, relheight=.13)

    # ZIP CODE --- 

    zip_lbl = tk.Label(addrs_rd, bg='#EBC89F', relief='ridge')
    zip_lbl.place(relx=.57, rely=.57, relwidth=.2, relheight=.39)

    zip_ent = tk.Entry(zip_lbl, bd=3, relief='sunken')
    zip_ent.place(relx=.04, rely=.25, relwidth=.92, relheight=.65)

    zip_ttl = tk.Label(addrs_rd, text='Zip Code', bg='#EBC89F')
    zip_ttl.place(relx=.59, rely=.5, relheight=.13)

    # RIDGE FOR CONTACT INFO --- 

    cnt_rdg = tk.Label(cntp_info2, bg='#EBC89F', relief='ridge')
    cnt_rdg.place(rely=.45, relwidth=.4, relheight=.26)

    # EMAIL --- 

    email_lbl = tk.Label(cnt_rdg, bg='#EBC89F', relief='ridge')
    email_lbl.place(relx=.03, rely=.21, relwidth=.5, relheight=.7)

    email_ent = tk.Entry(email_lbl, bd=3, relief='sunken')
    email_ent.place(relx=.03, rely=.25, relwidth=.94, relheight=.7)

    email_ttl = tk.Label(cnt_rdg, bg='#EBC89F', text='Email')
    email_ttl.place(relx=.05, rely=.02)

    # PHONE --- 

    phone_lbl = tk.Label(cnt_rdg, bg='#EBC89F', relief='ridge')
    phone_lbl.place(relx=.55, rely=.21, relwidth=.43, relheight=.7)

    phone_ent = tk.Entry(phone_lbl, bd=3, relief='sunken')
    phone_ent.place(relx=.03, rely=.25, relwidth=.94, relheight=.7)

    phone_ttl = tk.Label(cnt_rdg, bg='#EBC89F', text='Phone')
    phone_ttl.place(relx=.58, rely=.02)

    # RIDGE FOR DETAILS OF DEFECTIVE PRODUCT --- 

    ddp_rdg = tk.Label(cntp_info2, bg='#C6CAA2', relief='ridge')
    ddp_rdg.place(relx=.4, rely=.09, relwidth=.6, relheight=.9)

    # RIDGE FOR QUANTITY / INVOICE NUMBER / PN / SN 

    qips_rdg = tk.Label(ddp_rdg, bg='#C6CAA2', relief='ridge')
    qips_rdg.place(relx=.01, rely=.03, relwidth=.49, relheight=.94)

    # RIDGE FOR QUANTITY --- 

    quant_rdge = tk.Label(qips_rdg, bg='#C6CAA2', relief='ridge')
    quant_rdge.place(relx=.03, rely=.03, relwidth=.44, relheight=.18)

    # QUANTITY LABEL --- 

    quant_lbl = tk.Label(quant_rdge, bg='#C6CAA2', text='Quantity')
    quant_lbl.place(relx=.01, rely=.08)

    # QUANITY ENTRY BOX --- 

    quant_ent = tk.Entry(quant_rdge, bd=3, relief='sunken')
    quant_ent.place(relx=.52, rely=.1, relwidth=.43)

    # RIDGE FOR INVOICE NUMBER --- 

    invc_rdg = tk.Label(qips_rdg, bg='#C6CAA2', relief='ridge')
    invc_rdg.place(relx=.49, rely=.03, relwidth=.48, relheight=.21)

    # INVOICE NUMBER LABEL --- 

    invc_lbl = tk.Label(qips_rdg, bg='#C6CAA2', text='Invoice Number')
    invc_lbl.place(relx=.51, rely=.01, relheight=.07)

    # INVOICE ENTRY BOX --- 

    invc_ent = tk.Entry(invc_rdg, bd=3, relief='sunken')
    invc_ent.place(relx=.03, rely=.27, relwidth=.94)

    # PART NUMBER RIDGE --- 

    pn_rdg = tk.Label(qips_rdg, bg='#C6CAA2', relief='ridge')
    pn_rdg.place(relx=.03, rely=.32, relwidth=.7, relheight=.23)

    # PART NUMBER ENTRY BOX --- 

    pn_ent = tk.Entry(pn_rdg, bd=3, relief='sunken')
    pn_ent.place(relx=.03, rely=.25, relwidth=.94)

    # PART NUMBER LABEL --- 

    pn_lbl = tk.Label(qips_rdg, bg='#C6CAA2', text='Part Number')
    pn_lbl.place(relx=.05, rely=.26)

    # SERIAL NUMBER RIDGE --- 

    sn_rdg = tk.Label(qips_rdg, bg='#C6CAA2', relief='ridge')
    sn_rdg.place(relx=.03, rely=.64, relwidth=.7, relheight=.23)

    # SERIAL NUMBER ENTRY BOX --- 

    sn_ent = tk.Entry(sn_rdg, bd=3, relief='sunken')
    sn_ent.place(relx=.03, rely=.25, relwidth=.94)

    # SERIAL NUMBER LABEL --- 

    sn_lbl = tk.Label(qips_rdg, bg='#C6CAA2', text='Serial Number')
    sn_lbl.place(relx=.05, rely=.58)

    # RIDGE FOR PROBLEM DESCRIPTION --- 

    prbd_rdg1 = tk.Label(ddp_rdg, bg='#C6CAA2', relief='ridge')
    prbd_rdg1.place(relx=.51, rely=.03, relwidth=.48, relheight=.94)

    # RIDGE FOR PROBLEM DESCRIPTION ENTRY BOX --- 

    prbd_rdg2 = tk.Label(prbd_rdg1, bg='#C6CAA2', relief='ridge')
    prbd_rdg2.place(relx=.03, rely=.08, relwidth=.94, relheight=.89)

    # PROBLEM DESCRIPTION ENTRY BOX --- 

    prbd_ent = tk.Text(master=prbd_rdg2)
    prbd_ent.place(rely=.05, relwidth=1, relheight=.95)

    # PROBLEM DESCRIPTION LABEL --- 

    prbd_lbl = tk.Label(prbd_rdg1, bg='#C6CAA2', text='Describe Problem')
    prbd_lbl.place(relx=.05, rely=.02)

    # FRAME FOR DATE AND RMA NUMBER STORED IN ROOT CANVAS--- 

    date_rmaFrm = tk.Frame(rma_tpl, bg='#81781C')
    date_rmaFrm.place(relx=.5, rely=.01, relwidth=.46, relheight=.06)

    date_rmaFrm2 = tk.Frame(rma_tpl, bg='#BF833C', bd=3)
    date_rmaFrm2.place(relx=.51, rely=.02, relwidth=.44, relheight=.09)

    # RIDGE FOR DATES AND RMA NUMBER --- 

    date_rmaLbl = tk.Label(date_rmaFrm2, bg='#C9AD95', relief='ridge')
    date_rmaLbl.place(relwidth=1, relheight=1)

    # DATE --- 

    date_rdg = tk.Label(date_rmaLbl, bg='#C9AD95', relief='ridge')
    date_rdg.place(relx=.02, rely=.2, relwidth=.69, relheight=.7)

    date_ttl = tk.Label(date_rmaLbl, bg='#C9AD95', text='Date')
    date_ttl.place(relx=.05, relheight=.2, rely=.09)

    # OPTION BOX FOR MONTH --- 

    month_lst = [

        'Month', '01', '02', '03', '04',
        '05', '06', '07', '08',
        '09', '10', '11', '12'

    ]

    month_fltr = tk.StringVar(date_rdg)
    month_fltr.set('Month')

    month_opt = ttk.OptionMenu(date_rdg, month_fltr, *month_lst)
    month_opt.place(relx=.01, rely=.17, relwidth=.3)

    # SEPERATER FOR MONTH --- 

    sep1 = tk.Label(date_rdg, bg='#C9AD95', text='/')
    sep1.config(font=(16))
    sep1.place(relx=.3, rely=.1)

    # OPTION BOX FOR DAYS --- 

    day_lst = [

        'Day', '01', '02', '03', '04',
        '05', '06', '07', '08', '09',
        '10', '11', '12', '13', '14',
        '15', '16', '17', '18', '19',
        '20', '21', '22', '23', '24',
        '25', '26', '27', '28', '29',
        '30', '31'

    ]

    day_fltr = tk.StringVar(date_rdg)
    day_fltr.set('Day')

    day_opt = ttk.OptionMenu(date_rdg, day_fltr, *day_lst)
    day_opt.place(relx=.36, rely=.17, relwidth=.25)

    # SERPATOR FOR THE DAY --- 

    sep2 = tk.Label(date_rdg, bg='#C9AD95', text='/')
    sep2.config(font=(16))
    sep2.place(relx=.6, rely=.1)

    # OPTION FOR THE YEAR --- 

    yr_lst = [

        'Year', '2022', '2023', '2024', '2025'

    ]

    yr_fltr = tk.StringVar(date_rdg)
    yr_fltr.set('Year')

    yr_opt = ttk.OptionMenu(date_rdg, yr_fltr, *yr_lst)
    yr_opt.place(relx=.64, rely=.17, relwidth=.3)

    # RMA NUMBER --- 

    rma_numRdg = tk.Label(date_rmaLbl, bg='#C9AD95', relief='ridge')
    rma_numRdg.place(relx=.72, rely=.2, relwidth=.27, relheight=.7)

    rma_numEnt = tk.Entry(rma_numRdg, bd=3, relief='sunken')
    rma_numEnt.place(relx=.03, rely=.15, relwidth=.94)

    rma_ttl = tk.Label(date_rmaLbl, bg='#C9AD95', text='RMA Number')
    rma_ttl.place(relx=.75, rely=.1, relheight=.17)

    # SEPERATOR FOR QUESTIONS --- 

    ques_sep = tk.Label(cntp_info2, bd=3, bg='#BF833C', relief='ridge')
    ques_sep.place(relx=.02, rely=.89, relwidth=.34, relheight=.01)

    # QUESTION FRAME 1 AND 2 --- 

    ques_frm1 = tk.Frame(rma_tpl, bg='#81781C')
    ques_frm1.place(relx=.02, rely=.41, relwidth=.44, relheight=.43)

    ques_frm2 = tk.Frame(ques_frm1, bg='#BF833C', bd=3)
    ques_frm2.place(relx=.01, relwidth=.98, relheight=.99)

    # RIDGE FOR QUESTION 1 --- 

    ques1_rdg = tk.Label(ques_frm2, bg='#BF833C', relief='ridge')
    ques1_rdg.place(relx=.1, relwidth=.62, relheight=.18)

    # QUESTION 1 LABEL --- 

    ques1_lbl = tk.Label(ques1_rdg, bg='#CF8F44', text='What kind\nof OS')
    ques1_lbl.place(relx=.02, rely=.1)

    # QUESTION 1 OPTION BOX --- 

    ques1_lst = [

        'Answer', 'Mac', 'PC'

    ]

    ques1_fltr = tk.StringVar(ques1_rdg)
    ques1_fltr.set('Answer')

    ques1_opt = ttk.OptionMenu(ques1_rdg, ques1_fltr, *ques1_lst)
    ques1_opt.place(relx=.51, rely=.2, relwidth=.38)

    # RIDGE FOR QUESTION 2 --- 

    ques2_rdg = tk.Label(ques_frm2, bg='#BF833C', relief='ridge')
    ques2_rdg.place(relx=.1, rely=.24, relwidth=.62, relheight=.18)

    # QUESTION 2 LABEL --- 

    ques2_lbl = tk.Label(ques2_rdg, bg='#CF8F44', text='Permission\nto Reformat')
    ques2_lbl.place(relx=.02, rely=.1)

    # QUESTION 2 OPTION BOX --- 

    ques2_lst = [

        'Answer', 'Yes', 'No', 'Other'

    ]

    ques2_fltr = tk.StringVar(ques2_rdg)
    ques2_fltr.set('Answer')

    ques2_opt = ttk.OptionMenu(ques2_rdg, ques2_fltr, *ques2_lst)
    ques2_opt.place(relx=.51, rely=.2, relwidth=.38)

    # QUESTION 3 RIDGE --- 

    ques3_rdg = tk.Label(ques_frm2, bg='#BF833C', relief='ridge')
    ques3_rdg.place(relx=.1, rely=.48, relwidth=.62, relheight=.18)

    # QUESTION 3 LABEL --- 

    ques3_lbl = tk.Label(ques3_rdg, bg='#CF8F44', text='Residential\nor Company')
    ques3_lbl.place(relx=.02, rely=.1)

    # QUESTION 3 OPTION BOX --- 

    ques3_lst = [

        'Answer', 'Resident', 'Company'

    ]

    ques3_fltr = tk.StringVar(ques3_rdg)
    ques3_fltr.set('Answer')

    ques3_opt = ttk.OptionMenu(ques3_rdg, ques3_fltr, *ques3_lst)
    ques3_opt.place(relx=.51, rely=.2, relwidth=.38)

    # SUBMIT BUTTON RIDGE --- 

    rma_subRdg = tk.Label(ques_frm2, bg='#BF833C', relief='ridge')
    rma_subRdg.place(relx=.47, rely=.76, relwidth=.34, relheight=.14)

    # SUBMIT RMA FORM BUTTON --- 

    rma_subut = tk.Button(rma_subRdg, bg='#D6AB79', text='Submit', command=lambda: submit_rma())
    rma_subut.place(relwidth=1, relheight=1)

    # QUERY FRAME 1 & 2--- 

    qry_frm1 = tk.Frame(rma_tpl, bg='#81781C', bd=3)
    qry_frm1.place(relx=.4, rely=.41, relwidth=.58, relheight=.06)

    qry_frm2 = tk.Frame(qry_frm1, bg='#A7A16A', bd=3)
    qry_frm2.place(relwidth=1, relheight=1)

    # QUERY OPTION BOX --- 

    qryOpt_lst = [

        'Name / Company', 'Name / Company', 'Address', 'City',
        'State', 'Zip Code', 'Email', 'Phone', 'RMA Number',
        'Invoice Number', 'Part Number', 'Serial Number'

    ]

    qryOpt_fltr = tk.StringVar(qry_frm2)
    qryOpt_fltr.set('Name / Company')

    qry_opt = ttk.OptionMenu(qry_frm2, qryOpt_fltr, *qryOpt_lst)
    qry_opt.place(rely=.1, relwidth=.27)

    # QUERY ENTRY BOX --- 

    qry_ent = tk.Entry(qry_frm2, bd=3, relief='flat')
    qry_ent.place(relx=.28, rely=.1, relwidth=.43)

    # QUERY BUTTON --- 

    qry_but = tk.Button(qry_frm2, bg='#D6D4B7', text='Search', command=lambda: query_rma(et_sql, rma_tree))
    qry_but.place(relx=.72, rely=.1, relwidth=.28)

    # TREE FOR RMA DISPLAY --- 

    rma_tree = ttk.Treeview(rma_tpl)
    rma_tree.place(relx=.4, rely=.47, relwidth=.58, relheight=.49)

    # YSCROLL FOR TREE DISPLAY --- 

    rma_scrly = tk.Scrollbar(rma_tree, orient='vertical', command=rma_tree.yview)
    rma_scrly.place(relx=.97, relwidth=.03, relheight=1)

    rma_tree.config(yscrollcommand=rma_scrly.set)

    # XSCROLL FOR TREE DISPLAY --- 

    rma_scrlx = tk.Scrollbar(rma_tree, orient='horizontal', command=rma_tree.xview)
    rma_scrlx.place(rely=.94, relwidth=.97)

    rma_tree.config(xscrollcommand=rma_scrlx.set)

    while True:
        rma_tpl.update()


def inventory(sql):
    # INVENTORY GUI ---

    # FUNCTION TO QUERY INVENTORY --- 

    def inv_ftch():
        # DELETE TREE --- 

        global dF, mnF, yF
        for del_ in inv_tree.get_children():
            inv_tree.delete(del_)

        # FETCHING HARD DRIVE TABLES FROM ROCKTICK.DB --- 

        # STARTING CURSOR FOR FETCHING INVENTORY --- 

        inv_ftchCurs = sql.cursor()

        inv_exe = inv_ftchCurs.execute("SELECT rowid, * FROM hard_drive").fetchall()

        # HARD DRIVE TABLE INSERTED INTO INVENTORY TABLE --- 

        inv_tree['column'] = ('Index', 'Date of Manufactuer', 'Brands', 'Part Number',
                              'Serial Number', 'Size', 'Type', 'Connection', 'Firmware Number', 'Capacity')

        inv_tree['show'] = 'headings'

        for inv_col in inv_tree['column']:
            inv_tree.heading(inv_col, text=inv_col)

        # FUNCTION FOR "NO RESULTS FOUND" IN TREEVIEW --- 

        def inv_no():
            n = 1
            inv_tree.insert("", "end", values=(
                n, 'Sorry Couldnt Find Hard Drive.....')
                            )

        # FUNCTION FOR INVENTORY TREE RESULTS ---

        def inv_rslts(rn, in_):
            inv_tree.insert("", "end", values=(
                rn, in_[1], in_[2], in_[3], in_[4], in_[5],
                in_[6], in_[7], in_[8], in_[9])
                            )

        # INTEGER VALUE FOR TREEVIEW INDEX ---

        inv_num = 0

        # BOLEAN FOR NO DATE VALUES DETECTED --- 

        inv_bol2 = True

        # ATTEMPT TO GRAB DATE VALUES FOR INVENTORY MAIN MENU --- 

        try:
            mnF = int(monthInv_fltr.get())
            dF = int(dayInv_fltr.get())
            yF = int(yrInv_fltr.get())

        except:
            inv_bol2 = False

        for inv_in in inv_exe:
            # DATE VALUES FROM HARD DRIVE TABLE SEPERATED BY 'MONTH' / 'DATE' / 'YEAR' --- 

            invRm = int(inv_in[1][:2])
            invRd = int(inv_in[1][3:5])
            invRy = int(inv_in[1][6:10])

            # STATEMENT IF NO DATES ARE DETECTED BY BOLEAN --- 

            if inv_bol2 == False:
                break

            # DETECTING DATES FROM MAIN INVENTORY MENU FILTER --- 

            if dF > invRd or dF < invRd or dF == invRd:
                if mnF > invRm or mnF == invRm:
                    if yF > invRy or yF == invRy:

                        if filter_value.get() == 'Brand':
                            brnQv = inv_in[2]
                            brnQl = brnQv.lower()

                            if brnQl.find(inv_srch_ent.get()) != -1:
                                inv_num += 1
                                inv_rslts(inv_num, inv_in)

                        elif filter_value.get() == 'Part Number':
                            pnQv = inv_in[3]
                            pnQl = pnQv.upper()

                            if pnQl.find(inv_srch_ent.get().upper()) != -1:
                                inv_num += 1
                                inv_rslts(inv_num, inv_in)

                        elif filter_value.get() == 'Serial Number':
                            snQv = inv_in[4]
                            snQl = snQv.upper()
                            get1 = inv_srch_ent.get().upper()

                            if snQl.find(get1) != -1:
                                inv_num += 1
                                inv_rslts(inv_num, inv_in)

                        elif filter_value.get() == 'Firmware Number':
                            fnQv = inv_in[8]

                            if fnQv == inv_srch_ent.get().upper():
                                inv_num += 1
                                inv_rslts(inv_num, inv_in)

                        elif filter_value.get() == 'Type':
                            typQv = inv_in[6]
                            typQl = typQv.lower()

                            if typQl.find(inv_srch_ent.get()) != -1:
                                inv_num += 1
                                inv_rslts(inv_num, inv_in)

                        elif filter_value.get() == 'Size':
                            szQv = str(inv_in[5])

                            if szQv.find(inv_srch_ent.get()) != -1:
                                inv_num += 1
                                inv_rslts(inv_num, inv_in)

                        elif filter_value.get() == 'Connection':
                            cnQv = inv_in[7]
                            cnQl = cnQv.lower()

                            if cnQl.find(inv_srch_ent.get()) != -1:
                                inv_num += 1
                                inv_rslts(inv_num, inv_in)

                        elif filter_value.get() == 'Capacity':
                            if inv_in[9] == inv_srch_ent.get().upper():
                                inv_num += 1
                                inv_rslts(inv_num, inv_in)

        if inv_bol2 == False or inv_num == 0:
            inv_no()

    # FUNCTION FOR MENU: ADD HARD DRIVES / DELETE HARD DRIVES / CHECK OUT HARD DRIVES ---

    def inv_menu():
        # GUI FOR INVENTORY MENU --- 

        invM = tk.Toplevel()
        invM.title("Inventory Menu")
        invM.geometry("600x500")

        # CLOSE COULNT FIND HARD DRIVE WINDOW --- 

        def delete_gui(Ddrive):
            def cfhClose(close):
                close.destroy()

            # FUNCTION FOR SEARCHING RECORD TO DELETE ---

            def dele_srch():
                # FUNCTION FOR RECORD DELETE --- 

                def delete_hd(close):
                    # STARTING ROCKTICK.DB CURSOR --- 

                    dhd_curs = sql.cursor()

                    # FETCHING VALUES FROM HARD DRIVE TABLES ROCKTICK.DB --- 

                    dhdD_rslts = dhd_curs.execute("SELECT rowid, * FROM hard_drive").fetchall()

                    # DELETING RECORD FROM HARD DRIVE TABLES ROCTICK.DB --- 

                    for d_row in dhdD_rslts:
                        if dhd_ent.get().upper() == d_row[4]:
                            dhd_curs.execute("""DELETE FROM hard_drive WHERE rowid = """ + str(d_row[0]))

                    sql.commit()
                    close.destroy()

                # "DELETE" START SQL CURSOR ---

                dhdsrch_curs = sql.cursor()

                # INSERTING DATA FROM ROCKTICK.DB --- 

                dhd_rslts = dhdsrch_curs.execute("SELECT rowid, * FROM hard_drive").fetchall()

                dbool = True

                for d_rslt in dhd_rslts:
                    if dhd_ent.get().upper() == d_rslt[4]:

                        # "DELETE" WINDOW IF HARD DRIVE IS FOUND NOTIFICATION --- 

                        fhdw = tk.Toplevel()

                        # Gets the requested values of the height and widht.

                        fhdwww = fhdw.winfo_reqwidth()
                        fhdwwh = fhdw.winfo_reqheight()

                        # Gets both half the screen width/height and window width/height

                        fhdwpr = int(fhdw.winfo_screenwidth() / 2 - fhdwww / 2)
                        fhdwpd = int(fhdw.winfo_screenheight() / 2 - fhdwwh / 2)

                        # Positions the window in the center of the page.

                        fhdw.geometry("+{}+{}".format(fhdwpr, fhdwpd))
                        fhdw.title("Found Hard Drive")
                        fhdw.geometry("300x150")

                        # FRAME FOR QUESTION IF WANTING TO DELETE HARD DRIVE --- 

                        qdh1 = tk.Label(
                            fhdw, bg='#F7F6EE',
                            text='We Found Your Hard Drive \n Would you like to Delete from Inventory?', anchor='c')
                        qdh1.place(relx=.1, rely=.1, relwidth=.8, relheight=.3)

                        # "YES" BUTTON --- 

                        okbtt = ttk.Button(fhdw, text='Yes', command=lambda: delete_hd(fhdw))
                        okbtt.place(relx=.17, rely=.55, relwidth=.31, relheight=.2)

                        # "CANCEL" BUTTON --- 

                        cnclbtt = ttk.Button(fhdw, text='Cancel', command=lambda: cfhClose(fhdw))
                        cnclbtt.place(relx=.52, rely=.55, relwidth=.31, relheight=.2)

                        fhdw.mainloop()
                        break

                    else:
                        dbool = False

                if dbool == False:
                    dfhdw = tk.Toplevel()

                    # Gets the requested values of the height and widht.

                    windowWidth = dfhdw.winfo_reqwidth()
                    windowHeight = dfhdw.winfo_reqheight()

                    # Gets both half the screen width/height and window width/height

                    positionRight = int(dfhdw.winfo_screenwidth() / 2 - windowWidth / 2)
                    positionDown = int(dfhdw.winfo_screenheight() / 2 - windowHeight / 2)

                    # Positions the window in the center of the page.

                    dfhdw.geometry("+{}+{}".format(positionRight, positionDown))
                    dfhdw.title("Couldnt Find Hard Drive")
                    dfhdw.geometry("300x150")

                    # FRAME FOR QUESTION IF WANTING TO DELETE HARD DRIVE --- 

                    qdh2 = tk.Label(
                        dfhdw, bg='#F7F6EE',
                        text='Sorry but we couldnt find your hard drive\nplease try again...', anchor='c')
                    qdh2.place(relx=.1, rely=.17, relwidth=.8, relheight=.3)

                    cfhBtt = ttk.Button(dfhdw, text='OK', command=lambda: cfhClose(dfhdw))
                    cfhBtt.place(relx=.3, rely=.65, relwidth=.4, relheight=.2)

                    dfhdw.mainloop()

            # DELETE HARD DRIVE GUI ---

            # BACKGROUND IMAGE --- 

            dhd_png = tk.PhotoImage(file='upc_main.png')
            dhd_img = tk.Label(Ddrive, image=dhd_png)
            dhd_img.place(relwidth=1, relheight=1)

            # FRAME FOR SERIAL NUMBER ENTRY --- 

            dhd_frm = tk.Frame(Ddrive, bg='#374D65', bd=3)
            dhd_frm.place(relx=.15, rely=.4, relwidth=.7, relheight=.1)

            dhd_frm2 = tk.Frame(dhd_frm, bg='#A3B1C1', bd=3)
            dhd_frm2.place(relwidth=1, relheight=1)

            # "DELETE" ENTRY BOX --- 

            dhd_ent = tk.Entry(dhd_frm2, bd=3, relief='sunken', font=(4.5))
            dhd_ent.place(relx=.01, rely=.05, relwidth=.65, relheight=.9)

            # "DELETE" SEARCH BUTTTON ---

            dhd_but = tk.Button(dhd_frm2, bg='#F3F2EB', text='Delete', command=lambda: dele_srch())
            dhd_but.place(relx=.67, rely=.05, relwidth=.32, relheight=.9)

            # BACK TO MAIN MENU BUTTON FOR DELETE PAGE --- 

            bmmbdp = ttk.Button(Ddrive, text="Main Menu", command=lambda: inv_main())
            bmmbdp.place(relx=.7, rely=.03, relwidth=.25, relheight=.07)

            # "DELETE" TREEVIEW --- 

            # dhd_tree = tk.Text(Ddrive)
            # dhd_tree.place(relx=.05, rely=.2, relwidth=.9, relheight=.17)

            # DELETE BUTTON FRAME --- 

            '''dhd_frm = tk.Frame(Ddrive, bg='#374D65', bd=3)
            dhd_frm.place(relx=.3, rely=.55, relwidth=.35, relheight=.15)

            dhd_frm2 = tk.Frame(dhd_frm, bg='#A3B1C1', bd=3)
            dhd_frm2.place(relwidth=1, relheight=1)

            # "DELETE" BUTTON RIDGE --- 

            dhd_rdg  = tk.Label(dhd_frm2, bg='#A3B1C1', relief='ridge')
            dhd_rdg.place(relx=.02, rely=.15, relwidth=.96, relheight=.85)

            # "DELETE" BUTTON LABEL --- 

            dhd_lbl = tk.Label(dhd_frm2, bg='#A3B1C1', text='Delete Hard Drive?')
            dhd_lbl.place(relx=.18)

            # DELETE BUTTON --- 

            dhd_but2 = tk.Button(dhd_rdg, bg='#F3F2EB', text='Delete', command=lambda:delete_hd())
            dhd_but2.place(relx=.02, rely=.32, relwidth=.96, relheight=.66)'''

            # "DELETE" TEXT ENTRY DISPLAYING DELETE SUCCESS --- 

            # dhd_text = tk.Text(Ddrive)
            # dhd_text.place(relx=.25, rely=.74, relwidth=.45, relheight=.1)

            while True:
                Ddrive.update()

        # FUNCTION TO "ADD" HARD DRIVES TO DATABASE ---

        def add_drive(Adrive):
            # FUNCTION ACCESS ROCTICK.DB TO INSERT VALUES --- 

            def drive_insql():
                # FUNCTION FOR NOTIFICATION OF A DUPLICATE --- 

                def dup():
                    # FUNCTION TO CLOSE DUPLICATE NOTIFICATION WINDOW --- 

                    def dupcls(clse):
                        clse.destroy()

                    duptk = tk.Toplevel()

                    # Gets the requested values of the height and widht.

                    dpww = duptk.winfo_reqwidth()
                    dpwh = duptk.winfo_reqheight()

                    # Gets both half the screen width/height and window width/height

                    dppr = int(duptk.winfo_screenwidth() / 2 - dpww / 2)
                    dppd = int(duptk.winfo_screenheight() / 2 - dpwh / 2)

                    # Positions the window in the center of the page.

                    duptk.geometry("+{}+{}".format(dppr, dppd))
                    duptk.title("Duplicate Error")
                    duptk.geometry("300x150")

                    # FRAME FOR QUESTION IF WANTING TO DELETE HARD DRIVE --- 

                    dplb = tk.Label(
                        duptk, bg='#F7F6EE',
                        text='Sorry but this hard drive is already in\n inventory, please try again later, ',
                        anchor='c')
                    dplb.place(relx=.1, rely=.17, relwidth=.8, relheight=.3)

                    dpbtt = ttk.Button(duptk, text='OK', command=lambda: dupcls(duptk))
                    dpbtt.place(relx=.3, rely=.65, relwidth=.4, relheight=.2)

                    duptk.mainloop()

                # STARTING SQL CURSOR FOR INVENTORY ---

                inv_curs = sql.cursor()

                # CREATING TABLE IN ROCKTICK.DB --- 

                inv_table = """

                CREATE TABLE hard_drive(

                'DOM' TEXT,
                'BRANDS' TEXT,
                'PART_NUMBER' TEXT,
                'SERIAL_NUMBER' TEXT,
                'SIZE' TEXT,
                'TYPE' TEXT,
                'CONNECTION_TYPE' TEXT, 
                'FIRMWARE_NUMBER' TEXT,
                'CAPACITY' TEXT

                )"""

                try:
                    inv_curs.execute(inv_table)

                except:
                    print('')

                # STORING VALUES IN DICTIONARY --- 

                # DATE OF MANUFACTUER VALUE --- 

                mnthINVval = mnthADHfltr.get()
                dayINVval = dayADHfltr.get()
                yrINVval = yrADHfltr.get()

                dateINVval = mnthINVval + '/' + dayINVval + '/' + yrINVval

                # "ADD" TYPE OF HARD DRIVE VALUE --- 

                typInv_val = typAD_fltr.get()

                # "ADD" SIZE OF PHYSICAL HARD DRIVE VALUE --- 

                szInv_val = szADfltr.get()

                # "ADD" CONNECTION TYPE VALUE --- 

                ctyp_val = ctyp_fltr.get()

                # CAPACITY VALUE --- 

                capINVvalue = capADHfltr.get()

                # BRANDS VALUE --- 

                brndINVvalue = brndADHent.get()
                brndADHent.delete(0, "end")

                # PART NUMBER VALUE --- 

                pnINVvalue = pnADHent.get()
                pnADHent.delete(0, "end")

                # SERIAL NUMBER VALUE --- 

                snINVvalue = snADHent.get()
                snADHent.delete(0, "end")

                # FIRMWARE NUMBER VALUE --- 

                fwINVvalue = fwAD_ent.get()
                fwAD_ent.delete(0, 'end')

                # DICTIONARY TO STORE VALUES --- 

                inv_dict = {

                    'DOM': [dateINVval],
                    'BRANDS': [brndINVvalue],
                    'PART_NUMBER': [pnINVvalue],
                    'SERIAL_NUMBER': [snINVvalue],
                    'SIZE': [szInv_val],
                    'TYPE': [typInv_val],
                    'CONNECTION_TYPE': [ctyp_val],
                    'FIRMWARE_NUMBER': [fwINVvalue],
                    'CAPACITY': [capINVvalue]

                }

                # PLACE DICTIONARY VALUES IN DATAFRAME --- 

                df_inv = pd.DataFrame(inv_dict)

                # ACCESSING HARD DRIVE TABLE IN ROCKTICK DATABASE TO CHECK FOR ANY DUPLICATES --- 

                ahdtrdcd = inv_curs.execute("SELECT rowid, * FROM hard_drive").fetchall()

                # STATEMENT IN PLACE TO CHECK IF HARD DRIVE IS IN INVENTORY --- 

                schdbl = False

                for spchdiF in ahdtrdcd:
                    if snINVvalue.upper() == spchdiF[4]:
                        dup()
                        schdbl = True
                        break

                if schdbl == False:
                    # INSERTING DATA IN HARD DRIVE TABLES --- 

                    for inv_ in range(len(df_inv)):
                        inv_row = df_inv.iloc[inv_]
                        inv_curs.execute("INSERT INTO hard_drive VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", inv_row)

                sql.commit()

            # "ADD" HARD DRIVE GUI ---

            ahd_png = tk.PhotoImage(file='Capture.png')
            ahd_img = tk.Label(Adrive, image=ahd_png)
            ahd_img.place(relwidth=1, relheight=1)

            # "ADD" FRAME FOR DATE OF MANUFACTUERING --- 

            domAHDfrm = tk.Frame(Adrive, bg='#504B7E', bd=3)
            domAHDfrm.place(relx=.01, rely=.01, relwidth=.55, relheight=.17)

            domAHDfrm2 = tk.Frame(domAHDfrm, bg='#C9BFCA', bd=3)
            domAHDfrm2.place(relwidth=1, relheight=1)

            # "ADD" DATE OF MANUFACTURING RIDGE --- 

            domADHrdg = tk.Label(domAHDfrm2, bg='#C9BFCA', relief='ridge')
            domADHrdg.place(relx=.02, rely=.2, relwidth=.96, relheight=.76)

            # "ADD" DATE OF MANUFACTURING LABEL --- 

            domADHlbl = tk.Label(domAHDfrm2, bg='#C9BFCA', text='Date of Manufactuering')
            domADHlbl.place(relx=.06)

            # "ADD" MONTH OPTION BOX --- 

            mnthADHlst = [

                'Month', '00', '01', '02', '03', '04',
                '05', '06', '07', '08',
                '09', '10', '11', '12'

            ]

            mnthADHfltr = tk.StringVar(domADHrdg)

            mnthADHopt = ttk.OptionMenu(domADHrdg, mnthADHfltr, *mnthADHlst)
            mnthADHopt.place(relx=.02, rely=.2, relwidth=.28, relheight=.5)

            # "ADD" DAY OPTION BOX --- 

            dayADHlst = [

                'Day', '00', '01', '02', '03', '04',
                '05', '06', '07', '08', '09',
                '10', '11', '12', '13', '14',
                '15', '16', '17', '18', '19',
                '20', '21', '22', '23', '24',
                '25', '26', '27', '28', '29',
                '30', '31'

            ]

            dayADHfltr = tk.StringVar(domADHrdg)

            dayADHopt = ttk.OptionMenu(domADHrdg, dayADHfltr, *dayADHlst)
            dayADHopt.place(relx=.34, rely=.2, relwidth=.28, relheight=.5)

            # "ADD" YEAR OPTION BOX --- 

            yrADHlst = [

                'Year', '0000', '2023', '2022', '2021', '2020', '2019',
                '2018', '2017', '2016', '2015', '2014',
                '2013', '2012'

            ]

            yrADHfltr = tk.StringVar(domADHrdg)

            yrADHopt = ttk.OptionMenu(domADHrdg, yrADHfltr, *yrADHlst)
            yrADHopt.place(relx=.66, rely=.2, relwidth=.32, relheight=.5)

            # "ADD" CAPACITY FRAME --- 

            capADHfrm = tk.Frame(Adrive, bg='#374D65', bd=3)
            capADHfrm.place(relx=.74, rely=.18, relwidth=.23, relheight=.1)

            capADHfrm2 = tk.Frame(capADHfrm, bg='#A3B1C1', bd=3)
            capADHfrm2.place(relwidth=1, relheight=1)

            # "ADD" CAPACITY OPTION BOX --- 

            capADHlst = [

                'Capacity', '500GB', '1TB', '2TB', '3TB', '4TB',
                '5TB', '6TB', '7TB', '8TB', '9TB', '10TB',
                '11TB', '12TB', '13TB', '14TB', '15TB', '16TB',
                '17TB', '18TB', '20TB'

            ]

            capADHfltr = tk.StringVar(capADHfrm2)

            capADHopt = ttk.OptionMenu(capADHfrm2, capADHfltr, *capADHlst)
            capADHopt.place(relx=.02, rely=.05, relwidth=.96, relheight=.9)

            # "ADD" TYPE OF HARD DRIVE FRAME --- 

            typAD_frm = tk.Frame(Adrive, bg='#374D65', bd=3)
            typAD_frm.place(relx=.02, rely=.18, relwidth=.23, relheight=.1)

            typAD_frm2 = tk.Frame(typAD_frm, bg='#A3B1C1', bd=3)
            typAD_frm2.place(relwidth=1, relheight=1)

            # "ADD" TYPE OF HARD DRIVE OPTION BOX --- 

            typAD_lst = ['Type', 'HDD', 'SSD']

            typAD_fltr = tk.StringVar(typAD_frm2)

            typAD_opt = ttk.OptionMenu(typAD_frm2, typAD_fltr, *typAD_lst)
            typAD_opt.place(relwidth=1, relheight=1)

            # "ADD" CONNECTION TYPE FRAME --- 

            ctypAD_frm = tk.Frame(Adrive, bg='#374D65', bd=3)
            ctypAD_frm.place(relx=.5, rely=.18, relwidth=.23, relheight=.1)

            ctypAD_frm2 = tk.Frame(ctypAD_frm, bg='#A3B1C1', bd=3)
            ctypAD_frm2.place(relwidth=1, relheight=1)

            # "ADD" CONNECTION TYPE OPTION BOX --- 

            ctyp_lst = [

                'Connection', 'SATA', 'SAS'

            ]

            ctyp_fltr = tk.StringVar(ctypAD_frm2)

            ctyp_opt = ttk.OptionMenu(ctypAD_frm2, ctyp_fltr, *ctyp_lst)
            ctyp_opt.place(relx=.02, rely=.05, relwidth=.96, relheight=.9)

            # "ADD" SIZE OF PHYSICAL HARD DRIVE FRAME --- 

            szADfrm = tk.Frame(Adrive, bg='#374D65', bd=3)
            szADfrm.place(relx=.26, rely=.18, relwidth=.23, relheight=.1)

            szADfrm2 = tk.Frame(szADfrm, bg='#A3B1C1', bd=3)
            szADfrm2.place(relwidth=1, relheight=1)

            # "ADD" SIZE OF PHYSICAL HARD DRIVE OPTION BOX --- 

            szADlst = [

                'Size', '5400', '7200'

            ]

            szADfltr = tk.StringVar(szADfrm2)

            szADopt = ttk.OptionMenu(szADfrm2, szADfltr, *szADlst)
            szADopt.place(relx=.02, rely=.05, relwidth=.96, relheight=.9)

            # "ADD" BRANDS FRAME --- 

            brndADHfrm = tk.Frame(Adrive, bg='#374D65', bd=3)
            brndADHfrm.place(relx=.08, rely=.28, relwidth=.45, relheight=.14)

            brndADHfrm2 = tk.Frame(brndADHfrm, bg='#A3B1C1', bd=3)
            brndADHfrm2.place(relwidth=1, relheight=1)

            # "ADD" BRANDS RIDGE --- 

            brndADHrdg = tk.Label(brndADHfrm2, bg='#A3B1C1', relief='ridge')
            brndADHrdg.place(relx=.03, rely=.2, relwidth=.94, relheight=.77)

            # "ADD" BRANDS ENTRY BOX --- 

            brndADHent = tk.Entry(brndADHrdg, bd=3, relief='sunken')
            brndADHent.place(relx=.02, rely=.1, relwidth=.96, relheight=.8)

            # "ADD" BRANDS LABEL --- 

            brndADHlbl = tk.Label(brndADHfrm2, bg='#A3B1C1', text='Brand')
            brndADHlbl.place(relx=.06, rely=.1, relheight=.22)

            # "ADD" SN AND PN FRAME --- 

            spnADHfrm = tk.Frame(Adrive, bg='#374D65', bd=3)
            spnADHfrm.place(relx=.1, rely=.42, relwidth=.43, relheight=.45)

            spnADHfrm2 = tk.Frame(spnADHfrm, bg='#A3B1C1', bd=3)
            spnADHfrm2.place(relwidth=1, relheight=1)

            # "ADD" PN RIDGE --- 

            pnADHrdg = tk.Label(spnADHfrm2, bg='#A3B1C1', relief='ridge')
            pnADHrdg.place(relx=.03, rely=.08, relwidth=.7, relheight=.23)

            # "ADD" PN ENTRY --- 

            pnADHent = tk.Entry(pnADHrdg, bd=3, relief='sunken')
            pnADHent.place(relx=.02, rely=.18, relwidth=.96, relheight=.66)

            # "ADD" PN LABEL --- 

            pnADHlbl = tk.Label(spnADHfrm2, bg='#A3B1C1', text='Part Number')
            pnADHlbl.place(relx=.05)

            # "ADD" SN RIDGE --- 

            snADHrdg = tk.Label(spnADHfrm2, bg='#A3B1C1', relief='ridge')
            snADHrdg.place(relx=.03, rely=.39, relwidth=.7, relheight=.23)

            # "ADD" SN ENTRY --- 

            snADHent = tk.Entry(snADHrdg, bd=3, relief='sunken')
            snADHent.place(relx=.02, rely=.18, relwidth=.96, relheight=.66)

            # "ADD" SN LABEL --- 

            snADHlbl = tk.Label(spnADHfrm2, bg='#A3B1C1', text='Serial Number')
            snADHlbl.place(relx=.05, rely=.33, relheight=.08)

            # "ADD" FIRMWARE RIDGE --- 

            fwAD_rdg = tk.Label(spnADHfrm2, bg='#A3B1C1', relief='ridge')
            fwAD_rdg.place(relx=.03, rely=.7, relwidth=.7, relheight=.23)

            # "ADD" FIRMWARE ENTRY --- 

            fwAD_ent = tk.Entry(fwAD_rdg, bd=3, relief='sunken')
            fwAD_ent.place(relx=.02, rely=.18, relwidth=.96, relheight=.66)

            # "ADD" FIRMWARE LABEL --- 

            fwAD_lbl = tk.Label(spnADHfrm2, bg='#A3B1C1', text='Firmware Number')
            fwAD_lbl.place(relx=.05, rely=.65, relheight=.08)

            # "ADD" BUTTON FRAME --- 

            butADHfrm = tk.Frame(Adrive, bg='#374D65', bd=3)
            butADHfrm.place(relx=.15, rely=.84, relwidth=.33, relheight=.12)

            butADHfrm2 = tk.Frame(butADHfrm, bg='#A3B1C1', bd=3)
            butADHfrm2.place(relwidth=1, relheight=1)

            # "ADD" SUBMIT BUTTON --- 

            adh_but = tk.Button(butADHfrm2, bg='#F7F4DF', text='Add Drive', command=lambda: drive_insql())
            adh_but.place(relx=.05, rely=.05, relwidth=.9, relheight=.9)

            # BACK TO INVENTORY MENU BUTTON --- 

            btimb = ttk.Button(Adrive, text="Main Menu", command=lambda: inv_main())
            btimb.place(relx=.7, rely=.03, relwidth=.25, relheight=.07)

            while True:
                Adrive.update()

        # FUNCTION FOR CHECKING OUT HARD DRIVES FOR INVENTORY ---

        def chkout(chk):
            # FUNCTION TO QUERY DRIVE AND STORE IN CHECKED OUT TABLE IN ROCKTICK DATABASE --- 

            def chkqry():
                # ACTIVATING SQL CURSOR FOR CHECKOUT TABLE IN ROCKTICK DATABASE --- 

                chkdb = sql.cursor()

                # CREATING TABLE IN ROCKTICK.DB --- 

                chktbl = """

                CREATE TABLE CHK(

                'DOM' TEXT,
                'BRANDS' TEXT,
                'PART_NUMBER' TEXT,
                'SERIAL_NUMBER' TEXT,
                'SIZE' TEXT,
                'TYPE' TEXT,
                'CONNECTION_TYPE' TEXT, 
                'FIRMWARE_NUMBER' TEXT,
                'CAPACITY' TEXT

                )"""

                try:
                    chkdb.execute(chktbl)

                except:
                    print('')

                # CLOSING TREEVIEW FOR CHECK OUT / IN RESULTS --- 

                for chkdl in chktree.get_children():
                    chktree.delete(chkdl)

                chktree['column'] = ('Index', 'Date of Manufactuer', 'Brands', 'Part Number',
                                     'Serial Number', 'Size', 'Type', 'Connection', 'Firmware Number', 'Capacity')

                chktree['show'] = 'headings'

                for chkh in chktree['column']:
                    chktree.heading(chkh, text=chkh)

                # FUNCTION TO SHOW CHECK OUT / IN QUERY RESULTS IN TREEVIEW --- 

                def chkqt(coin, dbchk):
                    chktree.insert("", "end", values=(str(coin), dbchk[1], dbchk[2], dbchk[3],
                                                      dbchk[4], dbchk[5], dbchk[6], dbchk[7], dbchk[8], dbchk[9]))

                # FUNCTION FOR CLOSING ERROR NOTIFICATION WINDOW

                def chkcls(cerw):
                    cerw.destroy()

                # ACCESSING HARD DRIVE TABLE IN ROCKTICK DATABASE ---

                hddb = chkdb.execute("SELECT rowid, * FROM hard_drive").fetchall()

                # STATEMENT TO ACTIVATE CHECK OUT OPTIONS --- 

                if obcociStr.get() == "Check Out":
                    # STATEMENT FOR ENTRY BOX TO CHECK OUT SPECIFIC HARD DRIVE ---

                    for hddbF in hddb:
                        if ecoii.get().upper() == hddbF[4]:
                            # CREATING DICTIONARY TO STORE CHECKED OUT HARD DRIVE INTO CHK 
                            # TABLE IN ROCKTICK DATABASE --- 

                            chkqdic = {

                                'DOM': [hddbF[1]],
                                'BRANDS': [hddbF[2]],
                                'PART_NUMBER': [hddbF[3]],
                                'SERIAL_NUMBER': [hddbF[4]],
                                'SIZE': [hddbF[5]],
                                'TYPE': [hddbF[6]],
                                'CONNECTION_TYPE': [hddbF[7]],
                                'FIRMWARE_NUMBER': [hddbF[8]],
                                'CAPACITY': [hddbF[9]]

                            }

                            # STORING CHECKED OUT DICTIONARY IN DATAFRAME --- 

                            df_chkq = pd.DataFrame(chkqdic)

                            # STORING CHECKOUT HARD DRIVE IN CHK TABLE IN ROCKTICK DATABASE --- 

                            for chkstor in range(len(df_chkq)):
                                chkstR = df_chkq.iloc[chkstor]
                                chkdb.execute("INSERT INTO CHK VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", chkstR)

                            # DELETING HARD DRIVE FROM HARD DRIVE TABLE IN ROCKTICK DATABASE --- 

                            chkdb.execute("""DELETE FROM hard_drive WHERE rowid = """ + str(hddbF[0]))
                            break

                # ACCESSING CHK TABLE IN ROCKTICK DATABASE --- 

                chkfch = chkdb.execute("SELECT rowid, * FROM CHK").fetchall()

                # STATEMENT FOR CHECKED IN ITEMS --- 

                if obcociStr.get() == "Check In":
                    for chk2 in chkfch:
                        if ecoii.get().upper() == chk2[4]:
                            # CREATING DICTIONARY FOR STORING CHECKED IN ITEMS INTO HARD DRIVE IN 
                            # ROCKTICK DATABASE --- 

                            cdsdic = {

                                'DOM': [chk2[1]],
                                'BRANDS': [chk2[2]],
                                'PART_NUMBER': [chk2[3]],
                                'SERIAL_NUMBER': [chk2[4]],
                                'SIZE': [chk2[5]],
                                'TYPE': [chk2[6]],
                                'CONNECTION_TYPE': [chk2[7]],
                                'FIRMWARE_NUMBER': [chk2[8]],
                                'CAPACITY': [chk2[9]]

                            }

                            # STORING CHECKED IN QUERY RESULTS INSIDE DICTIONARY TO DATAFRAME --- 

                            dfcds = pd.DataFrame(cdsdic)

                            # STORING DATAFRAME INSIDE HARD DRIVE TABLE IN ROCKTICK DATABASE --- 

                            for sdihd in range(len(dfcds)):
                                sdir = dfcds.iloc[sdihd]
                                chkdb.execute("INSERT INTO hard_drive VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", sdir)

                            # DELETING ROW IN CHK TABLE IN ROCKTICK DATABASE --- 

                            chkdb.execute("DELETE FROM CHK WHERE rowid = " + str(chk2[0]))

                # ACCESSING CHK TABLE IN ROCKTICK DATABASE --- 

                chkfech = chkdb.execute("SELECT rowid, * FROM CHK").fetchall()

                # DISPLAYING CURRENT CHECKOUT RESULTS IN TREEVIEW ---

                chkn1 = 0
                for chk3 in chkfech:
                    chkn1 += 1
                    chkqt(chkn1, chk3)

                sql.commit()

            # BACKGROUND IMAGE FOR CHECKOUT PAGE ---

            bifcp = tk.PhotoImage(file="chk.png")
            bifcp2 = tk.Label(chk, image=bifcp)
            bifcp2.place(relwidth=1, relheight=1)

            # FRAME TREE VIEW FOR CHECKED OUT HARD DRIVES --- 

            ftvcohd = tk.Frame(chk, bg="#4B636C", bd=3)
            ftvcohd.place(relx=.1, rely=.25, relwidth=.8, relheight=.08)
            ftvcohd2 = tk.Frame(ftvcohd, bg="#9FA7B7", bd=3)
            ftvcohd2.place(relwidth=1, relheight=1)

            # OPTION BOX FOR CHECKED OUT / CHECK IN --- 

            obcociLs = [

                "Check Out", "Check Out", "Check In"

            ]

            obcociStr = tk.StringVar(ftvcohd2)

            opcoci = ttk.OptionMenu(ftvcohd2, obcociStr, *obcociLs)
            opcoci.place(relwidth=.2, relheight=1)

            # ENTRY FOR CHECKING OUT / IN INVENTORY --- 

            ecoii = tk.Entry(ftvcohd2, relief="flat")
            ecoii.config(font=("Calibri", 12))
            ecoii.place(relx=.21, relwidth=.53, relheight=1)

            # SUBMIT BUTTON TO CHECK OUT / IN INVENTORY --- 

            sbcoii = ttk.Button(ftvcohd2, text="Submit", command=lambda: chkqry())
            sbcoii.place(relx=.75, relwidth=.25, relheight=1)

            # TREEVIEW TO SEE WHICH HARD DRIVES ARE CHECKED OUT / IN --- 

            chktree = ttk.Treeview(chk)
            chktree.place(relx=.1, rely=.33, relwidth=.77, relheight=.5)

            # Y SCROLL FOR CHECK OUT / IN TREEVIEW --- 

            ysclcoit = tk.Scrollbar(chk, orient="vertical", command=chktree.yview)
            chktree.config(yscrollcommand=ysclcoit.set)
            ysclcoit.place(relx=.87, rely=.33, relwidth=.03, relheight=.5)

            # X SCROLL FOR CHECK OUT / IN --- 

            xsclcoit = tk.Scrollbar(chk, orient="horizontal", command=chktree.xview)
            chktree.config(xscrollcommand=xsclcoit.set)
            xsclcoit.place(relx=.1, rely=.83, relwidth=.8, relheight=.04)

            # BACK TO INVENTORY MENU BUTTON FOR CHECKED OUT PAGE--- 

            btimbcop = ttk.Button(chk, text="Main Menu", command=lambda: inv_main())
            btimbcop.place(relx=.7, rely=.03, relwidth=.25, relheight=.07)

            while True:
                chk.update()

        def inv_main():
            # BACGROUND FOR INVENTORY MENU --- 

            bfim = tk.PhotoImage(file="inv_m.png")
            bfim2 = tk.Label(invM, image=bfim)
            bfim2.place(relwidth=1, relheight=1)

            # FRAME FOR MENU OPTION BUTTONS --- 

            fmob = tk.Frame(invM, bg="#2C4A6C", bd=3)
            fmob.place(relx=.1, rely=.35, relwidth=.8, relheight=.2)
            fmob2 = tk.Frame(fmob, bg="#8191A4", bd=4)
            fmob2.place(relwidth=1, relheight=1)

            # BUTTON FOR ADDING HARD DRIVE TO INVENTORY --- 

            bahdi = ttk.Button(fmob2, text="Add Hard Drive\n   to Inventory", command=lambda: add_drive(invM))
            bahdi.place(relx=.02, rely=.03, relwidth=.3, relheight=.94)

            # BUTTON FOR DELETING HARD DRIVE FROM INVENTORY --- 

            bdhdi = ttk.Button(fmob2, text="Delete Hard Drive\n from Inventory", command=lambda: delete_gui(invM))
            bdhdi.place(relx=.35, rely=.03, relwidth=.3, relheight=.94)

            # BUTTON FOR CHECKING OUT HARD DRIVES FROM INVENTORY --- 

            bcohdi = ttk.Button(fmob2, text="Check Out\n Hard Drive", command=lambda: chkout(invM))
            bcohdi.place(relx=.68, rely=.03, relwidth=.3, relheight=.94)

            while True:
                invM.update()

        inv_main()

    # GUI ---

    inv_root = tk.Toplevel()

    inv_root.title('Inventory')
    inv_root.geometry("1000x800")

    # BACKGROUND FOR MAIN MENU ---

    inv_back_image = tk.PhotoImage(file='Capture.png')
    inv_back_label = tk.Label(inv_root, image=inv_back_image)
    inv_back_label.place(relwidth=1, relheight=1)

    # TITLE FRAME ---

    inv_ttl_frame = tk.Frame(inv_root, bg='#A56239', bd=3)
    inv_ttl_frame.place(relx=.02, rely=.03, relwidth=.22, relheight=.09)

    # TITLE IMAGE ---

    inv_ttl_img = tk.PhotoImage(file='image001.png')
    inv_ttl_label = tk.Label(inv_ttl_frame, image=inv_ttl_img)
    inv_ttl_label.place(relwidth=1, relheight=1)

    inv_body = tk.Frame(inv_root, bg='#D1550F', bd=5)
    inv_body.place(relx=.01, rely=.3, relwidth=.98, relheight=.68)

    inv_body2 = tk.Frame(inv_body, bg='#253037', bd=5)
    inv_body2.place(relwidth=.999, relheight=.999)

    # PORTAL TITLE FRAME ---

    bdy2_ttl_frm = tk.Frame(inv_root, bg='#07466E', bd=5)
    bdy2_ttl_frm.place(relx=.24, rely=.13, relwidth=.5, relheight=.2)

    # PORTAL TITLE IMG ---

    prtl_ttl_img = tk.PhotoImage(file='inv_img.png')
    prtl_ttl_label = tk.Label(bdy2_ttl_frm, image=prtl_ttl_img)
    prtl_ttl_label.place(relwidth=1, relheight=1)

    # OPTION / SEARCH / SUBMIT BUTTON FRAME ---

    inv_option_frm = tk.Frame(inv_body2, bg='#5F9BC1')
    inv_option_frm.place(relx=.11, rely=.04, relwidth=.78, relheight=.08)

    # Create the list of options
    options_list = [

        "Brand", "Brand", "Part Number",
        "Serial Number", "Firmware Number", "Type",
        "Size", "Connection", "Capacity"

    ]

    filter_value = tk.StringVar(inv_option_frm)

    # Set the default value of the variable

    fltr_menu = ttk.OptionMenu(inv_option_frm, filter_value, *options_list)
    fltr_menu.place(relx=.01, rely=.2, relwidth=.22, relheight=.6)

    # SEARCH ENTRY IN OPTION FRAME ---

    inv_srch_ent = tk.Entry(inv_option_frm, bd=5, font=('Calibri', 13))
    inv_srch_ent.place(relx=.24, rely=.1, relwidth=.53, relheight=.7)

    # SUBMIT BUTTON INSIDE OPTION FRAME ---

    inv_srchSubBtn = ttk.Button(inv_option_frm, text='SEARCH', command=lambda: inv_ftch())
    inv_srchSubBtn.place(relx=.78, rely=.2, relwidth=.2, relheight=.6)

    # FRAME FOR DATE OF MANUFACTUER --- 

    dom_frm = tk.Frame(inv_root, bg='#325E79', bd=3)
    dom_frm.place(relx=.02, rely=.26, relwidth=.22, relheight=.07)

    dom_frm2 = tk.Frame(dom_frm, bg='#7A8E9B')
    dom_frm2.place(relwidth=1, relheight=1)

    # RIDGE FOR DATE OF MANUFACTUER --- 

    dom_rdg = tk.Label(dom_frm2, bg='#7A8E9B', relief='ridge')
    dom_rdg.place(relx=.01, rely=.2, relwidth=.98, relheight=.75)

    # LABEL FOR DATE OF MANUFACTUERING --- 

    dom_lbl = tk.Label(dom_frm2, bg='#7A8E9B', text='Date of Manufactuering')
    dom_lbl.place(relx=.04, relheight=.34)

    # MONTH OPTION BOX --- 

    monthInv_lst = [

        'Month', '01', '02', '03', '04',
        '05', '06', '07', '08',
        '09', '10', '11', '12'

    ]

    monthInv_fltr = tk.StringVar(dom_rdg)

    monthInv_opt = ttk.OptionMenu(dom_rdg, monthInv_fltr, *monthInv_lst)
    monthInv_opt.place(relx=.01, rely=.2, relwidth=.34)

    # LABEL SEPERATOR --- 

    dom_sep = tk.Label(dom_rdg, bg='#7A8E9B', text='/')
    dom_sep.config(font=(12))
    dom_sep.place(relx=.33, rely=.18)

    # DAY OPTION BOX --- 

    dayInv_lst = [

        'Day', '00', '01', '02', '03', '04',
        '05', '06', '07', '08', '09',
        '10', '11', '12', '13', '14',
        '15', '16', '17', '18', '19',
        '20', '21', '22', '23', '24',
        '25', '26', '27', '28', '29',
        '30', '31'

    ]

    dayInv_fltr = tk.StringVar(dom_rdg)

    dayInv_opt = ttk.OptionMenu(dom_rdg, dayInv_fltr, *dayInv_lst)
    dayInv_opt.place(relx=.4, rely=.2, relwidth=.26)

    # LABEL SEPERATOR --- 

    dom_sep1 = tk.Label(dom_rdg, bg='#7A8E9B', text='/')
    dom_sep1.config(font=(12))
    dom_sep1.place(relx=.64, rely=.18)

    # YEAR OPTION --- 

    yrInv_lst = [

        'Year', '2023', '2022', '2021', '2020', '2019',
        '2018', '2017', '2016', '2015', '2014',
        '2013', '2012'

    ]

    yrInv_fltr = tk.StringVar(dom_rdg)

    yrInv_opt = ttk.OptionMenu(dom_rdg, yrInv_fltr, *yrInv_lst)
    yrInv_opt.place(relx=.71, rely=.2, relwidth=.28)

    # FRAME FOR MENU OPTIONS --- 

    menuInv_frm = tk.Frame(inv_root, bg='#325E79', bd=3)
    menuInv_frm.place(relx=.78, rely=.26, relwidth=.17, relheight=.07)

    menuInv_frm2 = tk.Frame(menuInv_frm, bg='#7A8E9B', bd=4)
    menuInv_frm2.place(relwidth=1, relheight=1)

    # RIDGE FOR OPTION MENU --- 

    menu_rdg = tk.Label(menuInv_frm2, bg='#7A8E9B', relief='ridge')
    menu_rdg.place(relwidth=1, relheight=1)

    # MENU BUTTON --- 

    menu_but = ttk.Button(menu_rdg, text='Menu', command=lambda: inv_menu())
    menu_but.place(relwidth=1, relheight=1)

    # INVENTORY TREEVIEW --- 

    inv_tree = ttk.Treeview(inv_body2)
    inv_tree.place(relx=.02, rely=.15, relwidth=.94, relheight=.78)

    # INVENTORY SCROLL --- 

    inv_yscrl = tk.Scrollbar(inv_body2, orient='vertical', command=inv_tree.yview)
    inv_yscrl.place(relx=.96, rely=.15, relwidth=.02, relheight=.82)

    inv_tree.config(yscrollcommand=inv_yscrl.set)

    inv_xscrl = tk.Scrollbar(inv_body2, orient='horizontal', command=inv_tree.xview)
    inv_xscrl.place(relx=.02, rely=.93, relwidth=.94, relheight=.04)

    inv_tree.config(xscrollcommand=inv_xscrl.set)

    while True:
        inv_root.update()


# FUNCTION FOR UPC CODES PAGE --- 

def upc(sql):
    # FUNCTION THAT ADDS UPC CODES INTO UPC TABLE ROCTICK.DB ---

    def add_upc(size, uom, brnd, pn, upc11, upc12, des):
        # STARTING SQL CURSOR --- 

        sqlc_upc = sql.cursor()

        # CREATE UPC TABLE IF NOT CREATED ALREADY --- 

        upc_table = """

        CREATE TABLE UPC(
        'Part Number' TEXT,
        'Brand' TEXT,
        'Size' TEXT,
        'UPC11' INTEGER,
        'UPC12' INTEGER,
        'Description' TEXT)
        
        """

        try:
            sqlc_upc.execute(upc_table)

        except:
            time.sleep(.1)

        # PUTTING UPC VALUES IN VARIABLE --- 

        # SIZE VALUE --- 

        upcval_size = size.get() + uom.get()

        # BRAND VALUE --- 

        upcval_brnd = brnd.get()
        brnd.delete(0, 'end')

        # PART NUMBER VALUE --- 

        upcval_pn = pn.get()
        pn.delete(0, 'end')

        # UPC-11 VALUE --- 

        upc11val = upc11.get() + ".0"
        upc11.delete(0, 'end')

        # UPC-12 VALUE --- 

        upc12val = upc12.get() + ".0"
        upc12.delete(0, 'end')

        # DESCRIPTION VALUE --- 

        upcval_des = des.get()
        des.delete(0, 'end')

        # STORING UPC VALUES INSIDE DICTIONARY --- 

        upc_cont = {

            'Part Number': [upcval_pn],
            'Brand': [upcval_brnd],
            'Size': [upcval_size],
            'UPC11': [upc11val],
            'UPC12': [upc12val],
            'Description': [upcval_des]

        }

        # CREATING DATA FRAME FROM UPC VALUES --- 

        df_upc = pd.DataFrame(upc_cont)

        # STORING DATAFRAME VALUES IN UPC TABLE ROCTICK.DB ---

        for upc_ins in range(len(df_upc)):
            upcsql_rw = df_upc.iloc[upc_ins]
            sqlc_upc.execute("INSERT INTO UPC VALUES(?, ?, ?, ?, ?, ?)", upcsql_rw)

        sql.commit()

    # FUNCTION SQLITE FETCHING UPC TABLE IN ROCTICK.DB ---

    def qry_upc(tree, fltr, ent):
        # DELETING TREE --- 

        for del_ in tree.get_children():
            tree.delete(del_)

        # STARTING SQL CURSOR --- 

        upc_sql = sql.cursor()

        # SELECTING UPC TABLE --- 

        upcSql_rslts = upc_sql.execute("SELECT rowid, * FROM UPC").fetchall()

        # INSERTING UPC TABLE INTO TREEVIEW --- 

        tree['column'] = ('Index', 'Part Number', 'Brands', 'Size', 'UPC11', 'UPC12', 'Description')
        tree['show'] = 'headings'

        for upc_col in tree['column']:
            tree.heading(upc_col, text=upc_col)

        def upcGet(fch, clm):
            upcGnum = 0
            for upc_row in fch:
                upcQ = upc_row[clm]
                if upcQ.find(ent.get().upper()) != -1:
                    upcGnum += 1
                    tree.insert("", "end", values=(
                        upcGnum, upc_row[1], upc_row[2], upc_row[3], upc_row[4][:-2], upc_row[5][:-2], upc_row[6]))

        # FILTERING QUERY TO SPECIFIC VALUES ---

        if fltr.get() == 'Brands':
            upcGet(upcSql_rslts, 2)

        elif fltr.get() == 'Part Number':
            upcGet(upcSql_rslts, 1)

    def create_label(cltp):
        def make_label():
            # DELETING LABEL IN TREEVIEW --- 

            global bl
            for dl in cltree.get_children():
                cltree.delete(dl)

            # CREATING DICTIONARY FOR LABEL TEMPLATE --- 

            cdflt = {

                "Qty": [],
                "SN": [],
                "PN": [],
                "UPC": [],
                "Desc": [],
                "Color": [],
                "Size": [],
                "RPM": [],
                "Connection": [],
                "LOT": []

            }

            # STATING ROCKTICK DB CURSOR --- 

            mlsql = sql.cursor()

            # ACCESSING HARD DRIVE TABLE --- 

            ahdt = mlsql.execute("SELECT rowid, * FROM hard_drive").fetchall()

            # ACCESSING UPC TABLE --- 

            aut = mlsql.execute("SELECT rowid, * FROM UPC").fetchall()

            # ACCESSING LABEL TABLE --- 

            alt = mlsql.execute("SELECT rowid, * FROM LABEL").fetchall()

            # APPENDING LOT NUMBER TO DICTIONARY --- 

            def lbl_date(lin):
                alnd = datetime.now().strftime("%m%d") + "V-" + lin
                cdflt["LOT"].append(alnd)

            if ffhdbstrv.get() == ffhdblst[1]:
                lbl_date("T")

            elif ffhdbstrv.get() == ffhdblst[2]:
                lbl_date("HT")

            elif ffhdbstrv.get() == ffhdblst[3]:
                lbl_date("SM")

            elif ffhdbstrv.get() == ffhdblst[4]:
                lbl_date("CR")

            elif ffhdbstrv.get() == ffhdblst[5]:
                lbl_date("SG")

            elif ffhdbstrv.get() == ffhdblst[6]:
                lbl_date("XX")

            # APPENDING SERIAL NUMBER TO DICTIONARY --- 

            cdflt["SN"].append(efsn.get().upper())

            # APPENDING QUANITY AMOUNT TO DICTIONARY --- 

            aqatd = float(len(cdflt["SN"]) + .0)
            cdflt["Qty"].append(aqatd)

            # APPENDING PART NUMBER TO DICTIONARY --- 

            cdflt["PN"].append(efpn.get().upper())

            # APPENDING UPC NUMBER / DESCRIPTION / SIZE TO DICTIONARY --- 

            for au in aut:
                if au[1].lower() == efpn.get().lower():
                    cdflt["UPC"].append(au[4][:-2])
                    cdflt["Desc"].append(au[2])
                    cdflt["Size"].append(au[3])
                    break

            # APPENDING RPM TO DICTIONARY --- 

            for ar in ahdt:
                if efsn.get().lower() == ar[4].lower():
                    cdflt["RPM"].append(ar[6])
                    bl = False
                    break

                else:
                    bl = True

            if bl == True:
                for a2 in aut:
                    if a2[1] == efpn.get():
                        if a2[3] == "No Drives":
                            cdflt["RPM"].append("Enclosure")
                            break

                        else:
                            cdflt["RPM"].append("7200")
                            break

            # APPENDING COLOR AND CONNECTION TO DICTIONARY --- 

            for ac in alt:
                if ac[1] == cdflt["Desc"][0]:
                    cdflt["Color"].append(ac[2])
                    cdflt["Connection"].append(ac[3])
                    break

            # SAVING LABEL TO CSV --- 

            csv_ = cdflt["Size"][0] + " " + cdflt["RPM"][0] + " " + cdflt["Desc"][0] + " " + efpn.get().upper() + ".csv"

            dflbl = pd.DataFrame(cdflt)
            dflbl.to_csv(csv_)

            shutil.move(csv_, "D:")

            # DISPLAY LABEL IN TREE VIEW --- 

            cltree["column"] = (
                'Quantity', 'Serial Number', 'Part Number', 'UPC', 'Description', 'Color', 'Size', 'RPM', 'Connection',
                'LOT')

            cltree["show"] = "headings"

            for dlt in cltree["column"]:
                cltree.heading(dlt, text=dlt)

            for x in range(len(dflbl)):
                cltree.insert(

                    "", "end", values=(dflbl["Qty"].iloc[x], dflbl["SN"].iloc[x],
                                       dflbl["PN"].iloc[x], dflbl["UPC"].iloc[x], dflbl["Desc"].iloc[x],
                                       dflbl["Color"].iloc[x], dflbl["Size"].iloc[x], dflbl["RPM"].iloc[x],
                                       dflbl["Connection"].iloc[x], dflbl["LOT"].iloc[x]

                                       )
                )

        # LABEL PAGE BACKGROUND IMAGE ---

        lpbi = tk.PhotoImage(file="upc_main.png")
        lpbi2 = tk.Label(cltp, image=lpbi)
        lpbi2.place(relwidth=1, relheight=1)

        # 1ST AND 2ND FRAME FOR HARD DRIVE TYPE FILTER / PART AND SERIAL NUMBER ENTRY --- 

        ffhdtf = tk.Frame(cltp, bg="#526787", bd=3)
        ffhdtf.place(relx=.2, rely=.15, relwidth=.6, relheight=.53)

        ffhdtf2 = tk.Frame(ffhdtf, bg="#A2B7C1", bd=5)
        ffhdtf2.place(relwidth=1, relheight=.65)

        # SUNKEN LABEL FOR PART NUMBER AND SERIAL NUMBER --- 

        slfpsn = tk.Label(ffhdtf2, bg="#A2B7C1", bd=3, relief="sunken")
        slfpsn.place(relwidth=1, relheight=.7)

        # LABEL RIDGE FOR PART NUMBER ENTRY --- 

        lrfpne = tk.Label(slfpsn, bg="#A2B7C1", relief="ridge")
        lrfpne.place(relx=.05, rely=.5, relwidth=.4, relheight=.44)

        # LABEL TEXT "PART NUMBER" --- 

        ltpn = tk.Label(slfpsn, bg="#A2B7C1", text="Part Number")
        ltpn.place(relx=.07, rely=.45, relheight=.1)

        # ENTRY FOR PART NUMBER --- 

        efpn = tk.Entry(lrfpne, relief="sunken", bd=3)
        efpn.config(font=("Calibri", 11))
        efpn.place(relx=.02, rely=.2, relwidth=.96, relheight=.7)

        # LABEL RIDGE FOR SERIAL NUMBERS --- 

        lrfsn = tk.Label(slfpsn, bg="#A2B7C1", relief="ridge")
        lrfsn.place(relx=.5, rely=.5, relwidth=.45, relheight=.44)

        # LABEL TEXT "SERIAL NUMBERS" --- 

        ltsn = tk.Label(slfpsn, bg="#A2B7C1", text="Serial Number")
        ltsn.place(relx=.53, rely=.45, relheight=.1)

        # ENTRY FOR SERIAL NUMBERS --- 

        efsn = tk.Entry(lrfsn, bd=3, relief="sunken")
        efsn.config(font=("Calibri", 11))
        efsn.place(relx=.02, rely=.2, relwidth=.96, relheight=.7)

        # FILTER FOR HARD DRIVE BRANDS --- 

        ffhdblst = [

            "Hard Drive", "Toshiba", "Hitachi", "Samsung", "Crucial",
            "Seagate", "No Drives"

        ]

        ffhdbstrv = tk.StringVar(slfpsn)

        ffhdbopt = ttk.OptionMenu(slfpsn, ffhdbstrv, *ffhdblst)
        ffhdbopt.place(relx=.35, rely=.05, relwidth=.25, relheight=.32)

        # BUTTON FOR CREATING LABEL --- 

        bfcl = ttk.Button(ffhdtf2, text="Create Label", command=lambda: make_label())
        bfcl.place(relx=.3, rely=.75, relwidth=.35, relheight=.2)

        # BACK TO UPC MENU BUTTON FOR LABEL MAKER PAGE --- 

        bumb = ttk.Button(cltp, text="Main Menu", command=lambda: upc_gui())
        bumb.place(relx=.8, rely=.03, relwidth=.15, relheight=.07)

        # TREE VIEW FOR UPC CREATE A LABEL PAGE --- 

        cltree = ttk.Treeview(ffhdtf)
        cltree.place(rely=.66, relwidth=.96, relheight=.27)

        # YSCROLL FOR CREATE A LABEL PAGE TREEVIEW --- 

        yclpt = tk.Scrollbar(ffhdtf, orient="vertical", command=cltree.yview)
        yclpt.place(relx=.96, rely=.66, relwidth=.04, relheight=.34)
        cltree.config(yscrollcommand=yclpt.set)

        # XSCROLL FOR CREATE A LABEL PAGE TREEVIEW --- 

        xclpt = tk.Scrollbar(ffhdtf, orient="horizontal", command=cltree.xview)
        xclpt.place(rely=.93, relwidth=.96, relheight=.07)
        cltree.config(xscrollcommand=xclpt.set)

        while True:
            cltp.update()

    def upc_gui():
        # BACKGROUND IMG --- 

        mainPng_upc = tk.PhotoImage(file='upc_main.png')
        mainImg_upc = tk.Label(upcRoot, image=mainPng_upc)
        mainImg_upc.place(relwidth=1, relheight=1)

        # FRAME FOR UPC "PART NUMBER / BRANDS / SIZE / UOM / UPC11 / UPC12 / DESCRIPTION"

        upcInFrm = tk.Frame(upcRoot, bg='#526787', bd=3)
        upcInFrm.place(relx=.02, rely=.09, relwidth=.4, relheight=.88)

        upcInFrm2 = tk.Frame(upcInFrm, bg='#95A2B4', bd=3)
        upcInFrm2.place(relwidth=1, relheight=1)

        # RIDGE FOR "PART NUMBER / BRANDS / SIZE / UOM / UPC11 / UPC12 / DESCRIPTION" --- 

        upcInlbl = tk.Label(upcInFrm2, bg='#95A2B4', relief='ridge')
        upcInlbl.place(relx=.03, rely=.05, relwidth=.94, relheight=.9)

        # "SIZE" AND "UOM" OPTION SUNKEN --- 

        sizeSnk_upc = tk.Label(upcInlbl, bg='#95A2B4', relief='sunken')
        sizeSnk_upc.place(relx=.3, rely=.02, relwidth=.65, relheight=.1)

        # SIZE OPTION --- 

        sizeLst_upc = [

            'Size', '1', '2', '3', '4', '5', '6',
            '7', '8', '9', '10', '11', '12',
            '13', '14', '15', '16', '17', '18', '20',
            '24', '28', '32', '36', '70', 'No Drives'

        ]

        sizeFltr_upc = tk.StringVar(sizeSnk_upc)

        sizeOpt_upc = ttk.OptionMenu(sizeSnk_upc, sizeFltr_upc, *sizeLst_upc)
        sizeOpt_upc.place(relx=.02, rely=.15, relwidth=.46, relheight=.75)

        # UOM OPTION --- 

        uom_lst = [

            'UOM', 'GB', 'TB', ''

        ]

        uom_fltr = tk.StringVar(sizeSnk_upc)

        uom_opt = ttk.OptionMenu(sizeSnk_upc, uom_fltr, *uom_lst)
        uom_opt.place(relx=.5, rely=.15, relwidth=.48, relheight=.75)

        # "UPC" BRAND AND PART NUMBER SUNKEN --- 

        brndPnSunk_upc = tk.Label(upcInlbl, bg='#95A2B4', relief='sunken')
        brndPnSunk_upc.place(relx=.02, rely=.14, relwidth=.96, relheight=.3)

        # "UPC" BRANDS RIDGE --- 

        brndRdg_upc = tk.Label(brndPnSunk_upc, bg='#95A2B4', relief='ridge')
        brndRdg_upc.place(relx=.02, rely=.13, relwidth=.47, relheight=.3)

        # "UPC" BRAND ENTRY --- 

        brndEnt_upc = tk.Entry(brndRdg_upc, bd=3, relief='sunken')
        brndEnt_upc.place(relx=.02, rely=.15, relwidth=.96, relheight=.75)

        # "UPC" BRANDS LABEL --- 

        brndLbl_upc = tk.Label(brndPnSunk_upc, bg='#95A2B4', text='Brand')
        brndLbl_upc.place(relx=.04, rely=.1, relheight=.08)

        # "UPC" PART NUMBER RIDGE --- 

        pnRdg_upc = tk.Label(brndPnSunk_upc, bg='#95A2B4', relief='ridge')
        pnRdg_upc.place(relx=.02, rely=.57, relwidth=.55, relheight=.3)

        # "UPC" PART NUMBER ENTRY --- 

        pnEnt_upc = tk.Entry(pnRdg_upc, bd=3, relief='sunken')
        pnEnt_upc.place(relx=.02, rely=.15, relwidth=.96, relheight=.75)

        # "UPC" PART NUMBER LABEL --- 

        pnLbl_upc = tk.Label(brndPnSunk_upc, bg='#95A2B4', text='Part Number')
        pnLbl_upc.place(relx=.04, rely=.54, relheight=.08)

        # "UPC" UPC-11 AND UPC-12 SUNKEN --- 

        upc112Snk = tk.Label(upcInlbl, bg='#95A2B4', relief='sunken')
        upc112Snk.place(relx=.02, rely=.47, relwidth=.96, relheight=.3)

        # "UPC" UPC-11 RIDGE --- 

        upc11_rgd = tk.Label(upc112Snk, bg='#95A2B4', relief='ridge')
        upc11_rgd.place(relx=.02, rely=.13, relwidth=.47, relheight=.3)

        # "UPC" UPC-11 ENTRY --- 

        upc11_ent = tk.Entry(upc11_rgd, bd=3, relief='sunken')
        upc11_ent.place(relx=.02, rely=.15, relwidth=.96, relheight=.75)

        # "UPC" UPC-11 LABEL --- 

        upc11_lbl = tk.Label(upc112Snk, bg='#95A2B4', text='UPC-11')
        upc11_lbl.place(relx=.04, rely=.1, relheight=.08)

        # "UPC" UPC-12 RIDGE --- 

        upc12_rdg = tk.Label(upc112Snk, bg='#95A2B4', relief='ridge')
        upc12_rdg.place(relx=.02, rely=.55, relwidth=.47, relheight=.3)

        # "UPC" UPC-12 ENTRY --- 

        upc12_ent = tk.Entry(upc12_rdg, bd=3, relief='sunken')
        upc12_ent.place(relx=.02, rely=.15, relwidth=.96, relheight=.75)

        # "UPC" UPC-12 LABEL --- 

        upc12_lbl = tk.Label(upc112Snk, bg='#95A2B4', text='UPC-12')
        upc12_lbl.place(relx=.04, rely=.52, relheight=.08)

        # "UPC" DESCRIPTION RIDGE --- 

        upcDes_rdg = tk.Label(upcInlbl, bg='#95A2B4', relief='ridge')
        upcDes_rdg.place(relx=.02, rely=.8, relwidth=.96, relheight=.1)

        # "UPC" DESCRIPTION ENTRY --- 

        upcDes_ent = tk.Entry(upcDes_rdg, bd=3, relief='sunken')
        upcDes_ent.place(relx=.02, rely=.15, relwidth=.96, relheight=.75)

        # "UPC" DESCRIPTION LABEL --- 

        ucpDes_lbl = tk.Label(upcInlbl, bg='#95A2B4', text='Description')
        ucpDes_lbl.place(relx=.04, rely=.78, relheight=.04)

        # "UPC" BUTTON --- 

        upcSub_but = tk.Button(
            upcInlbl, bg='#FFEFE6', text='Submit', command=lambda: add_upc(
                sizeFltr_upc, uom_fltr, brndEnt_upc, pnEnt_upc,
                upc11_ent, upc12_ent, upcDes_ent))
        upcSub_but.place(relx=.6, rely=.91, relwidth=.35, relheight=.08)

        # MAIN TITLE IMG --- 

        ttlFrm_upc = tk.Frame(upcRoot, bg='#526787', bd=3)
        ttlFrm_upc.place(relx=.01, rely=.01, relwidth=.25, relheight=.11)

        ttlPng_upc = tk.PhotoImage(file='image001.png')
        ttlImg_upc = tk.Label(ttlFrm_upc, image=ttlPng_upc)
        ttlImg_upc.place(relwidth=1, relheight=1)

        # "UPC" FRAME FOR TREEVIEW --- 

        upctree_frm = tk.Frame(upcRoot, bg='#526787', bd=3)
        upctree_frm.place(relx=.44, rely=.17, relwidth=.54, relheight=.8)

        # "UPC" QUERY SUNKEN LABEL --- 

        qrySnk_upc = tk.Label(upctree_frm, bg='#95A2B4', relief='sunken')
        qrySnk_upc.place(relwidth=1, relheight=.09)

        # "UPC" QUERY OPTION BOX ---

        qryLst_upc = [

            'Brands', 'Brands', 'Part Number'

        ]

        qryFltr_upc = tk.StringVar(qrySnk_upc)

        qryOpt_upc = ttk.OptionMenu(qrySnk_upc, qryFltr_upc, *qryLst_upc)
        qryOpt_upc.place(relx=.01, rely=.1, relwidth=.23, relheight=.8)

        # "UPC" QUERY ENTRY --- 

        qryEnt_upc = tk.Entry(qrySnk_upc, bd=3, relief='sunken')
        qryEnt_upc.place(relx=.25, rely=.1, relwidth=.45, relheight=.8)

        # "UPC" TREEVIEW --- 

        upc_tree = ttk.Treeview(upctree_frm)
        upc_tree.place(rely=.1, relwidth=.96, relheight=.86)

        # "UPC" QUERY BUTTON --- 

        qryBut_upc = tk.Button(
            qrySnk_upc, bg='#FFEFE6', text='Search', command=lambda: qry_upc(
                upc_tree, qryFltr_upc, qryEnt_upc))
        qryBut_upc.place(relx=.71, rely=.1, relwidth=.28, relheight=.8)

        # "UPC" YSCROLL IN TREEVIEW --- 

        upc_yscrl = tk.Scrollbar(upctree_frm, orient='vertical', command=upc_tree.yview)
        upc_yscrl.place(relx=.96, rely=.1, relwidth=.04, relheight=.9)
        upc_tree.config(yscrollcommand=upc_yscrl.set)

        # "UPC" XSCROLL IN TREEVIEW --- 

        upc_xscrl = tk.Scrollbar(upctree_frm, orient='horizontal', command=upc_tree.xview)
        upc_xscrl.place(rely=.96, relwidth=.96, relheight=.04)
        upc_tree.config(xscrollcommand=upc_xscrl.set)

        # BUTTON TO CREATE LABELS --- 

        btcl = ttk.Button(upcRoot, text="Create Label", command=lambda: create_label(upcRoot))
        btcl.place(relx=.85, rely=.03, relwidth=.13, relheight=.07)

        while True:
            upcRoot.update()

    # UPC GUI ---

    upcRoot = tk.Toplevel()
    upcRoot.title("UPC Codes")
    upcRoot.geometry("850x500")
    upc_gui()


# CLI TITLE ---

print('')
print(figlet_format(' ROCTICK', font='dotmatrix', width=200))
print('')
time.sleep(1.5)
stop = 0

while True:
    stop += 1

    # CLI USER AND PASSWORD LOGIN --- 

    usr_tic = input('                                    UserEmail:~$> ')
    pass_tic = getpass.getpass('                                    Password:~$> ')
    time.sleep(3)
    print('')
    print('                                               .....\n')
    time.sleep(1.7)
    print('                                           Please Wait.....\n')
    time.sleep(3)

    if usr_tic == 'jonathan@rocstor.com' and pass_tic == 'Je2744465314139':
        print(figlet_format('    Welcome ' + usr_tic[:-12].upper() + '\n', font='bulbhead', width=200))
        time.sleep(4)
        print(figlet_format('===========================================================\n', font='digital', width=200))
        print('                                          Activating Portal.... \n')
        time.sleep(3)
        print(figlet_format('===========================================================\n', font='digital', width=200))
        time.sleep(2.5)

        # CONNECTING TO RMA DATABASE --- 

        et_sql = sqlite3.connect('ROCTICK.db')

        # ETICKETS GUI --- 

        root = tk.Tk()

        # Gets the requested values of the height and widht.

        rww = root.winfo_reqwidth()
        rwh = root.winfo_reqheight()

        # Gets both half the screen width/height and window width/height

        rpr = int(root.winfo_screenwidth() / 2 - rww / 2)
        rpd = int(root.winfo_screenheight() / 2 - rwh / 2)

        # Positions the window in the center of the page.

        root.geometry("+{}+{}".format(rpr, rpd))
        root.title('Rocstor')
        root.geometry("500x500")

        # TITLE IN ROOT FRAME --- 

        bimg = tk.PhotoImage(file="bc.png")
        biLbl = tk.Label(root, image=bimg)
        biLbl.place(relwidth=1, relheight=1)

        body2 = tk.Label(root, bg='#F1EBE9', relief='ridge')
        body2.place(relx=.1, rely=.37, relwidth=.8, relheight=.5)

        ttl_img = tk.PhotoImage(file='img.png')
        ttl_label = tk.Label(root, image=ttl_img)
        ttl_label.place(relx=.21, rely=.13, relwidth=.58, relheight=.14)

        # SUNKEN LABEL FOR INVENTORY BUTTON --- 

        slfib = tk.Label(body2, bg='#F1EBE9', relief='sunken', bd=3)
        slfib.place(relx=.1, rely=.1, relwidth=.35, relheight=.35)

        # BUTTON FOR INVENTORY --- 

        bfi = ttk.Button(slfib, text="Inventory", command=lambda: inventory(et_sql))
        bfi.place(relwidth=1, relheight=1)

        # SUNKEN LABEL FOR UPC / LABELS BUTTON --- 

        slfulb = tk.Label(body2, bg='#F1EBE9', relief='sunken', bd=3)
        slfulb.place(relx=.32, rely=.6, relwidth=.35, relheight=.35)

        # BUTTON FOR UPC AND LABELS --- 

        bfual = ttk.Button(slfulb, text="UPC & Labels", command=lambda: upc(et_sql))
        bfual.place(relwidth=1, relheight=1)

        # SUNKEN LABEL FOR RMA BUTTON --- 

        slfrb = tk.Label(body2, bg='#F1EBE9', relief='sunken', bd=3)
        slfrb.place(relx=.55, rely=.1, relwidth=.35, relheight=.35)

        # BUTTON FOR RMA --- 

        bur = ttk.Button(slfrb, text="RMA", command=lambda: rma_frm(et_sql))
        bur.place(relwidth=1, relheight=1)

        root.mainloop()
        break

    elif stop == 2:
        time.sleep(3)
        print('                                    Logging Out... ')
        time.sleep(3)
        break

    else:
        time.sleep(2.5)
        print('                            ................................................')
        print('                            .     Sorry, Incorrect Username or Password    .')
        print('                            .                Try Again....                 .')
        print('                            ................................................ \n')
        time.sleep(3)
        print(figlet_format('===========================================================\n', font='digital', width=200))
        time.sleep(1.5)
