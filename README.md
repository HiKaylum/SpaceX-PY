<h1 align="center">
SpaceX-PY
</h1>

<div align="center">

[![Build Status](https://travis-ci.org/HiKaylum/SpaceX-PY.svg?branch=master)](https://travis-ci.org/TheDigitalTaste/digitalt-cli)
[![GitHub issues](https://img.shields.io/github/issues/HiKaylum/SpaceX-PY.svg)](https://github.com/HiKaylum/SpaceX-PY/issues)
[![GitHub license](https://img.shields.io/github/license/HiKaylum/SpaceX-PY.svg)](https://github.com/HiKaylum/SpaceX-PY/blob/master/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/HiKaylum/SpaceX-PY.svg)](https://github.com/HiKaylum/SpaceX-PY/stargazers)

</div>

## About
Python wrapper for the unofficial SpaceX REST API. All information on such can be found [here](https://github.com/r-spacex/SpaceX-API). Used for retrieving information about:

* Capsules
* Cores
* Launches
* Launchpads
* Rockets
* Miscellaneous data


## Installation
Command to install the package into your environment:
```BASH
pip install spacex-py
```

## Usage
Documentation for all queries can be found in their respective source files.
This wrapper matches the [SpaceX API](https://github.com/r-spacex/SpaceX-API), allowing for ease uf use. Let's go through some examples:

```PYTHON
from spacex_py import launches

# Returns a tuple
got_launches, header = launches.get_launches()

# PyLint being a pain about header? use the following:
got_launches, _ = launches.get_launches()

# Prints a list of launches
print(got_launches)
```

Now let's get launches using a query:

```PYTHON
from spacex_py import launches

#Queries launches using the specific site id
got_launches, _ = launches.get_launches(site_id="ksc_lc_39a")

#Example query using multiple parameters
got_launches, _ = launches.get_launches(site_id="ksc_lc_39a", payload_type='Satellite')

#Prints a list of launches fitting the above parameters
print(got_launches)
```

## License
This project uses the [MIT License](https://opensource.org/licenses/MIT).
More information can be found in [LICENSE](https://github.com/HiKaylum/SpaceX-PY/blob/master/LICENSE).

