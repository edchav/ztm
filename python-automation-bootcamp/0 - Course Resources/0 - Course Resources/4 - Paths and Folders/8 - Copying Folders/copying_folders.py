from pathlib import Path
import shutil

src = Path.home() / 'documents' / 'python_automation' / 'fun_w_folders'
dest = Path.home() / 'documents' / 'python_automation' / 'copying_stuff' / 'fun_w_folders'

shutil.copytree(src, dest , dirs_exist_ok=True)