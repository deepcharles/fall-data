import os
import tarfile
from pathlib import Path
from urllib.request import urlretrieve

from tqdm.auto import tqdm

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


if __name__ == "__main__":
    download_data()
