# generate_10000_chars.py

def make_text_file(filename: str, length: int = 10_000) -> None:
    """
    정확히 length 글자(기본 10,000 글자)의 텍스트 파일을 생성합니다.
    filename: 생성할 파일 이름
    length: 생성할 글자 수
    """
    content = "A" * length  # 원하는 문자로 변경 가능

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)


if __name__ == "__main__":
    make_text_file("output.txt")
    print("output.txt 생성 완료")