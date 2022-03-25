import jieba
import wordcloud
import time

def stopwordslist(filepath):    # 读取停用词表
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords

filepath = input("请输入绝对或相对路径：")
time_start = time.time()    # 运行时间计时开始
with open(filepath, encoding="utf-8") as f:   #打开文件，可以使用相对路径或绝对路径
    s = f.read()
ls = jieba.lcut(s)  # 分词列表
text = ' '.join(ls)  # 连接字符串

stopwords = stopwordslist('stopwordslist.txt')   # 停用词

wc = wordcloud.WordCloud(
    font_path = "方正GDC体 简 Light.TTF",     # 设定字体，可以使用相对路径或绝对路径
    width = 4096,     # 宽度-像素
    height = 2160,    # 高度-像素
    background_color = 'white',   # 背景色
    max_words = 250,  # 最多显示的单词数量
    stopwords = stopwords     # 停用词
    )

wc.generate(text)  # 加载文本
wc.to_file("result.png")  # 输出词云图片
time_end = time.time()  # 运行时间计时结束
time_cost = time_end - time_start
print("计算完成，图片已保存在工作目录下，共耗时" + str("%.3f" % time_cost) + "s.")