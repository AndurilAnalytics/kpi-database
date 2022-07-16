


def app_handler():
    pass

class Uploader:
    """
        Purpose: Manages the uploads to the application
        Parameters:
            handler(str) - handler to use to upload
                path - upload to a specific folder
            options(dict) - 
                path
                    root: pathlib.Path to the root folder
                    structure: dict of dict keys to be walked to create folder structure

    """
    UPLOAD_HANDLERS = {
        'path': None,
        'app': app_handler,
    }
    def __init__(self, data, meta, handler, options) -> None:
        self._handler = self.UPLOAD_HANDLERS[handler]

    def _check_structure():
        pass
    
def upload():
    pass