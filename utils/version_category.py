def get_version_category(version):
    if 1 <= version <= 9:
        return 0
    elif 10 <= version <= 26:
        return 1
    else:
        return 2
