from tree_sitter import Language, Parser
import os

# Use local dylib built from source
LIB_PATH = os.path.abspath('libtree-sitter-cobol.dylib')
LANGUAGE = Language(LIB_PATH, 'COBOL')
parser = Parser()
parser.set_language(LANGUAGE)

def extract_cobol_schema(code_content):
    tree = parser.parse(bytes(code_content, "utf8"))
    
    # 2. 定义查询：寻找数据项、层级号、变量名和 PIC 格式
    query_string = """
    (data_description
        (level_number) @lvl
        (entry_name) @name
        (picture_clause)? @format)
    """
    query = LANGUAGE.query(query_string)
    captures = query.captures(tree.root_node)
    
    schema = []
    # Handle tree-sitter 0.21 captures (list of tuples) vs 0.23 (dict)
    # In 0.21.3 it returns [(node, capture_name), ...]
    for node, tag in captures:
        # 我们只在捕捉到 data_name 时处理该节点
        if tag == 'name':
            parent = node.parent
            lvl = ""
            pic_format = "GROUP" # 默认为组项
            
            # 提取详细属性
            for child in parent.children:
                if child.type == 'level_number':
                    lvl = code_content[child.start_byte:child.end_byte]
                if child.type == 'picture_clause':
                    pic_format = code_content[child.start_byte:child.end_byte]
            
            schema.append({
                "level": lvl,
                "field": code_content[node.start_byte:node.end_byte],
                "format": pic_format.replace("PIC ", "").strip()
            })
    return schema

# 测试代码：解析一段典型的银行账户记录
cobol_data = """
       IDENTIFICATION DIVISION.
       PROGRAM-ID. TEST-PROG.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 ACCOUNT-RECORD.
           05 ACCOUNT-ID    PIC X(10).
           05 BALANCE       PIC S9(9)V99.
           05 USER-NAME     PIC X(30).
"""

results = extract_cobol_schema(cobol_data)
for item in results:
    print(f"Level {item['level']}: {item['field']} -> {item['format']}")