from dataclasses import dataclass, field


def read_file(filename: str) -> str:
    with open(filename, "r") as f:
        raw = f.read()
    return raw


def write_file(filename: str, data: str):
    with open(filename, "w") as f:
        f.write(data)


@dataclass
class File:
    name: str
    size: int


@dataclass
class Directory:
    name: str
    files: list[File] = field(default_factory=list)
    children: list["Directory"] = field(default_factory=list)
    parent: "Directory" = None

    @property
    def size(self):
        return sum(file.size for file in self.files) + sum(directory.size for directory in self.children)

    def add_directory(self, new_directory: "Directory"):
        if new_directory.name in (directory.name for directory in self.children):
            raise Exception("Directory already exists")
        self.children.append(new_directory)

    def get_descendants(self) -> list["Directory"]:
        all_descendants = []
        if self.children:
            all_descendants.extend(self.children)
            for child in self.children:
                all_descendants.extend(child.get_descendants())
        return all_descendants


@dataclass
class FileSystem:
    cwd: Directory = None
    base_directory: Directory = Directory("/")

    @property
    def total_size(self) -> int:
        return self.base_directory.size

    def handle_input(self, lines: list[str]):
        while lines:
            next_line = lines.pop()
            if is_command(next_line):
                split_raw_command = next_line.split(" ")[1]
                if split_raw_command == "ls":
                    self.handle_ls(lines)
                elif split_raw_command == "cd":
                    self.handle_cd(next_line)
                else:
                    raise Exception("Invalid command")

    def handle_ls(self, lines: list[str]):
        while lines and not is_command(lines[-1]):
            next_line = lines.pop()
            if next_line[:3] == "dir":
                continue
            file_size, file_name = next_line.split(" ", 2)
            self.cwd.files.append(File(file_name, int(file_size)))

    def get_all_directories(self) -> list[Directory]:
        all_directories = [self.base_directory]
        all_directories.extend(self.base_directory.get_descendants())
        return all_directories

    def handle_cd(self, cd_command: str):
        param = cd_command.split(" ")[-1]
        if param == "/":
            self.cwd = self.base_directory
        elif param == "..":
            self.cwd = self.cwd.parent
        else:
            new_directory = Directory(param, parent=self.cwd)
            self.cwd.add_directory(new_directory)
            self.cwd = new_directory


def is_command(s):
    return s[0] == "$"


def main():
    raw_in = read_file("in.txt").split("\n")[::-1]
    file_system = FileSystem()
    file_system.handle_input(raw_in)
    all_directories = file_system.get_all_directories()
    directories_below_threshold = [directory for directory in all_directories if directory.size <= 100_000]
    size_of_directories_below_threshold = sum(directory.size for directory in directories_below_threshold)
    write_file("pt1.txt", str(size_of_directories_below_threshold))
    remaining_space = 70_000_000 - file_system.total_size
    space_to_delete = 30_000_000 - remaining_space
    potential_directories_to_delete = [directory for directory in all_directories if directory.size >= space_to_delete]
    directory_to_delete = min(potential_directories_to_delete, key=lambda directory: directory.size)
    write_file("pt2.txt", str(directory_to_delete.size))



if __name__ == "__main__":
    main()
