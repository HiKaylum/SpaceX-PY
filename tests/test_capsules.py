from spacex_py import capsules

def get_capsules():
    got_capsules, _ = capsules.get_capsules()
    return got_capsules

def get_capsule_parts():
    got_capsule_parts, _ = capsules.get_capsule_parts()
    return got_capsule_parts

def get_capsule_part_by_serial():
    got_capsule_part, _ = capsules.get_capsule_parts("C201")
    return got_capsule_part

def get_capsule_part_by_query():
    got_capsule_parts, _ = capsules.get_capsule_parts(status="active")
    return got_capsule_parts

def test_get_capsules():
    assert type(get_capsules()) is list

def test_get_capsule_parts():
    assert type(get_capsule_parts()) is list

def test_get_capsule_part_by_serial():
    assert type(get_capsule_part_by_serial()) is dict

def test_get_capsule_part_by_query():
    assert type(get_capsule_part_by_query()) is list