import cv2
import numpy as np
import pyautogui

# Define the resolution (change according to your screen)
SCREEN_SIZE = (1920, 1080)

# Define the codec and create VideoWriter object
FOURCC = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("screen_record.avi", FOURCC, 20.0, SCREEN_SIZE)

print("Recording started... Press 'q' to stop.")

try:
    while True:
        # Capture the screen
        img = pyautogui.screenshot()

        # Convert screenshot to NumPy array
        frame = np.array(img)

        # Convert colors from BGR to RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Write frame to output file
        out.write(frame)

        # Optional: show recording preview
        cv2.imshow("Recording", frame)

        # Stop when 'q' is pressed
        if cv2.waitKey(1) == ord('q'):
            break
finally:
    # Release everything
    out.release()
    cv2.destroyAllWindows()
    print("Recording stopped. Saved as 'screen_record.avi'")
