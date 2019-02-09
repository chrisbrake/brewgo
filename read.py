#!/bin/env python3

import json
import yaml


def main():
    with open('inventory.yml') as f:
        print(json.dumps(yaml.load(f), indent=2))


if '__main__' == __name__:
    main()
