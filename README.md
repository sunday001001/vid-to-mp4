# MTS to MP4 Converter

MTS 및 M2TS 동영상 파일을 화질 저하 없이 고속으로 MP4로 변환해주는 파이썬 도구입니다. 원본의 **해상도, 화질, 메타데이터, 그리고 파일 수정 날짜**를 그대로 보존합니다.

## 🌟 주요 특징

- **무손실 변환**: FFmpeg의 `copy` 코덱을 사용하여 재인코딩 없이 컨테이너만 교체하므로 화질 저하가 없고 속도가 매우 빠릅니다.
- **날짜 보존**: 변환 후 파일의 수정 시간(mtime)을 원본과 동일하게 맞추어 타임라인 정렬을 유지합니다.
- **유연한 인자**: 단일 파일(`-f`) 또는 디렉토리 전체(`-d`) 변환을 지원합니다.
- **현대적인 관리**: `uv`를 사용하여 의존성 및 파이썬 버전을 깔끔하게 관리합니다.

## 📋 요구 사항

- **macOS** (Apple Silicon 권장)
- **FFmpeg**: 시스템에 설치되어 있어야 합니다.
  ```bash
  brew install ffmpeg
  ```

## 🚀 설치 및 설정
1. 저장소 클론 또는 폴더 이동:
  ```bash
  cd vid-to-mp4
  ```
2. 의존성 설치 (uv 사용):
  ```bash
  uv add ffmpeg-python
  ```

## 💻 사용법
**단일 파일 변환**
  ```bash
  uv run convert.py -f "경로/파일명.mts"
  ```
**디렉토리 내 모든 파일 변환**
  ```bash
  uv run convert.py -d "/Volumes/980PRO/Photos/2013"
  ```

## 🛠 디버깅 (VS Code)
.vscode/launch.json 설정이 포함되어 있어, F5 키를 눌러 즉시 디버깅이 가능합니다. 인자 값은 launch.json의 args 항목에서 수정할 수 있습니다.

## 📝 라이선스
MIT License