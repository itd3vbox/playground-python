# module (libs) are reusable code (file, function, ...)
def users_create(data):
    print('Create Data ...', data)

def users_delete(data):
    print('Delete Data ...', data)

def users_update(data):
    print('Update Data ...', data)

def users_find_by_id(id):
    print('Find User By id ...', id)

def users_find_all(data):
    print('Find All User ...', data)

# run module as main app
if __name__ == "__main__":
    
    import sys

    value = int(sys.argv[1])

    if(value == 1):
        users_create( sys.argv[2] )

    elif(value == 2):
        users_delete( sys.argv[2] )

    elif(value == 3):
        users_update( sys.argv[2] )

    elif(value == 4):
        users_find_by_id( int( sys.argv[2] ) )
    
    elif(value == 5):
        users_find_all( sys.argv[2] )

