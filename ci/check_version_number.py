"""
On release, ensure that the release tag matches the InvenTree version number!
"""

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
import re
import os
import argparse

if __name__ == '__main__':

    here = os.path.abspath(os.path.dirname(__file__))

    version_file = os.path.join(here, '..', 'InvenTree', 'InvenTree', 'version.py')

    with open(version_file, 'r') as f:

        results = re.findall(r'INVENTREE_SW_VERSION = "(.*)"', f.read())

        if not len(results) == 1:
            print(f"Could not find INVENTREE_SW_VERSION in {version_file}")
            sys.exit(1)

        version = results[0]

    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--tag', help='Compare against specified version tag', action='store')
    parser.add_argument('-r', '--release', help='Check that this is a release version', action='store_true')
    parser.add_argument('-d', '--dev', help='Check that this is a development version', action='store_true')

    args = parser.parse_args()

    if args.dev:
        """
        Check that the current verrsion number matches the "development" format
        e.g. "0.5 dev"
        """

        pattern = "^\d+(\.\d+)+ dev$"

        result = re.match(pattern, version)

        if result is None:
            print(f"Version number '{version}' does not match required pattern for development branch")
            sys.exit(1)

    elif args.release:
        """
        Check that the current version number matches the "release" format
        e.g. "0.5.1"
        """

        pattern = "^\d+(\.\d+)+$"

        result = re.match(pattern, version)

        if result is None:
            print(f"Version number '{version}' does not match required pattern for stable branch")

    if args.tag:
        if not args.tag == version:
            print(f"Release tag '{args.tag}' does not match INVENTREE_SW_VERSION '{version}'")
            sys.exit(1)

sys.exit(0)