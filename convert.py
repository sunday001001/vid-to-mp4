import ffmpeg
import os
import sys
import argparse
from pathlib import Path

def convert_video(input_path):
    input_path = Path(input_path)
    if not input_path.exists():
        print(f"파일이 없습니다: {input_path}")
        return

    output_path = input_path.with_suffix('.mp4')
    
    # 원본 파일의 시간 정보 기록
    stat = os.stat(input_path)
    atime = stat.st_atime
    mtime = stat.st_mtime

    print(f"변환 중 (데이터 복사): {input_path.name}")

    try:
        # vcodec='copy', acodec='copy'를 사용해 원본 화질/정보 유지
        (
            ffmpeg
            .input(str(input_path))
            .output(str(output_path), c='copy', map_metadata=0)
            .run(overwrite_output=True, quiet=True)
        )
        
        # 원본 수정 날짜 적용
        os.utime(output_path, (atime, mtime))
        print(f"성공: {output_path.name} (날짜 복원 완료)")
        
    except ffmpeg.Error as e:
        print(f"에러 발생 ({input_path.name}): {e}")

def main():
    parser = argparse.ArgumentParser(description="MTS to MP4 변환기 (화질/날짜 유지)")
    parser.add_argument("-f", "--file", help="변환할 특정 파일 경로")
    parser.add_argument("-d", "--dir", help="변환할 파일들이 있는 디렉토리 경로")

    args = parser.parse_args()

    if args.file:
        convert_video(args.file)
    elif args.dir:
        dir_path = Path(args.dir)
        # mts, m2ts 파일 모두 찾기
        files = list(dir_path.glob("*.mts")) + list(dir_path.glob("*.m2ts"))
        if not files:
            print("변환할 MTS 파일이 없습니다.")
            return
        for f in files:
            convert_video(f)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()