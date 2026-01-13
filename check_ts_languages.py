from tree_sitter_languages import get_language, get_parser

try:
    language = get_language('cobol')
    print("COBOL found in tree-sitter-languages")
except Exception as e:
    print(f"COBOL NOT found in tree-sitter-languages: {e}")
