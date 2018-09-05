<div align="center">

[![Build Status](https://travis-ci.org/HiKaylum/SpaceX-PY.svg?branch=master)](https://travis-ci.org/TheDigitalTaste/digitalt-cli)
[![GitHub issues](https://img.shields.io/github/issues/HiKaylum/SpaceX-PY.svg)](https://github.com/HiKaylum/SpaceX-PY/issues)
[![GitHub license](https://img.shields.io/github/license/HiKaylum/SpaceX-PY.svg)](https://github.com/HiKaylum/SpaceX-PY/blob/master/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/HiKaylum/SpaceX-PY.svg)](https://github.com/HiKaylum/SpaceX-PY/stargazers)

</div>

# SpaceX-PY
Python wrapper for the [SpaceX API](https://github.com/r-spacex/SpaceX-API)

## Install
```BASH
pip install spacex-py
```

## Usage
This wrapper matches the [SpaceX API](https://github.com/r-spacex/SpaceX-API) so its pretty easy to use. Lets go through some examples;

```PYTHON
from spacex_py import launches

# Returns a tuple
got_launches, header = launches.get_launches()

# PyLint being a pain about header? use:
got_launches, _ = launches.get_launches()

print(got_launches)
# Prints list: of launches
```

Okay well, lets get launches using a query;

```PYTHON
from spacex_py import launches

got_launches, _ = launches.get_launches(site_id="ksc_lc_39a")

print(got_launches)
# Prints the launhces for the given site
```
