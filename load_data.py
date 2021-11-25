import json
from pathlib import Path

import numpy as np

from code_list import CODE_LIST
from download_data import DATA_HOME


def get_filename(code: str) -> Path:
    """Returns the filename of the signal file and the metadata file.

    Args:
        code (str): code of the trial ("c-id" or "u-id", where id=1,2,...).

    Returns:
        Path: filename
    """
    filename = DATA_HOME / code
    err_msg = f"The code {code} cannot be found in the data set."
    assert filename.with_suffix(".csv").exists(), err_msg
    return filename


def load_signal(code: str) -> np.ndarray:
    """Returns the signal of the trial.

    Args:
        code (str): code of the trial ("c-id" or "u-id", where id=1,2,...).

    Returns:
        ndarray: signal of the the trial, shape (n_samples, n_sensors), with
            n_sensors=8.
    """
    fname = get_filename(code=code)
    signal = np.loadtxt(fname=fname.with_suffix(".csv"), delimiter=",")
    return signal


def load_metadata(code: str) -> dict:
    """Returns the metadata of the trial.

    Args:
        code (str): code of the trial ("c-id" or "u-id", where id=1,2,...).

    Returns:
        dict: metadata dictionary.
    """
    fname = get_filename(code=code)
    with open(fname.with_suffix(".json"), "r") as f:
        metadata = json.load(f)
    return metadata


def get_code_list() -> list:
    """Returns the list of all available codes.

    Returns:
        list: list of codes.
    """
    return CODE_LIST


if __name__ == "__main__":
    all_codes = get_code_list()
    print("There are {} trials.".format(len(all_codes)))
    for code in all_codes:
        signal = load_signal(code)
        metadata = load_metadata(code)
        # Do something.
        # ...
