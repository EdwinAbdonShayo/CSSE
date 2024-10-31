import os
from PIL import Image, ImageFilter, ImageEnhance

# Define the root directory and the output directory
ROOT_DIR = r'AI in Robotics/Labs/Week 7/dataset'
OUTPUT_DIR = r'AI in Robotics/Labs/Week 7/dataset2'

# Image formats of interest
IMAGE_FORMATS = ('.jpg', '.png', '.jpeg')

# Define the filters
def define_filters():
    return {
        "Blur": ImageFilter.BLUR,
        "Contour": ImageFilter.CONTOUR,
        "Detail": ImageFilter.DETAIL,
        "Edge Enhance": ImageFilter.EDGE_ENHANCE,
        "Emboss": ImageFilter.EMBOSS,
        "Find Edges": ImageFilter.FIND_EDGES,
        "Sharpen": ImageFilter.SHARPEN,
        "Brightness Increase": lambda img: ImageEnhance.Brightness(img).enhance(1.5),
        "Contrast Increase": lambda img: ImageEnhance.Contrast(img).enhance(1.5),
        "Identity": lambda img: img
    }

def process_images(root_dir, output_dir):
    filters = define_filters()
    
    # Traverse directories
    for subdir, dirs, files in os.walk(root_dir):
        relative_path = os.path.relpath(subdir, root_dir)
        output_path = os.path.join(output_dir, relative_path)
        os.makedirs(output_path, exist_ok=True)  # Create output path if it doesn't exist
        
        for file in files:
            if file.endswith(IMAGE_FORMATS):
                file_path = os.path.join(subdir, file)
                try:
                    img = Image.open(file_path).convert("RGB")
                    for filter_name, filter_func in filters.items():
                        try:
                            # Call the filter function, whether it's a lambda or constant
                            filtered_img = filter_func(img) if callable(filter_func) else img.filter(filter_func)
                            filename, file_extension = os.path.splitext(file)
                            new_filename = f"{filename}_{filter_name}{file_extension}"
                            new_file_path = os.path.join(output_path, new_filename)
                            filtered_img.save(new_file_path)
                            print(f"Saved: {new_file_path}")
                        except Exception as e:
                            print(f"Error applying filter {filter_name} on {file_path}: {e}")
                except Exception as e:
                    print(f"Error opening or processing {file_path}: {e}")

if __name__ == "__main__":
    process_images(ROOT_DIR, OUTPUT_DIR)