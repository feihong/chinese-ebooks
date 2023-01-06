import pprint
import tatsu

GRAMMAR = """
@@grammar::BOOK

start = book $ ;

book = '\n\n'.{ section }+ ;

section = title [ '\n\n' body ] ;

title = ('#' | /\d+\./) ->&'\n' ;

body = '\n\n'.{ paragraph }+ ;

paragraph = ->&('\n\n' | '\n' $) ;
"""

example = """
#god

Let there be light!
"""

ast = tatsu.parse(GRAMMAR, example)
# pprint.pprint(ast, indent=2, width=20)
