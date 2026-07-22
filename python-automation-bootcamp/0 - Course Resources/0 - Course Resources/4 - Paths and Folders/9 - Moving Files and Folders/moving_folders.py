from pathlib import Path
import shutil

src = Path.home() / 'documents' / 'python_automation' / 'copying_stuff' / 'fun_w_folders' / 'my_3rd_folder'
dest = Path.home() / 'documents' / 'python_automation' / 'moving_n_renaming' / 'my_3rd_folder'

if src.exists():
    shutil.move(src, dest)