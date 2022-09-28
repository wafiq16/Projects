

import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog
import numpy as np
import tensorflow
from tensorflow.keras.applications import vgg16
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.vgg16 import decode_predictions
from keras.models import load_model

import os


def load_img():
    global img, image_data
    for img_display in frame.winfo_children():
        img_display.destroy()

    image_data = filedialog.askopenfilename(initialdir="/", title="Choose an image",
                                            filetypes=(("all files", "*.*"), ("png files", "*.png")))
    basewidth = 400  # Processing image for dysplaying
    print(image_data)
    img = Image.open(image_data)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    file_name = image_data.split('/')
    panel = tk.Label(frame, text=str(
        file_name[len(file_name)-1]).upper()).pack()
    panel_image = tk.Label(frame, image=img).pack()


def identify():
    os.system('python yolov5/detect.py --weights yolov5/runs/train/yolov5s_results/weights/best.pt --img 416 --conf 0.4 --source ' + image_data)
    file1 = open("bounded.txt", "r+")
    global img, original
    for img_display in frame.winfo_children():
        img_display.destroy()
    path = file1.read()
    original = Image.open(path)
    print(path)
    file1.close()
    img = original
    basewidth = 400
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    file_name = path.split('/')
    file1 = open("status.txt", "r+")
    status = file1.read()
    print(status)
    file1.close()
    panel = tk.Label(frame, text=str(
        file_name[len(file_name)-1]).upper()).pack()
    panel = tk.Label(frame, text=str(status).upper()).pack()
    panel_image = tk.Label(frame, image=img).pack()


def classify():
    file1 = open("cropped.txt", "r+")
    global img, original
    for img_display in frame.winfo_children():
        img_display.destroy()
    path = file1.read()
    original = Image.open(path)
    print(path)
    file1.close()
    original = original.resize((150, 150), Image.ANTIALIAS)
    img_arr = img_to_array(original)
    x = np.array([img_arr])
    preds = gender_model.predict(x)[0]
    pred_class = np.argmax(preds)
    classes = ['betina', 'jantan']
    label = classes[pred_class]
    # table = tk.Label(
    #     frame, text="Top image class predictions and confidences").pack()
    print(preds)
    result = tk.Label(frame,
                      text="gender : " + str(label).upper()).pack()
    img = original
    basewidth = 400
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    file_name = path.split('/')
    panel = tk.Label(frame, text=str(
        file_name[len(file_name)-1]).upper()).pack()
    panel_image = tk.Label(frame, image=img).pack()


root = tk.Tk()
root.title('Portable Image Classifier')
root.iconbitmap('parrot.png')
root.resizable(False, False)
tit = tk.Label(root, text="Portable Image Classifier",
               padx=25, pady=6, font=("", 12)).pack()
canvas = tk.Canvas(root, height=500, width=500, bg='grey')
canvas.pack()
# frame = tk.Frame(root, bg='white')
# frame.place(relwidth=0.8, relheight=0.3, relx=0.1, rely=0.1)
frame = tk.Frame(root, bg='white')
frame.place(relwidth=0.8, relheight=0.6, relx=0.1, rely=0.1)
chose_image = tk.Button(root, text='Choose Image',
                        padx=35, pady=10,
                        fg="white", bg="gray", command=load_img)
chose_image.pack(side=tk.LEFT)
class_image_cere = tk.Button(root, text='Identify',
                             padx=35, pady=10,
                             fg="white", bg="gray", command=identify)
class_image_cere.place(relx=0.5, rely=0.96, anchor=tk.CENTER)
class_image_gender = tk.Button(root, text='Classify',
                               padx=35, pady=10,
                               fg="white", bg="gray", command=classify)
class_image_gender.pack(side=tk.RIGHT)
gender_model = load_model('Xception_model.h5')
root.mainloop()
