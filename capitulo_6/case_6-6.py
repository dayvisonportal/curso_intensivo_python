# 6.6 Enquete
favorite_languages = {
    'jen':'python', 'sarah':'c'
    , 'edward':'ruby', 'phil':'python'
    , 'dayvison':'', 'portal':''
}

for pessoa, resposta in sorted(favorite_languages.items()):
    if resposta == '': 
        print(pessoa.title() + ", por favor, responda o questionario.")
    else:
        print(pessoa.title() + ", muito obrigado por responder o questionario!")
