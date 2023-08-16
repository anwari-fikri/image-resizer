from PIL import Image
import os

def resize_image(input_path, output_path, target_size):
    original_image = Image.open(input_path)
    original_width, original_height = original_image.size

    aspect_ratio = original_width / original_height
    new_width = target_size
    new_height = int(new_width / aspect_ratio) if aspect_ratio > 0 else target_size

    resized_image = original_image.resize((new_width, new_height))
    resized_image.save(output_path)

if __name__ == '__main__':
    # just change these 2
    folder_path = 'C:/Users/AK MD ANWARI FIKRI/Desktop/resizepls' 
    target_size_px = 500

    output_folder = os.path.join(folder_path, 'edited')
    os.makedirs(output_folder, exist_ok=True)

    for file_name in os.listdir(folder_path):
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(folder_path, file_name)
            output_name = f"{os.path.splitext(file_name)[0]}_edited{os.path.splitext(file_name)[1]}"
            output_path = os.path.join(output_folder, output_name)
            resize_image(input_path, output_path, target_size_px)
