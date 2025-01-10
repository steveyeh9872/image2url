import os
import time
from pathlib import Path
from PIL import Image
import requests
import io

class FolderImageSender:
    def __init__(self, imgur_client_id):
        """
        初始化 Imgur API
        
        Args:
            imgur_client_id (str): Imgur API Client ID
        """
        self.imgur_client_id = imgur_client_id
        self.imgur_upload_url = "https://api.imgur.com/3/image"
        self.supported_formats = {'.jpg', '.jpeg', '.png', '.gif', '.bmp'}
        
    def is_valid_image(self, file_path):
        """檢查是否為支援的圖片格式"""
        return Path(file_path).suffix.lower() in self.supported_formats
    
    def prepare_image(self, image_path):
        """準備圖片用於上傳"""
        try:
            with Image.open(image_path) as img:
                # 如果是 RGBA 或調色盤模式，轉換為 RGB
                if img.mode in ['RGBA', 'P']:
                    img = img.convert('RGB')
                    
                # 將圖片儲存到記憶體緩衝區
                buffer = io.BytesIO()
                img.save(buffer, format='JPEG', quality=95)
                buffer.seek(0)
                return buffer
        except Exception as e:
            raise Exception(f"圖片處理失敗: {str(e)}")
        
    def upload_to_imgur(self, image_path):
        """上傳圖片到 Imgur 並獲得 URL"""
        try:
            # 準備圖片
            image_data = self.prepare_image(image_path)
            
            headers = {
                'Authorization': f'Client-ID {self.imgur_client_id}'
            }
            
            files = {
                'image': ('image.jpg', image_data, 'image/jpeg')
            }
            
            response = requests.post(
                self.imgur_upload_url,
                headers=headers,
                files=files
            )
            
            if response.status_code == 200:
                return response.json()['data']['link']
            else:
                raise Exception(f"Imgur 上傳失敗: {response.text}")
                
        except Exception as e:
            raise Exception(f"上傳圖片時發生錯誤: {str(e)}")
    
    def process_folder(self, folder_path):
        """處理整個資料夾的圖片"""
        results = {
            'success': [],
            'failed': []
        }
        
        # 確保資料夾存在
        if not os.path.exists(folder_path):
            raise FileNotFoundError(f"找不到資料夾: {folder_path}")
            
        # 取得所有圖片檔案
        image_files = [
            f for f in os.listdir(folder_path) 
            if os.path.isfile(os.path.join(folder_path, f)) and 
            self.is_valid_image(f)
        ]
        
        total_images = len(image_files)
        print(f"找到 {total_images} 張圖片")
        
        for index, image_file in enumerate(image_files, 1):
            image_path = os.path.join(folder_path, image_file)
            print(f"處理第 {index}/{total_images} 張圖片: {image_file}")
            
            try:
                # 上傳到 Imgur
                image_url = self.upload_to_imgur(image_path)
                results['success'].append((image_file, image_url))
                print(image_url)
                
                # 延遲一下避免觸發 API 限制
                time.sleep(1)
                
            except Exception as e:
                results['failed'].append((image_file, str(e)))
                print(f"✗ {image_file} 處理失敗: {str(e)}")
        
        return results

def main():
    # 設定參數
    IMGUR_CLIENT_ID = "YOUR_IMGUR_CLIENT_ID"
    FOLDER_PATH = "YOUR_FOLDER_PATH"
    
    # 建立發送器
    sender = FolderImageSender(IMGUR_CLIENT_ID)
    
    try:
        # 處理資料夾
        results = sender.process_folder(FOLDER_PATH)
        
        # 輸出結果摘要
        print("\n處理完成!")
        print(f"成功: {len(results['success'])} 張")
        print(f"失敗: {len(results['failed'])} 張")
        
        if results['failed']:
            print("\n失敗的圖片:")
            for file_name, error in results['failed']:
                print(f"- {file_name}: {error}")
                
    except Exception as e:
        print(f"發生錯誤: {str(e)}")

if __name__ == "__main__":
    main()