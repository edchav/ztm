from pathlib import Path

p = Path.home() / 'documents' / 'python_automation' / 'moving_n_renaming' / 'my_123rd_folder' / 'sad_jokes.txt'

p.unlink(missing_ok=True)