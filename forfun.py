import random

def generate_massive_code(filename="generated_10k.py", target_lines=10000):
    """
    1만 줄 이상의 유효한 파이썬 코드를 생성하여 파일로 저장하는 스크립트입니다.
    """
    
    with open(filename, "w", encoding="utf-8") as f:
        # 1. 기본 임포트 구문 작성
        f.write("import random\n")
        f.write("import time\n")
        f.write("import math\n\n")
        
        current_lines = 4
        class_count = 0
        
        # 2. 목표 라인 수에 도달할 때까지 반복해서 클래스와 함수 생성
        while current_lines < target_lines:
            class_name = f"DataProcessor_{class_count}"
            
            # 클래스 선언 (약 1~2줄)
            f.write(f"class {class_name}:\n")
            f.write(f"    '''\n    This is an auto-generated class number {class_count}\n    '''\n")
            
            # __init__ 메서드 (약 4줄)
            f.write("    def __init__(self, value):\n")
            f.write(f"        self.value = value\n")
            f.write(f"        self.id = {class_count}\n")
            f.write(f"        self.timestamp = time.time()\n\n")
            
            # 복잡한 연산 메서드 추가 (약 6~7줄)
            f.write("    def complex_calculation(self):\n")
            f.write("        result = 0\n")
            f.write("        for i in range(10):\n")
            f.write("            result += (self.value * i) + math.sqrt(self.id + 1)\n")
            f.write("        if result > 1000:\n")
            f.write("            return 'High'\n")
            f.write("        return result\n\n")

            # 데이터 처리 메서드 추가 (약 5줄)
            f.write("    def process_data(self):\n")
            f.write("        data_list = [x for x in range(self.id, self.id + 5)]\n")
            f.write("        random.shuffle(data_list)\n")
            f.write("        return sum(data_list)\n\n")

            # 라인 수 카운트 업데이트 (한 반복당 약 20줄 정도 생성됨)
            current_lines += 20
            class_count += 1
        
        # 3. 실행 구문 추가 (Main Block)
        f.write("\nif __name__ == '__main__':\n")
        f.write("    print('Starting Bulk Process...')\n")
        f.write(f"    processor = DataProcessor_{class_count-1}(100)\n")
        f.write("    print(processor.complex_calculation())\n")
        f.write("    print('Done.')\n")

    print(f"✅ 생성이 완료되었습니다: {filename}")
    print(f"📂 총 라인 수(예상): 약 {current_lines}줄")
    print(f"🔨 생성된 클래스 수: {class_count}개")

# 실행
if __name__ == "__main__":
    generate_massive_code()