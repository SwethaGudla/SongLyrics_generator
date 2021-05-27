import os
song_list = os.listdir('songslyrics')
while True:
    for i in range(len(song_list)):
        print(i+1,song_list[i][:-4])
    try:
        song_name = int(input('enter you choice: '))
    except:
         print('invalid')
         break
    try: 
        if song_list[song_name-1] in song_list:
            f=open(f'songslyrics\{song_list[song_name-1]}','r')
            print(f.read())
            f.close()    
    except:
        print('Invalid option\make correct choice')
    x=input('press * to choose again')
    if '*' != x:
        break
