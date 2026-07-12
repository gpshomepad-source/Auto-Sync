import requests
SOURCE_URL = "http://www.英格里希嗷呜.top/tv"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
try:
    response = requests.get(SOURCE_URL, headers=headers, timeout=15)
    response.raise_for_status()
    raw_text = response.text
    with open("tvbox.json", "w", encoding="utf-8") as f:
        f.write(raw_text)
    print("✅ 成功！")
except Exception as e:
    with open("tvbox.json", "w", encoding="utf-8") as f:
        f.write(str(e))
    print("❌ 失敗")
           
        print("✅ 成功解密並更新 tvbox.json！")
        
    except Exception as e:
        print(f"❌ 更新失敗: {e}")

if __name__ == "__main__":
    main()
