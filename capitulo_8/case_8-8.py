# 8.8 Album
def make_album(artist, album, track=''):
    album_list = {'artist': artist, 'album': album, 'track': track}
    # Se houver informação na chave do dicionario track
    if track:
        album_list['track'] = track
    return album_list


while True:
    print('\nColoque o nome do artista, do album e a quantidade de musicas')
    print('do seu album favorito.')
    print("(Digite 'q' para sair do programa)")
    la_artist = input('Artista: ')
    if la_artist == 'q':
        break
    la_album = input('Album: ')
    if la_album == 'q':
        break
    la_track = input('Qtd músicas: ')
    if la_track == 'q':
        break
    # A variavel a ser mostrada em tela recebera o retorno da função
    list_album = make_album(la_artist.title(), la_album.title(), la_track)
    print(list_album)
