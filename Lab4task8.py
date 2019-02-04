import os
import hashlib
def walk(dirname):
    names = []
    if '__pycache__'in dirname:
        return names
    for name in os.listdir(dirname):
          path = os.path.join(dirname, name)
          if os.path.isfile(path):
            names.append(path)
          else:
            names.extend(walk(path))
    return names

def filter_paths_file_extension(paths, file_extension):
    file_extension = file_extension.lower()
    result = []
    for path in paths:
      if path.lower().endswith(file_extension):
        result.append(path)

    return result
def compute_checksum(paths):
    checksum_paths = {}
    for path in paths:
        with open(path, "rb") as file:
            file_contents = file.read()
            checksum = hashlib.md5(file_contents).hexdigest()
            if checksum in checksum_paths:
                checksum_paths[checksum].append(path)
            else:
                checksum_paths[checksum] = [path]
    return checksum_paths

def check_duplicates(dir, file_extension):
    paths = walk(dir)
    paths = filter_paths_file_extension(paths, file_extension)
    checksums = compute_checksum(paths)
    for _, files in checksums.items():
        if len(files) > 1:
            for file in files[:-1]:
                print(file, end=', ')
            print(files[-1])

if __name__ == "__main__":
    check_duplicates()

