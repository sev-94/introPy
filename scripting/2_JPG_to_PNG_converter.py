import sys
import os
from PIL import Image

image_folder = sys.argv[0]
#output_folder = sys.argv[2]

print(os.path.exists(image_folder))
print(image_folder)