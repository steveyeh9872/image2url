# Image2URL

A Python tool to convert local images to URLs using Imgur API.

## Description

Image2URL is a simple tool that helps you:
- Upload local images to Imgur
- Get permanent URLs for your images
- Process multiple images in a folder
- Handle various image formats (jpg, jpeg, png, gif, bmp)

## Installation

1. Clone this repository
2. Install required packages:
    ```bash
    pip install requests pillow
    ```
3. Setup Imgur Client ID and Local Image Folder Path

## Register Imgur Account

1. Go to [Imgur](https://imgur.com/)
2. Click "Sign up" in the top right corner (or login if you already have an account)

## Register API Application

1. After login, go to [Imgur API](https://api.imgur.com/oauth2/addclient)
2. Fill in application information:
    - **Application name:** Choose a name (e.g., "Image2URL")
    - **Authorization type:** Select "OAuth 2 authorization without a callback URL"
    - **Email:** Your email address
    - **Description:** Brief description of your application
3. Check "I am not a robot"

## Get Client ID

1. After registration, you'll receive:
    - **Client ID**
    - **Client Secret**
2. Copy the Client ID (we only need this)

## Usage

1. Put your images in a folder
2. Update the script with your folder path:
    ```python
    FOLDER_PATH = "your_folder_path_here"
    ```
3. Update the script with your Imgur Client ID:
    ```python
    IMGUR_CLIENT_ID = "your_client_id_here"
    ```
4. Run the script:
    ```bash
    python image2url.py
    ```

## Example Output
![Sample Image](https://i.imgur.com/ao7jcS3.jpeg)
