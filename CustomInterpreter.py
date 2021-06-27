# 分词--》 一句话代码  切分成 Tokens
#
# Token 词法单元  --》 <token-name, attribute-value>
#
# 算术器：1 + 1 - 2 + 4 = 4; (1 + 1) * 2 = 4; 1 *+ 1 = Error

from Lexer import Lexer


def run(fn, text):
    lexer = Lexer(fn, text)
    tokens. error = lexer.make_token()
    return tokens, error
