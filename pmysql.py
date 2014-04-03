import _mysql
import ConfigParser
import os.path

class PasteConn(object):
    def __init__(self):
        config = ConfigParser.ConfigParser()
        config.read(os.path.expanduser('~/.my.cnf'))
        self.mysqluser = config.get('client', 'user')
        self.mysqlpass = config.get('client', 'pass')
        try:
            self.mysqlhost = config.get('client', 'host')
        except:
            self.mysqlhost = 'localhost'

        try:
            self.mysqldb = config.get('client', 'database')
        except:
            self.mysqldb = 'pastes'

        self.db = _mysql.connect(
            host=self.mysqlhost,
            user=self.mysqluser,
            passwd=self.mysqlpass,
            db=self.mysqldb
        )

def lookup(pasteid):
    db = PasteConn()
    _db = db.db

    try:
        _db.query((
            "select paste from {0}.pastes where id='{1}';"
        ).format(db.mysqldb, pasteid))
        return _db.store_result()
    except:
        return False

def post_paste(pasteid, text):
    db = PasteConn()
    _db = db.db
    entry = (
        "Insert into {0}.pastes (id, paste) values ('{1}', '{2}');"
    ).format(db.mysqldb, pasteid, text)
    _db.query(entry)
