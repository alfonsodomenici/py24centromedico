from flask import Blueprint

checkpoints=Blueprint('checkpoints',__name__,url_prefix='/checkpoints')

@checkpoints.get('/')
def all():
    return 'all checkpoints'

    