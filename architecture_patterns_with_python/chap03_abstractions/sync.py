import hashlib
import os
import shutil
from pathlib import Path


BLOCKSIZE = 65536


def hash_file(path):
    hasher = hashlib.sha1()
    with path.open("rb") as file:
        buf = file.read(BLOCKSIZE)
        while buf:
            hasher.update(buf)
            buf = file.read(BLOCKSIZE)
    return hasher.hexdigest()


def sync(source, dest):
    # 원본 폴더의 자식들을 순회하면서 파일 이름과 해시의 사전을 만든다.
    source_hashes = {}
    for folder, _, files in os.walk(source):
        for fn in files:
            source_hashes[hash_file(Path(folder) / fn)] = fn

    seen = set()  # 사본 폴더에서 찾은 파일을 추적한다

    # 사본 폴더 자식들을 순회하면서 파일 이름과 해시를 얻는다.
    for folder, _, files in os.walk(dest):
        for fn in files:
            dest_path = Path(folder) / fn
            dest_hash = hash_file(dest_path)
            seen.add(dest_hash)

            # 사본에는 있지만 원본에 없는 파일을 찾으면 삭제한다.
            if dest_hash not in source_hashes:
                dest_path.remove()

            # 사본에 있는 파일이 원본과 다른 이름이라면
            # 사본 이름을 올바른 이름(원본 이름)으로 바꾼다.
            elif dest_hash in source_hashes and fn != source_hashes[dest_hash]:
                shutil.move(dest_path, Path(folder) / source_hashes[dest_hash])

        # 원본에는 있지만 사본에 없는 모든 파일을 사본으로 복사한다.
        for src_hash, fn in source_hashes.items():
            if src_hash not in seen:
                shutil.copy(Path(source) / fn, Path(dest) / fn)
