# image2url

transfer local image to url

# 如何取得 Imgur Client ID 的詳細步驟：

1. 註冊 Imgur 帳號
   前往 https://imgur.com/
   點擊右上角的 "Sign up" 註冊新帳號（如果已有帳號就直接登入）

2. 註冊 API 應用程式
   登入後前往 https://api.imgur.com/oauth2/addclient
   填寫應用程式資訊：

Application name(應用程式名稱): 自訂一個名稱，例如 "My LINE Bot"
Authorization type: 選擇 "OAuth 2 authorization without a callback URL"
Email: 填寫你的電子郵件
Description(描述): 簡單描述你的應用用途
勾選 "I am not a robot" 驗證碼

3. 取得 Client ID
   註冊完成後，你會看到兩個重要的資訊：
   Client ID(客戶端 ID)
   Client Secret(客戶端密鑰)
   我們只需要 Client ID, 把它複製下來
   將 Client ID 放入程式碼
