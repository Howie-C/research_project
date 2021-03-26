
import tkinter as tk

global username

class Login_window(tk.Frame):

    def __init__(self, master = None):
        super().__init__(master)

        self.master = master
        self.font = ("Comic Sans MS", 10, "bold")
        self.grid()
        self.login_page()

        # Doing some spacing here
        self.grid_rowconfigure(0, minsize=80)
        self.grid_rowconfigure(2, minsize=50)
        self.grid_columnconfigure(0, minsize=200)
        self.grid_columnconfigure(2, minsize=50)


    def login_page(self):

        self.user_txt = tk.Label(self)
        self.user_txt.configure(font = self.font)
        self.user_txt['text'] = 'User Name: '
        self.user_txt.grid(row = 1, column = 1, sticky = 'W')

        self.user_entry = tk.Entry(self)
        self.user_entry = tk.Entry(self)
        self.user_entry.configure(font = self.font)
        self.user_entry.grid(row = 1, column = 3, sticky = 'E')

        #print(self.user_entry.get())
        #print('None')


        self.login = tk.Button(self, text = 'Login', height = 1, width = 10,
                               command = self.go_menu_window)
        self.login.configure(font = self.font)

        self.login.grid(row = 3, column = 1, sticky = 'E')

        self.quit = tk.Button(self, text = 'Exit', fg = 'red', height = 1, width = 10,
                              command = self.master.destroy)
        self.quit.configure(font = self.font)

        self.quit.grid(row = 3, column = 3, sticky = 'W')



    def go_menu_window(self):
        # Close the current window
        global username
        username = self.user_entry.get()
        #print(username)

        self.master.destroy() 
        # Create another window
        self.master = tk.Tk(className = ' Menu Page !') 
        self.master.geometry("600x300")
        self.app = Menu_window(self.master)
        self.master.mainloop()


class Menu_window(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)

        self.master = master
        self.font = ("Comic Sans MS", 10, "bold")
        self.grid()
        self.menu_page()

        # Doing some spacing here
        self.grid_rowconfigure(1, minsize=80)
        self.grid_rowconfigure(3, minsize=20)
        self.grid_rowconfigure(5, minsize=20)
        self.grid_rowconfigure(7, minsize=20)
        self.grid_columnconfigure(0, minsize=220)
        self.grid_columnconfigure(2, minsize=100)



    def menu_page(self):

        self.welcome_txt = tk.Label(self)
        self.welcome_txt.configure(font = self.font)
        self.welcome_txt['text'] = 'Welcome, ' + username + ' !'
        self.welcome_txt.grid(row = 0, column = 0, sticky = 'W')



        self.func_1 = tk.Button(self, text = 'Search Patient Info', height = 1, width = 20,
                               command = self.get_patient_info)

        self.func_1.configure(font = self.font)

        self.func_1.grid(row = 2, column = 1, sticky = 'W')



        self.func_2 = tk.Button(self, text = 'Give Prediction', height = 1, width = 20,
                               command = self.test)

        self.func_2.configure(font = self.font)

        self.func_2.grid(row = 4, column = 1, sticky = 'W')



        self.func_3 = tk.Button(self, text = 'Data Visualization', height = 1, width = 20,
                               command = self.test)

        self.func_3.configure(font = self.font)

        self.func_3.grid(row = 6, column = 1, sticky = 'W')

        self.quit = tk.Button(self, text = 'Exit', fg = 'red', height = 1, width = 10,
                              command = self.master.destroy)
        self.quit.configure(font = self.font)

        self.quit.grid(row = 8, column = 3, sticky = 'W')


    def get_patient_info(self):
        print(username)

    def test(self):
        print('test.')


def task():
    root = tk.Tk(className = ' Welcome !')
    root.geometry("600x300")
    app = Login_window(master=root)

    app.mainloop()

if __name__ == '__main__':
    task()