"""Simple text file operations."""
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent.parent / 'toolkit_notes.txt'

def write_text(text):
    DATA_FILE.write_text(text + '\n', encoding='utf-8')
    return DATA_FILE

def append_text(text):
    with DATA_FILE.open('a', encoding='utf-8') as file:
        file.write(text + '\n')
    return DATA_FILE

def read_text():
    if not DATA_FILE.exists():
        return 'No notes saved yet.'
    return DATA_FILE.read_text(encoding='utf-8') or 'The file is empty.'
