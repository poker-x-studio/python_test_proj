#功能：测试excel
#说明: Python版本 3.13.5

import yt_dlp

#下载youtube视频
def download_youtube_video(url, output_path='.') ->None:
    """
    下载YouTube视频。

    Args:
        url (str): 视频的URL。
        output_path (str, optional):  下载视频保存的路径。默认为当前目录。
    """
    ydl_opts = {
        'outtmpl': f'{output_path}/%(title)s-%(id)s.%(ext)s',  # 下载的视频文件名格式
        'noplaylist': True,  # 不下载播放列表
        'quiet': True,  # 禁止输出详细信息
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"视频已成功下载到 {output_path}")
    except Exception as e:
        print(f"下载失败: {e}")

def main():
    video_url = input("请输入YouTube视频URL: ")
    download_path = input("请输入保存路径 (留空则为当前目录): ")
    if not download_path:
       download_path = "."
    download_youtube_video(video_url, download_path)
    return 


if __name__ == "__main__":
    main()