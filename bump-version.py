import yaml
import re
import argparse
import json 

def bump_versions():
    print(f"::set-output name=module_bumped::Hello")

if __name__ == "__main__":
    bump_versions()
