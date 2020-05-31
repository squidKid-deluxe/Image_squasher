# usr/bin/python3.7
"""
A simple script that compresses *.jpg image files.
"""

# Import necessary modules
import os
from time import time
from PIL import Image


def main():
    """
    Main process, does it all
    """
    # Get the start time
    start = time()

    # Delete the folder from outputs
    os.system("rm -rf outputs")

    # Create the folder for outputs
    os.system("mkdir outputs")

    # Clear the screen
    print("\033c")

    # Input the wanted quality
    qualities = int(input("Enter approximate quality as integer:   "))

    # Get all of the JPEG files in the current folder
    jpegs = [
        filer
        for filer in os.listdir()
        if filer.endswith(".jpg") or filer.endswith(".JPG")
    ]


    # For every file in that list:
    for name in jpegs:
        # Print the image we are compressing.
        print("Compressing image:", name)

        # Open the image.
        current_image = Image.open(name)

        # Print the original image size.
        print("Original image size:", str(int(os.path.getsize(name)) / 1000) + "kb")

        # Store it.
        orig_size = os.path.getsize(name)

        # Add the directory name to the file name.
        name = "outputs/" + name

        # Save the image, compressed.
        current_image.save(name, optimize=0, quality=qualities)

        # Print the compressed image file size.
        print("Compressed image size:", str(int(os.path.getsize(name)) / 1000) + "kb")

        # Print the percent compressed.
        print(
            "Percent compressed:",
            str(-int((os.path.getsize(name) / orig_size) * 100) + 100) + "% reduced.",
        )

        # Print a divider.
        print("-" * 100)

    # Get the end time:
    end = time()

    # Find the time it took to compress the images.
    took = end - start

    # Print that time.
    print("Compressing", len(jpegs), "images took", took, "seconds.")


if __name__ == "__main__":
    main()
