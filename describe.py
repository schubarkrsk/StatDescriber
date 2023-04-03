from pathlib import Path
from os import listdir
from os.path import isfile, join

from datetime import datetime

import pandas
import pandas as pd

OUTPUT_PATH = Path(Path.cwd(), "reports")
INPUT_PATH = Path(Path.cwd(), "input")

pd.options.display.max_rows
pd.set_option('display.max_columns', None)


def get_files(path):
    files = [f for f in listdir(path) if isfile(join(path, f))]
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
    fname = f"ReportN{filename}_date_{str(datetime.now().day)}_{str(datetime.now().month)}_{str(datetime.now().year)}.txt"
    f = open(Path(OUTPUT_PATH, fname), "w")
    str_of_data = f"{file}\n{data}"
    print(f"\n\n================================================="
          f"\n======SAVE AS \"{fname}\"======\n"
          f"file structure::\n")
    print(str_of_data)
    f.write(str_of_data)
    f.close()


if __name__ == "__main__":
    CSV_FILES = get_files(INPUT_PATH)
    CSV_FILE_PATHS = get_full_path(CSV_FILES)
    iter = len(get_files(OUTPUT_PATH))
    for file in CSV_FILE_PATHS:
        dataset = pd_dateset(file)
        stat_describe = describer(dataset)
        write_to_file(iter, file, stat_describe)
        iter += 1

    print("\n\n\nWe are finished!")
