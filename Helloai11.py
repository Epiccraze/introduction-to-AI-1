import cv2
import numpy as np
def apply_color_filter(image, filter_type):
    filtered_image=image.copy()
    if filter_type=="original":
        return filtered_image
    elif filter_type=="red_tint":
        filtered_image[:,:,0]=0
        filtered_image[:,:,1]=0
    elif filter_type=="blue_tint":
        filtered_image[:,:,1]=0
        filtered_image[:,:,2]=0
    elif filter_type=="green_tint":
        filtered_image[:,:,0]=0
        filtered_image[:,:,2]=0
    elif filter_type=="increase_red":
        filtered_image[:,:,2]=cv2.add(filtered_image[:,:,2],50)
    elif filter_type=="decrease_blue":
        filtered_image[:,:,0]=cv2.subtract(filtered_image[:,:,0],50)
    return filtered_image
image=cv2.imread(r"C:\Users\ansh\Desktop\Python\Helloai\opencv\example.jpg")
if image is None:
    print("Error: Image not found!")
else:
    filter_type="original"
    print("r-Red Tint")
    print("b-Blue Tint")
    print("g-Green Tint")
    print("i-Increase Red")
    print("d-Decrease Blue")
    print("o-Original")
    print("q-Quit")
    while True:
        filtered_image=apply_color_filter(image,filter_type)
        cv2.imshow("Filtered Image",filtered_image)
        key=cv2.waitKey(1)&0xFF
        if key==ord('r'):
            filter_type="red_tint"
        elif key==ord('b'):
            filter_type="blue_tint"
        elif key==ord('g'):
            filter_type="green_tint"
        elif key==ord('i'):
            filter_type="increase_red"
        elif key==ord('d'):
            filter_type="decrease_blue"
        elif key==ord('o'):
            filter_type="original"
        elif key==ord('q'):
            break
    cv2.destroyAllWindows()