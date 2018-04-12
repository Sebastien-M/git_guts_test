import subprocess
import os


def write_git_object(content):
    print '-------new git object------'
    os.system("echo '{}' | git hash-object -w --stdin".format(content))


def get_git_objects():
    proc = subprocess.Popen('find .git/objects -type f', stdout=subprocess.PIPE, shell=True)
    out = proc.stdout.readlines()
    objects = []
    for line in out:
        git_hash = line[-42:-1]
        git_hash = git_hash.replace('/', '')
        objects.append(git_hash)
    return objects


def get_content(hash):
    proc = subprocess.Popen('git cat-file -p {}'.format(hash), stdout=subprocess.PIPE, shell=True)
    out = proc.stdout.readlines()
    return out


def get_type(hash):
    proc = subprocess.Popen('git cat-file -t {}'.format(hash), stdout=subprocess.PIPE, shell=True)
    out = proc.stdout.readlines()
    return out[0][:-1]


def get_full_desc():
    git_objects = get_git_objects()
    print '--------git objects--------'
    for object in git_objects:
        print object
        print 'Type: {}'.format(get_type(object))
        print 'Content: {}'.format(get_content(object))
        print('-------')


def log():
    git_objects = get_git_objects()
    for object in git_objects:
        object_type = get_type(object)
        if object_type != 'blob' and object_type != 'tree':
            object_content = get_content(object)
            print '-----------------------'
            print '{} {}'.format(object_type, object)
            print object_content[1][:-1]
            print '-----------------------'

log()