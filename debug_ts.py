from tree_sitter import Parser
from tree_sitter_languages import get_language

FORTRAN_LANGUAGE = get_language('fortran')
query_string = """
(subroutine_statement 
    name: (name) @proc_name) @subroutine
"""
query = FORTRAN_LANGUAGE.query(query_string)
parser = Parser()
parser.language = FORTRAN_LANGUAGE
tree = parser.parse(b"subroutine foo\nend subroutine foo")

captures = query.captures(tree.root_node)
print(f"Type of captures: {type(captures)}")
if isinstance(captures, list):
    if len(captures) > 0:
        print(f"First element: {captures[0]}")
        print(f"Length of first element: {len(captures[0])}")
elif isinstance(captures, dict):
    print(f"Keys: {captures.keys()}")
else:
    print(captures)

try:
    import tree_sitter_languages
except ImportError:
    pass

print(f"Language methods: {dir(Language)}")
try:
    print(f"build_library in Language: {'build_library' in dir(Language)}")
except:
    pass
