import cv2


def capture_video_from_camera(output_file='output.avi', codec='XVID', frame_rate=20.0, resolution=(640, 480)):
    # Open a connection to the default camera (usually the first camera, index 0)
    cap = cv2.VideoCapture(0)

    # Check if the camera is opened correctly
    if not cap.isOpened():
        print("Error: Could not open video capture.")
        return

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*codec)  # Codec (e.g., XVID, MJPG)
    out = cv2.VideoWriter(output_file, fourcc, frame_rate, resolution)

    # Set the resolution
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, resolution[0])
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, resolution[1])

    print("Press 'q' to quit the video capture.")

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            print("Error: Failed to grab frame.")
            break

        # Optional: Flip the frame horizontally if it's inverted (uncomment if needed)
        frame = cv2.flip(frame, 1)  # Flip horizontally

        # Write the frame to the output file
        out.write(frame)

        # Display the resulting frame
        cv2.imshow('Video Capture', frame)

        # Exit on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close windows
    cap.release()
    out.release()
    cv2.destroyAllWindows()


# Call the function to start capturing video
capture_video_from_camera()
