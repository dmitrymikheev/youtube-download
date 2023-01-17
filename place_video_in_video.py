from moviepy.editor import VideoFileClip, CompositeVideoClip
from moviepy.video.fx.all import resize

output_path="output.mp4"
video_view="first.mp4"
animeeer="second.mp4"

video_background = VideoFileClip((video_view))
clipped_video = VideoFileClip(animeeer)

clipped_video = clipped_video.fx(resize, 0.4)

video_backgroundX1 = video_background.size[0]
video_backgroundY1 = video_background.size[1]

clipped_video = clipped_video.set_position((video_backgroundX1 - clipped_video.size[0], video_backgroundY1 - clipped_video.size[1]))

final_video = CompositeVideoClip([video_background, clipped_video])

final_video.write_videofile(
    output_path,
    fps=30,
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
    threads = 6,
)