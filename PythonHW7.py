from PIL import Image
from pillow_heif import register_heif_opener, from_pillow as heif_from_pillow
import pillow_avif
import os


source_path = r"c:\Users\User\Desktop\PythonHW7\images"

files = os.listdir(source_path)
for file in files:
    full_path = os.path.join(source_path, file)
    if os.path.isfile(full_path):
        print(f"Found file: {full_path}")


for root, dirs, files in os.walk(source_path):
    for file in files:
        full_path = os.path.join(root, file)
        print(f"Found file: {full_path}")


my_image = r"c:\Users\User\Desktop\PythonHW7\images\image.jpg"


try:
    
    register_heif_opener()
    
    
    print("HEIF opener registered successfully")
    
    
    source_image = Image.open(my_image)
    print(f"Image opened successfully: {source_image.format}, size: {source_image.size}")
    
    
    source_image.save(
        "output.webp",
        format="WEBP",
        quality=40
    )
    print("WEBP conversion completed")
    
    
    heif_file = heif_from_pillow(source_image)
    heif_file.save(
        "output.heic",
        quality=40
    )
    print("HEIC conversion completed")
    
    
    source_image.save(
        "output.avif",
        quality=45
    )
    print("AVIF conversion completed")

except Exception as e:
    print(f"Error occurred: {str(e)}")


current_dir = os.getcwd()
print(f"Check these files in: {current_dir}")
for ext in ['webp', 'heic', 'avif']:
    filepath = os.path.join(current_dir, f'output.{ext}')
    if os.path.exists(filepath):
        print(f"Found: output.{ext}")

