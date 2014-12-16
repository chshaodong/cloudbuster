import os
import sys
import re
import datetime
import traceback
from ansible import utils
from ansible.utils import module_docs
import ansible.constants as C
from ansible.utils import version
import yaml
import anyjson
from collections import defaultdict 

MODULEDIR = C.DEFAULT_MODULE_PATH

BLACKLIST_EXTS = ('.pyc', '.swp', '.bak', '~', '.rpm')
IGNORE_FILES = [ "COPYING", "CONTRIBUTING", "LICENSE", "README", "async_wrapper.py" ]

# Here, we're using ansible.modules, but we could use this for any python package by overriding this.
package = 'ansible.modules'

# We import the package, get it's full path, and set it in PACKAGE_PATH var.
m = __import__(package)
parts = package.split('.')[1:]
PACKAGE_PATH = os.path.join(os.path.dirname(m.__file__), *parts)


def get_module_doc(module):
    '''
    Takes a module name and returns a dict made from the DOCSTRING of the module. We also add some useful fields.
    '''
    filename = utils.plugins.module_finder.find_plugin(module)
    if filename is None:
        pass
    if any(filename.endswith(x) for x in BLACKLIST_EXTS):
        pass
    try:
        doc, plainexamples = module_docs.get_docstring(filename)
    except:
        traceback.print_exc()
        sys.stderr.write("ERROR: module %s has a documentation error formatting or is missing documentation\n" % module)
        pass
    if doc is not None:

        all_keys = []
        for (k,v) in doc['options'].iteritems():
            all_keys.append(k)
        all_keys = sorted(all_keys)
        doc['option_keys'] = all_keys
        doc['filename'] = filename
        doc['module_path'] = '%s' % os.path.split(re.sub('^%s' % PACKAGE_PATH, '', filename))[0] 
        doc['docuri'] = doc['module'].replace('_', '-')
    else:
        sys.stderr.write("ERROR: module %s missing documentation (or could not parse documentation)\n" % module)
    return doc


def filter_modules(files_list):
    '''
    Takes a list of files and returns a list of python modules (python files) with the extension removed.
    '''
    module_list = []
    for module in files_list:
        if module.startswith('.'):
            continue
        elif any(module.endswith(x) for x in BLACKLIST_EXTS):
            continue
        elif module.startswith('__'):
            continue
        elif module in IGNORE_FILES:
            continue
        elif module.startswith('_'):
            continue
        module = os.path.splitext(module)[0] # removes the extension
        module_list.append(module)
    return module_list

def get_all_module_docs():
    '''
    Returns a list of all module docs in dict form.
    '''
    results = []
    for root, dirs, files in os.walk(PACKAGE_PATH):
        if len(files) > 0:
            modules = filter_modules(files)
            if len(modules) > 0:
               for module in modules:
                   results.append(get_module_doc(module))
    return results

