import os
import time
import random
import requests
from dotenv import load_dotenv

load_dotenv()

SESSDATA = os.getenv("SESSDATA")
BILI_JCT = os.getenv("BILI_JCT")
BUVID3 = os.getenv("BUVID3")

MAX_LIKE = int(os.getenv("MAX_LIKE", 3))
DELAY_MIN = int(os.getenv("DELAY_MIN", 12))
DELAY_MAX = int(os.getenv("DELAY_MAX", 28))
TID = int(os.getenv("TID", 188)) #科技区代码188为例其他在说明里

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Cookie": f"SESSDATA={SESSDATA}; bili_jct={BILI_JCT}; buvid3={BUVID3}",
    "Referer": "https://www.bilibili.com/"
}

def like_aid(aid):
    url = "https://api.bilibili.com/x/web-interface/archive/like"
    data = {
        "aid": aid,
        "like": 1,
        "csrf": BILI_JCT
    }
    try:
        r = requests.post(url, headers=HEADERS, data=data, timeout=10)
        res = r.json()
        if res["code"] == 0:
            print(f"[点赞成功] AV{aid}")
        else:
            print(f"[点赞失败] AV{aid} {res}")
    except Exception as e:
        print(f"[请求异常] {e}")

def get_zone_videos(tid=188, ps=30):
    url = f"https://api.bilibili.com/x/web-interface/newlist?rid={tid}&pn=1&ps={ps}"
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        res = r.json()
        if res["code"] != 0:
            print(f"[获取视频失败] code={res['code']}, msg={res.get('message')}")
            return []
        return [v["aid"] for v in res["data"]["archives"]]
    except Exception as e:
        print(f"[获取视频异常] {e}")
        return []

def main_loop():
    while True:
        print("=" * 50)
        print(f"【开始新一轮点赞】时间: {time.strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 50)

        aids = get_zone_videos(TID, 30)
        if not aids:
            print("[未获取到视频]")
        else:
            print(f"[获取到 {len(aids)} 个视频]")
            count = 0
            for aid in aids:
                if count >= MAX_LIKE:
                    break
                like_aid(aid)
                sleep_time = random.randint(DELAY_MIN, DELAY_MAX)
                print(f"[等待 {sleep_time} 秒]")
                time.sleep(sleep_time)
                count += 1

        print("\n 本轮点赞完成")
        print("=" * 50)
        nap = random.randint(20, 40)
        print(f"\n 休息 {nap} 分钟后继续...\n")
        time.sleep(nap * 60)

if __name__ == "__main__":
    main_loop()
