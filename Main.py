# Data Standardization
# By Dr. HA DO with help from Tallen Smith, Zach Holden, and Hassan Abdulkareem, students at CSUPueblo
# 10/04/19

# Imports necessary libraries
import tkinter as tk
from PIL import Image, ImageTk
import tkinter.filedialog
import time, os, math, glob
import datetime


# Creates a class to hold all the frame information
class App(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        # Isn't currently used
        self.IsLoaded = False
        # This setting will turn the outputted image greyscale
        self.IsGreyscale = False
        self.pack()
        # This is the title of the window
        self.master.title("Data Standardization")
        # This is the primary background color of the window
        self.master.tk_setPalette(background="#4d4d4d")
        # Windows have big spacing issues to think about when they get resized... so I don't let them be resized
        self.master.resizable(False, False)
        # The iconbitmap is the small image in the top left of the window
        self.master.iconbitmap('Wolf.ico')
        # This variable will house the loaded image
        self.loadedImage = 'none'
        # Frames to put the widgets into. Run the program to see where they are, since they're labeled currently
        ImageFrame = tk.Frame(self)
        ImageFrame.pack(side='left', padx=25)
        ProcessedFrame = tk.Frame(self)
        ProcessedFrame.pack(side='right')
        OptionsFrame = tk.Frame(ImageFrame)
        OptionsFrame.pack(side='bottom', pady=10)
        SelectFrame = tk.Frame(ProcessedFrame, height=2)
        SelectFrame.pack(side='top', padx=25)

        # This is where I labeled all the frames. We can delete this in the final product
        tk.Label(ImageFrame, text='This is the Image Frame').pack()
        tk.Label(ProcessedFrame, text='This is the Processed Frame').pack()
        tk.Label(OptionsFrame, text='This is the Options Frame').pack()
        tk.Label(SelectFrame, text='This is the Select Frame').grid(row=0, column=0, columnspan=2)

        # These are the variables to create the canvas where the image will be loaded onto
        canvasHeight = 1080 / 2
        canvasWidth = 1920 / 2
        canvasHeightRegion = 10000
        canvasWidthRegion = 10000
        self.canvas = tk.Canvas(ImageFrame, width=canvasWidth, height=canvasHeight, bg='white', scrollregion=(0,0,canvasHeightRegion,canvasWidthRegion))
        hbar = tk.Scrollbar(ImageFrame, orient=tk.HORIZONTAL)
        hbar.pack(side=tk.BOTTOM, fill=tk.X)
        hbar.config(command=self.canvas.xview)
        vbar = tk.Scrollbar(ImageFrame, orient=tk.VERTICAL)
        vbar.pack(side=tk.RIGHT, fill=tk.Y)
        vbar.config(command=self.canvas.yview)
        self.canvas.config(width=canvasWidth, height=canvasHeight)
        self.canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
        self.canvas.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        #  Bind a click event of the mouse to the canvas
        root.bind("<Key>", self.Key)
        self.canvas.bind("<Button-1>", self.Single_Click)
        self.canvas.bind("<Double-1>", self.Double_Click)
        # This is where I create all the buttons on the screen
        tk.Button(OptionsFrame, text='Load Image', command=self.Load_Image, bg='#6C6C6C', fg='white').pack(side='left',
                                                                                                           padx=10)
        tk.Button(OptionsFrame, text='Saved Folder', command=self.Select_Dir, bg='#6C6C6C', fg='white').pack(side='left',
                                                                                                           padx=10)
        self.folder_entry = tk.Entry(OptionsFrame, bg='#6C6C6C', fg='white')
        self.folder_entry.pack(side='left', padx=10)

        tk.Label(OptionsFrame, text='Image Name:').pack(side='left', padx=10)
        self.image_name = tk.Entry(OptionsFrame, bg='#6C6C6C', fg='white')
        self.image_name.pack(side='left', padx=10)
        self.image_name.insert(tk.END, "image")

        tk.Button(OptionsFrame, text='Save Images', command=self.Save_Images, bg='#6C6C6C', fg='white').pack(
            side='left', padx=10)

        tk.Button(SelectFrame, text='Select All', command=self.Select_All, bg='#6C6C6C', fg='white').grid(row=1,
                                                                                                          column=0)
        tk.Button(SelectFrame, text='Delete Selected', command=self.Delete_Selected, bg='#6C6C6C', fg='white').grid(
            row=1, column=1)

        # This is for the options widgets at the bottom of the page
        # This checkbutton will determine if the output is greyscale or not
        #tk.Checkbutton(OptionsFrame, text='Greyscale', variable=self.IsGreyscale).pack(side='left', padx=30)
        # This creates the slider that will determine the size of the square that each image will be
        #self.resolution = tk.Scale(OptionsFrame, from_=10, to=500, orient='horizontal')
        #self.resolution.pack()
        # This sets the default size to be 125x125
        #self.resolution.set(125)

        # This loads up my 'No Image' picture onto the canvas. Just a placeholder.
        self.loadedImage = ImageTk.PhotoImage(Image.open('crack1.jpg'))
        self.orginalImage = Image.open('crack1.jpg')
        # This self object is required to prevent tkinter from deleting the picture in a trash roundup
        self.img_width = self.loadedImage.width()
        self.img_heigh = self.loadedImage.height()
        self.canvas.create_image(0, 0, anchor='nw', image=self.loadedImage)
        self.img_folder = self.Select_Dir("C:/CSUPueblo/CBASE19/CrackDetection/GUI/images")
        self.Setting() # Default settings

    # Settings
    def Setting(self, box_height=128, box_width=128):
        self.box_height = box_height
        self.box_width = box_width

    # Select a directory
    def Select_Dir(self, img_folder=''):
        if img_folder=='':
            self.img_folder = tk.filedialog.askdirectory()
        else:
            self.img_folder = img_folder
        self.crack_folder = self.img_folder + '/crack'
        self.no_crack_folder = self.img_folder + '/no_crack'
        self.folder_entry.delete(0, len(self.folder_entry.get()))
        self.folder_entry.insert(0, self.img_folder)

    # These callback functions for mouse and keyboard events
    def Key(self, event):
        print("Key pressed", repr(event.char))
        if event.char in ['C', 'c']:   # Save image to folder Crack
            filename = self.Generate_Filename(self.crack_folder, self.image_name.get(), 'crack', 'jpg')
            print(filename)
            self.box_img.save(filename)
        if event.char in ['n', 'N']:   # Save image to folder Crack
            filename = self.Generate_Filename(self.no_crack_folder, self.image_name.get(), 'no_crack', 'jpg')
            print(filename)
            self.box_img.save(filename)

    def Generate_Filename(self, folder, basename, name, extention):
        uniq_filename = str(datetime.datetime.now().date()) + '_' + str(datetime.datetime.now().time()).replace(':','-').replace('.','-')[0:11]
        return "{}/{}_{}_{}.{}".format(folder, basename, name, uniq_filename, extention)



    def Single_Click(self, event):
        print("Left button clicked at", event.x, event.y)
        self.point_x = event.x
        self.point_y = event.y
        # Compute the rectangle coordinators in (x, y)
        box = [event.x - math.ceil(self.box_width/2), event.y - math.ceil(self.box_height/2),
                    event.x + math.floor(self.box_width/2), event.y + math.floor(self.box_height/2)]
        # Correct if box is out of boundaries
        if box[0] < 0:
            box[2] = box[2] - box[0]
            box[0] = 0
        if box[1] < 0:
            box[3] = box[3] - box[1]
            box[1] = 0
        if box[2] > self.img_width:
            box[2] = self.img_width
            box[0] = box[2] - self.box_width
        if box[3] > self.img_heigh:
            box[3] = self.img_heigh
            box[1] = box[3] - self.box_height
        print(self.img_width, self.img_heigh)
        print(box)
        self.box = tuple(box)
        # crop a box
        self.box_img = self.orginalImage.crop(self.box)

    def Double_Click(self, event):
        print("Left button double clicked at", event.x, event.y)

    # These functions control what all the buttons do
    # PyCharm likes to complain because I like do write my functions Like_This
    def Load_Image(self):
        # Troubleshooting dialog
        print('Loading Up Images!')
        # Removes the previously loaded images
        self.canvas.delete('all')
        # Opens up a dialog path where you can find the image you wish to load.
        self.orginalImage = Image.open(tk.filedialog.askopenfilename())
        self.loadedImage = ImageTk.PhotoImage(self.orginalImage)
        self.canvas.create_image(0, 0, anchor='nw', image=self.loadedImage)
        # I still don't currently use this variable. Idk. Could be useful.
        self.IsLoaded = True
        # Image sizes
        self.img_width = self.loadedImage.width()
        self.img_heigh = self.loadedImage.height()

    def Save_Images(self):
        print('Saving Those Images!')

    def Select_All(self):
        print('Selecting All!')

    def Delete_Selected(self):
        print('Delete Selected!')


# I genuinely don't know what this does tbh. But it works so.
if __name__ == '__main__':
    # Uh... create a new window class named root
    root = tk.Tk()
    # Then... make an App with root in it?
    app = App(root)
    # This one runs the mainloop of the app! I know that one. This is what draws the window.
    app.mainloop()
