#!/usr/bin/env python

####
# Generates article index
####

import os
import json
import frontmatter

# local path to article files
local_path: str = './'
# remote path to article files
remote: str = 'https://raw.githubusercontent.com/sjsadowski/builders-journey/main'
# files to exclude from index
exclusions: list = ['template.md', 'README.md']

# set up type-hinted variables
# f used for files in comprehension
# mdfiles used for list of files returned by list comprehension
# mdfile used for individual files
f: str
mdfile: str
mdfiles: list

# list comprehension to get article files and exclude files in the list defined above
mdfiles = [f for f in os.listdir(local_path)
           if os.path.isfile(os.path.join(local_path, f))
           and f.endswith('.md')
           and f not in exclusions]

# sort list of files by file name
mdfiles = sorted(mdfiles)

# iterate through files and augment with remote
for mdfile in mdfiles:
    fm: object = frontmatter.load(mdfile)
    fm_dict = fm.to_dict()
    # we don't want to capture content for the index, that's for later
    del fm_dict['content']
    fm_dict['remote_file'] = remote + '/' + mdfile
    print(json.dumps(fm_dict, indent=2))


