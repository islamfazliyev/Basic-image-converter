from tkinter import *
from tkinter import ttk, filedialog
import os
from src.converter import convert_image

engine = Tk()
engine.title("Image Converter")
engine.resizable(False, False)

# ----------------------------
# STYLE
style = ttk.Style()
style.theme_use("clam")

style.configure("TButton", padding=8)
style.configure("TLabel", font=("Segoe UI", 10))
style.configure("Title.TLabel", font=("Segoe UI", 14, "bold"))

# ----------------------------
# CALLBACKS
def select_image():
    file_path = filedialog.askopenfilename(
        title="Select Image",
        filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")]
    )
    if file_path:
        e1.delete(0, END)
        e1.insert(0, file_path)

def target_export_folder():
    folder_path = filedialog.askdirectory(title="Select Target Folder")
    if folder_path:
        e2.delete(0, END)
        e2.insert(0, folder_path)

def convert():
    img_path = e1.get()
    out_folder = e2.get()
    fmt = combo.get()
    convert_image(img_path, out_folder, fmt)

# ----------------------------
# LAYOUT
frm = ttk.Frame(engine, padding=20)
frm.grid(sticky="nsew")

frm.columnconfigure(0, weight=1)
frm.columnconfigure(1, weight=1)

ttk.Label(frm, text="Image Converter", style="Title.TLabel")\
    .grid(column=0, row=0, columnspan=2, pady=(0, 15))

ttk.Button(frm, text="Select Image", command=select_image)\
    .grid(column=0, row=1, sticky="ew", padx=5, pady=5)

ttk.Button(frm, text="Target Export Folder", command=target_export_folder)\
    .grid(column=1, row=1, sticky="ew", padx=5, pady=5)

ttk.Label(frm, text="Selected Image")\
    .grid(column=0, row=2, sticky="w", padx=5)

e1 = ttk.Entry(frm, width=45)
e1.grid(column=0, row=3, columnspan=2, sticky="ew", padx=5, pady=5)

ttk.Label(frm, text="Target Folder")\
    .grid(column=0, row=4, sticky="w", padx=5)

e2 = ttk.Entry(frm, width=45)
e2.grid(column=0, row=5, columnspan=2, sticky="ew", padx=5, pady=5)

ttk.Label(frm, text="Output Format")\
    .grid(column=0, row=6, sticky="w", padx=5)

formats = ["PNG", "JPEG", "BMP", "GIF"]
combo = ttk.Combobox(frm, values=formats, state="readonly")
combo.current(0)
combo.grid(column=1, row=6, sticky="ew", padx=5, pady=5)

ttk.Button(frm, text="Convert Image", command=convert)\
    .grid(column=0, row=7, columnspan=2, sticky="ew", padx=5, pady=(15, 5))

engine.mainloop()
