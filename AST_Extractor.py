from tree_sitter_languages import get_language, get_parser

def extract_function_metadata(code_content, language='c'):
    parser = get_parser(language)
    tree = parser.parse(bytes(code_content, "utf8"))
    cursor = tree.walk()
    
    functions = []
    
    # 定义一个简单的 AST 遍历逻辑，寻找函数定义
    def walk_nodes(node):
        if node.type == 'function_definition':
            # 提取函数名节点
            name_node = node.child_by_field_name('declarator')
            functions.append({
                "type": node.type,
                "start_line": node.start_point[0],
                "end_line": node.end_point[0],
                "raw_structure": code_content[node.start_byte:node.end_byte]
            })
        for child in node.children:
            walk_nodes(child)

    walk_nodes(tree.root_node)
    return functions