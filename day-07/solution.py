from pathlib import Path
from typing import Optional
import networkx as nx


script_dir = Path(__file__).parent


class Directory:
	def __init__(self, parent: Optional["Directory"] = None):
		self.parent: "Directory" = self if parent is None else parent
		self.directories: dict[str, "Directory"] = {}
		self.files: list[tuple[int, str]] = []
		self.size: int = 0

	def create_sizes(self):
		self.size = sum([file[0] for file in self.files]) + sum([directory.create_sizes() for directory in self.directories.values()])
		return self.size

	def get_sizes(self):
		self.create_sizes()
		sizes = [self.size]

		for directory in self.directories.values():
			sizes += directory.get_sizes()
		
		return sizes

def build_file_tree(input: list[str]) -> Directory:

    filesystem = Directory()
    ref = filesystem

    i = 0

    while i < len(input):
        command = input[i].split()
        if command[1] == "cd":
            if command[2] == "/":
                ref = filesystem
            elif command[2] == "..":
                ref = ref.parent
            else:
                ref = ref.directories[command[2]]
        elif command[1] != "ls":
            if command[0] == "dir":
                ref.directories[command[1]] = Directory(ref)
            else:
                ref.files.append((int(command[0]), command[1]))

        i += 1

    return filesystem


if __name__ == "__main__":

    with open(script_dir / "input.txt") as f:
        input_raw = f.read().splitlines()

    file_tree = build_file_tree(input_raw)

    sizes = file_tree.get_sizes()
    dirs_small_sum = sum([size for size in sorted(sizes) if size <= 100000])

    part_1 = dirs_small_sum
    print(f"Part 1: {part_1}")

    delete_dir_size = next(size for size in sorted(sizes) if size >= sizes[0] - 40000000)

    part_2 = delete_dir_size
    print(f"Part 2: {part_2}")
