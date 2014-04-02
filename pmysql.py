import _mysql
import ConfigParser

def _get_conn():
    config = ConfigParser.ConfigParser()
    cfg = config.read(os.path.expanduser('~/.my.cnf'))
    mysqluser = cfg.get('client', 'user')
    mysqlpass = cfg.get('client', 'pass')
    try:
        mysqlhost = cfg.get('client', 'host')
    except:
        mysqlhost = 'localhost'

    try:
        mysqldb = cfg.get('client', 'database')
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

    return _db.execute('Insert into pastes (id, paste) values ({0}, {1})'.format(pasteid, text))
