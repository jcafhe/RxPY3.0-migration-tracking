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

    data = {}
    lines = read_conf_file(fpath)

    for line in lines:
        isplit = line.find(',')
        if isplit < 0:
            continue

        test_path = format_test_filename(line[0: isplit])
        comment = line[isplit+1:].strip()
        data[test_path] = comment

    return data


def read_updated(fpath):

    lines = read_conf_file(fpath)

    data = {}
    for line in lines:
        items = line.split(',')
        items = [item.strip() for item in items]

        test_path, updated, *operators = items
        test_path = format_test_filename(test_path)
        if updated.lower() == 'false':
            updated = False
        elif updated.lower() == 'true':
            updated = True
        else:
            raise ValueError('unable to determine status True or False for '
                             '{} in file {} Got "{}"'.format(
                                     test_path, fpath, updated)
                             )

        operators = sorted(operators)

        d = {'updated': updated, 'operators': operators}
        data[test_path] = d

    return data


def compile_to_markdown_table(fnames, updates, comments):

    lines = []
    lines.append('')
    lines.append('|file|operator(s)|comment|')
    lines.append('|:-- |:---       |:----  |')

    for fname in fnames:
        try:
            ops = updates[fname]['operators']
            ops = reduce(lambda x, y: x + ' ' + y, ops, '')
            ops = ops.strip()
        except KeyError:
            ops = '?'

        try:
            com = comments[fname]
        except KeyError:
            com = ''

        try:
            updated = updates[fname]['updated']
            fname_text = '{}'.format(fname)
            if updated:
                fname_text = '__{}__'.format(fname)

        except KeyError:
            fname_text = '_{}_'.format(fname)

        line = '|{fname}|{ops}|{com}|'.format(
                fname=fname_text,
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

        updates = read_updated(osp.join(script_dir, 'updated_files.conf'))

        print('\nreading updated_files\n')
        for k, v in updates.items():
            print('[{}][{}] {}'.format(k,v['updated'], v['operators']))

        print('\nreading comments\n')
        comments = read_comments(osp.join(script_dir, 'comments.conf'))
        for k, v in comments.items():
            print('[{}][{}]'.format(k, v))


        print('\nscanning {}'.format(tests_path))
        fnames = scan(tests_path)
        print('{} test files discovered'.format(len(fnames)))

        print('\ncompile document')
        lines = compile_to_markdown_table(fnames, updates,  comments)

        print('\nsaving document')
        save_to_readme(lines, osp.join(script_dir, 'README.md'))

