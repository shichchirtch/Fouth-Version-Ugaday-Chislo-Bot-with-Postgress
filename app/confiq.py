
host ='172.28.221.122'
user = 'postgres'
password = 'postgres'
db_name = 'postgres'

db_path = f"postgresql+asyncpg://{user}:{password}@{host}:5432/{db_name}"
