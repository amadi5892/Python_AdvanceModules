import shutil

shutil.unpack_archive('unzip_me_for_instructions.zip','','zip')

with open('extracted_content/Instructoins.txt') as f:
    content = f.read()
    print(content)