#
#
#           .        .--.   _..._
#         .'|        |__| .'     '.   .--./)
#     .| <  |        .--..   .-.   . /.''\\
#   .' |_ | |        |  ||  '   '  || |  | |
# .'     || | .'''-. |  ||  |   |  | \`-' /
#'--.  .-'| |/.'''. \|  ||  |   |  | /("'`
#   |  |  |  /    | ||  ||  |   |  | \ '---.
#   |  |  | |     | ||__||  |   |  |  /'""'.\
#   |  '.'| |     | |    |  |   |  | ||     ||
#   |   / | '.    | '.   |  |   |  | \'. __//
#   `'-'  '---'   '---'  '--'   '--'  `'---'
#"thing" database - github/itslukej
try:
    import anydbm
except ImportError:
    import dbm as anydbm
try:
    from UserDict import DictMixin
except ImportError:
    from collections import MutableMapping as DictMixin
try:
    import cPickle as pickle
except ImportError:
    import pickle
try:
    from StringIO import StringIO as BytesIO
except ImportError:
    from io import BytesIO
import sys

class _ClosedDict(DictMixin):
    """Returns ValueError when trying to get/set/del item"""

    def closed(self, *args):
        raise ValueError('invalid operation on closed thing')
    __len__ = __getitem__ = __setitem__ = __delitem__ = __iter__ = keys = closed

    def __repr__(self):
        return '<Closed Dictionary>'

class _Wrapper(DictMixin):
    """Main wrapper for thingdb"""
    def __init__(self, dict):
        self.dict = dict
        self.cache={}
    def keys(self):
        return self.dict.keys()
    def has_key(self, key):
        return key in self.dict
    def __getitem__(self, key):
        try:
            value = self.cache[key]
        except KeyError:
            value = self.dict[key]
        return pickle.Unpickler(BytesIO(value)).load()
    def __setitem__(self, key, value):
        f = BytesIO()
        p = pickle.Pickler(f)
        p.dump(value)
        self.cache[key] = f.getvalue()
    def __delitem__(self, key):
        try:
            del self.dict[key]
        except KeyError:
            del self.cache[key]
    def __contains__(self, key):
        return key in self.dict
    def __len__(self):
        return len(self.dict)
    def __iter__(self):
        for k in self.dict.keys():
            return k,pickle.Unpickler(BytesIO(self.dict[k])).load()
    
class _DB(_Wrapper):
    def __init__(self, filename, flag="c"):
        database = anydbm.open(filename, flag)
        self.filename=filename
        self.flags = flag
        _Wrapper.__init__(self, database)
    def sync(self):
        for key, entry in self.cache.items():
            self.dict[key] = entry
        if hasattr(self.dict, 'save'):
            self.dict.save()
    def close(self):
        self.sync()
        self.dict.close()
        self.dict = _ClosedDict()
    def __repr__(self):
        return "thingDB({0})".format(self.filename)
        
        
def thing(filename, flag="c"):
    return _DB(filename, flag)
