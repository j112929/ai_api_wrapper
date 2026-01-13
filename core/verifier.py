import decimal
import random
from decimal import Decimal
from core.reporting import ReportGenerator

class ShadowVerifier:
    """核心卖点：双轨运行与模糊测试"""
    def __init__(self, schema):
        self.schema = schema
        decimal.getcontext().prec = 28

    def _mock_cobol_execution(self, inputs):
        """模拟旧系统的黑盒行为 (用于演示)"""
        p = Decimal(str(inputs['PRINCIPAL']))
        r = Decimal(str(inputs['RATE']))
        t = Decimal(str(inputs['TERM']))
        interest = (p * (r / 100) * t) / 12
        return interest.quantize(Decimal("0.01"), rounding=decimal.ROUND_HALF_UP)

    def _execute_generated_code(self, code_str, inputs):
        """动态执行生成的 Python 代码"""
        local_scope = {}
        exec(code_str, {}, local_scope)
        # Using the same generated Decimal object from the exec context ensures compatibility
        func = local_scope['calculate_interest']
        return func(inputs['PRINCIPAL'], inputs['RATE'], inputs['TERM'])

    def run_audit(self, python_code_str, num_cases=5):
        ReportGenerator.print_header("Starting Shadow Verification Loop")
        
        stats = {
            "total_fields": len(self.schema),
            "cases_generated": num_cases,
            "passed": 0,
            "precision": "Decimal-128",
            "risk_level": "LOW"
        }

        for i in range(num_cases):
            # 1. 生成 Fuzzing 数据
            case_input = {}
            for field in self.schema:
                if field['type'] == 'integer':
                    val = random.randint(int(field['min']), int(field['max']))
                else:
                    val = round(random.uniform(field['min'], field['max']), 2)
                case_input[field['name']] = val

            # 2. 双轨执行
            legacy_result = self._mock_cobol_execution(case_input)
            modern_result = self._execute_generated_code(python_code_str, case_input)

            # 3. 比对
            if legacy_result == modern_result:
                print(f"✅ Case #{i+1:02d}: MATCH | Input: {str(case_input)[:50]}... | Result: {legacy_result}")
                stats["passed"] += 1
            else:
                print(f"❌ Case #{i+1:02d}: FAIL  | Legacy: {legacy_result} vs Modern: {modern_result}")
                stats["risk_level"] = "CRITICAL"

        return stats
