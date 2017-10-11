# osx-photos-export-renamer
Utility for renaming OSX Photos export folders from moment name to a format where alphabetical sorting equals soring by date (YYYY-MM-DD, location). 

### Usage

```python rename.py <diretory>```, where ```<directory>``` contains all the exported moments from photos.

```
usage: rename.py [-h] directory

Rename OSX Photos export directory from moment name to have date in the front.

positional arguments:
  directory   The root directory of the exported Photos moments

optional arguments:
  -h, --help  show this help message and exit
```
### Disclaimer
This utility has only been tested with export directories only containing the exported images, each within its own folder named after the "moment".

### Example 

The following table shows example renames. FROM has the original directory name (moment name), TO has the result of the rename (date and alhbabetical sort is the same)

| FROM                                              | TO                                           |
|---------------------------------------------------|----------------------------------------------|
| Chicago - Edison Park - Illinois, October 1, 2017 | 2017-10-01, Chicago - Edison Park - Illinois |
| October 4, 2017                                   | 2017-10-04                                   |

