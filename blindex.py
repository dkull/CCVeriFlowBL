from CodernityDB.hash_index import HashIndex

class WithIPIndex(HashIndex):
    def __init__(self, *args, **kwargs):
        kwargs['key_format'] = '15s'
        super(WithIPIndex, self).__init__(*args, **kwargs)

    def make_key_value(self, data):
        a_val = data.get("ip")
        a_val = "%015s" % a_val
        if a_val is not None:
            return a_val, None
        return None

    def make_key(self, key):
        key = "%015s" % key
        return key

class WithDateIndex(HashIndex):
    def __init__(self, *args, **kwargs):
        kwargs['key_format'] = '10s'
        super(WithDateIndex, self).__init__(*args, **kwargs)

    def make_key_value(self, data):
        a_val = data.get("date")
        a_val = "%010s" % a_val
        if a_val is not None:
            return a_val, None
        return None

    def make_key(self, key):
        key = "%010s" % key
        return key

