from pathlib import Path

path = Path.home() / 'PycharmProjects' / 'plaintext-files'

for item in path.iterdir():
    print(item)