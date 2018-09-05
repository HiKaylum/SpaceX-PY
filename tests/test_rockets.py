from spacex_py import rockets

def get_rockets():
    got_rockets, _ = rockets.get_rockets()
    return got_rockets

def get_rockets_by_method():
    got_rockets, _ = rockets.get_rockets('bfr')
    return got_rockets

def test_get_rockets():
    assert type(get_rockets()) is list

def test_get_rockets_by_method():
    assert type(get_rockets_by_method()) is dict