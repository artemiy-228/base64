import base64
import numpy as np
from moviepy.editor import VideoFileClip
from PIL import Image, ImageDraw
import os

frames = np.empty(50, dtype=object)


def main(video, folder):
    c = 1
    j = 0
    video_clip = VideoFileClip(video)
    file_name, _ = os.path.split(video)

    x_size = int(input("Input x size of video: "))
    y_size = int(input("Input y size of video: "))

    try:
        os.mkdir(folder)
    except:
        print("Directory already exists")

    step = 1

    for curr in np.arange(0, video_clip.duration, step):
        frame = video_clip.get_frame(curr)
        img = Image.fromarray(frame)
        draw = ImageDraw.Draw(img)
        draw.rectangle((x_size - 270, y_size - 270, x_size, y_size), fill=(255, 255, 255))
        frames[j] = base64.b64encode(img.tobytes())
        j += 1
        if (j == 20):
            c = save_frames(folder, c)
            j = 0


def save_frames(folder, c):
    for i in frames:
        path = f"{folder}/Frame_number_{c}.jpg"
        image_bytes = base64.b64decode(i)
        image = Image.frombytes('RGB', (1280, 720), image_bytes)
        image.save(path)
        c += 1

main("math.mp4", "math") # First is name of file, seconnd is name of folder or directory("with /")

