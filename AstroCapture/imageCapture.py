import cv2
import time


def capture_long_exposure(exposure_time_seconds):
    # print(cv2.getBuildInformation())
    start_time = time.time()

    cap = cv2.VideoCapture(0)

    # Convert seconds to milliseconds for OpenCV
    exposure_time_ms = int(exposure_time_seconds * 1000)

    # ret_val, cap_for_exposure = cap.read()
    cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 3)  # auto mode
    cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 1)  # manual mode

    # cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.25)

    cap.set(cv2.CAP_PROP_EXPOSURE, exposure_time_ms)

    ret, frame = cap.read()
    print(ret)

    if ret:
        cv2.imwrite('long_exposure.jpg', frame)

    cap.release()

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Image captured in {elapsed_time:.2f} seconds")


if __name__ == "__main__":
    exposure_time = 5  # Adjust exposure time in seconds
    capture_long_exposure(exposure_time)
