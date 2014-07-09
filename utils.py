__author__ = 'Marco'


import yaml


__CONF = None


def get_conf():
    global __CONF
    if __CONF is None:
        f = open('conf.yaml')
        # use safe_load instead load
        __CONF = yaml.safe_load(f)
        f.close()
    return __CONF