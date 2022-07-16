
class Folder:
    def __init__(self, path) -> None:
        self._path = path

    def extension_filter(file_):
        f, extension = file_
        return f.suffix[1:] == extension

    @staticmethod
    def files(file_path, extension=None, return_type=None):
        """
            Parameters:
                file_path(pathlib.Path) 
                extension(str) - extension to filter for
                return_type(str) - None=paths, name=names with extension, stem=names without extensions
            Returns:
                files
                file_names(str) - file.extension
                file_stems(str)
        """
        files = [(f, extension) for f in file_path.iterdir() if f.is_file()]

        if extension:
            files = filter(Folder.extension_filter, files)

        if return_type:
            return [getattr(f, return_type, f) for f, extension_ in files]
        return [f for f, extension_ in files]

    @staticmethod
    def folders(folder_path, return_type=None):
        folders = [f for f in folder_path.iterdir() if f.is_dir()]
        if return_type:
            return [getattr(f, return_type, f) for f in folders]
        return folders

    def create(self):
        try:
            self._path.mkdir(parents=True, exists_ok=True)
            return self._path
        except Exception as e:
            return None

def create(folder_path):
    f = Folder(path=folder_path)
    return f.create()

def files_in_folder(folder_path, extension=None, return_type=None):
    return Folder.files(folder_path, extension, return_type)

def folders_in_folder(folder_path, return_type=None):
    return Folder.folders(folder_path, return_type)