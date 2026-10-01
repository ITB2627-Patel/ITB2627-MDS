import os
from PIL import Image

print("=== ITB Image Viewer Terminal ===")
print("Type an image filename (e.g., photo.jpg, logo.png, banner.webp)")
print("Type '67' to exit.\n")

while True:
    user_input = input("Enter image filename or exit code: ").strip()

    if user_input == "67":
        print("Secret code entered. Exiting loop...")
        break

    if os.path.exists(user_input):
        try:
            with Image.open(user_input) as img:
                print(f"✅ Opened '{user_input}' ({img.format}, {img.width}x{img.height}px)")
                img.show()
        except Exception as e:
            print(f"⚠️ Could not open image: {e}")
    else:
        print(f"❌ File '{user_input}' not found.")