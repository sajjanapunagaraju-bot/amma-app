import tkinter as tk
import webbrowser

def greet():
    resultLabel.config(text="🎉 Happy Birthday AMMA 🎉", fg="gold")
    cakeLabel.config(image=cake_img)
    
    # This opens your link after clicking
    webbrowser.open("https://example.com/birthday.py")

root = tk.Tk()
root.title("Birthday Wishes")
root.geometry("400x400")

cake_img = tk.PhotoImage(file="cake.png")

button = tk.Button(root, text="Click for Wishes", command=greet)
button.pack(pady=20)

resultLabel = tk.Label(root, text="", font=("Arial", 16))
resultLabel.pack(pady=20)

cakeLabel = tk.Label(root)
cakeLabel.pack(pady=20)

root.mainloop()
