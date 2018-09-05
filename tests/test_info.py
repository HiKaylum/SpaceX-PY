from spacex_py import info

def get_company_info():
    got_info, _ = info.get_company_info()
    return got_info

def get_company_history_info():
    got_info, _ = info.get_company_history_info()
    return got_info

def get_roadster_info():
    got_info, _ = info.get_roadster_info()
    return got_info

def test_get_company_info():
    assert type(get_company_info()) is dict

def test_get_company_history_info():
    assert type(get_company_history_info()) is list

def test_get_roadster_info():
    assert type(get_roadster_info()) is dict