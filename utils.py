import os
import re
import glob
import shutil
import errno


def copy_dir(src, dest):
    """Copies the source dir files to dest"""
    if os.path.exists(dest):
        shutil.rmtree(dest)

    try:
        shutil.copytree(src, dest)
    except shutil.Error as err:
        print("Images folder not copied. Error: %s" % err)


def clean_dir(d, pattern):
    """ Deletes all files in the directory"""
    filelist = glob.glob(os.path.join(d, pattern))
    for f in filelist:
        os.remove(f)


def get_valid_filename(s):
    """
    Return the given string converted to a string that can be used for a clean
    filename. Remove leading and trailing spaces; convert other spaces to
    underscores; and remove anything that is not an alphanumeric, dash,
    underscore, or dot.

    Source Django Framework: https://github.com/django/django/blob/master/django/utils/text.py
    """

    s = str(s).strip().replace(" ", "_")
    return re.sub(r"(?u)[^-\w.]", "", s)
