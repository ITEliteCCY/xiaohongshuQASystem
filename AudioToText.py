# coding=utf-8
import whisper
import zhconv


def audioToText(audio_path,text_path):

    whisper_model = whisper.load_model("large")  # 跑不起来可用则可选 base small medium large(其中 medium large 会转为繁体字，需要搭配 zhconv.convert(text, 'zh-cn'))
    result = whisper_model.transcribe(audio_path)
    textResult = ", ".join([i["text"] for i in result["segments"] if i is not None])
    textResult = zhconv.convert(textResult, 'zh-cn')
    with open(text_path, 'w', encoding='UTF-8') as f:
        f.write(textResult)

    f.close()
if __name__ == '__main__':
    audio_path = "/Users/caochongyang/Downloads/audio/a6.wav"
    text_path = "/Users/caochongyang/Downloads/text/a6.text"
    audioToText(audio_path,text_path)

    # text = '真的不允許還有哪個胖胖姐妹還不知道正肩T恤, 如果你也和我一樣肩寬背厚手臂酥肚子還大, 那就不要再穿這種寬寬打大的落肩袖T恤了, 正肩T才是顯瘦天花板, 那今天讓我來跟你們分享幾件很顯瘦, 很適合我們胖胖女生的正肩T恤, 一起看看吧, 首先是一件方領的修身短款正肩T, 腰部的褶皺設計可以很好地凸顯我們的腰身, 這種弧形的下擺可以很好地遮住我們的小肚子, 而且這個大方領真的很顯瘦很凸顯鎖骨, 它的面料是這種很有彈力的設計的, 所以上身之後穿起來還是很舒服的, 這件的話就可以簡單地配一條這種龍仔過腿, 這就很顯瘦了, 第二件呢是一個卡其色澤黑色拼接的修身T恤, 這件也是我昨天視頻裡身上穿的那一件, 它同樣做的是一個這種不規則的弧形下擺, 上身之後的包裹性很好, 就顯得整個人的線條都很好看, 領口的位置它做了一排這種小暗扣, 稍微解開兩顆就可以形成一個這種小衛理的感覺, 搭配一條挺色系的長褲, 就能穿出時髦又優雅的感覺了, 接下來是一件偏長款一點的灰色印花T恤, 這件它整體做的就會偏長一點, 而且版型也是一種很修身的類型, 胸前的紅色印花和這個灰色T恤搭配在一起, 還蠻有美式街頭感的, 這件整體的質感還是不錯的, 不過面料相對來說彈力會差一點點, 可以搭配我身上這種偏長款的半身裙, 也能穿出很休閒的感覺, 接下來是一件軍綠色的正肩T恤, 它的版型做的也會寬鬆一些, 各個維度包括手臂這位置都是有餘量的, 胸前還有做這種水鑽鑲嵌的印花, 整體的風格就會更偏酷女孩一些, 下半身可以像我這樣搭配一條, 這種棕色系的牛仔褲也是很有辨識度的一套, 接下來依舊是一件偏短款一點的印花T恤, 這件做的是一個淺黃色的設計, 就很有夏日的氛圍感, 它的長度同樣是可以帶過肚臍的, 上面這種大片的字母加印花的設計, 就很有美式復古風的感覺, 同樣搭配一條紅色系的長褲, 就既顯瘦又有辣妹風的感覺了, 這款是一個黑色和杏色拼接的印花T恤, 它同樣做也是偏長的, 上面這個小印花就很有那種, 乖巧童趣的感覺, 領口和袖邊都有做這種黑色的拼接, 同樣做也是這種偏厚的純棉的料子, 所以相對的彈力會沒有那麼強, 這件就比較適合搭配一條, 黑色的高腰短裙, 就很乖巧很有少女感了'
    # print(zhconv.convert(text, 'zh-cn'))
