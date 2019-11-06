#!/usr/bin/env python3

import yaml, glob, math

files = glob.glob("recipes/*.yaml")
file_index = dict()

def read_recipes(filename):
    with open(filename, 'r') as stream:
        try:
            recipe = yaml.safe_load(stream)
            name = recipe.get('recipe_name')
            key = filename.split('/',1)[1][:1]
            if key in file_index:
                file_index[key].append({'file': filename, 'name': name})
            else:
                file_index[key] = [{'file': filename, 'name': name}]
        except yaml.YAMLError as exc:
            print(exc)

for file in files:
    read_recipes(file)

f = open('index.md', mode='w')
f.write('## Index\n')

for key, value in sorted(file_index.items()):
    f.write('## {}\n'.format(str(key).upper()))
    f.write('|||\n|-|-|\n')
    offset = math.ceil(len(value) / 2)
    i = 0
    while i in range(0, offset):
        first = value[i]
        if i + offset < len(value):
            second_name = value[i + offset].get('name')
            second_file = value[i + offset].get('file')
        else:
            second_name = ''
            second_file = ''
        f.write('| [{}]({}) | [{}]({}) |\n'.format(first.get('name'), first.get('file'), second_name, second_file))
        i = i + 1
f.close()