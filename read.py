#!/bin/env python3

import argparse
import json
import time
import yaml


def get_options():
    parser = argparse.ArgumentParser(description='Read inventory.yml')
    parser.add_argument(
        '--refresh-rate', dest='refresh_rate', action='store', default=0,
        type=int, help='How often to refresh, (seconds).')

    options = parser.parse_args()
    return options


def main():
    inventory = None
    options = get_options()

    while not inventory or options.refresh_rate:
        with open('inventory.yml') as f:
            inventory = yaml.load(f)
        print(json.dumps(inventory, indent=2))
        time.sleep(options.refresh_rate)


if '__main__' == __name__:
    main()
