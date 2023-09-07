import requests
from selenium import webdriver
import re



def download_mp4(url, save_path):
    response = requests.get(url, stream=True)
    response.raise_for_status()  # 检查响应是否成功

    with open(save_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                file.write(chunk)


def downloadMp4FromURL(inputXHSShareURL,locDir):

    # 正则提取复制链接中的真实URL
    pattern = r"[a-zA-z]+://[^\s]*"
    urlsToEnd = re.findall(pattern, inputXHSShareURL)  # ['http://xhslink.com/Uu4Teu，复制本条信息，打开【小红书】App查看精彩内容！']
    xhsUrl = urlsToEnd[0].split("，")[0]  # http://xhslink.com/Uu4Teu
    print("小红书地址：", xhsUrl)

    # selenium爬虫得到视频URL
    videoUrl = ""
    while (videoUrl == ""):
        driver = webdriver.Chrome()
        driver.get(xhsUrl)
        network = driver.execute_script("return window.performance.getEntries();")
        for data in network:
            if data["name"].startswith("http") and data["name"].endswith("mp4"):
                videoUrl = data["name"]
                print("视频地址：", data[
                    "name"])  # https://sns-video-hw.xhscdn.com/stream/110/259/01e4e40d1a1429ae010377038a201784eb_259.mp4
                break

    # 视频下载到本地
    video_url = videoUrl
    save_path = locDir + "/video/" + videoUrl.split("/")[-1]
    download_mp4(video_url, save_path)
    print("视频已成功下载到:",
          save_path)  # /Users/caochongyang/Downloads/video/01e4e40d1a1429ae010377038a201784eb_259.mp4

    return save_path

if __name__ == '__main__':

    inputXHSShareURL = "15 瓦瓦妮莎发布了一篇小红书笔记，快来看吧！ 😆 p3KLyhqkkkhATrb 😆 http://xhslink.com/Uu4Teu，复制本条信息，打开【小红书】App查看精彩内容！"
    downloadMp4FromURL(inputXHSShareURL)
















