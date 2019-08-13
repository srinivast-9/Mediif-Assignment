class Path:
    def __init__(self, current_path):
        self.current_path = current_path

    def cd(self, path):
        # absolute path
        if path.startswith('/') and '..' not in path:
                self.current_path = path
        # relative parent path
        elif '..' in path:
            if self.current_path != '/':
                if path.startswith('/'):
                    path_list = (self.current_path + path).split('/')[1:]
                else:
                    path_list = (self.current_path + '/' + path).split('/')[1:]

                count = path_list.count('..')
                for i in range(count):
                    index = path_list.index('..')
                    path_list.pop(index - 1)
                    path_list.pop(index - 1)
                temppath = '/'
                self.current_path = temppath + temppath.join(path_list)
        # relative child path
        elif self.current_path != '/':
            temppath = self.current_path + '/' + path
            self.current_path = temppath
        else:
            temppath = self.current_path + path
            self.current_path = temppath

    def printpath(self):
        print(self.current_path)

path = Path('/a/b/c/d')
path.printpath()
path.cd('../x')
path.printpath()
path.cd('y/z')
path.printpath()
path.cd('/d/e/f')
path.printpath()
path.cd('../..')
path.printpath()
path.cd('..')
path.printpath()
path.cd('..')
path.printpath()