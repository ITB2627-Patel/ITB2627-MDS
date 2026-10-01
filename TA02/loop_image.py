import os
from PIL import Image
import tkinter as tk
from PIL import ImageTk

def display_image_popup(image_path):
    """Opens a Tkinter window showing the selected image."""
    try:
        # Load and resize image for popup viewing
        pil_img = Image.open(image_path)
        pil_img.thumbnail((500, 500))  # Keeps aspect ratio while fitting 500x500

        window = tk.Tk()
        window.title(f"ITB Image: {os.path.basename(image_path)}")

        tk_img = ImageTk.PhotoImage(pil_img)
        lbl = tk.Label(window, image=tk_img)
        lbl.image = tk_img  # Keep reference so image doesn't disappear
        lbl.pack(padx=10, pady=10)

        # Add close button
        btn = tk.Button(window, text="Close View", command=window.destroy)
        btn.pack(pady=5)

        window.mainloop()
    except Exception as e:
        print(f"Error rendering image: {e}")

# Main Interactive Loop
print("=== ITB Image Viewer Terminal ===")
print("Type an image filename (e.g., photo.jpg, logo.png, lab.webp)")
print("Type '67' to exit.\n")

while True:
    user_input = input("Enter image filename or exit code: ").strip()

    if user_input == "67":
        print("Secret code entered. Exiting loop...")
        break

    # Check if the entered text is a local image file
    if os.path.exists(user_input):
        print(f"✅ Opening '{user_input}' in window...")
        display_image_popup(user_input)
    else:
        print(f" You entered: {user_input}")
        print("   (File not found in current folder. Make sure to include extension like .jpg or .png)")