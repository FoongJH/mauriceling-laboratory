import datetime

utcnow = datetime.datetime.utcnow()

notalogger_db = SQLDB('sqlite://notalogger.sqlite')

notalogger_db.define_table('logger',
                SQLField('notarizecode', 'text'),
                SQLField('name', 'text'),
                SQLField('pidentifier', 'text'),
                SQLField('email', 'text'),
                SQLField('usage', 'text'),
                SQLField('comments', 'text'),
                SQLField('datetimeserver', 'text'),
                SQLField('utc', 'datetime', default=utcnow),
                SQLField('seconds_since_epoch', 'text')
               )
