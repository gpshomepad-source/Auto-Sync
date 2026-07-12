import requests

SOURCE_URL = "http://www.英格里希嗷呜.top/tv"

def main():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    try:
        print("🔄 正在獲取資料...")
        response = requests.get(SOURCE_URL, headers=headers, timeout=15)
        response.raise_for_status()
        
        # 直接獲取並儲存原始內容，不做任何複雜格式化
        raw_text = response.text
        
        with open("tvbox.json", "w", encoding="utf-8") as f:
            f.write(raw_text)
            
        print("✅ 成功儲存內容到 tvbox.json！")
            
    except Exception as e:
        print(f"❌ 失敗: {e}")
        # 出錯時保底開一個檔案
        with open("tvbox.json", "w", encoding="utf-8") as f:
            f.write(f"Error: {e}")

if __name__ == "__main__":
    main()
       with open("tvbox.json", "w", encoding="utf-8") as f:
            f.write(f"Error: {e}")

if __name__ == "__main__":
    main()
           json.dump(config_data, f, ensure_ascii=False, indent=2)
            
        print("✅ 成功解密並更新 tvbox.json！")
        
    except Exception as e:
        print(f"❌ 更新失敗: {e}")

if __name__ == "__main__":
    main()
