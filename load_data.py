import json
import os
import tarfile
from pathlib import Path
from urllib.request import urlretrieve

import numpy as np
import pandas as pd
from tqdm.auto import tqdm

from code_list import CODE_LIST

DATA_HOME = Path.cwd() / Path("FallData")
DOWNLOAD_URL = "https://plmbox.math.cnrs.fr/f/a05ad8fbe7674392962b/?dl=1"
ARCHIVE_FNAME = "FallData.tar.gz"


class TqdmUpTo(tqdm):
    """Class-based progress bar.

    Provides `update_to(n)` which uses `tqdm.update(delta_n)`.
    Inspired by [twine#242](https://github.com/pypa/twine/pull/242),
    [here](https://github.com/pypa/twine/commit/42e55e06).
    """

    def update_to(self, b=1, bsize=1, tsize=None):
        """
        b  : int, optional
            Number of blocks transferred so far [default: 1].
        bsize  : int, optional
            Size of each block (in tqdm units) [default: 1].
        tsize  : int, optional
            Total size (in tqdm units). If [default: None] remains unchanged.
        """
        if tsize is not None:
            self.total = tsize
        return self.update(b * bsize - self.n)  # also sets self.n = b * bsize


def download_data() -> None:
    """Download the data, extract them and remove the archive."""
    if DATA_HOME.exists():
        print(f"Data already exist ({DATA_HOME}).")
    else:
        print("Data are missing. Downloading them now...", end="", flush=True)
        with TqdmUpTo(
            unit="M",
            unit_scale=True,
            unit_divisor=1024,
            miniters=1,
            desc=ARCHIVE_FNAME,
        ) as t:
            urlretrieve(
                url=DOWNLOAD_URL,
                filename=ARCHIVE_FNAME,
                reporthook=t.update_to,
                data=None,
            )
            t.total = t.n

        print("Ok.")
        print("Extracting now...", end="", flush=True)
        tf = tarfile.open(ARCHIVE_FNAME)
        tf.extractall()
        print("Ok.")
        print("Removing the archive...", end="", flush=True)
        os.remove(ARCHIVE_FNAME)
        print("Ok.")


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
    download_data()
    all_codes = get_code_list()
    print("There are {} trials.".format(len(all_codes)))
    for code in all_codes:
        signal = load_signal(code)
        metadata = load_metadata(code)
        # Do something.
        # ...
