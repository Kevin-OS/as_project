from subprocess import call
from glob import glob

call('bash feed_export_script.sh')

filenames = glob('*.csv')
print(filenames)