# A data set for fall detection with smart floor sensors

Data can be downloaded as a zipped archive (FallData.tar.gz, ~330MB):
- [link 1](https://plmbox.math.cnrs.fr/f/a05ad8fbe7674392962b/?dl=1)

Alternatively, running in a terminal

> python download_data.py

automatically downloads and extracts the data. This code requires Python 3 and `tqdm` (`pip install tqdm`).

Once extracted, the data can be read using the following code snippets (in Python, R). Be sure to execute those lines while in the same directory as the extracted `FallData` folder.

#### Python

Signals are loaded into Numpy arrays. Please be sure to have it installed (`pip install numpy`), as well as `tqdm` (`pip install tqdm`).

```python
from load_data import get_code_list, load_signal, load_metadata


# Load and manipulate all signals and metadata.
all_codes = get_code_list()
print("There are {} trials.".format(len(all_codes)))
for code in all_codes:
    signal = load_signal(code)  # numpy array (n_samples, n_dims)
    metadata = load_metadata(code)  # dictionary
    # Do something.
    # ...
```

#### R

Be sure to set the working directory (with the function `setwd`) to wherever the data file has been unzipped. To read JSON files, the package `jsonlite` must be installed.

```R
library("jsonlite")
code_list <- fromJSON("code_list.json")

for(code in code_list){
    if (startsWith(code, "u-")){
        filename <- paste("FallData/Unconstrained/", code, sep="")
    }
    if (startsWith(code, "c-")){
        filename <- paste("FallData/Controlled/", code, sep="")
    }
    signal <- read.csv(paste(filename, ".csv", sep=""))
    metadata <- fromJSON(paste(filename, ".json", sep=""))
    # Do something.
    # ...
}

```
