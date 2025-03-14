# NM

## 개요
이 프로젝트는 특정 키워드(예: "노무현")에 대한 이미지를 크롤링한 후, 해당 이미지를 이용하여 모자이크를 생성하는 Python 스크립트로 구성되어 있습니다.

## 파일 구성
- `crawling.py`: Google 이미지 검색을 통해 특정 키워드에 대한 이미지를 크롤링하고 다운로드하는 스크립트입니다.
- `mosaic.py`: 다운로드된 이미지를 활용하여 기준 이미지(`노무현.jpg`)의 모자이크를 생성하는 스크립트입니다.
- `노무현.jpg`: 모자이크의 메인 이미지로 사용될 기준 이미지입니다.
- `noh_images/`: 크롤링한 이미지가 저장될 폴더입니다.
- `noh_mosaic.jpg`: 생성된 모자이크 이미지의 출력 파일입니다.

## 사용 방법

### 1. 크롤링 실행
1. `crawling.py`를 실행하여 특정 키워드의 이미지를 크롤링합니다.
   ```bash
   python crawling.py
   ```
2. 다운로드된 이미지들은 `noh_images/` 폴더에 저장됩니다.

### 2. 모자이크 생성
1. `mosaic.py`를 실행하여 `노무현.jpg`를 기준으로 크롤링한 이미지를 사용해 모자이크를 생성합니다.
   ```bash
   python mosaic.py
   ```
2. 생성된 모자이크 이미지는 `noh_mosaic.jpg`로 저장됩니다.

## 설정 값 변경
`mosaic.py` 내에서 다음 값을 조정하여 원하는 결과를 얻을 수 있습니다.
- `TILE_SIZE`: 개별 타일 이미지의 크기 (기본값: `30`x`30` 픽셀)
- `GRID_SIZE`: 모자이크의 가로/세로 타일 개수 (기본값: `1000`)

## 라이브러리 요구사항
이 프로젝트를 실행하려면 다음 Python 라이브러리가 필요합니다.
```bash
pip install requests beautifulsoup4 pillow numpy tqdm
```

## 주의 사항
- 큰 `GRID_SIZE` 값을 설정하면 모자이크 생성에 많은 시간이 걸릴 수 있습니다.

## 기여
버그 리포트 및 기능 개선 제안은 PR(Pull Request) 또는 이슈 등록을 통해 환영합니다.
