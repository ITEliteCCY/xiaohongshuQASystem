from ffmpy3 import FFmpeg
import os
import time

def convert_to_audio(video_path, audio_path):


    # 本函数两个逻辑：
    #   一是转录代码ff.run()
    #   二是处理FFmpeg中对于已经存在的输出路径audio_path会报错的问题： 我们的做法是修改函数名来完成转录，最终还要写入传入的文件名

    fatherDir = os.path.dirname(audio_path)
    fileName = audio_path.split("/")[-1]
    deal_audio_path = ""
    for root, dirs, files in os.walk(fatherDir):
        for file_name in files:
            if fileName == file_name:
                deal_audio_path = os.path.join(root, str(time.time()) + fileName)
                print(deal_audio_path)


    if(deal_audio_path == ""):
        ff = FFmpeg(
            inputs={video_path: None},
            outputs={audio_path: '-vn -f wav'}  # -vn -ar 44100 -ac 2 -ab 192 -f wav
        )
        print(ff.cmd)
        ff.run()

        print("音频已成功转换为:", audio_path)
    else:
        ff = FFmpeg(
            inputs={video_path: None},
            outputs={deal_audio_path: '-vn -f wav'}  # -vn -ar 44100 -ac 2 -ab 192 -f wav
        )
        print(ff.cmd)
        ff.run()
        #改回文件名 同名则覆盖原来文件
        os.rename(deal_audio_path,audio_path)
        print("音频已成功转换为:", audio_path)



if __name__ == '__main__':
    video_path = "/Users/caochongyang/Downloads/video/v1.mp4"
    audio_path = "/Users/caochongyang/Downloads/audio/a6.wav"

    convert_to_audio(video_path, audio_path)

