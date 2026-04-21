import yaml

def load_yaml(path):
    o = open(path,encoding="utf-8")
    r = o.read()

    data =yaml.safe_load(r)

    return data