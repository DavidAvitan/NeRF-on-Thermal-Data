import cv2
import os


def video_to_frames(video_path, frames_per_second):
    # create directory to save the frames
    if not os.path.exists('results'):
        os.makedirs('results')

    # open video file
    cap = cv2.VideoCapture(video_path)

    # get frames per second of video
    fps = cap.get(cv2.CAP_PROP_FPS)

    # calculate frame interval to achieve desired FPS
    frame_interval = round(fps / frames_per_second)

    # initialize frame count
    frame_count = 0

    # loop through video frames
    while True:
        # read frame
        ret, frame = cap.read()

        # break loop if end of video file is reached
        if not ret:
            break

        # save frame if it's the right interval
        if frame_count % frame_interval == 0:
            cv2.imwrite(f"results/image{frame_count}.jpg", frame)

        # increment frame count
        frame_count += 1

    # release video capture and destroy all windows
    cap.release()
    cv2.destroyAllWindows()


# example usage: convert video file "example.mp4" to 5 frames per second
video_to_frames("video.MP4", 2)
