from spacex_py import launchpads

def get_launchpads():
    got_launchpads, _ = launchpads.get_launchpads()
    return got_launchpads

def get_launchpad_by_method():
    got_launchpad, _ = launchpads.get_launchpads('ksc_lc_39a')
    return got_launchpad

def test_get_launchpads():
    assert type(get_launchpads()) is list

def test_get_launchpad_by_method():
    assert type(get_launchpad_by_method()) is dict