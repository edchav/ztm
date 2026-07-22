from pathlib import Path
import shutil

p = Path.home() / 'documents' / 'python_automation' / 'doomed_folder'

if p.exists():
    p.rmdir()

p2 = Path.home() / 'documents' / 'python_automation' / 'fun_w_folders'

if p2.exists():
    #p2.rmdir()
    shutil.rmtree(p2)