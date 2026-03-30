import cv2
import os
import numpy as np

img_path = r"C:\Users\henok\Open-Vision-Lab\problem\problem-1\input-image\sample-image.jpg"

# Load image ONCE (GLOBAL)
img = cv2.imread(img_path)

if img is None:
    print("Failed to load image")
    exit()

print("Image shape:", img.shape)  # should be (1280, 1275, 3)

# Show full image (scaled)
def show_image(image, max_width=1000, max_height=800):
    h, w = image.shape[:2]

    scale = min(max_width / w, max_height / h, 1.0)

    new_w = int(w * scale)
    new_h = int(h * scale)

    resized = cv2.resize(image, (new_w, new_h), interpolation=cv2.INTER_AREA)

    cv2.imshow("Image", resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Crop region (if needed)
cut_image = img[100:1280, 100:1275].copy()

# Draw grid (FIRST ROW)
# cv2.rectangle(cut_image, (7, 0), (196, 168), (0, 255, 0), 2)
# cv2.rectangle(cut_image, (200, 0), (390, 168), (0, 255, 0), 2)
# cv2.rectangle(cut_image, (394, 0), (584, 168), (0, 255, 0), 2)
# cv2.rectangle(cut_image, (592, 0), (780, 168), (0, 255, 0), 2)
# cv2.rectangle(cut_image, (786, 0), (976, 168), (0, 255, 0), 2)
# cv2.rectangle(cut_image, (982, 0), (1172, 168), (0, 255, 0), 2)

# cut grid (FIRST ROW)
#formula: cut_image[y1:y2, x1:x2]
cell_1 = cut_image[0:168, 7:196]
cell_2 = cut_image[0:168, 200:390]
cell_3 = cut_image[0:168, 394:584]
cell_4 = cut_image[0:168, 592:780]
cell_5 = cut_image[0:168, 786:976]
cell_6 = cut_image[0:168, 982:1172]


# Always save to the correct output folder, regardless of where the script is run from
output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'output-image'))
os.makedirs(output_dir, exist_ok=True)
cv2.imwrite(os.path.join(output_dir, "cell_1.png"), cell_1)
cv2.imwrite(os.path.join(output_dir, "cell_2.png"), cell_2)
cv2.imwrite(os.path.join(output_dir, "cell_3.png"), cell_3)
cv2.imwrite(os.path.join(output_dir, "cell_4.png"), cell_4)
cv2.imwrite(os.path.join(output_dir, "cell_5.png"), cell_5)
cv2.imwrite(os.path.join(output_dir, "cell_6.png"), cell_6)

# Draw grid (SECOND ROW)

# cv2.rectangle(cut_image, (7, 178), (196, 370), (0, 255, 0), 2)
# cv2.rectangle(cut_image, (200, 178), (390, 370), (0, 255, 0), 2)
# cv2.rectangle(cut_image, (394, 178), (584, 370), (0, 255, 0), 2)
# cv2.rectangle(cut_image, (592, 178), (780, 370), (0, 255, 0), 2)
# cv2.rectangle(cut_image, (786, 178), (976, 370), (0, 255, 0), 2)
# cv2.rectangle(cut_image, (982, 178), (1172, 370), (0, 255, 0), 2)

# cut grid (SECOND ROW)
#formula: cut_image[y1:y2, x1:x2]
cell_7 = cut_image[178:370, 7:196]
cell_8 = cut_image[178:370, 200:390]
cell_9 = cut_image[178:370, 394:584]
cell_10 = cut_image[178:370, 592:780]
cell_11 = cut_image[178:370, 786:976]
cell_12 = cut_image[178:370, 982:1172]

# Save the cropped image
cv2.imwrite(os.path.join(output_dir, "cell_7.png"), cell_7)
cv2.imwrite(os.path.join(output_dir, "cell_8.png"), cell_8)
cv2.imwrite(os.path.join(output_dir, "cell_9.png"), cell_9)
cv2.imwrite(os.path.join(output_dir, "cell_10.png"), cell_10)
cv2.imwrite(os.path.join(output_dir, "cell_11.png"), cell_11)
cv2.imwrite(os.path.join(output_dir, "cell_12.png"), cell_12)

# Draw grid (THIRD ROW)
# cv2.rectangle(cut_image, (7, 380), (196, 570), (0, 255, 0), 2)
# cv2.rectangle(cut_image, (200, 380), (390, 570), (0, 255, 0), 2)
# cv2.rectangle(cut_image, (394, 380), (584, 570), (0, 255, 0), 2)
# cv2.rectangle(cut_image, (592, 380), (780, 570), (0, 255, 0), 2)
# cv2.rectangle(cut_image, (786, 380), (976, 570), (0, 255, 0), 2)
# cv2.rectangle(cut_image, (982, 380), (1172, 570), (0, 255, 0), 2)

# cut grid (THIRD ROW)
#formula: cut_image[y1:y2, x1:x2]
cell_13 = cut_image[380:570, 7:196]
cell_14 = cut_image[380:570, 200:390]
cell_15 = cut_image[380:570, 394:584]
cell_16 = cut_image[380:570, 592:780]
cell_17 = cut_image[380:570, 786:976]
cell_18 = cut_image[380:570, 982:1172]

# Save the cropped image
cv2.imwrite(os.path.join(output_dir, "cell_13.png"), cell_13)
cv2.imwrite(os.path.join(output_dir, "cell_14.png"), cell_14)
cv2.imwrite(os.path.join(output_dir, "cell_15.png"), cell_15)
cv2.imwrite(os.path.join(output_dir, "cell_16.png"), cell_16)
cv2.imwrite(os.path.join(output_dir, "cell_17.png"), cell_17)
cv2.imwrite(os.path.join(output_dir, "cell_18.png"), cell_18)

# Draw grid (FOURTH ROW)
# cv2.rectangle(cut_image, (7, 581), (196, 770), (0, 255, 0), 2)
# cv2.rectangle(cut_image, (200, 581), (390, 770), (0, 255, 0), 2)
# cv2.rectangle(cut_image, (394, 581), (584, 770), (0, 255, 0), 2)
# cv2.rectangle(cut_image, (592, 581), (780, 770), (0, 255, 0), 2)
# cv2.rectangle(cut_image, (786, 581), (976, 770), (0, 255, 0), 2)
# cv2.rectangle(cut_image, (982, 581), (1172, 770), (0, 255, 0), 2)

# cut grid (FOURTH ROW)
#formula: cut_image[y1:y2, x1:x2]
cell_19 = cut_image[581:770, 7:196]
cell_20 = cut_image[581:770, 200:390]
cell_21 = cut_image[581:770, 394:584]
cell_22 = cut_image[581:770, 592:780]
cell_23 = cut_image[581:770, 786:976]
cell_24 = cut_image[581:770, 982:1172]

# Save the cropped image
cv2.imwrite(os.path.join(output_dir, "cell_19.png"), cell_19)
cv2.imwrite(os.path.join(output_dir, "cell_20.png"), cell_20)
cv2.imwrite(os.path.join(output_dir, "cell_21.png"), cell_21)
cv2.imwrite(os.path.join(output_dir, "cell_22.png"), cell_22)
cv2.imwrite(os.path.join(output_dir, "cell_23.png"), cell_23)
cv2.imwrite(os.path.join(output_dir, "cell_24.png"), cell_24)

# Draw grid (FIFTH ROW)
# cv2.rectangle(cut_image, (7, 782), (196, 972), (0, 255, 0), 2)
# cv2.rectangle(cut_image, (200, 782), (390, 972), (0, 255, 0), 2)
# cv2.rectangle(cut_image, (394, 782), (584, 972), (0, 255, 0), 2)
# cv2.rectangle(cut_image, (592, 782), (780, 972), (0, 255, 0), 2)
# cv2.rectangle(cut_image, (786, 782), (976, 972), (0, 255, 0), 2)
# cv2.rectangle(cut_image, (982, 782), (1172, 972), (0, 255, 0), 2)

# cut grid (FIFTH ROW)
#formula: cut_image[y1:y2, x1:x2]
cell_25 = cut_image[782:972, 7:196]
cell_26 = cut_image[782:972, 200:390]
cell_27 = cut_image[782:972, 394:584]
cell_28 = cut_image[782:972, 592:780]
cell_29 = cut_image[782:972, 786:976]
cell_30 = cut_image[782:972, 982:1172]

# Save the cropped image
cv2.imwrite(os.path.join(output_dir, "cell_25.png"), cell_25)
cv2.imwrite(os.path.join(output_dir, "cell_26.png"), cell_26)
cv2.imwrite(os.path.join(output_dir, "cell_27.png"), cell_27)
cv2.imwrite(os.path.join(output_dir, "cell_28.png"), cell_28)
cv2.imwrite(os.path.join(output_dir, "cell_29.png"), cell_29)
cv2.imwrite(os.path.join(output_dir, "cell_30.png"), cell_30)


# Draw grid (SIXTH ROW)
# cv2.rectangle(cut_image, (7, 984), (196, 1172), (0, 255, 0), 2)
# cv2.rectangle(cut_image, (200, 984), (390, 1172), (0, 255, 0), 2)
# cv2.rectangle(cut_image, (394, 984), (584, 1172), (0, 255, 0), 2)
# cv2.rectangle(cut_image, (592, 984), (780, 1172), (0, 255, 0), 2)
# cv2.rectangle(cut_image, (786, 984), (976, 1172), (0, 255, 0), 2)
# cv2.rectangle(cut_image, (982, 984), (1172, 1172), (0, 255, 0), 2)
# # cut grid (SIXTH ROW)
#formula: cut_image[y1:y2, x1:x2]
cell_31 = cut_image[984:1172, 7:196]
cell_32 = cut_image[984:1172, 200:390]
cell_33 = cut_image[984:1172, 394:584]
cell_34 = cut_image[984:1172, 592:780]
cell_35 = cut_image[984:1172, 786:976]
cell_36 = cut_image[984:1172, 982:1172]
# Save the cropped image
cv2.imwrite(os.path.join(output_dir, "cell_31.png"), cell_31)
cv2.imwrite(os.path.join(output_dir, "cell_32.png"), cell_32)
cv2.imwrite(os.path.join(output_dir, "cell_33.png"), cell_33)
cv2.imwrite(os.path.join(output_dir, "cell_34.png"), cell_34)
cv2.imwrite(os.path.join(output_dir, "cell_35.png"), cell_35)
cv2.imwrite(os.path.join(output_dir, "cell_36.png"), cell_36)

# Show result

show_image(cut_image)