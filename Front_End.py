"""
A Program that stores this book info
Title, Author
Year, ISBN

User can:
view all records
search an entry
add an entry
update entry
delete
close
"""

from tkinter import *
from Back_End import Database


database = Database("books.db")


class Window(object):

    def __init__(self, window):

        self.window = window

        self.window.wm_title("Bookstore")

        l1 = Label(window, text="Title")
        l1.grid(row=0, column=0)

        l1 = Label(window, text="Author")
        l1.grid(row=0, column=2)

        l1 = Label(window, text="Year")
        l1.grid(row=1, column=0)

        l1 = Label(window, text="ISBN")
        l1.grid(row=1, column=2)

        self.title_text = StringVar()
        self.e1 = Entry(window, textvariable=self.title_text)
        self.e1.grid(row=0, column=1)

        self.author_text = StringVar()
        self.e2 = Entry(window, textvariable=self.author_text)
        self.e2.grid(row=0, column=3)

        self.year_text = StringVar()
        self.e3 = Entry(window, textvariable=self.year_text)
        self.e3.grid(row=1, column=1)

        self.isbn_text = StringVar()
        self.e4 = Entry(window, textvariable=self.isbn_text)
        self.e4.grid(row=1, column=3)

        self.list1 = Listbox(window, height=6, width=35)
        self.list1.grid(row=2, column=0, rowspan=6, columnspan=2)

        sb1 = Scrollbar(window)
        sb1.grid(row=2, column=2, rowspan=6)

        self.list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=self.list1.yview)

        self.list1.bind("<<ListboxSelect>>", self.get_selected_row)

        b1 = Button(window, text="View All", width=12,
                    command=self.view_command)
        b1.grid(row=2, column=3)

        b2 = Button(window, text="Search Entry",
                    width=12, command=self.search_command)
        b2.grid(row=3, column=3)

        b3 = Button(window, text="Add Entry",
                    width=12, command=self.add_command)
        b3.grid(row=4, column=3)

        b4 = Button(window, text="Update", width=12,
                    command=self.update_command)
        b4.grid(row=5, column=3)

        b5 = Button(window, text="Delete", width=12,
                    command=self.delete_command)
        b5.grid(row=6, column=3)

        b6 = Button(window, text="Close", width=12, command=window.destroy)
        b6.grid(row=7, column=3)

    def get_selected_row(self, event):

        try:

            index = self.list1.curselection()[0]
            self.selected_row = self.list1.get(index)
            self.e1.delete(0, END)
            self.e1.insert(END, self.selected_row[1])
            self.e2.delete(0, END)
            self.e2.insert(END, self.selected_row[2])
            self.e3.delete(0, END)
            self.e3.insert(END, self.selected_row[3])
            self.e4.delete(0, END)
            self.e4.insert(END, self.selected_row[4])
        except IndexError:
            pass

    def view_command(self):
        self.list1.delete(0, END)
        for row in database.view():
            self.list1.insert(END, row)

    def search_command(self):
        self.list1.delete(0, END)
        for row in database.search(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()):
            self.list1.insert(END, row)

    def add_command(self):
        database.insert(self.title_text.get(), self.author_text.get(),
                        self.year_text.get(), self.isbn_text.get())
        self.list1.delete(0, END)
        self.list1.insert(END, (self.title_text.get(), self.author_text.get(
        ), self.year_text.get(), self.isbn_text.get()))

    def delete_command(self):
        database.delete(self.selected_row[0])

    def update_command(self):
        database.update(self.selected_row[0], self.title_text.get(
        ), self.author_text.get(), self.year_text.get(), self.isbn_text.get())


window = Tk()
Window(window)
window.mainloop()
