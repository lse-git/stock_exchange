# Author:
# _____ ___
#|  ___/ _ \__/\__
#| |_ | | | \    /
#|  _|| |_| /_  _\
#|_|   \___/  \/


# Import all dependencies
from tkinter import *
import csv


class chart():
    def __init__(self, root):
        self.chartCanvas = Canvas(root)
        self.arc = self.chartCanvas.create_arc(0, 0, 100, 100, start=0, extent=90, fill="#ff0000")

    def read_file_and_plot(self, path):
        with open(path) as self.csvFile:
            self.csvReader = csv.reader(self.csvFile, delimiter=",")
            for self.row in self.csvReader:
                print(self.row)

    def pack(self, expand, fill):
        self.chartCanvas.pack(expand=expand, fill=fill)
