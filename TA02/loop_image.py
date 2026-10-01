import os
from PIL import Image

# Get the directory where this script file is saved
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

print("=== ITB Image Viewer Terminal ===")
print("Type an image filename (e.g., photo.jpg, logo.png, banner.webp)")
print("Type '67' to exit.\n")

while True:
    user_input = input("Enter image filename or exit code: ").strip()

    if user_input == "67":
        print("Secret code entered. Exiting loop...")
        break

    # Build the absolute path to the file inside the script's folder
    file_path = os.path.join(SCRIPT_DIR, user_input)

    if os.path.exists(file_path):
        try:
            with Image.open(file_path) as img:
                print(f"✅ Opened '{user_input}' ({img.format}, {img.width}x{img.height}px)")
                img.show()
        except Exception as e:
            print(f"⚠️ Could not open image: {e}")
    else:
        print(f"❌ File '{user_input}' not found in {SCRIPT_DIR}.")