# -*- coding: utf-8 -*-

import os.path as osp
import glob
from functools import reduce


def format_test_filename(fname):
    fname = osp.basename(fname).strip()
    if '.py' not in fname:
        fname = fname + '.py'
    return fname


def scan(dpath):
    paths = glob.glob(osp.join(dpath, 'test_*.py'))
    paths = [osp.basename(p) for p in paths]
    paths.sort()
    return paths


def read_conf_file(fpath):
    """reads a conf file removing blanks and comments (#') and returns a list
    of lines (without '\\n').
    """
    with open(fpath, 'rt') as f:
        rawlines = f.readlines()
        lines = [l.strip() for l in rawlines]
        lines = [l for l in lines if l != '']
        lines = [l for l in lines if l[0] != '#']

    return lines


def save_to_readme(lines, fpath):
    print('save file to {}'.format(fpath))
    lines = [l + '\n' for l in lines]

    with open(fpath, 'wt') as f:
        f.writelines(lines)


def read_comments(fpath):
    print('read comments from {}'.format(fpath))
    data = {}
    lines = read_conf_file(fpath)

    for line in lines:
        isplit = line.find(',')
        if isplit < 0:
            continue

        test_path = format_test_filename(line[0: isplit])
        comment = line[isplit+1:].strip()
        data[test_path] = comment

    for k, v in data.items():
        print('[{}][{}]'.format(k, v))

    return data


def read_updated(fpath):
    print('read updated from {}'.format(fpath))

    lines = read_conf_file(fpath)

    data = {}
    for line in lines:
        items = line.split(',')
        items = [item.strip() for item in items]

        test_path, *operators = items
        test_path = format_test_filename(test_path)

        operators = sorted(operators)

        data[test_path] = operators

    for k, v in data.items():
        print('[{}]{}'.format(k, v))

    return data


def compile_to_markdown_table(fnames, updated, comments):

    lines = []
    lines.append('')
    lines.append('|file|operator(s)|comment|')
    lines.append('|:-- |:---       |:----  |')

    for fname in fnames:
        try:
            ops = updated[fname]
            ops = reduce(lambda x, y: x + ' ' + y, ops, '')
            ops = ops.strip()
            updated_flag = True
        except KeyError:
            ops = '?'
            updated_flag = False

        try:
            com = comments[fname]
        except KeyError:
            com = ''

        line = '|{fname}|{ops}|{com}|'.format(
                fname=fname if not updated_flag else '__{}__'.format(fname),
                ops=ops,
                com=com,
                )

        lines.append(line)

    lines.append('')
    return lines


if __name__ == '__main__':

    script_dir = osp.dirname(__file__)
    try:
        with open(osp.join(script_dir, 'tests_directory.conf'), 'r') as f:
            tests_path = f.read().strip()
            tests_dir_needed = False
    except FileNotFoundError:
        with open(osp.join(script_dir, 'tests_directory.conf'), 'w') as f:
            pass
        tests_dir_needed = True

    if not tests_dir_needed:
        tests_path = osp.expanduser(tests_path)


        updated = read_updated(osp.join(script_dir, 'updated_files.conf'))
        comments = read_comments(osp.join(script_dir, 'comments.conf'))
        fnames = scan(tests_path)

        lines = compile_to_markdown_table(fnames, updated,  comments)

        save_to_readme(lines, osp.join(script_dir, 'README.md'))

