from PIL import Image, ImageEnhance, ImageFilter
import os

def generate_augmented_images(input_image_path, output_folder):
    # Load the image
    img = Image.open(input_image_path)
    
    # Create output directory if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List of transformations and filters to apply
    transformations = [
        ("original", img),
        ("grayscale", img.convert("L")),
        ("blur", img.filter(ImageFilter.BLUR)),
        ("contour", img.filter(ImageFilter.CONTOUR)),
        ("edge_enhance", img.filter(ImageFilter.EDGE_ENHANCE)),
        ("sharpen", img.filter(ImageFilter.SHARPEN)),
        ("detail", img.filter(ImageFilter.DETAIL)),
        ("contrast", ImageEnhance.Contrast(img).enhance(2.0)),
        ("brightness", ImageEnhance.Brightness(img).enhance(1.5)),
        ("rotate", img.rotate(45)),
        ("flip_horizontal", img.transpose(Image.FLIP_LEFT_RIGHT)),
        ("flip_vertical", img.transpose(Image.FLIP_TOP_BOTTOM))
    ]

    # Apply each transformation and save the result
    for name, transformed_img in transformations:
        output_path = os.path.join(output_folder, f"{os.path.splitext(os.path.basename(input_image_path))[0]}_{name}.png")
        transformed_img.save(output_path)
        print(f"Saved: {output_path}")

# Example usage
input_image_path = "AI in Robotics\Labs\Week 7\dataset\Blue_0\Blue_0.jpg"
output_folder = "AI in Robotics\Labs\Week 7\dataset2"
generate_augmented_images(input_image_path, output_folder)
