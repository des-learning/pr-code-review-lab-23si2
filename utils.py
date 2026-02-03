def is_empty(value):
    return not value or (isinstance(value, str) and value.strip() == "")
