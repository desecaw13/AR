# Joe Olpin
# Accounts Receivable
# 8/30/2021 - 9/3/2021

from tkinter import *
import mysql


def openC():
    root.withdraw()

    cw = Toplevel(root, takefocus=True)
    cw.title('Customers')
    cw.grid_columnconfigure(0, weight=1)

    def openI():
        cw.withdraw()

        w = Toplevel(cw, takefocus=True)
        w.title('Create New Customer')
        w.resizable(width=False, height=False)

        f = Frame(w, bg='#808080')
        f.grid()

        cid_l = Label(f, text='Customer Code')
        cid_l.grid(row=0, column=0, sticky=EW, padx=5, pady=5)
        cid_e = Entry(f)
        cid_e.grid(row=0, column=1, sticky=EW, padx=5, pady=5)

        fname_l = Label(f, text='First Name')
        fname_l.grid(row=1, column=0, sticky=EW, padx=5, pady=5)
        fname_e = Entry(f)
        fname_e.grid(row=1, column=1, sticky=EW, padx=5, pady=5)

        lname_l = Label(f, text='Last Name')
        lname_l.grid(row=2, column=0, sticky=EW, padx=5, pady=5)
        lname_e = Entry(f)
        lname_e.grid(row=2, column=1, sticky=EW, padx=5, pady=5)

        email_l = Label(f, text='Email Address')
        email_l.grid(row=3, column=0, sticky=EW, padx=5, pady=5)
        email_e = Entry(f)
        email_e.grid(row=3, column=1, sticky=EW, padx=5, pady=5)

        phone_l = Label(f, text='Phone Number')
        phone_l.grid(row=4, column=0, sticky=EW, padx=5, pady=5)
        phone_e = Entry(f)
        phone_e.grid(row=4, column=1, sticky=EW, padx=5, pady=5)

        address_l = Label(f, text='Mailing Address')
        address_l.grid(row=5, column=0, sticky=EW, padx=5, pady=5)
        address_e = Entry(f)
        address_e.grid(row=5, column=1, sticky=EW, padx=5, pady=5)

        state_l = Label(f, text='State')
        state_l.grid(row=6, column=0, sticky=EW, padx=5, pady=5)
        state_e = Entry(f)
        state_e.grid(row=6, column=1, sticky=EW, padx=5, pady=5)

        city_l = Label(f, text='City')
        city_l.grid(row=7, column=0, sticky=EW, padx=5, pady=5)
        city_e = Entry(f)
        city_e.grid(row=7, column=1, sticky=EW, padx=5, pady=5)

        zipcode_l = Label(f, text='Zip Code')
        zipcode_l.grid(row=8, column=0, sticky=EW, padx=5, pady=5)
        zipcode_e = Entry(f)
        zipcode_e.grid(row=8, column=1, sticky=EW, padx=5, pady=5)

        def do():
            mysql.insertCustomer(cid_e.get(), fname_e.get(), lname_e.get(), email_e.get(), phone_e.get(), address_e.get(), state_e.get(), city_e.get(), zipcode_e.get())
            cid_e.delete(0, END)
            fname_e.delete(0, END)
            lname_e.delete(0, END)
            email_e.delete(0, END)
            phone_e.delete(0, END)
            address_e.delete(0, END)
            state_e.delete(0, END)
            city_e.delete(0, END)
            zipcode_e.delete(0, END)

        summit_b = Button(f, fg='white', bg='#d33d00', text='Create', command=do)
        summit_b.grid(row=9, column=1, sticky=EW, padx=5, pady=5)

        def iBack():
            cw.deiconify()
            w.destroy()

        back_b = Button(f, fg='white', bg='#d30000', text='Back to Customer Menu', command=iBack)
        back_b.grid(row=9, column=0, sticky=EW, padx=5, pady=5)

        w.update()
        w.geometry(f'{w.winfo_width()}x{w.winfo_height()}+{(w.winfo_screenwidth() - w.winfo_width()) // 2}+{(w.winfo_screenheight() - w.winfo_height()) // 2}')

    ct_f = Frame(cw, bg='#3D3D3D', highlightbackground='gray', highlightthickness=5)
    ct_f.grid_columnconfigure(0, weight=1)
    ct_f.grid(row=0, column=0, sticky=EW)

    ct_l = Label(ct_f, fg='white', bg='#3D3D3D', font=('TkDefaultFont', 13), text='Customer Database')
    ct_l.grid(padx=5, pady=5)

    cm_f = Frame(cw, bg='#808080')
    cm_f.grid(row=1, column=0)

    new_b = Button(cm_f, fg='white', bg='#d33d00', width=20, height=3, text='Enter New Customer', command=openI)
    new_b.grid(row=0, column=0, sticky=EW, padx=5, pady=5)

    edit_b = Button(cm_f, fg='white', bg='#d33d00', width=20, height=3, text='Edit Existing Customer', command=lambda: print('ec'))  # mysql
    edit_b.grid(row=0, column=1, sticky=EW, padx=5, pady=5)

    def Back():
        root.deiconify()
        cw.destroy()

    ce_b = Button(cm_f, fg='white', bg='#d30000', width=20, height=3, text='Return to Menu', command=Back)
    ce_b.grid(row=1, columnspan=2, sticky=EW, padx=5, pady=5)

    cw.update()
    cw.geometry(f'{cw.winfo_width()}x{cw.winfo_height()}+{(cw.winfo_screenwidth() - cw.winfo_width()) // 2}+{(cw.winfo_screenheight() - cw.winfo_height()) // 2}')
    cw.minsize(width=cw.winfo_width(), height=cw.winfo_height())


def openP():
    root.withdraw()

    pw = Toplevel(root)
    pw.title('Products')
    pw.grid_columnconfigure(0, weight=1)

    def openI():
        pw.withdraw()

        w = Toplevel(pw, takefocus=True)
        w.title('Create New Product')
        w.resizable(width=False, height=False)

        f = Frame(w, bg='#808080')
        f.grid()

        pid_l = Label(f, text='Product Code')
        pid_l.grid(row=0, column=0, sticky=EW, padx=5, pady=5)
        pid_e = Entry(f)
        pid_e.grid(row=0, column=1, sticky=EW, padx=5, pady=5)

        title_l = Label(f, text='Title')
        title_l.grid(row=1, column=0, sticky=EW, padx=5, pady=5)
        title_e = Entry(f)
        title_e.grid(row=1, column=1, sticky=EW, padx=5, pady=5)

        mingrade_l = Label(f, text='Date Purchased')
        mingrade_l.grid(row=2, column=0, sticky=EW, padx=5, pady=5)
        mingrade_e = Entry(f)
        mingrade_e.grid(row=2, column=1, sticky=EW, padx=5, pady=5)

        maxgrade_l = Label(f, text='Date Purchased')
        maxgrade_l.grid(row=3, column=0, sticky=EW, padx=5, pady=5)
        maxgrade_e = Entry(f)
        maxgrade_e.grid(row=3, column=1, sticky=EW, padx=5, pady=5)

        price_l = Label(f, text='Price $')
        price_l.grid(row=4, column=0, sticky=EW, padx=5, pady=5)
        price_e = Entry(f)
        price_e.grid(row=4, column=1, sticky=EW, padx=5, pady=5)

        def do():
            mysql.insertProduct(pid_e.get(), title_e.get(), mingrade_e.get(), maxgrade_e.get(), price_e.get())
            pid_e.delete(0, END)
            title_e.delete(0, END)
            mingrade_e.delete(0, END)
            maxgrade_e.delete(0, END)
            price_e.delete(0, END)

        summit_b = Button(f, fg='white', bg='#d33d00', text='Create', command=do)
        summit_b.grid(row=9, column=1, sticky=EW, padx=5, pady=5)

        def iBack():
            pw.deiconify()
            w.destroy()

        back_b = Button(f, fg='white', bg='#d30000', text='Back to Products Menu', command=iBack)
        back_b.grid(row=9, column=0, sticky=EW, padx=5, pady=5)

        w.update()
        w.geometry(f'{w.winfo_width()}x{w.winfo_height()}+{(w.winfo_screenwidth() - w.winfo_width()) // 2}+{(w.winfo_screenheight() - w.winfo_height()) // 2}')

    pt_f = Frame(pw, bg='#3D3D3D', highlightbackground='gray', highlightthickness=5)
    pt_f.grid_columnconfigure(0, weight=1)
    pt_f.grid(row=0, column=0, sticky=EW)

    pt_l = Label(pt_f, fg='white', bg='#3D3D3D', font=('TkDefaultFont', 13), text='Product Database')
    pt_l.grid(padx=5, pady=5)

    pm_f = Frame(pw, bg='#808080')
    pm_f.grid(row=1, column=0)

    new_b = Button(pm_f, fg='white', bg='#d33d00', width=20, height=3, text='Enter New Product', command=openI)
    new_b.grid(row=0, column=0, sticky=EW, padx=5, pady=5)

    edit_b = Button(pm_f, fg='white', bg='#d33d00', width=20, height=3, text='Edit Existing Product', command=lambda: print('ep'))  # mysql
    edit_b.grid(row=0, column=1, sticky=EW, padx=5, pady=5)

    def Back():
        root.deiconify()
        pw.destroy()

    pe_b = Button(pm_f, fg='white', bg='#d30000', width=20, height=3, text='Return to Menu', command=Back)
    pe_b.grid(row=1, columnspan=2, sticky=EW, padx=5, pady=5)

    pw.update()
    pw.geometry(f'{pw.winfo_width()}x{pw.winfo_height()}+{(pw.winfo_screenwidth() - pw.winfo_width()) // 2}+{(pw.winfo_screenheight() - pw.winfo_height()) // 2}')
    pw.minsize(width=pw.winfo_width(), height=pw.winfo_height())


def openS():
    root.withdraw()

    sw = Toplevel(root)
    sw.title('Sales')
    sw.grid_columnconfigure(0, weight=1)

    def openI():
        sw.withdraw()

        w = Toplevel(sw, takefocus=True)
        w.title('Create New Sale')
        w.resizable(width=False, height=False)

        f = Frame(w, bg='#808080')
        f.grid()

        pid_l = Label(f, text='Product Code')
        pid_l.grid(row=0, column=0, sticky=EW, padx=5, pady=5)
        pid_e = Entry(f)
        pid_e.grid(row=0, column=1, sticky=EW, padx=5, pady=5)

        cid_l = Label(f, text='Customer Code')
        cid_l.grid(row=1, column=0, sticky=EW, padx=5, pady=5)
        cid_e = Entry(f)
        cid_e.grid(row=1, column=1, sticky=EW, padx=5, pady=5)

        date_l = Label(f, text='Date Purchased')
        date_l.grid(row=2, column=0, sticky=EW, padx=5, pady=5)
        date_e = Entry(f)
        date_e.grid(row=2, column=1, sticky=EW, padx=5, pady=5)

        price_l = Label(f, text='Price Paid')
        price_l.grid(row=3, column=0, sticky=EW, padx=5, pady=5)
        price_e = Entry(f)
        price_e.grid(row=3, column=1, sticky=EW, padx=5, pady=5)

        def do():
            mysql.insertSale(pid_e.get(), cid_e.get(), date_e.get(), price_e.get())
            pid_e.delete(0, END)
            cid_e.delete(0, END)
            date_e.delete(0, END)
            price_e.delete(0, END)

        summit_b = Button(f, fg='white', bg='#d33d00', text='Create', command=do)
        summit_b.grid(row=9, column=1, sticky=EW, padx=5, pady=5)

        def iBack():
            sw.deiconify()
            w.destroy()

        back_b = Button(f, fg='white', bg='#d30000', text='Back to Sales Menu', command=iBack)
        back_b.grid(row=9, column=0, sticky=EW, padx=5, pady=5)

        w.update()
        w.geometry(f'{w.winfo_width()}x{w.winfo_height()}+{(w.winfo_screenwidth() - w.winfo_width()) // 2}+{(w.winfo_screenheight() - w.winfo_height()) // 2}')

    st_f = Frame(sw, bg='#3D3D3D', highlightbackground='gray', highlightthickness=5)
    st_f.grid_columnconfigure(0, weight=1)
    st_f.grid(row=0, column=0, sticky=EW)

    st_l = Label(st_f, fg='white', bg='#3D3D3D', font=('TkDefaultFont', 13), text='Sales Database')
    st_l.grid(padx=5, pady=5)

    sm_f = Frame(sw, bg='#808080')
    sm_f.grid(row=1, column=0)

    new_b = Button(sm_f, fg='white', bg='#d33d00', width=20, height=3, text='Enter New Sale', command=openI)
    new_b.grid(row=0, column=0, sticky=EW, padx=5, pady=5)

    edit_b = Button(sm_f, fg='white', bg='#d33d00', width=20, height=3, text='Edit Existing Sale', command=lambda: print('es'))  # mysql
    edit_b.grid(row=0, column=1, sticky=EW, padx=5, pady=5)

    def Back():
        root.deiconify()
        sw.destroy()

    se_b = Button(sm_f, fg='white', bg='#d30000', width=20, height=3, text='Return to Menu', command=Back)
    se_b.grid(row=1, columnspan=2, sticky=EW, padx=5, pady=5)

    sw.update()
    sw.geometry(f'{sw.winfo_width()}x{sw.winfo_height()}+{(sw.winfo_screenwidth() - sw.winfo_width()) // 2}+{(sw.winfo_screenheight() - sw.winfo_height()) // 2}')
    sw.minsize(width=sw.winfo_width(), height=sw.winfo_height())


def openR():
    root.withdraw()

    rw = Toplevel(root)
    rw.title('Views')
    rw.grid_columnconfigure(0, weight=1)

    rt_f = Frame(rw, bg='#3D3D3D', highlightbackground='gray', highlightthickness=5)
    rt_f.grid_columnconfigure(0, weight=1)
    rt_f.grid(row=0, column=0, sticky=EW)

    rt_l = Label(rt_f, fg='white', bg='#3D3D3D', font=('TkDefaultFont', 13), text='Reports')
    rt_l.grid(padx=5, pady=5)

    rm_f = Frame(rw, bg='#808080')
    rm_f.grid(row=1, column=0)

    cr_b = Button(rm_f, fg='white', bg='#d33d00', width=20, height=3, text='Customers', command=lambda: print('cr'))  # mysql
    cr_b.grid(row=0, column=0, sticky=EW, padx=5, pady=5)

    pr_b = Button(rm_f, fg='white', bg='#d33d00', width=20, height=3, text='Products', command=lambda: print('pr'))  # mysql
    pr_b.grid(row=0, column=1, sticky=EW, padx=5, pady=5)

    sr_b = Button(rm_f, fg='white', bg='#d33d00', width=20, height=3, text='Sales', command=lambda: print('sr'))  # mysql
    sr_b.grid(row=0, column=2, sticky=EW, padx=5, pady=5)

    def Back():
        root.deiconify()
        rw.destroy()

    re_b = Button(rm_f, fg='white', bg='#d30000', width=20, height=3, text='Return to Menu', command=Back)
    re_b.grid(row=1, columnspan=3, sticky=EW, padx=5, pady=5)

    rw.update()
    rw.geometry(f'{rw.winfo_width()}x{rw.winfo_height()}+{(rw.winfo_screenwidth() - rw.winfo_width()) // 2}+{(rw.winfo_screenheight() - rw.winfo_height()) // 2}')
    rw.minsize(width=rw.winfo_width(), height=rw.winfo_height())


if __name__ == '__main__':
    root = Tk()
    root.title('Accounts Receivable')
    root.grid_columnconfigure(0, weight=1)

    title_f = Frame(root, bg='#3D3D3D', highlightbackground='gray', highlightthickness=5)
    title_f.grid_columnconfigure(0, weight=1)
    title_f.grid(row=0, column=0, sticky=EW)

    title_l = Label(title_f, fg='white', bg='#3D3D3D', font=('TkDefaultFont', 16), text='Customer Sales')
    title_l.grid(padx=5, pady=5)

    menu_f = Frame(root, bg='#808080')
    menu_f.grid(row=1, column=0)

    customers_b = Button(menu_f, fg='white', bg='#d33d00', width=20, height=3, text='Edit / Enter Customers',
                         command=openC)
    customers_b.grid(row=0, column=0, sticky=EW, padx=5, pady=5)

    products_b = Button(menu_f, fg='white', bg='#d33d00', width=20, height=3, text='Edit / Enter Products',
                        command=openP)
    products_b.grid(row=0, column=1, sticky=EW, padx=5, pady=5)

    sales_b = Button(menu_f, fg='white', bg='#d33d00', width=20, height=3, text='Edit / Enter Sales', command=openS)
    sales_b.grid(row=0, column=2, sticky=EW, padx=5, pady=5)

    reports_b = Button(menu_f, fg='white', bg='#A14C4C', width=20, height=3, text='Reports', command=openR)
    reports_b.grid(row=1, column=0, sticky=EW, padx=5, pady=5)

    exit_b = Button(menu_f, fg='white', bg='#d30000', width=20, height=3, text='Exit', command=root.destroy)
    exit_b.grid(row=1, column=2, sticky=EW, padx=5, pady=5)

    root.update()
    root.geometry(f'{root.winfo_width()}x{root.winfo_height()}+{(root.winfo_screenwidth() - root.winfo_width()) // 2}+{(root.winfo_screenheight() - root.winfo_height()) // 2}')
    root.minsize(width=root.winfo_width(), height=root.winfo_height())

    root.mainloop()
