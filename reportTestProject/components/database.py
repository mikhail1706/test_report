import os

DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_CONNECTION'),
        'NAME': os.getenv('DB_NAME'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'OPTIONS': {
            'sql_mode': 'traditional',
            'init_command': 'SET innodb_strict_mode=1',
            'charset': 'utf8mb4'
        },
        'TEST': {
            'CHARSET': 'utf8',
            'COLLATION': 'utf8_general_ci',
        }
    }
}