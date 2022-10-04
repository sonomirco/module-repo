import yaml
import re
import argparse
import json 
import ast

# https://www.thecodeforest.io/post/2022-01-04-automate-github-actions/automate-github-actions/
def read_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create player id dataframe")
    # this is the way of parsig a list of elements.
    # parser.add_argument("--modules", nargs="+", default=["Dyn-Module", "Gh-Module"], help="modules listed in an array")
    # we will parse the list as a string.
    parser.add_argument("--modules", type=str, help="modules listed in an array as a string")
    
    args = parser.parse_args()
    return args

def bump_versions():
    args = read_args()
    inputs = ast.literal_eval(args.modules)
    print(f"inputs -> {inputs}")
    bumped_versions = {}

    with open('versions.yaml', 'r') as file:
        prime_service = yaml.safe_load(file)

        for input in inputs:
            split_path = input.split('-') 
            version = prime_service[split_path[0]][split_path[1]]
            print(version)
            if 'alpha' in version:
                old_num = re.search('alpha[.]*(\d+)', version)[1]
                bump_num = int(old_num)+1
                new_version = re.sub('alpha.*\d+', f'alpha.{bump_num}', version)
                bumped_versions[input]=new_version
            else:
                new_version = version + '-alpha.0'
                bumped_versions[input]=new_version
    json_object = json.dumps(bumped_versions) 
    print(json_object)
    print(f"::set-output name=module_bumped::{json_object}")

if __name__ == "__main__":
    bump_versions()
