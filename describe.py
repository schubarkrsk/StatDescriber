import pandas
from pathlib import Path
from os import listdir
from os.path import isfile, join

import pandas as pd

OUTPUT_PATH = Path(Path.cwd(), "reports")
INPUT_PATH = Path(Path.cwd(), "input")

pd.options.display.max_rows
pd.set_option('display.max_columns', None)


def get_csv_files():
    files = [f for f in listdir(INPUT_PATH) if isfile(join(INPUT_PATH, f))]
    return files


def get_full_path(files):
    for cur_file in range(len(files)):
        files[cur_file] = Path(INPUT_PATH, files[cur_file])
    return files


def pd_dateset(file):
    dataset = pandas.read_csv(file, sep=';')
    return dataset


def describer(dataset=None):
    if dataset is None:
        dataset = pd_dateset(file)
    return dataset.describe()


def write_to_file(filename, file, data):
    f = open(Path(OUTPUT_PATH, f"{filename}.txt"), "w")
    f.write(f"{file}\n{data}")


if __name__ == "__main__":
    CSV_FILES = get_csv_files()
    CSV_FILE_PATHS = get_full_path(CSV_FILES)
    iter = 1
    for file in CSV_FILE_PATHS:
        dataset = pd_dateset(file)
        stat_describe = describer(dataset)
        write_to_file(iter, file, stat_describe)
        iter += 1
