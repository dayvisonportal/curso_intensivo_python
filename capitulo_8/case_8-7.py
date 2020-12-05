# 8.7 Album
def make_album(artist, album, track=''):
    album_list = {'artist': artist, 'album': album, 'track': track}
    # Se houver informação na chave do dicionario track
    if track:
        album_list['track'] = track
    return album_list


lista_album = make_album('metallica', 'ride the lightning')
print(lista_album)

lista_album = make_album('metallica', 'kill em all', 12)
print(lista_album)
