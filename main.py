import argparse
import time
from dotenv import load_dotenv

# Load config
load_dotenv()

from core.reporting import ReportGenerator
from core.parser import LegacyParser
from core.architect import CodeArchitect
from core.verifier import ShadowVerifier

def main():
    parser = argparse.ArgumentParser(description="LegacyCode AI Adapter - COBOL Modernization Tool")
    parser.add_argument("file", help="Path to legacy .cbl file")
    parser.add_argument("--demo", action="store_true", default=True, help="Run in simulation mode without external deps")
    args = parser.parse_args()

    start_time = time.time()
    ReportGenerator.print_header("Legacy System Transformation Engine v1.0")

    # 1. 考古
    archaeologist = LegacyParser(demo_mode=args.demo)
    schema = archaeologist.parse(args.file)
    ReportGenerator.print_success(f"Extracted Data Schema: {len(schema)} fields identified.")

    # 2. 架构
    architect = CodeArchitect(demo_mode=args.demo)
    modern_code = architect.generate_modern_implementation(schema)
    ReportGenerator.print_success("Generated Python Microservice logic.")
    
    # 3. 验证
    verifier = ShadowVerifier(schema)
    audit_stats = verifier.run_audit(modern_code, num_cases=10)

    # 4. 报告
    ReportGenerator.print_audit_table(audit_stats)
    
    # 5. 生成最终产物
    with open("modernized_api.py", "w") as f:
        f.write(modern_code)
    ReportGenerator.print_success(f"Production-ready code saved to 'modernized_api.py' in {time.time()-start_time:.2f}s")

if __name__ == "__main__":
    main()