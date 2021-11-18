# Author:
# _____ ___
#|  ___/ _ \__/\__
#| |_ | | | \    /
#|  _|| |_| /_  _\
#|_|   \___/  \/


# Import dependencies
from charts import chart
from tkinter import *
from tkinter import ttk

class stock_exchange:
    def __init__(self):

        # Creating root window
        self.root = Tk()
        # Giving the window a title
        self.root.title("stock_exchange")

        # Setting up the tabs
        self.tabControl = ttk.Notebook(self.root)
        self.tab1 = ttk.Frame(self.tabControl)
        self.tab2 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab1, text="Tab 1")
        self.tabControl.add(self.tab2, text="Tab 2")
        self.tabControl.pack(expand=1, fill="both")

        self.chartTest = chart(self.tab1)
        self.chartTest.read_file_and_plot("./data/values.csv")
        self.chartTest.pack(expand=1, fill="both")

        self.root.mainloop()
