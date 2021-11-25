# A data set for fall detection with smart floor sensors


<!-- The data provided in this repository are described in the following article: -->
<!-- - Truong, C., Barrois-Müller, R., Moreau, T., Provost, C., Vienne-Jumeau, A., Moreau, A., Vidal, P.-P., Vayatis, N., Buffat, S., Yelnik, A., Ricard, D., & Oudre, L. (2019). A data set for the study of human locomotion with inertial measurements units. Image Processing On Line (IPOL), 9. [[abstract]](https://deepcharles.github.io/publication/ipol-data-2019) [[doi]](https://doi.org/10.5201/ipol.2019.265) [[pdf]](http://deepcharles.github.io/files/ipol-walk-data-2019.pdf) [[online demo]](http://ipolcore.ipol.im/demo/clientApp/demo.html?id=265) -->


<!-- Please cite this article whenever you want to make a reference to this data set. -->


<!-- A simple online exploration tool is available [online](http://ipolcore.ipol.im/demo/clientApp/demo.html?id=77777000084). -->
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
    signal <- read.csv(paste(code, ".csv", sep=""))
    metadata <- fromJSON(paste(code, ".json", sep=""))
    # Do something.
    # ...
}

```
