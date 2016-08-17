
class WithableDict(dict):
    def __enter__(self):
        self._context_withable = {}
        for k, v in self.items():
            print globals()
            if k in globals():
                self._context_withable[k] = globals()[k]
            exec('global {0};{0} = {1}'.format(k, v))
    
    def __exit__(self, exc_type, exc_value, traceback):
        for k, v in locals().items():
            self[k] = v
        for k, v in self._context_withable.items():
            exec('global {0};{0} = {1}'.format(k, v))

if __name__ == '__main__':
    wd = WithableDict({
        'a': 100
    })
    a = 1000
    with wd:
        print a
    print a

