from pathlib import Path

new_folder = Path.home() / 'documents' / 'python_automation'

new_folder.mkdir(exist_ok=True)

another_folder = new_folder / 'fun_w_folders' / 'my_3rd_folder'

another_folder.mkdir(exist_ok=True, parents=True)