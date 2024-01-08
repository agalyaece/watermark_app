from tkinter import *
from PIL import Image, ImageDraw, ImageFont


def watermark_image():
    image_path = input_path_entry.get()
    watermark = watermark_input.get()

    img = Image.open(image_path,"r")
    width, height = img.size

    draw = ImageDraw.Draw(img)
    text = watermark

    font_size = int(width/8)

    font = ImageFont.truetype("arial.ttf", font_size)
    textwidth = draw.textlength(text=text, font=font)
    textheight = draw.textlength(text=text, font=font)

    margin = 10

    x = width - textwidth - margin
    y = height - textheight -margin

    draw.text((x,y), text, font=font,fill="#ed1654")
    img.show()

    img.save("C:/Users/Admin/Downloads/output")


window = Tk()
window.title("Watermarking Images app")
window.config(padx=20,pady=20)


input_path = Label(text="input files path  ")
input_path.grid(row=0, column=0)

input_path_entry = Entry(width=70)
input_path_entry.grid(row=0, column=1)
input_path_entry.focus()

watermark = Label(text="Watermark text  ")
watermark.grid(row=1, column=0)

watermark_input = Entry(width=70)
watermark_input.grid(row=1, column=1)

watermark_button = Button(text="Watermark Image", command=watermark_image)
watermark_button.grid(row=2, column=1)


window.mainloop()
