#! /usr/bin/env python3

import json, yaml, os, socket, pprint

with open('json.json', 'r') as js:
    some_dict = json.load(js)
print(some_dict)

hosts=["drive.google.com","mail.google.com","google.com"]
file_js="oldip.json"
file_yml="oldip.yaml"
file_js="oldip2.json"
file_yml="oldip2.yaml"
str1 = {}
rewr = False
if os.path.exists(file_js):
    with open(file_js, 'r') as f:
        oldip = f.read()
    print("Прошлые значения "+oldip)
    oldip=json.loads(oldip)
else:
    oldip = {}
print("Новые значения:")
for h in hosts:
#    host=socket.gethostbyname(h)
    host=socket.gethostbyname_ex(h)
    str0 = h+" - "+str(host[2])
#    str0 = h+" - "+host
    str1[h] = host
    print(str0)
    if len(oldip)>0:
#        if oldip.get(h)!=host:
         dfr=list(set(oldip[h][2]) ^ set(host[2]))
         print("[info] "+h+" different IP: "+str(dfr))
         if len(dfr)>0:
            print("[ERROR] "+h+" IP mismatch: "+str(dfr))
#            print("[ERROR] "+h+" IP mismatch: "+host)
            rewr = True
    else:
        rewr = True
    if rewr:
        with open(file_js, 'w') as f:
            f.write(json.dumps(str1))
        with open(file_yml, 'w') as f:
            f.write(yaml.dump(str1, explicit_start=True, explicit_end=True))
#            yaml.dump(str1,f)
print(yaml.dump(str1))

def tuple_constructor(loader, node):
    # Load the sequence of values from the YAML node
    values = loader.construct_sequence(node)
    # Return a tuple constructed from the sequence
    return tuple(values)
# Register the constructor with PyYAML
yaml.SafeLoader.add_constructor('tag:yaml.org,2002:python/tuple', tuple_constructor)
with open(file_yml,'r') as f:
    print(yaml.safe_load(f))

