from pathlib import Path

from sync import sync, FileSystem


class FakeFileSystem(FileSystem):
    def __init__(self):
        self.actions = []

    def copy(self, src, dest):
        self.actions.append(("COPY", src, dest))

    def move(self, src, dest):
        self.actions.append(("MOVE", src, dest))

    def delete(self, dest):
        self.actions.append(("DELETE", dest))


def test_when_a_file_exists_in_the_source_but_not_the_destination():
    source_hashes = {"hash1": "fn1"}
    dest_hashes = {}

    file_system = FakeFileSystem()
    reader = {Path("/src"): source_hashes, Path("/dest"): dest_hashes}

    sync(reader.pop, file_system, Path("/src"), Path("/dest"))

    assert file_system.actions == [("COPY", Path("/src/fn1"), Path("/dest/fn1"))]


def test_when_a_file_has_been_renamed_in_the_source():
    source_hashes = {"hash1": "fn1"}
    dest_hashes = {"hash1": "fn2"}

    file_system = FakeFileSystem()
    reader = {Path("/src"): source_hashes, Path("/dest"): dest_hashes}

    sync(reader.pop, file_system, Path("/src"), Path("/dest"))
    assert file_system.actions == [("MOVE", Path("/dest/fn2"), Path("/dest/fn1"))]


def test_when_a_file_in_the_source_removed():
    source_hashes = {}
    dest_hashes = {"hash1": "fn1"}

    file_system = FakeFileSystem()
    reader = {Path("/src"): source_hashes, Path("/dest"): dest_hashes}

    sync(reader.pop, file_system, Path("/src"), Path("/dest"))
    assert file_system.actions == [("DELETE", Path("/dest/fn1"))]
