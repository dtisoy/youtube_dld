from os import listdir, rename
import re


class Rename_music:
    def __init__(self):
        self.path = '/home/ltisoy/Music/music/'
        self.dirlist = listdir(path=self.path)

    def rename_music(self):
        _new_list = self.new_names()
        _old_files_path = [self.path+i for i in self.dirlist]
        _new_files_path = [self.path+i for i in _new_list]

        for i in range(len(_new_files_path)):
            rename(_old_files_path[i], _new_files_path[i])

    def new_names(self):
        _search = ['mp4', r'\(Official Music Video\)', r'\(Audio\)',
                   r'\(Official Video\)',r'\(Official Lyric Video\)',  
                   r'\(Lyric Video\)',r'\(Video Oficial\)',
                   r'\(Official Audio\)',
                   r'\(Traducida Al Español\)', r'\(Lyrics\)', r'\[Official Music Video\]', r'\[OFFICIAL VIDEO\]']
        _new_list_names = list()
        for i in self.dirlist:
            try:
                for j in _search:
                    m = re.search(j, i)
                    if m:
                        i = i[:m.start()]+i[m.end():]
                    else: 
                        continue
                i = i+'mp3'
                _new_list_names.append(i)
            except:
                # voy aqui
                print('El video {} no se pudo cambiar el nombre'.format(i))
        return _new_list_names


if __name__ == '__main__':
    cambios = Rename_music()
    cambios.rename_music()
