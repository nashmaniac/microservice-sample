import os
DATABASES = dict(
    default='postgres',
    postgres=dict(
        driver='postgres',
        host=os.environ['host'],
        port=os.environ['port'],
        password=os.environ['password'],
        user=os.environ['user'],
        database=os.environ['database']
    )
)
