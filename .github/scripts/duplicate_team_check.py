import glob
import sys
import yaml

file_list = glob.glob('./*/*')


def yaml_load(path):
    try:
        with open(path) as file:
            obj = yaml.safe_load(file)
    except Exception as e:
        print(e, file=sys.stderr)
        sys.exit(1)
    return obj

for f in file_list:
    l = []
    obj = yaml_load(f)
    for _, v in obj.items():
        l.append(v)
    l = sum(l, [])
    dup = [x for x in set(l) if l.count(x) > 1]
    if dup:
        print(f'{dup} is duplicate in {f}')
        sys.exit(1)
