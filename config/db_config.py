import os
config = dict(
    default='postgres',
    postgres=dict(
        driver='postgres',
        host=os.environ['host'],
        database=os.environ['database'],
        user=os.environ['user'],
        password=os.environ['password'],
        port=os.environ['port'],
        prefix=''
    )
)
