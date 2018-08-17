from ._helpers._api import _get

def get_company_info():
    return _get("info")

def get_company_history_info():
    return _get("info/history")

def get_roadster_info():
    return _get("info/roadster")