# Joe Olpin
# Accounts Receivable
# 8/30/2021 - 9/8/2021

from tkinter import *
from tkinter import messagebox
import mysql


def openC():
    root.withdraw()

    cw = Toplevel(root, bg='#808080')
    cw.title('Customers')
    cw.grid_columnconfigure(0, weight=1)

    def openI():
        cw.withdraw()

        w = Toplevel(cw, bg='#808080')
        w.title('Create New Customer')
        w.grid_columnconfigure(0, weight=1)

        f = Frame(w, bg='#808080')
        f.grid()

        fname_l = Label(f, text='First Name')
        fname_l.grid(row=0, column=0, sticky=EW, padx=5, pady=5)
        fname_e = Entry(f)
        fname_e.grid(row=0, column=1, sticky=EW, padx=5, pady=5)

        lname_l = Label(f, text='Last Name')
        lname_l.grid(row=1, column=0, sticky=EW, padx=5, pady=5)
        lname_e = Entry(f)
        lname_e.grid(row=1, column=1, sticky=EW, padx=5, pady=5)

        email_l = Label(f, text='Email Address')
        email_l.grid(row=2, column=0, sticky=EW, padx=5, pady=5)
        email_e = Entry(f)
        email_e.grid(row=2, column=1, sticky=EW, padx=5, pady=5)

        phone_l = Label(f, text='Phone Number')
        phone_l.grid(row=3, column=0, sticky=EW, padx=5, pady=5)
        phone_e = Entry(f)
        phone_e.grid(row=3, column=1, sticky=EW, padx=5, pady=5)

        address_l = Label(f, text='Mailing Address')
        address_l.grid(row=4, column=0, sticky=EW, padx=5, pady=5)
        address_e = Entry(f)
        address_e.grid(row=4, column=1, sticky=EW, padx=5, pady=5)

        state_l = Label(f, text='State')
        state_l.grid(row=5, column=0, sticky=EW, padx=5, pady=5)
        state_e = Entry(f)
        state_e.grid(row=5, column=1, sticky=EW, padx=5, pady=5)

        city_l = Label(f, text='City')
        city_l.grid(row=6, column=0, sticky=EW, padx=5, pady=5)
        city_e = Entry(f)
        city_e.grid(row=6, column=1, sticky=EW, padx=5, pady=5)

        zipcode_l = Label(f, text='Zip Code')
        zipcode_l.grid(row=7, column=0, sticky=EW, padx=5, pady=5)
        zipcode_e = Entry(f)
        zipcode_e.grid(row=7, column=1, sticky=EW, padx=5, pady=5)

        def do():
            mysql.insertCustomer(fname_e.get(), lname_e.get(), email_e.get(), phone_e.get(), address_e.get(), state_e.get(), city_e.get(), zipcode_e.get())
            fname_e.delete(0, END)
            lname_e.delete(0, END)
            email_e.delete(0, END)
            phone_e.delete(0, END)
            address_e.delete(0, END)
            state_e.delete(0, END)
            city_e.delete(0, END)
            zipcode_e.delete(0, END)
            messagebox.showinfo('Created', 'A customer was made.')

        summit_b = Button(f, fg='white', bg='#d33d00', text='Create', command=do)
        summit_b.grid(row=8, column=1, sticky=EW, padx=5, pady=5)

        def iBack():
            cw.deiconify()
            w.destroy()

        back_b = Button(f, fg='white', bg='#d30000', text='Back to Customer Menu', command=iBack)
        back_b.grid(row=8, column=0, sticky=EW, padx=5, pady=5)

        w.update()
        w.focus_force()
        w.geometry(f'{w.winfo_width()}x{w.winfo_height()}+{(w.winfo_screenwidth() - w.winfo_width()) // 2}+{(w.winfo_screenheight() - w.winfo_height()) // 2}')
        w.minsize(width=w.winfo_width(), height=w.winfo_height())

    def openE():
        cw.withdraw()
        cid = IntVar(cw, 1)

        w = Toplevel(cw, bg='#808080')
        w.title('Edit Existing Customer')
        w.grid_columnconfigure(0, weight=1)

        f = Frame(w, bg='#808080')
        f.grid()

        cid_l = Label(f, text='Customer Code')
        cid_l.grid(row=0, column=0, sticky=EW, padx=5, pady=5, columnspan=3)

        fname_l = Label(f, text='First Name')
        fname_l.grid(row=1, column=0, sticky=EW, padx=5, pady=5)
        fname_e = Entry(f)
        fname_e.grid(row=1, column=1, sticky=EW, padx=5, pady=5, columnspan=2)

        lname_l = Label(f, text='Last Name')
        lname_l.grid(row=2, column=0, sticky=EW, padx=5, pady=5)
        lname_e = Entry(f)
        lname_e.grid(row=2, column=1, sticky=EW, padx=5, pady=5, columnspan=2)

        email_l = Label(f, text='Email Address')
        email_l.grid(row=3, column=0, sticky=EW, padx=5, pady=5)
        email_e = Entry(f)
        email_e.grid(row=3, column=1, sticky=EW, padx=5, pady=5, columnspan=2)

        phone_l = Label(f, text='Phone Number')
        phone_l.grid(row=4, column=0, sticky=EW, padx=5, pady=5)
        phone_e = Entry(f)
        phone_e.grid(row=4, column=1, sticky=EW, padx=5, pady=5, columnspan=2)

        address_l = Label(f, text='Mailing Address')
        address_l.grid(row=5, column=0, sticky=EW, padx=5, pady=5)
        address_e = Entry(f)
        address_e.grid(row=5, column=1, sticky=EW, padx=5, pady=5, columnspan=2)

        state_l = Label(f, text='State')
        state_l.grid(row=6, column=0, sticky=EW, padx=5, pady=5)
        state_e = Entry(f)
        state_e.grid(row=6, column=1, sticky=EW, padx=5, pady=5, columnspan=2)

        city_l = Label(f, text='City')
        city_l.grid(row=7, column=0, sticky=EW, padx=5, pady=5)
        city_e = Entry(f)
        city_e.grid(row=7, column=1, sticky=EW, padx=5, pady=5, columnspan=2)

        zipcode_l = Label(f, text='Zip Code')
        zipcode_l.grid(row=8, column=0, sticky=EW, padx=5, pady=5)
        zipcode_e = Entry(f)
        zipcode_e.grid(row=8, column=1, sticky=EW, padx=5, pady=5, columnspan=2)

        def do():
            mysql.updateCustomer(cid.get(), fname_e.get(), lname_e.get(), email_e.get(), phone_e.get(), address_e.get(), state_e.get(), city_e.get(), zipcode_e.get())
            messagebox.showinfo('Changed', 'A customer was edited.')

        summit_b = Button(f, fg='white', bg='#d33d00', text='Edit', command=do)
        summit_b.grid(row=9, column=1, sticky=EW, padx=5, pady=5)

        def iBack():
            cw.deiconify()
            w.destroy()

        back_b = Button(f, fg='white', bg='#d30000', text='Back to Customer Menu', command=iBack)
        back_b.grid(row=9, column=0, sticky=EW, padx=5, pady=5)

        def remove():
            mysql.deleteCustomer(cid.get())
            messagebox.showinfo('Deleted', 'A customer was removed.')
            iBack()

        delete_b = Button(f, fg='white', bg='#d3d300', text='Delete Customer', command=remove)
        delete_b.grid(row=9, column=2, sticky=EW, padx=5, pady=5)

        w.withdraw()

        iw = Toplevel(root, bg='#808080')
        iw.resizable(width=False, height=False)

        coptions = mysql.getOptions('Customers')
        if not coptions:
            iw.withdraw()
            messagebox.showerror('Database Error', 'There are no customers to edit.')
            iw.destroy()
            iBack()
            return

        wcid_l = Label(iw, text='Customer Code')
        wcid_l.grid(row=0, column=0, sticky=EW, padx=5, pady=5)
        wcid_m = OptionMenu(iw, cid, *coptions)
        #wcid_m.config(bd=0)
        wcid_m.grid(row=0, column=1, sticky=EW, padx=5, pady=5)

        def enable():
            c = mysql.getCustomer(cid.get())
            cid_l.configure(text=f'Customer Code: {c[0]}')
            fname_e.insert(0, c[1])
            lname_e.insert(0, c[2])
            email_e.insert(0, c[3])
            phone_e.insert(0, c[4])
            address_e.insert(0, c[5])
            state_e.insert(0, c[6])
            city_e.insert(0, c[7])
            zipcode_e.insert(0, c[8])
            w.deiconify()
            iw.destroy()

        grab_b = Button(iw, fg='white', bg='#d33d00', text='Get Customer to edit', command=enable)
        grab_b.grid(row=1, column=1, sticky=EW, padx=5, pady=5)

        def iiBack():
            iw.destroy()
            iBack()

        ib_b = Button(iw, fg='white', bg='#d30000', text='Back to Customer Menu', command=iiBack)
        ib_b.grid(row=1, column=0, sticky=EW, padx=5, pady=5)

        iw.update()
        iw.focus_force()
        iw.geometry(f'{iw.winfo_width()}x{iw.winfo_height()}+{(iw.winfo_screenwidth() - iw.winfo_width()) // 2}+{(iw.winfo_screenheight() - iw.winfo_height()) // 2}')

        w.update()
        w.focus_force()
        w.geometry(f'{w.winfo_width()}x{w.winfo_height()}+{(w.winfo_screenwidth() - w.winfo_width()) // 2}+{(w.winfo_screenheight() - w.winfo_height()) // 2}')
        w.minsize(width=w.winfo_width(), height=w.winfo_height())

    ct_f = Frame(cw, bg='#3D3D3D', highlightbackground='gray', highlightthickness=5)
    ct_f.grid_columnconfigure(0, weight=1)
    ct_f.grid(row=0, column=0, sticky=EW)

    ct_l = Label(ct_f, fg='white', bg='#3D3D3D', font=('TkDefaultFont', 13), text='Customer Database')
    ct_l.grid(padx=5, pady=5)

    cm_f = Frame(cw, bg='#808080')
    cm_f.grid(row=1, column=0)

    new_b = Button(cm_f, fg='white', bg='#d33d00', width=20, height=3, text='Enter New Customer', command=openI)
    new_b.grid(row=0, column=0, padx=5, pady=5)

    edit_b = Button(cm_f, fg='white', bg='#d33d00', width=20, height=3, text='Edit Existing Customer', command=openE)
    edit_b.grid(row=0, column=1, padx=5, pady=5)

    def Back():
        root.deiconify()
        cw.destroy()

    ce_b = Button(cm_f, fg='white', bg='#d30000', width=20, height=3, text='Return to Menu', command=Back)
    ce_b.grid(row=1, columnspan=2, padx=5, pady=5)

    cw.update()
    cw.focus_force()
    cw.geometry(f'{cw.winfo_width()}x{cw.winfo_height()}+{(cw.winfo_screenwidth() - cw.winfo_width()) // 2}+{(cw.winfo_screenheight() - cw.winfo_height()) // 2}')
    cw.minsize(width=cw.winfo_width(), height=cw.winfo_height())


def openP():
    root.withdraw()

    pw = Toplevel(root, bg='#808080')
    pw.title('Products')
    pw.grid_columnconfigure(0, weight=1)

    def openI():
        pw.withdraw()

        w = Toplevel(pw, bg='#808080')
        w.title('Create New Product')
        w.grid_columnconfigure(0, weight=1)

        f = Frame(w, bg='#808080')
        f.grid()

        title_l = Label(f, text='Title')
        title_l.grid(row=0, column=0, sticky=EW, padx=5, pady=5)
        title_e = Entry(f)
        title_e.grid(row=0, column=1, sticky=EW, padx=5, pady=5)

        mingrade_l = Label(f, text='Date Purchased')
        mingrade_l.grid(row=1, column=0, sticky=EW, padx=5, pady=5)
        mingrade_e = Entry(f)
        mingrade_e.grid(row=1, column=1, sticky=EW, padx=5, pady=5)

        maxgrade_l = Label(f, text='Date Purchased')
        maxgrade_l.grid(row=2, column=0, sticky=EW, padx=5, pady=5)
        maxgrade_e = Entry(f)
        maxgrade_e.grid(row=2, column=1, sticky=EW, padx=5, pady=5)

        price_l = Label(f, text='Price $')
        price_l.grid(row=3, column=0, sticky=EW, padx=5, pady=5)
        price_e = Entry(f)
        price_e.grid(row=3, column=1, sticky=EW, padx=5, pady=5)

        def do():
            mysql.insertProduct(title_e.get(), mingrade_e.get(), maxgrade_e.get(), price_e.get())
            title_e.delete(0, END)
            mingrade_e.delete(0, END)
            maxgrade_e.delete(0, END)
            price_e.delete(0, END)
            messagebox.showinfo('Created', 'A product was made.')

        summit_b = Button(f, fg='white', bg='#d33d00', text='Create', command=do)
        summit_b.grid(row=4, column=1, sticky=EW, padx=5, pady=5)

        def iBack():
            pw.deiconify()
            w.destroy()

        back_b = Button(f, fg='white', bg='#d30000', text='Back to Product Menu', command=iBack)
        back_b.grid(row=4, column=0, sticky=EW, padx=5, pady=5)

        w.update()
        w.focus_force()
        w.geometry(f'{w.winfo_width()}x{w.winfo_height()}+{(w.winfo_screenwidth() - w.winfo_width()) // 2}+{(w.winfo_screenheight() - w.winfo_height()) // 2}')
        w.minsize(width=w.winfo_width(), height=w.winfo_height())

    def openE():
        pw.withdraw()
        pid = IntVar(pw, 1)

        w = Toplevel(pw, bg='#808080')
        w.title('Edit Existing Product')
        w.grid_columnconfigure(0, weight=1)

        f = Frame(w, bg='#808080')
        f.grid()

        pid_l = Label(f, text='Product Code')
        pid_l.grid(row=0, column=0, sticky=EW, padx=5, pady=5, columnspan=3)

        title_l = Label(f, text='Title')
        title_l.grid(row=1, column=0, sticky=EW, padx=5, pady=5)
        title_e = Entry(f)
        title_e.grid(row=1, column=1, sticky=EW, padx=5, pady=5, columnspan=2)

        mingrade_l = Label(f, text='Date Purchased')
        mingrade_l.grid(row=2, column=0, sticky=EW, padx=5, pady=5)
        mingrade_e = Entry(f)
        mingrade_e.grid(row=2, column=1, sticky=EW, padx=5, pady=5, columnspan=2)

        maxgrade_l = Label(f, text='Date Purchased')
        maxgrade_l.grid(row=3, column=0, sticky=EW, padx=5, pady=5)
        maxgrade_e = Entry(f)
        maxgrade_e.grid(row=3, column=1, sticky=EW, padx=5, pady=5, columnspan=2)

        price_l = Label(f, text='Price $')
        price_l.grid(row=4, column=0, sticky=EW, padx=5, pady=5)
        price_e = Entry(f)
        price_e.grid(row=4, column=1, sticky=EW, padx=5, pady=5, columnspan=2)

        def do():
            mysql.updateProduct(pid.get(), title_e.get(), mingrade_e.get(), maxgrade_e.get(), price_e.get())
            messagebox.showinfo('Changed', 'A Product was edited.')

        summit_b = Button(f, fg='white', bg='#d33d00', text='Edit', command=do)
        summit_b.grid(row=5, column=1, sticky=EW, padx=5, pady=5)

        def iBack():
            pw.deiconify()
            w.destroy()

        back_b = Button(f, fg='white', bg='#d30000', text='Back to Product Menu', command=iBack)
        back_b.grid(row=5, column=0, sticky=EW, padx=5, pady=5)

        def remove():
            mysql.deleteProduct(pid.get())
            messagebox.showinfo('Deleted', 'A Product was removed.')
            iBack()

        delete_b = Button(f, fg='white', bg='#d3d300', text='Delete Product', command=remove)
        delete_b.grid(row=5, column=2, sticky=EW, padx=5, pady=5)

        w.withdraw()

        iw = Toplevel(root, bg='#808080')
        iw.resizable(width=False, height=False)

        coptions = mysql.getOptions('Products')
        if not coptions:
            iw.withdraw()
            messagebox.showerror('Database Error', 'There are no products to edit.')
            iw.destroy()
            iBack()
            return

        wpid_l = Label(iw, text='Product Code')
        wpid_l.grid(row=0, column=0, sticky=EW, padx=5, pady=5)
        wpid_m = OptionMenu(iw, pid, *coptions)
        #wpid_m.config(bd=0)
        wpid_m.grid(row=0, column=1, sticky=EW, padx=5, pady=5)

        def enable():
            c = mysql.getProduct(pid.get())
            pid_l.configure(text=f'Product Code: {c[0]}')
            title_e.insert(0, c[1])
            mingrade_e.insert(0, c[2])
            maxgrade_e.insert(0, c[3])
            price_e.insert(0, c[4])
            w.deiconify()
            iw.destroy()

        grab_b = Button(iw, fg='white', bg='#d33d00', text='Get Product to edit', command=enable)
        grab_b.grid(row=1, column=1, sticky=EW, padx=5, pady=5)

        def iiBack():
            iw.destroy()
            iBack()

        ib_b = Button(iw, fg='white', bg='#d30000', text='Back to Product Menu', command=iiBack)
        ib_b.grid(row=1, column=0, sticky=EW, padx=5, pady=5)

        iw.update()
        iw.focus_force()
        iw.geometry(f'{iw.winfo_width()}x{iw.winfo_height()}+{(iw.winfo_screenwidth() - iw.winfo_width()) // 2}+{(iw.winfo_screenheight() - iw.winfo_height()) // 2}')

        w.update()
        w.focus_force()
        w.geometry(f'{w.winfo_width()}x{w.winfo_height()}+{(w.winfo_screenwidth() - w.winfo_width()) // 2}+{(w.winfo_screenheight() - w.winfo_height()) // 2}')
        w.minsize(width=w.winfo_width(), height=w.winfo_height())

    pt_f = Frame(pw, bg='#3D3D3D', highlightbackground='gray', highlightthickness=5)
    pt_f.grid_columnconfigure(0, weight=1)
    pt_f.grid(row=0, column=0, sticky=EW)

    pt_l = Label(pt_f, fg='white', bg='#3D3D3D', font=('TkDefaultFont', 13), text='Product Database')
    pt_l.grid(padx=5, pady=5)

    pm_f = Frame(pw, bg='#808080')
    pm_f.grid(row=1, column=0)

    new_b = Button(pm_f, fg='white', bg='#d33d00', width=20, height=3, text='Enter New Product', command=openI)
    new_b.grid(row=0, column=0, padx=5, pady=5)

    edit_b = Button(pm_f, fg='white', bg='#d33d00', width=20, height=3, text='Edit Existing Product', command=openE)
    edit_b.grid(row=0, column=1, padx=5, pady=5)

    def Back():
        root.deiconify()
        pw.destroy()

    pe_b = Button(pm_f, fg='white', bg='#d30000', width=20, height=3, text='Return to Menu', command=Back)
    pe_b.grid(row=1, columnspan=2, padx=5, pady=5)

    pw.update()
    pw.focus_force()
    pw.geometry(f'{pw.winfo_width()}x{pw.winfo_height()}+{(pw.winfo_screenwidth() - pw.winfo_width()) // 2}+{(pw.winfo_screenheight() - pw.winfo_height()) // 2}')
    pw.minsize(width=pw.winfo_width(), height=pw.winfo_height())


def openS():
    root.withdraw()

    sw = Toplevel(root, bg='#808080')
    sw.title('Sales')
    sw.grid_columnconfigure(0, weight=1)

    def openI():
        sw.withdraw()

        w = Toplevel(sw, bg='#808080')
        w.title('Create New Sale')
        w.grid_columnconfigure(0, weight=1)

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
            if not pid_e.get().strip():
                messagebox.showerror('Bad input', 'The product code cannot be blank')
                return
            if not cid_e.get().strip():
                messagebox.showerror('Bad input', 'The customer code cannot be blank')
                return
            mysql.insertSale(pid_e.get(), cid_e.get(), date_e.get(), price_e.get())
            pid_e.delete(0, END)
            cid_e.delete(0, END)
            date_e.delete(0, END)
            price_e.delete(0, END)
            messagebox.showinfo('Created', 'A sale was made.')

        summit_b = Button(f, fg='white', bg='#d33d00', text='Create', command=do)
        summit_b.grid(row=4, column=1, sticky=EW, padx=5, pady=5)

        def iBack():
            sw.deiconify()
            w.destroy()

        back_b = Button(f, fg='white', bg='#d30000', text='Back to Sales Menu', command=iBack)
        back_b.grid(row=4, column=0, sticky=EW, padx=5, pady=5)

        w.update()
        w.focus_force()
        w.geometry(f'{w.winfo_width()}x{w.winfo_height()}+{(w.winfo_screenwidth() - w.winfo_width()) // 2}+{(w.winfo_screenheight() - w.winfo_height()) // 2}')
        w.minsize(width=w.winfo_width(), height=w.winfo_height())

    def openE():
        sw.withdraw()
        sid = IntVar(sw, 1)

        w = Toplevel(sw, bg='#808080')
        w.title('Edit Existing Sale')
        w.grid_columnconfigure(0, weight=1)

        f = Frame(w, bg='#808080')
        f.grid()

        sid_l = Label(f, text='Sale Code')
        sid_l.grid(row=0, column=0, sticky=EW, padx=5, pady=5, columnspan=3)

        pid_l = Label(f, text='Product Code')
        pid_l.grid(row=1, column=0, sticky=EW, padx=5, pady=5)
        pid_e = Entry(f)
        pid_e.grid(row=1, column=1, sticky=EW, padx=5, pady=5, columnspan=2)

        cid_l = Label(f, text='Customer Code')
        cid_l.grid(row=2, column=0, sticky=EW, padx=5, pady=5)
        cid_e = Entry(f)
        cid_e.grid(row=2, column=1, sticky=EW, padx=5, pady=5, columnspan=2)

        date_l = Label(f, text='Date Purchased')
        date_l.grid(row=3, column=0, sticky=EW, padx=5, pady=5)
        date_e = Entry(f)
        date_e.grid(row=3, column=1, sticky=EW, padx=5, pady=5, columnspan=2)

        price_l = Label(f, text='Price Paid')
        price_l.grid(row=4, column=0, sticky=EW, padx=5, pady=5)
        price_e = Entry(f)
        price_e.grid(row=4, column=1, sticky=EW, padx=5, pady=5, columnspan=2)

        def do():
            mysql.updateSale(sid.get(), pid_e.get(), cid_e.get(), date_e.get(), price_e.get())
            messagebox.showinfo('Changed', 'A Sale was edited.')

        summit_b = Button(f, fg='white', bg='#d33d00', text='Edit', command=do)
        summit_b.grid(row=5, column=1, sticky=EW, padx=5, pady=5)

        def iBack():
            sw.deiconify()
            w.destroy()

        back_b = Button(f, fg='white', bg='#d30000', text='Back to Sales Menu', command=iBack)
        back_b.grid(row=5, column=0, sticky=EW, padx=5, pady=5)

        def remove():
            mysql.deleteSale(sid.get())
            messagebox.showinfo('Deleted', 'A Sale was removed.')
            iBack()

        delete_b = Button(f, fg='white', bg='#d3d300', text='Delete Sale', command=remove)
        delete_b.grid(row=5, column=2, sticky=EW, padx=5, pady=5)

        w.withdraw()

        iw = Toplevel(root, bg='#808080')
        iw.resizable(width=False, height=False)

        coptions = mysql.getOptions('Sales')
        if not coptions:
            iw.withdraw()
            messagebox.showerror('Database Error', 'There are no products to edit.')
            iw.destroy()
            iBack()
            return

        wsid_l = Label(iw, text='Sale Code')
        wsid_l.grid(row=0, column=0, sticky=EW, padx=5, pady=5)
        wsid_m = OptionMenu(iw, sid, *coptions)
        #wsid_m.config(bd=0)
        wsid_m.grid(row=0, column=1, sticky=EW, padx=5, pady=5)

        def enable():
            c = mysql.getSale(sid.get())
            sid_l.configure(text=f'Sale Code: {c[0]}')
            pid_e.insert(0, c[1])
            cid_e.insert(0, c[2])
            date_e.insert(0, c[3])
            price_e.insert(0, c[4])
            w.deiconify()
            iw.destroy()

        grab_b = Button(iw, fg='white', bg='#d33d00', text='Get Sale to edit', command=enable)
        grab_b.grid(row=1, column=1, sticky=EW, padx=5, pady=5)

        def iiBack():
            iw.destroy()
            iBack()

        ib_b = Button(iw, fg='white', bg='#d30000', text='Back to Sales Menu', command=iiBack)
        ib_b.grid(row=1, column=0, sticky=EW, padx=5, pady=5)

        iw.update()
        iw.focus_force()
        iw.geometry(f'{iw.winfo_width()}x{iw.winfo_height()}+{(iw.winfo_screenwidth() - iw.winfo_width()) // 2}+{(iw.winfo_screenheight() - iw.winfo_height()) // 2}')

        w.withdraw()
        w.update()
        w.focus_force()
        w.geometry(f'{w.winfo_width()}x{w.winfo_height()}+{(w.winfo_screenwidth() - w.winfo_width()) // 2}+{(w.winfo_screenheight() - w.winfo_height()) // 2}')
        w.minsize(width=w.winfo_width(), height=w.winfo_height())

    st_f = Frame(sw, bg='#3D3D3D', highlightbackground='gray', highlightthickness=5)
    st_f.grid_columnconfigure(0, weight=1)
    st_f.grid(row=0, column=0, sticky=EW)

    st_l = Label(st_f, fg='white', bg='#3D3D3D', font=('TkDefaultFont', 13), text='Sales Database')
    st_l.grid(padx=5, pady=5)

    sm_f = Frame(sw, bg='#808080')
    sm_f.grid(row=1, column=0)

    new_b = Button(sm_f, fg='white', bg='#d33d00', width=20, height=3, text='Enter New Sale', command=openI)
    new_b.grid(row=0, column=0, padx=5, pady=5)

    edit_b = Button(sm_f, fg='white', bg='#d33d00', width=20, height=3, text='Edit Existing Sale', command=openE)
    edit_b.grid(row=0, column=1, padx=5, pady=5)

    def Back():
        root.deiconify()
        sw.destroy()

    se_b = Button(sm_f, fg='white', bg='#d30000', width=20, height=3, text='Return to Menu', command=Back)
    se_b.grid(row=1, columnspan=2, padx=5, pady=5)

    sw.update()
    sw.focus_force()
    sw.geometry(f'{sw.winfo_width()}x{sw.winfo_height()}+{(sw.winfo_screenwidth() - sw.winfo_width()) // 2}+{(sw.winfo_screenheight() - sw.winfo_height()) // 2}')
    sw.minsize(width=sw.winfo_width(), height=sw.winfo_height())


def openR():
    root.withdraw()

    rw = Toplevel(root, bg='#808080')
    rw.title('Views')
    rw.grid_columnconfigure(0, weight=1)

    def openV(what):
        rw.withdraw()

        w = Toplevel(rw, bg='#808080')
        w.title(f'Viewing {what}')
        w.grid_columnconfigure(0, weight=1)

        f_c = Frame(w, bg='#808080')  # 455, 1000
        f_c.grid(row=1, ipadx=5, ipady=5, sticky=EW)
        f_c.grid_columnconfigure(0, weight=1)
        f_c.grid_rowconfigure(0, weight=1)

        f = Canvas(f_c, bg='#808080', bd=1, relief='solid', width=450, height=300, scrollregion=(0, 0, 900, 600))  # 430, 1000 | 430, 256
        f.grid()

        s = Scrollbar(f_c, orient=VERTICAL)
        s.grid(row=0, column=1, sticky=NS)

        s.config(command=f.yview)
        f.config(yscrollcommand=s.set)
        # ^ todo https://tkdocs.com/shipman/connecting-scrollbars.html

        tv = mysql.viewTable(what)

        fields = {
            'Customers': ['Customer Code', 'First Name', 'Last Name', 'Email', 'Phone', 'Address', 'State', 'City', 'Zipcode'],
            'Products': ['Product code', 'Title', 'Min Grade', 'Max Grade', 'Price'],
            'Sales': ['Sale code', 'Product code', 'Customer Code', 'Date', 'Price Paid']
        }[what]

        for i in range(len(fields)):
            Label(f, relief='solid', bd=1, bg='#878787', text=fields[i]).grid(row=0, column=i, sticky=EW)

        for r in range(len(tv)):
            for c in range(len(tv[r])):
                bg = '#A0A0A0' if r % 2 == 0 else '#606060'
                Label(f, relief='solid', bd=1, bg=bg, text=tv[r][c]).grid(row=r+1, column=c, sticky=EW)

        def iBack():
            rw.deiconify()
            w.destroy()

        b_f = Frame(w, bg='#808080')
        b_f.grid(row=2, sticky=EW)
        b_f.grid_columnconfigure(0, weight=1)
        back_b = Button(b_f, fg='white', bg='#d30000', text='Back to Reports Menu', command=iBack)
        back_b.grid(pady=5)

        w.update()
        w.focus_force()
        w_height = w.winfo_height() if w.winfo_height()+20 < w.winfo_screenheight() else w.winfo_screenheight()//3
        w.geometry(f'{w.winfo_width()}x{w_height}+{(w.winfo_screenwidth() - w.winfo_width()) // 2}+{(w.winfo_screenheight() - w_height) // 2}')
        w.minsize(width=w.winfo_width(), height=1)

    rt_f = Frame(rw, bg='#3D3D3D', highlightbackground='gray', highlightthickness=5)
    rt_f.grid_columnconfigure(0, weight=1)
    rt_f.grid(row=0, column=0, sticky=EW)

    rt_l = Label(rt_f, fg='white', bg='#3D3D3D', font=('TkDefaultFont', 13), text='Reports')
    rt_l.grid(padx=5, pady=5)

    rm_f = Frame(rw, bg='#808080')
    rm_f.grid(row=1, column=0)

    cr_b = Button(rm_f, fg='white', bg='#d33d00', width=20, height=3, text='Customers', command=lambda: openV('Customers'))
    cr_b.grid(row=0, column=0, padx=5, pady=5)

    pr_b = Button(rm_f, fg='white', bg='#d33d00', width=20, height=3, text='Products', command=lambda: openV('Products'))
    pr_b.grid(row=0, column=1, padx=5, pady=5)

    sr_b = Button(rm_f, fg='white', bg='#d33d00', width=20, height=3, text='Sales', command=lambda: openV('Sales'))
    sr_b.grid(row=0, column=2, padx=5, pady=5)

    def Back():
        root.deiconify()
        rw.destroy()

    re_b = Button(rm_f, fg='white', bg='#d30000', height=3, text='Return to Menu', command=Back)
    re_b.grid(row=1, columnspan=3, sticky=EW, padx=5, pady=5)

    rw.update()
    rw.focus_force()
    rw.geometry(f'{rw.winfo_width()}x{rw.winfo_height()}+{(rw.winfo_screenwidth() - rw.winfo_width()) // 2}+{(rw.winfo_screenheight() - rw.winfo_height()) // 2}')
    rw.minsize(width=rw.winfo_width(), height=rw.winfo_height())

    '''DGS needs the following features of their database:
        1) Customer Report
        2) Product Sales History
        3) Product Marketing Schedule'''  # todo


if __name__ == '__main__':
    root = Tk()
    root.config(bg='#808080')
    root.title('Accounts Receivable')
    root.grid_columnconfigure(0, weight=1)

    head_f = Frame(root, bg='#3D3D3D', highlightbackground='gray', highlightthickness=5)
    head_f.grid_columnconfigure(0, weight=1)
    head_f.grid(row=0, column=0, sticky=EW)

    head_l = Label(head_f, fg='white', bg='#3D3D3D', font=('TkDefaultFont', 16), text='Customer Sales')
    head_l.grid(padx=5, pady=5)

    menu_f = Frame(root, bg='#808080')
    menu_f.grid(row=1, column=0)

    customers_b = Button(menu_f, fg='white', bg='#d33d00', width=20, height=3, text='Edit / Enter Customers', command=openC)
    customers_b.grid(row=0, column=0, padx=5, pady=5)

    products_b = Button(menu_f, fg='white', bg='#d33d00', width=20, height=3, text='Edit / Enter Products', command=openP)
    products_b.grid(row=0, column=1, padx=5, pady=5)

    sales_b = Button(menu_f, fg='white', bg='#d33d00', width=20, height=3, text='Edit / Enter Sales', command=openS)
    sales_b.grid(row=0, column=2, padx=5, pady=5)

    reports_b = Button(menu_f, fg='white', bg='#A14C4C', width=20, height=3, text='Reports', command=openR)
    reports_b.grid(row=1, column=0, padx=5, pady=5)

    exit_b = Button(menu_f, fg='white', bg='#d30000', width=20, height=3, text='Exit', command=root.destroy)
    exit_b.grid(row=1, column=2, padx=5, pady=5)

    root.update()
    root.geometry(f'{root.winfo_width()}x{root.winfo_height()}+{(root.winfo_screenwidth() - root.winfo_width()) // 2}+{(root.winfo_screenheight() - root.winfo_height()) // 2}')
    root.minsize(width=root.winfo_width(), height=root.winfo_height())

    root.mainloop()
