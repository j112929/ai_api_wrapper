import subprocess
import random
import decimal
from decimal import Decimal
from typing import List, Dict, Any

# 假设这是通过 Tree-sitter 解析出来的 COBOL 输入定义
# PIC S9(5)V99 代表：带符号，5位整数，2位小数
COBOL_SCHEMA = [
    {"name": "PRINCIPAL", "type": "numeric", "pic": "S9(7)V99", "min": 0, "max": 9999999.99},
    {"name": "RATE", "type": "numeric", "pic": "9(3)V999", "min": 0, "max": 100.000}, # 利率
    {"name": "TERM", "type": "integer", "pic": "9(3)", "min": 1, "max": 360} # 期限（月）
]

class ValidationAgent:
    def __init__(self, schema):
        self.schema = schema
        # 设置全局精度，防止 Python 浮点误差导致误判
        decimal.getcontext().prec = 28 

    def generate_edge_cases(self, num_cases=5) -> List[Dict[str, Any]]:
        """
        智能生成测试数据，专注于边界条件 (Fuzzing)
        """
        test_cases = []
        
        # 1. 极值测试 (Max/Min)
        max_case = {item['name']: item['max'] for item in self.schema}
        min_case = {item['name']: item['min'] for item in self.schema}
        test_cases.append(max_case)
        test_cases.append(min_case)
        
        # 2. 随机 fuzzing
        for _ in range(num_cases):
            case = {}
            for item in self.schema:
                if item['type'] == 'integer':
                    val = random.randint(int(item['min']), int(item['max']))
                else:
                    # 生成随机小数
                    val = random.uniform(item['min'], item['max'])
                    # 格式化为固定精度字符串再转 Decimal，模拟 COBOL 行为
                    val = round(val, 2 if "V99" in item['pic'] else 3) 
                case[item['name']] = val
            test_cases.append(case)
            
        return test_cases

    def run_cobol_legacy(self, inputs: Dict) -> Decimal:
        """
        模拟调用旧的 COBOL 二进制文件 (Legacy System)
        实际中这里会是: subprocess.run(['./calc_interest'], input=...)
        """
        # 这里模拟一个简单的利息计算逻辑 (I = P * R * T / 12)
        # 注意：COBOL 的运算通常会截断而不是四舍五入，这里模拟这种行为
        p = Decimal(str(inputs['PRINCIPAL']))
        r = Decimal(str(inputs['RATE']))
        t = Decimal(str(inputs['TERM']))
        
        # 模拟 COBOL 可能的中间运算精度逻辑
        interest = (p * (r / 100) * t) / 12
        return interest.quantize(Decimal("0.01"), rounding=decimal.ROUND_HALF_UP)

    def run_python_modern(self, inputs: Dict) -> Decimal:
        """
        这是 Agent 刚刚生成的新 Python 代码
        """
        try:
            p = Decimal(str(inputs['PRINCIPAL']))
            r = Decimal(str(inputs['RATE']))
            t = Decimal(str(inputs['TERM']))
            
            # 现代 Python 实现
            result = (p * (r / 100) * t) / 12
            return result.quantize(Decimal("0.01"), rounding=decimal.ROUND_HALF_UP)
        except Exception as e:
            return Decimal("-1") # Error flag

    def verify(self):
        print(f"🕵️ Starting Audit Loop for {len(self.schema)} fields...")
        cases = self.generate_edge_cases()
        
        passed = 0
        failed = 0
        
        for i, case in enumerate(cases):
            # 1. 执行双轨
            cobol_res = self.run_cobol_legacy(case)
            python_res = self.run_python_modern(case)
            
            # 2. 精确比对
            # 金融系统容忍度通常为 0，或者极小的 epsilon
            is_match = cobol_res == python_res
            
            status = "✅ PASS" if is_match else "❌ FAIL"
            print(f"Case #{i+1} | Input: {case}")
            print(f"   Legacy (COBOL): {cobol_res}")
            print(f"   Modern (Python): {python_res}")
            print(f"   Status: {status}\n")
            
            if is_match:
                passed += 1
            else:
                failed += 1
                # 记录失败案例用于后续微调 Prompt
                self.log_failure(case, cobol_res, python_res)

        print(f"audit_complete: {passed} Passed, {failed} Failed.")

    def log_failure(self, case, expected, actual):
        # 在真实场景中，这里会将失败案例回传给 'Code Architect' Agent 进行代码修正
        pass

# 运行 Agent
agent = ValidationAgent(COBOL_SCHEMA)
agent.verify()