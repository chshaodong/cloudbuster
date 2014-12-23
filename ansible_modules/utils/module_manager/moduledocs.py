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

BLACKLIST_EXTS = ('.pyc', '.swp', '.bak', '~', '.rpm', '.ps1')
IGNORE_FILES = [ "COPYING", "CONTRIBUTING", "LICENSE", "README", "async_wrapper.py" ]

_ITALIC = re.compile(r"I\(([^)]+)\)")
_BOLD   = re.compile(r"B\(([^)]+)\)")
_MODULE = re.compile(r"M\(([^)]+)\)")
_URL    = re.compile(r"U\(([^)]+)\)")
_CONST  = re.compile(r"C\(([^)]+)\)")

# Here, we're using ansible.modules, but we could use this for any python package by overriding this.
package = 'ansible.modules'

# We import the package, get it's full path, and set it in PACKAGE_PATH var.
m = __import__(package)
parts = package.split('.')[1:]
PACKAGE_PATH = os.path.join(os.path.dirname(m.__file__), *parts)

def strip_doc_formatting(text):

    t = _ITALIC.sub(r"\1", text)    # I(word) => `word'
    t = _BOLD.sub(r"\1", t)         # B(word) => *word*
    t = _MODULE.sub(r"\1", t)       # M(word) => [word]
    t = _URL.sub(r"\1", t)          # U(word) => word
    t = _CONST.sub(r"\1", t)        # C(word) => `word'

    return t

def unformat(value):
    if isinstance(value, basestring):
        return strip_doc_formatting(value)
    elif isinstance(value, list):
        newlist = []
        for x in value:
            newlist.append(unformat(x))
        return newlist
    elif isinstance(value,dict):     
        newdict = {}
        for k, v in value.iteritems():
            newdict[k] = unformat(v)
        return newdict


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
        options = []
        for (k,v) in doc['options'].iteritems():
            all_keys.append(k)
            option = {'name':k} 
            for key, value in v.iteritems():
                if key == 'description':
                    value = ''.join(value)
                if key == 'required':
                    if value == True:
                        value = 'yes'
                    else:
                        value = 'no'
                params = {key: value}
                option.update(params)
            if 'required' not in option.keys():
                option['required'] = 'no'
            options.append(option)
        doc['options'] = options
        doc['description'] = str('\n'.join(doc['description']))
        doc['option_keys'] = all_keys
        doc['filename'] = filename
        doc['module_path'] = '%s/%s' % (os.path.split(re.sub('^%s' % PACKAGE_PATH, '', filename))[0], doc['module']) 
        doc['docuri'] = doc['module'].replace('_', '-')
    else:
        sys.stderr.write("ERROR: module %s missing documentation (or could not parse documentation)\n" % module)
    return unformat(doc)


def filter_modules(files_list):
    '''
    Takes a list of files and returns a list of python modules (python files) with the extension removed.
    '''
    module_list = []
    for module in list(set(files_list)):
        basename = os.path.basename(module)
        if basename.startswith('.'):
            continue
        elif any(basename.endswith(x) for x in BLACKLIST_EXTS):
            continue
        elif basename.startswith('__'):
            continue
        elif basename in IGNORE_FILES:
            continue
        elif basename.startswith('_'):
            continue
        module_list.append(module)
    return list(set(module_list))

def get_all_module_docs():
    '''
    Returns a list of all module docs in dict form.
    '''
    results = []
    for root, dirs, files in os.walk(PACKAGE_PATH):
        if len(files) > 0:
            full_paths = []
            for file in files:
                full_paths.append(os.path.join(root, file))
            modules = filter_modules(full_paths)
            if len(modules) > 0:
               for module in list(set(modules)):
                   results.append(get_module_doc(module))
    return results

