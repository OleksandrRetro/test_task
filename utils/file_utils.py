import json
import os
from pathlib import Path


class FileUtils:
    """
    Utility class to make operations with files.
    """
    ROOT_DIR = Path(__file__).parent.parent
    RESOURCES_DIR: str = "resources/"

    def read_file(self, file_path):
        with open(self.ROOT_DIR.joinpath(self.RESOURCES_DIR).joinpath(file_path), 'r') as f:
            file_content = json.load(f)
        return file_content

    def get_all_files_from_dir(self, dir_path):
        json_text = list()
        json_files_dir = self.ROOT_DIR.joinpath(self.RESOURCES_DIR).joinpath(dir_path)
        json_file_names = [filename for filename in
                           os.listdir(json_files_dir) if
                           filename.endswith('.json')]

        for json_file_name in json_file_names:
            with open(os.path.join(json_files_dir, json_file_name)) as json_file:
                json_text.append(json.load(json_file))
        return json_text
