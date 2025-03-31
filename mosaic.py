import os
import numpy as np
from PIL import Image
from tqdm import tqdm

# 설정 값
MAIN_IMAGE_PATH = "노무현.jpg"  # 기준이 될 메인 이미지
TILE_IMAGES_DIR = "noh_images"  # 작은 이미지 폴더
OUTPUT_IMAGE_PATH = "noh_mosaic.jpg"  # 출력 이미지
TILE_SIZE = input("각 조각의 크기(해상도)를 입력해주십시오.")  # 작은 타일 크기 
GRID_SIZE = input("모자이크 그림의 크기(해상도)를 입력해주십시오.")  # 모자이크의 가로/세로 타일 개수

# 1. 작은 이미지 로드 & 평균 색상 계산
def load_tile_images(tile_dir):
    tile_images = []
    avg_colors = []
    
    for filename in os.listdir(tile_dir):
        img_path = os.path.join(tile_dir, filename)
        img = Image.open(img_path).convert("RGB").resize((TILE_SIZE, TILE_SIZE))
        
        img_array = np.array(img)
        avg_color = img_array.mean(axis=(0, 1))  # RGB 평균 계산
        
        tile_images.append(img_array)
        avg_colors.append(avg_color)
    
    return np.array(tile_images), np.array(avg_colors)

# 2. 가장 유사한 타일 찾기
def find_best_match(target_color, avg_colors):
    return np.argmin(np.linalg.norm(avg_colors - target_color, axis=1))

# 3. 모자이크 생성
def create_mosaic():
    # 메인 이미지 로드
    main_img = Image.open(MAIN_IMAGE_PATH).convert("RGB")
    main_img = main_img.resize((GRID_SIZE * TILE_SIZE, GRID_SIZE * TILE_SIZE))  # 모자이크 크기로 변경
    main_pixels = np.array(main_img)

    # 타일 이미지 로드
    tile_images, avg_colors = load_tile_images(TILE_IMAGES_DIR)

    # 빈 모자이크 캔버스 (NumPy 배열로 생성)
    mosaic = np.zeros_like(main_pixels)

    # 타일로 채우기
    for i in tqdm(range(GRID_SIZE), desc="모자이크 생성 중"):
        for j in range(GRID_SIZE):
            # 현재 위치의 평균 색상 계산
            region = main_pixels[i*TILE_SIZE:(i+1)*TILE_SIZE, j*TILE_SIZE:(j+1)*TILE_SIZE]
            target_color = region.mean(axis=(0, 1))

            # 가장 유사한 타일 찾기
            best_match_idx = find_best_match(target_color, avg_colors)

            # 모자이크 배열에 할당 (한 번에 처리)
            mosaic[i*TILE_SIZE:(i+1)*TILE_SIZE, j*TILE_SIZE:(j+1)*TILE_SIZE] = tile_images[best_match_idx]

    # PIL을 사용하여 최종 이미지 저장
    mosaic_img = Image.fromarray(mosaic)
    mosaic_img.save(OUTPUT_IMAGE_PATH)
    print("모자이크 생성 완료! 저장됨:", OUTPUT_IMAGE_PATH)

# 실행
create_mosaic()
