import _mysql
import ConfigParser
import os.path

def _get_conn():
    config = ConfigParser.ConfigParser()
    config.read(os.path.expanduser('~/.my.cnf'))
    mysqluser = config.get('client', 'user')
    mysqlpass = config.get('client', 'pass')
    try:
        mysqlhost = config.get('client', 'host')
    except:
        mysqlhost = 'localhost'

    try:
        mysqldb = config.get('client', 'database')
    except:
        mysqldb = 'pastes'

    db = _mysql.connect(host=mysqlhost, user=mysqluser, passwd=mysqlpass, db=mysqldb)

    return db

def lookup(pasteid):
    _db = _get_conn()

    try:
        return _db.query((
            'select paste from {0} where id={1}'
        ).format(mysqldb, pasteid))
    except:
        return False

def post_paste(pasteid, text):
    _db = _get_conn()

    return _db.query('Insert into pastes (id, paste) values ({0}, {1})'.format(pasteid, text))
