#!/usr/bin/python3
"""RBNB clone modules tester"""
import os
from typing import TextIO
from models.engine.file_storage import FileStorage


def clear_stream(stream: TextIO):
    """deletes the contents of a stream

    Args:
        stream (TextIO): stream to clear.
    """
    if stream.seekable():
        stream.seek(0)
        stream.truncate(0)


def delete_file(file_path: str):
    """deleting file if it exists.
    Args:
        file_path (str): file to remove.
    """
    if os.path.isfile(file_path):
        os.unlink(file_path)


def reset_store(store: FileStorage, file_path='file.json'):
    """items in the given store.
    Args:
        store (FileStorage): FileStorage to reset.
        file_path (str): path to the store's file.
    """
    with open(file_path, mode='w') as file:
        file.write('{}')

    if store is not None:
        store.reload()


def read_text_file(file_name):
    """contents of a given file.

    Args:
        file_name (str): file to read.

    Returns:
        str: contents of the file if it exists.
    """
    lines = []
    if os.path.isfile(file_name):

        with open(file_name, mode='r') as file:
            for line in file.readlines():
                lines.append(line)
    return ''.join(lines)


def write_text_file(file_name, text):
    """gives a text to a given file.

    Args:
        file_name (str): file to write to.
        text (str): content of the file.
    """
    with open(file_name, mode='w') as file:
        file.write(text)
