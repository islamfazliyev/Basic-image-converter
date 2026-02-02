from PIL import Image
import os

def convert_image(input_path, output_folder, target_format):
    Img = Image.open(input_path)

    name = os.path.splitext(os.path.basename(input_path))[0]
    output_path = os.path.join(
        output_folder,
        f"{name}.{target_format.lower()}"
    )
    if target_format.upper() == "JPEG":
        Img = Img.convert("RGB")

    Img.save(output_path, target_format.upper())