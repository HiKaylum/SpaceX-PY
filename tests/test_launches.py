from spacex_py import launches

def get_launches():
    got_launches, _ = launches.get_launches()
    return got_launches

def get_launches_by_query():
    got_launches, _ = launches.get_launches(site_id="ksc_lc_39a")
    return got_launches

def get_past_launches():
    got_launches, _ = launches.get_past_launches()
    return got_launches

def get_past_launches_by_query():
    got_launches, _ = launches.get_past_launches(site_id="ksc_lc_39a")
    return got_launches

def get_latest_launch():
    got_launch, _ = launches.get_latest_launch()
    return got_launch

def get_next_launch():
    got_launch, _ = launches.get_next_launch()
    return got_launch

def get_upcoming_launches():
    got_launches, _ = launches.get_upcoming_launches()
    return got_launches

def get_upcoming_launches_by_query():
    got_launches, _ = launches.get_upcoming_launches(site_id="ksc_lc_39a")
    return got_launches

def test_get_launches():
    assert type(get_launches()) is list

def test_get_launches_by_query():
    assert type(get_launches_by_query()) is list

def test_get_past_launches():
    assert type(get_past_launches()) is list

def test_get_past_launches_by_query():
    assert type(get_launches_by_query()) is list

def test_get_latest_launch():
    assert type(get_latest_launch()) is dict

def test_get_next_launch():
    assert type(get_next_launch()) is dict

def test_get_upcoming_launches():
    assert type(get_upcoming_launches()) is list

def test_get_upcoming_launches_by_query():
    assert type(get_past_launches_by_query()) is list