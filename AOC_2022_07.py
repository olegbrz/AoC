#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from aoc_helper import *
from dataclasses import dataclass


class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.subdirs = []
        self.files = []

    def dir_size(self):
        files_size = sum([file.size for file in self.files])
        self.d_size = files_size + sum([direc.dir_size() for direc in self.subdirs])
        return self.d_size

    def pretty_print(self, indent=0):
        if indent < 20:
            for dr in self.subdirs:
                print(f"{' ' * indent* 2}├── {dr.name} (dir)")
                dr.pretty_print(indent=indent + 1)
            for fi in self.files:
                print(f"{'  ' * indent*2}├── {fi.name} (file, size: {fi.size})")

    def __repr__(self) -> str:
        return f"Directory(name={self.name}, parent={self.parent})"


@dataclass
class File:
    name: str
    size: int
    parent: Directory


@parsing_benchmark
def build_tree(data):
    curr_dir = Directory(name="/")
    root_dir = curr_dir

    for line in data[1:]:
        # If the line starts with $ cd, we change the current directory
        if line[0:4] == "$ cd":
            target_dir = line.split()[-1]
            if target_dir == "..":
                curr_dir = curr_dir.parent
            else:
                curr_dir = next(
                    filter(lambda x: x.name == target_dir, curr_dir.subdirs)
                )

        # If the line starts with d (dir), we create a new directory
        elif line[0] == "d":
            dir_name = line.split()[-1]
            curr_dir.subdirs.append(Directory(name=dir_name, parent=curr_dir))

        # If the line starts with a number (size), we create a new file
        elif line[0].isnumeric():
            file_size, file_name = line.split()
            file_size = int(file_size)
            curr_dir.files.append(File(name=file_name, size=file_size, parent=curr_dir))
    root_dir.dir_size()
    return root_dir


def get_small_dirs_size(node, threshold=100_000):
    below_threshold = node.d_size <= threshold
    if not node.subdirs and below_threshold:
        return node.d_size
    elif node.subdirs and below_threshold:
        return node.d_size + sum([get_small_dirs_size(n) for n in node.subdirs])
    elif node.subdirs and not below_threshold:
        return sum([get_small_dirs_size(n) for n in node.subdirs])
    else:
        return 0


@benchmark
def small_dirs_size_wrapper(nd, th=100_000):
    return get_small_dirs_size(nd, threshold=th)


def get_sizes_list(root_node):
    sizes = [root_node.d_size]
    if root_node.subdirs:
        for node in root_node.subdirs:
            sizes += get_sizes_list(node)
    return sizes


@benchmark
def get_best_dir_to_del(root_node, available_disk, needed_disk):
    dir_sizes = get_sizes_list(root_node)
    unused = available_disk - dir_sizes[0]
    needed = abs(needed_disk - unused)
    best_solution = min(filter(lambda x: x > needed, dir_sizes[:-1]))
    return best_solution


AVAILABLE_DISK = 70_000_000
NEEDED_DISK = 30_000_000
data = get_input()
root_node = build_tree(data)

print(f"Part 1: {small_dirs_size_wrapper(nd=root_node)}")
print(f"Part 2: {get_best_dir_to_del(root_node, AVAILABLE_DISK, NEEDED_DISK)}")
