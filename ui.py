from tkinter import *
from PIL import Image,ImageTk
import cv2 as cv
import numpy as np
img=cv.imread('widya.jpg')

def convert_image(image):

    pre_sized_tuple = (300,300)
    img1 = cv.resize(image,pre_sized_tuple)
    img1 = cv.cvtColor(img1,cv.COLOR_BGR2RGB)
    return img1


def load_img_button():
    

    global tk_img
    global default_img
    pil_image = Image.fromarray(convert_image(img))

    tk_img = ImageTk.PhotoImage(pil_image)
    default_img = tk_img
    image_label.config(image=tk_img,text=" ")


def reset_button_func():

    image_label.config(image=default_img,text="")


def blur_button_func():
    global tk_img
    
    blur=convert_image(img)
    
    
    blur=cv.GaussianBlur(blur,(3,3),cv.BORDER_DEFAULT)

    tk_img=ImageTk.PhotoImage(Image.fromarray(blur))

    image_label.config(image=tk_img,text="")

def contour_button_func():
    global tk_img
    gray=convert_image(img)
    gray=cv.cvtColor(gray,cv.COLOR_BGR2GRAY)
    canny=cv.Canny(gray,75,200)
    tk_img=ImageTk.PhotoImage(Image.fromarray(canny))
    image_label.config(image=tk_img,text="")
   

def sharpen_button_func():
   
    global tk_img
    image = convert_image(img)
    
   
    blurred = cv.GaussianBlur(image, (0, 0), 3)

    sharpened = cv.addWeighted(image, 1.5, blurred, -0.5, 0)
    
    tk_img = ImageTk.PhotoImage(Image.fromarray(sharpened))
    image_label.config(image=tk_img, text="")

def emboss_button_func():
    global tk_img
    img_emboss = convert_image(img)
    
    
    gray = cv.cvtColor(img_emboss, cv.COLOR_RGB2GRAY)
    
    
    kernel = np.array([[-2, -1, 0],
                       [-1,  1, 1],
                       [ 0,  1, 2]])
    
    img_emboss = cv.filter2D(gray, -1, kernel)
    
    
    img_emboss = cv.cvtColor(img_emboss, cv.COLOR_GRAY2RGB)
    
    tk_img = ImageTk.PhotoImage(Image.fromarray(img_emboss))
    image_label.config(image=tk_img, text="")

def edge_enhance_button_func():
    global tk_img
    img_enhanced = convert_image(img)
    
    # Edge enhancement using a kernel
    kernel = np.array([[-1, -1, -1],
                      [-1,  9, -1],
                      [-1, -1, -1]])
    
    img_enhanced = cv.filter2D(img_enhanced, -1, kernel)
    
    tk_img = ImageTk.PhotoImage(Image.fromarray(img_enhanced))
    image_label.config(image=tk_img, text="")

def smooth_button_func():
    
    global tk_img
    img_smooth = convert_image(img)
    
    # Apply Gaussian blur (adjust kernel size and sigma)
    img_smooth = cv.GaussianBlur(img_smooth, (5, 5), 0)
    
    tk_img = ImageTk.PhotoImage(Image.fromarray(img_smooth))
    image_label.config(image=tk_img, text="")





window = Tk()

window.title("Image Processing Tool")
window.configure(bg="gray22")
window.minsize(height=600,width=900)


title=Label(window,text="Image Processing",padx=400,font=("Helvetica",20,"bold"),fg="white",bg="gray22")
load_image_btn = Button(text="Load Image",padx=400,command=load_img_button,bg="deep sky blue")

title.grid(row=0,columnspan=10)
load_image_btn.grid(row=1,columnspan=10)


#----button sets-----------

blur_button=Button(text="Blur",command=blur_button_func,bg="turquoise3")
contour_button=Button(text="Contour",command=contour_button_func,bg="turquoise3")
edge_enchane_button=Button(text="Edge Enchance",command=edge_enhance_button_func,bg="turquoise3")
emboss_button=Button(text="Emboss",command=emboss_button_func,bg="turquoise3")
sharpen_button=Button(text="Sharpen",command=sharpen_button_func,bg="turquoise3")
smooth_button=Button(text="Smooth",command=smooth_button_func,bg="turquoise3")
reset_image=Button(text="Reset Image",command=reset_button_func,bg="lime green",padx=100)
save_image=Button(text="Save Image",command=None,bg="purple1",padx=100)

image_label=Label(window,text="",bg="gray22")

image_label.grid(row=3,columnspan=10)


#-----------button set aligment----------


blur_button.grid(row=4,column=1)
contour_button.grid(row=4,column=2)
edge_enchane_button.grid(row=4,column=3)
emboss_button.grid(row=4,column=6)
sharpen_button.grid(row=4,column=7)
smooth_button.grid(row=4,column=8)
reset_image.grid(row=5,column=4)
save_image.grid(row=10,column=4)



window.mainloop()





