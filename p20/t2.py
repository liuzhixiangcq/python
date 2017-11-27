# @author page
# @date 2017/11/27
# coding:utf-8
#!/usr/bin/python

import shutil
import os

#shutil.make_archive('t2_dir','zip',base_dir = 't2_dir')
#os.system('rm -r t2_dir')
#os.system('ls -al')
shutil.unpack_archive('t2_dir.zip')
