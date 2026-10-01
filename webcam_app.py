# Webcam App using Python OpenCV

import cv2


def main():
    # Open default webcam. 0 = default laptop/computer webcam.
    cap = cv2.VideoCapture(0)

    # Check if webcam opened successfully.
    if not cap.isOpened():
        print("Error: Webcam not found")
        return

    print("Webcam started.")
    print("Press 's' to save a screenshot.")
    print("Press ESC to exit.")

    while True:
        # Read one frame from the webcam.
        success, frame = cap.read()

        if not success:
            print("Error: Cannot read frame")
            break

        # Flip frame horizontally like a mirror.
        frame = cv2.flip(frame, 1)

        # Add text on webcam screen.
        cv2.putText(
            frame,
            "My Webcam App",
            (30, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2,
        )

        # Show webcam window.
        cv2.imshow("Webcam App", frame)

        # Read keyboard key.
        key = cv2.waitKey(1)

        # Press 's' to save screenshot.
        if key == ord("s"):
            cv2.imwrite("screenshot.jpg", frame)
            print("Screenshot saved as screenshot.jpg")

        # Press ESC to close webcam.
        if key == 27:
            print("Webcam closed")
            break

    # Release webcam.
    cap.release()

    # Close all OpenCV windows.
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()