from tree_sitter import Language, Parser
from tree_sitter_languages import get_language

# 1. 初始化 Fortran 解析器
FORTRAN_LANGUAGE = get_language('fortran')
parser = Parser()
parser.set_language(FORTRAN_LANGUAGE)

def extract_fortran_metadata(code_content):
    # 将代码解析为语法树 (AST)
    tree = parser.parse(bytes(code_content, "utf8"))
    print(tree.root_node.sexp())
    
    # 2. 定义查询语句 (S-expressions)
    # 捕捉子例程和函数定义
    query_string = """
    (subroutine_statement 
        name: (name) @proc_name) @subroutine
    (function_statement 
        name: (name) @proc_name) @function
    """
    query = FORTRAN_LANGUAGE.query(query_string)
    
    # 3. 执行查询并解析结果
    captures = query.captures(tree.root_node)
    
    metadata = []
    for node, tag in captures:
        if tag == 'proc_name':
            proc_name = code_content[node.start_byte:node.end_byte]
            # 获取父节点（即整个声明语句）来提取位置
            parent = node.parent
            metadata.append({
                "name": proc_name,
                "type": "subroutine" if "subroutine" in parent.type else "function",
                "start_line": parent.start_point[0] + 1,
                "end_line": parent.end_point[0] + 1,
                "raw": code_content[parent.start_byte:parent.end_byte]
            })
            
    return metadata

# 测试代码
fortran_code = """
subroutine calc_velocity(a, b, res)
    real, intent(in) :: a, b
    real, intent(out) :: res
    res = a * b + 9.8
end subroutine calc_velocity

function get_constant() result(val)
    real :: val
    val = 3.14159
end function get_constant
"""

results = extract_fortran_metadata(fortran_code)
for item in results:
    print(f"Detected {item['type'].upper()}: {item['name']} (Lines {item['start_line']}-{item['end_line']})")