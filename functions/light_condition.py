import cv2
import time


def check_light_condition():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Could not open camera")
        return
    time.sleep(5)  # Allow camera to adjust
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame")
        cap.release()
        return
    # Compute mean brightness
    mean = cv2.meanStdDev(frame)
    #print("Mean brightness:", mean[0][0])  
    if mean[0][0] < 50:  
        cap.release()
        cv2.destroyAllWindows()
        return "الإضاءةغير كافية"
    else:
        cap.release()
        cv2.destroyAllWindows()
        return "الإضاءة كافية"



