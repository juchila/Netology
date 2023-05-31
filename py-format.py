#! /usr/bin/env python3

import os, sys, json, yaml, re, magic

mime = magic.Magic(mime=True)

file_f=sys.argv[1]
fn=os.path.splitext(file_f)[0]
ext=os.path.splitext(file_f)[1]
some_dict = {}
print("file "+fn+" ext  "+ext+"\nmagic type "+magic.from_file(file_f, mime=False))
with open(file_f, 'r') as f:
    if ext==".json":
        try:
            some_dict = json.load(f)
            print("format is JSON")
            with open(fn+".yml",'w') as f:
                f.write(yaml.dump(some_dict, explicit_start=True, explicit_end=True))
        except json.JSONDecodeError as e:
                print(e)
#                print("File "+file_f+" is not JSON or YAML or file have a mistake")
    elif re.match('(\.yaml|\.yml)',ext):
        try:
            some_dict = yaml.safe_load(f)
            print("format is YAML")
            with open(fn+".json",'w') as f:
                f.write(json.dumps(some_dict))
        except yaml.YAMLError as e:
            print(e)
#            print("File "+file_f+" is not YAML or JSON or file have a mistake")

    else:
        print("Not right extension")
