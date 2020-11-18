import os
import optparse
import zipfile

comp_file = zipfile.ZipFile('comp_file.zip','w')

f = open('fileone.txt','w+')
f.write('ONE FILE')
f.close()

f = open('filetwo.txt','w+')
f.write('TWO FILE')
f.close()