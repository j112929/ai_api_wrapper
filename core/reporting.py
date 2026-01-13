class ReportGenerator:
    """生成让 CTO 们眼前一亮的审计报告"""
    @staticmethod
    def print_header(title):
        print(f"\n{'='*60}")
        print(f"🚀 {title.upper()}")
        print(f"{'='*60}")

    @staticmethod
    def print_success(msg):
        print(f"✅ [SUCCESS] {msg}")

    @staticmethod
    def print_info(msg):
        print(f"ℹ️  [INFO]    {msg}")

    @staticmethod
    def print_audit_table(stats):
        print("\n📊 MIGRATION AUDIT SUMMARY")
        print("-" * 30)
        print(f"Total Fields Analyzed : {stats['total_fields']}")
        print(f"Test Cases Generated  : {stats['cases_generated']}")
        print(f"Verified Exact Matches: {stats['passed']}")
        print(f"Precision Level       : {stats['precision']}")
        print(f"Risk Assessment       : {stats['risk_level']}")
        print("-" * 30 + "\n")
