import time
from typing import List, Dict
from core.reporting import ReportGenerator

class LegacyParser:
    """负责解析旧 COBOL 代码结构 (Tree-sitter 封装)"""
    def __init__(self, demo_mode=True):
        self.demo_mode = demo_mode

    def parse(self, file_path: str) -> List[Dict]:
        ReportGenerator.print_info(f"Parsing legacy structure from {file_path}...")
        
        if self.demo_mode:
            # 模拟 Tree-sitter 的提取结果
            time.sleep(1) # 假装在努力工作
            return [
                {"name": "PRINCIPAL", "type": "numeric", "pic": "S9(7)V99", "min": 0, "max": 9999999.99},
                {"name": "RATE", "type": "numeric", "pic": "9(3)V999", "min": 0, "max": 100.000},
                {"name": "TERM", "type": "integer", "pic": "9(3)", "min": 1, "max": 360}
            ]
        else:
            # 这里接入真实的 tree-sitter-cobol 逻辑
            pass
