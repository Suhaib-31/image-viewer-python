from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

root = Tk()
root.title("Image Viewer")
root.geometry("900x700")

image_label = Label(root)
image_label.pack(expand=True)

current_image = None

def open_image():

    global current_image

    file_path = filedialog.askopenfilename(
        filetypes=[
            ("Image Files", "*.png *.jpg *.jpeg *.gif"),
            ("All Files", "*.*")
        ]
    )

    if file_path:

        image = Image.open(file_path)

        image.thumbnail((800, 600))

        current_image = ImageTk.PhotoImage(image)

        image_label.config(image=current_image)

open_btn = Button(
    root,
    text="Open Image",
    font=("Arial", 14),
    command=open_image
)

open_btn.pack(pady=10)

root.mainloop()