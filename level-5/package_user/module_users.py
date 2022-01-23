# module (libs) are reusable code (file, function, ...)
def users_create(data):
    print('Create Data ...')

def users_delete(data):
    print('Delete Data ...')

def users_update(data):
    print('Delete Data ...')

def users_find_by_id(id):
    print('Find User By id ...')

def users_find_all(data):
    print('Find All User ...')

if __name__ == "__main__":
    import sys
    users_find_by_id( int( sys.argv[1] ) )

