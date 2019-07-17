# Introduction: #
The purpose of this project is to create a GUI (Graphic user interface) to classify images with cracks, also to let the whole team works on it and share codes with each other. We will be using python along with Tkinter or any GUI library available through python. Below, I will be explaining the over-all expectation for this project. Planning how it approximately will look like and explain the functionality of the program. 
<br />
<br />

# Details
Image below is an approximate of what the final product should look like. 

![alt text](https://i.imgur.com/V1Al9Hm.png)

<br />

### Now lets go over the details of the functiality this GUI should have:
<br />

**1. Open Button:** This button should have the functionality to load an image to our program. When loaded, we should be able to edit it.

**2. Open Directory:** The purpose of creating this button is when we have a lot of images, we can load them all through a directory and just go through them instead of open each image individually. 

**3. Save Crack:** Save crack will be very convenient to have in our program, once we select a crack in an image we can just click save crack button to a directory of our choice. So that we don't have to open a directory and save it there each time. It will save us a lot of time and effort. 
<br />

![alt text](https://i.imgur.com/3Ve0nKw.png)
<br />
<br />
<br />

**4. Save Non-Crack:** Same as save crack, it will save a selected image to a non-crack directory. 
<br />

![alt text](https://i.imgur.com/iXRztt8.png)
<br />
<br />
<br />

**5. Crop Tool:** This tool should allow us to select an image of the crack with a box **(128 by 128)** as shown in the image. 

**6. Work Place:** Work place will be the most challenging code for us, when loaded through the open button, is should show up on the frame as shown on the image. 
**We also need to figure out a way to make keymap for all these buttons to make our life easier.**
# How it works?
<br />

**1. Locate cracks in the image and press left click on your mouse to operate.**
<br />
<br />
![alt text](https://i.imgur.com/dnyeJWS.png)                                                                                              <br /> 
<br />

**2. New window will pop up, with 2 options (Proceed, Discard)**
<br />
<br />
![alt text](https://i.imgur.com/mmfWPpK.png)  
<br /> 
<br />
**3. After saving, should come back to work place. A box should be highlighted to indicate that spot have been already worked on and new box will appear. See figure(1)**
<br />
<br />
![alt text](https://i.imgur.com/7ldvZ92.png)  
<br />
<br />
**This is how it should look like after locating all cracks in the image**
<br />
<br />
![alt text](https://i.imgur.com/WMtImN2.png)  
<br /> 
<br />


# Working with GUI: 
We will be using Python to create this GUI. We can use [TKinter Library](https://www.tutorialspoint.com/python/python_gui_programming). There is [6 libraries for GUI framework](https://blog.resellerclub.com/the-6-best-python-gui-frameworks-for-developers/), You can chose whatever it's easier for you. Personally, I will be using Tkinter. We will use Github to communicate our codes. [Please see Reference](https://help.github.com/en/articles/basic-writing-and-formatting-syntax#relative-links) to get familiar with Github. 

# How to start? 
We will start by creating phases, each phase will have its own set of challenges. With each phase we will try to make everyone on the team to have role. we will discuss roles later.



