from sys import argv
from urllib3.util.url import parse_url
from pyperclip import paste
from path import Path,getcwdu
from sh import wget
import tarfile

target = ''
try:
    if len(argv) == 2:
        target = argv[1]
    else:
        target = paste()
except Exception:
    print('no arguments or clipboard contents')
if not Path(target).exists():
    wget(target, O='temporary_tar')
    maybeU = parse_url(target)
    maybeF = maybeU.path.split('/')[-1]
    targetF = getcwdu() + '/' + maybeF.split('.')[0]
else:
    Path(target).move('temporary_tar')
    targetF = target.split('/')[-1]
    targetF = getcwdu() + '/' + targetF.split('.')[0]
with tarfile.open('temporary_tar') as tf:
    tf.extractall()
Path('temporary_tar').remove()
print(Path(targetF), end='')
