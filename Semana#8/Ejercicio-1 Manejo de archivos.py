"""
Cree un programa que lea nombres de canciones de un archivo (línea por línea) 
y guarde en otro archivo los mismos nombres ordenados alfabéticamente.
"""
list_of_songs=[]
def open_list(names_songs):
	with open(names_songs,encoding='utf-8') as file:
		for line in file.readlines():
			list_of_songs.append(line)
			#print(line)

			
			list_of_songs.sort()

	
	#print(list_of_songs)

open_list('canciones.txt')



def list_order(name_song, text):
	with open(name_song,'w',encoding='utf-8') as file:
		file.writelines(text)
	
text_to_write = list_of_songs

list_order('lista ordenada.txt',text_to_write)