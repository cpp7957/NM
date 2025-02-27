import os
import requests
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def is_valid_image(url):
    # Favicon, base64, 작은 이미지 필터링
    if 'favicon' in url.lower():
        return False
    if url.startswith('data:image'):  # Base64 인코딩된 이미지 제외
        return False
    return True

def download_image(url, folder='images'):
    try:
        response = requests.get(url, stream=True, timeout=5)
        if response.status_code == 200:
            content_type = response.headers.get('content-type', '')
            if 'image' in content_type:
                ext = content_type.split('/')[-1]
                filename = os.path.join(folder, f"{hash(url)}.{ext}")
                with open(filename, 'wb') as f:
                    for chunk in response.iter_content(1024):
                        f.write(chunk)
                print(f"[✅] 다운로드 완료: {filename}")
                return filename
    except Exception as e:
        print(f"[❌] 다운로드 실패: {url}, 오류: {e}")
    return None

def google_image_search(query, max_images=50):
    search_url = f"https://www.google.com/search?tbm=isch&q={query}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(search_url, headers=headers)
    if response.status_code != 200:
        print("[❌] 구글 이미지 검색 실패")
        return []
    
    soup = BeautifulSoup(response.text, 'html.parser')
    image_tags = soup.find_all('img')
    
    image_urls = []
    for img_tag in image_tags:
        img_url = img_tag.get('src') or img_tag.get('data-src')
        if img_url and is_valid_image(img_url):
            image_urls.append(urljoin(search_url, img_url))
            if len(image_urls) >= max_images:
                break
    
    return image_urls

# 실행 예제
query = "노무현"
image_urls = google_image_search(query, max_images=700)  # 이미지 개수 증가
print(f"[🔍] 크롤링된 이미지 개수: {len(image_urls)}")

# 이미지 다운로드
os.makedirs("images", exist_ok=True)
for img_url in image_urls:
    download_image(img_url)
