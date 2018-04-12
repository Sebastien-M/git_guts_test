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


def get_desc(hash):
    proc = subprocess.Popen('git cat-file -p {}'.format(hash), stdout=subprocess.PIPE, shell=True)
    out = proc.stdout.readlines()
    print('Content: {}'.format(out))


def get_type(hash):
    proc = subprocess.Popen('git cat-file -t {}'.format(hash), stdout=subprocess.PIPE, shell=True)
    out = proc.stdout.readlines()
    print('Type: {}'.format(out[0][:-1]))


# write_git_object('test3')
git_objects = get_git_objects()
print '--------git objects--------'
for object in git_objects:
    print object
    get_type(object)
    get_desc(object)
    print('-------')
