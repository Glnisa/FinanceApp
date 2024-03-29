import os

class Config:
    """ Server Service Configuration
    Can be modified in .env, examples are in .env.example """
    
    # Helper to read numbers using var envs
    def cast_to_number(id):
        temp = os.environ[id]
        if temp is not None:
            try:
                return float(temp)
            except ValueError:
                return None
        return None
    
    user = os.environ['MYSQL_USER']
    password = os.environ['MYSQL_PASSWORD']
    host = os.environ['MYSQL_HOST'] 
    database = os.environ['MYSQL_DATABASE']
    DATABASE_URL = f"mysql://{user}:{password}@{host}/{database}"
    