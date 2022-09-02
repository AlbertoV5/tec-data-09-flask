# [[file:../readme.org::wrap_img_html.py][wrap_img_html.py]]
files="[img.png, img2.png]"
width=480
height=480
import re

files = re.sub("['\[\]]", "", files).split(",")
for f in files:
    print(f"#+attr_html: :width {width}px")
    print(f"file:{f.strip()}")
# wrap_img_html.py ends here
