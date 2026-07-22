from pathlib import Path
import shutil

#src = Path.home() / 'documents' / 'python_automation' / 'moving_n_renaming' / 'dad_jokes.txt'
#dest = Path.home() / 'documents' / 'python_automation' / 'moving_n_renaming' / 'bad_jokes.txt'

src = Path.home() / 'documents' / 'python_automation' / 'moving_n_renaming' / 'bad_jokes.txt'
dest = Path.home() / 'documents' / 'python_automation' / 'moving_n_renaming' / 'my_123rd_folder' / 'sad_jokes.txt'

if src.exists():
    shutil.move(src, dest)