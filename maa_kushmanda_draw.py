import cv2
import numpy as np
import os

image_path = "maa_kushmanda.jpg"

if os.path.exists(image_path):
    img = cv2.imread(image_path)
    
    # Resize canvas for full page / large screen display
    img = cv2.resize(img, (1200, 900))
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blur, 50, 150)
    
    # White background canvas
    canvas = np.ones_like(img) * 255
    
    # BGR Colors
    black_color = (0, 0, 0)      # Maa Durga, lotus & weapons in black
    orange_color = (0, 165, 255) # ONLY Lion in orange
    
    contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    
    cv2.namedWindow("Maa Kushmanda Live Drawing", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Maa Kushmanda Live Drawing", 1200, 900)
    
    height, width = img.shape[:2]
    
    for cnt in contours:
        # Get exact center coordinates of each line/contour
        M = cv2.moments(cnt)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
        else:
            cX, cY = 0, 0
            
        # STRICT BOUNDING AREA FOR LION ONLY:
        # Lion bottom-left corner mein hai (X < 38% width AND Y > 42% height)
        if cX < width * 0.38 and cY > height * 0.42:
            current_color = orange_color
        else:
            current_color = black_color
            
        cv2.drawContours(canvas, [cnt], -1, current_color, 2)
        cv2.imshow("Maa Kushmanda Live Drawing", canvas)
        
        if cv2.waitKey(1) & 0xFF == 27:  # ESC to exit
            break
            
    # Save final output
    cv2.imwrite("maa_kushmanda_drawing.jpg", canvas)
    print("Drawing complete! Press any key on the image window to close.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: 'maa_kushmanda.jpg' file nahi mili!")