import hashlib
import os
import shutil
from abc import ABC
from pathlib import Path
from typing import Callable


def sync(reader: Callable[..., dict], filesystem: 'FileSystem', source, dest):
    source_hashes = reader(source)
    dest_hashes = reader(dest)

    for sha, filename in source_hashes.items():
        if sha not in dest_hashes:
            source_path = source / filename
            dest_path = dest / filename
            filesystem.copy(source_path, dest_path)
        elif dest_hashes[sha] != filename:
            oldest_path = dest / dest_hashes[sha]
            newest_path = dest / filename
            filesystem.move(oldest_path, newest_path)

    for sha, filename in dest_hashes.items():
        if sha not in source_hashes:
            filesystem.delete(dest / filename)


BLOCKSIZE = 65536


def hash_file(path):
    hasher = hashlib.sha1()
    with path.open("rb") as file:
        buf = file.read(BLOCKSIZE)
        while buf:
            hasher.update(buf)
            buf = file.read(BLOCKSIZE)
    return hasher.hexdigest()


def read_paths_and_hashes(root):
    hashes = {}
    for folder, _, files in os.walk(root):
        for fn in files:
            hashes[hash_file(Path(folder) / fn)] = fn
    return hashes


class FileSystem(ABC):
    def copy(self, src, dest):
        ...

    def move(self, src, dest):
        ...

    def delete(self, dest):
        ...


class LocalFileSystem(FileSystem):
    def copy(self, src, dest):
        shutil.copyfile(src, dest)

    def move(self, src, dest):
        shutil.move(src, dest)

    def delete(self, dest):
        os.remove(dest)
