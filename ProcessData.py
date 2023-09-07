from MP4ToAudio import convert_to_audio
from AudioToText import audioToText
from DownloadMP4ByURL import  downloadMp4FromURL

locDir = "/Users/caochongyang/Downloads"

def processData(inputXHSShareURL):


    save_path = downloadMp4FromURL(inputXHSShareURL,locDir)



    video_path = save_path
    audio_path = locDir+"/audio/ " + video_path.split("/")[-1].split(".")[0] + ".wav"
    convert_to_audio(video_path, audio_path)  # /Users/caochongyang/Downloads/audio/01e4e40d1a1429ae010377038a201784eb_259.wav




    audio_path = audio_path
    text_path = locDir+"/text/ " + audio_path.split("/")[-1].split(".")[0] + ".text"
    audioToText(audio_path, text_path)

    return text_path

if __name__ == '__main__':

    # inputXHSShareURL = "15 瓦瓦妮莎发布了一篇小红书笔记，快来看吧！ 😆 p3KLyhqkkkhATrb 😆 http://xhslink.com/Uu4Teu，复制本条信息，打开【小红书】App查看精彩内容！"
    inputXHSShareURL = "40 黑娃呦～发布了一篇小红书笔记，快来看吧！ 😆 4hydQI4uMU4D8yf 😆 http://xhslink.com/8VNHfu，复制本条信息，打开【小红书】App查看精彩内容！"
    # processData 耗时不到三分钟
    print("processData：" + processData(inputXHSShareURL))





