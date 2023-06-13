import base64
import numpy as np
from moviepy.editor import VideoFileClip
from PIL import Image
import os

SAVING_FRAMES_PS = 2

frames = set()

def main(video, folder):
    c = 1
    video_clip = VideoFileClip(video)
    file_name, _ = os.path.split(video)

    try:
        os.mkdir(folder)
    except:
        print("Directory already exist")

    step = 1 / SAVING_FRAMES_PS

    for curr in np.arange(0, video_clip.duration, step):

        filename = f"{folder}/Frame number {c}.jpg"
        frame = video_clip.get_frame(curr)
        img = Image.fromarray(frame)
        img.save(filename)
        c += 1


main("math_lesson.mp4", "video")