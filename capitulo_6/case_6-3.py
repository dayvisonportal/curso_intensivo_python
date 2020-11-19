# 6.3 Glossario
glossaries = {
    'sorted':'ordenar valores'
    , 'print':'mostrar na tela o valor'
    , 'del':'deletar o valor'
    , '.title':'mostrar primeira letra em maiusculo'
    , 'set':'retornar distinct do sql'
}

for comando, significado in sorted(set(glossaries.items())):
    print(
        "O termo " + comando.title() 
        + " serve para " + significado.title() 
        + "."
    )

print("\n")

# 6.4 Glossario 2
glossaries['keys']='retornar o par valor-chave do dicionario'
glossaries['clear']='limpar o conteudo de uma lista'
glossaries['append']='adicionar um valor no final da lista'
glossaries['range']='retornar uma serie dentro de um intervalo enviado como argumento'
glossaries['list']='armazenar multiplos itens em apenas uma variavel'

for comando, significado in sorted(set(glossaries.items())):
    print(
        "O termo " + comando.title() 
        + " serve para " + significado.title() 
        + "."
    )