from CodernityDB.hash_index import HashIndex

class WithPartyIndex(HashIndex):

    def __init__(self, *args, **kwargs):
        kwargs['key_format'] = '15s'
        super(WithPartyIndex, self).__init__(*args, **kwargs)

    def make_key_value(self, data):
        a_val = data.get("srcip")

        a_val = "%015s" % a_val

        if a_val is not None:
            return a_val, data
        return None

    def make_key(self, key):
        key = "%015s" % key
        return key
