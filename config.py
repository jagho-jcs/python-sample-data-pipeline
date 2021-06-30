import os

DB_DETAILS = {
    'dev': {
        'SOURCE_DB': {
            'DB_TYPE': 'mysql',
            'DB_HOST': '139.99.209.131',
            'DB_NAME': 'retail_db',
            'DB_USER': os.getenv('SOURCE_DB_USER'),
            'DB_PASS': os.getenv('SOURCE_DB_PASS')
        },
        'TARGET_DB': {
            'DB_TYPE': 'postgres',
            'DB_HOST': '139.99.209.131',
            'DB_NAME': 'retail_db',
            'DB_USER': os.getenv('TARGET_DB_USER'),
            'DB_PASS': os.getenv('TARGET_DB_PASS')
        }
    }
}
