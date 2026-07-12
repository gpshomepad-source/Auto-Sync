import requests
import json

SOURCE_URL = "http://www.英格里希嗷呜.top/tv"

def main():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    try:
        print(f"🔄 正在從 {SOURCE_URL} 獲取資料...")
        response = requests.get(SOURCE_URL, headers=headers, timeout=15)
        response.raise_for_status()
        
        # 獲取原始內容
        raw_text = response.text
        
        # 嘗試當作普通 JSON 解析
        try:
            config_data = json.loads(raw_text)
            # 如果成功，就排好版儲存
            with open("tvbox.json", "w", encoding="utf-8") as f:
                json.dump(config_data, f, ensure_ascii=False, indent=2)
            print("✅ 成功獲取並儲存 JSON！")
            
        except json.JSONDecodeError:
            # 如果失敗（證明係密文），就將原始密文直接寫入檔案
            print("⚠️ 獲取到的內容不是標準 JSON，可能是加密狀態。將直接儲存原始內容...")
            with open("tvbox.json", "w", encoding="utf-8") as f:
                f.write(raw_text)
            print("✅ 已強制儲存原始密文。")
            
    except Exception as e:
        print(f"❌ 腳本執行失敗: {e}")
        # 就算失敗都開一個空檔案，防止 GitHub Git Add 報錯
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
