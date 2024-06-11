# builders-journey

## posts
### creating a post
copy the ```template.md``` file to a new file using the naming convention below

### naming convention
Filenames should follow the pattern YYYY-MM-DD-Number-Underscore_Replaced_Short_Title

### front matter

#### keys
**\*** indicates a required non-blank key in the front matter

- title: \* the title to be displayed
- slug: \* the slug that's used to view a single article like https://<site>/article/<slug>
- description: description of the article
- author: \*
- type: [post, page] page is currently unused
- date: \* required, ISO format, ex: '2024-01-01T01:59:00.000-0000'
- revisions: \* yaml list of revisions
- draft: \* [true, false] display status
- tags: yaml list of tags
- preview: short excerpt
- category: \* [tech, business, etc]


## generating the index

### prerequisites
1. Install pdm dependencies/create virt-env
2. run ```pdm run ./genindex.py```