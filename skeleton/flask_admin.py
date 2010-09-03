# -*- coding:utf-8 -*-
import os, re
import shutil, logging

# which folder are we in?
base_dir = os.path.abspath(os.path.dirname(__file__))

print base_dir

# match: startproject project_name[ in dir_path]
st_re = re.compile("^startproject (?P<name>[\w\-]+)(\sin\s(?P<path>.+))?$")

def parse_args(args):
    # make a string from commandline input so we can work with regex
    cline = " ".join(args)

    # starting a project?
    m = st_re.match(cline)
    if m is not None:
        groupdict = m.groupdict()
        p_name = groupdict['name']
        p_path = os.path.abspath(groupdict['path'] or '.')
        project_path = os.path.join(p_path, p_name)
        skeleton_dir = os.path.join(base_dir, "skeleton")
        shutil.copytree(skeleton_dir, project_path)
        logging.info("flask project created at %s" % project_path)
    else: print False

if __name__=="__main__":
    import sys
    parse_args(sys.argv[1:])
