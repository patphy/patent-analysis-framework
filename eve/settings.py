
# Let's just use the local mongod instance. Edit as needed.

# Please note that MONGO_HOST and MONGO_PORT could very well be left
# out as they already default to a bare bones local 'mongod' instance.
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_USERNAME = 'lala'
MONGO_PASSWORD = '1234'
MONGO_DBNAME = 'patentdb'

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

#schema = {
    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/nicolaiarocci/cerberus) for details.
#    'firstname': {
#        'type': 'string',
#        'minlength': 1,
#        'maxlength': 10,
#    },
#    'lastname': {
#        'type': 'string',
#        'minlength': 1,
#        'maxlength': 15,
#        'required': True,
        # talk about hard constraints! For the purpose of the demo
        # 'lastname' is an API entry-point, so we need it to be unique.
#        'unique': False,
#    },
    # 'role' is a list, and can only contain values from 'allowed'.
#    'role': {
#        'type': 'list',
#        'allowed': ["author", "contributor", "copy"],
#    },
    # An embedded 'strongly-typed' dictionary.
#    'location': {
#        'type': 'dict',
#        'schema': {
#            'address': {'type': 'string'},
#            'city': {'type': 'string'}
#        },
#    },
 #   'born': {
 #       'type': 'datetime',
 #   },
#}
patent_schema = {
    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/nicolaiarocci/cerberus) for details.
        'kind': {
            'type':'string'
        }, 
        'date-published': {
            'type':'string'
        }, 
        'number-of-claims': {
            'type':'string'
        }, 
        'country': {
            'type':'string'
        }, 
        'doc-number': {
            'type':'string', 
            'required':True,
        }, 
        'invention-title': {
            'type':'string'
        },
        'application-number': {
            'type':'string'
        }, 
        'citations':{
            'type':'list',
            'schema':{
                'type':'dict',
                'schema':{
                    'doc-number':{
                        'type':'string',
                    }
                }
            }
        },
        'date-produced':{
            'type':'string'
        }, 
        'inventors':{
            'type':'list',
            'schema':{
                'type':'dict',
                'schema':{
                    'city':{
                        'type':'string'
                    }, 
                    'last-name':{
                        'type':'string'
                    }, 
                    'country':{
                        'type':'string'
                    }, 
                    'first-name':{
                        'type':'string'
                    }
                }
            }
        }
    }

inventor_schema={
        'city':{
            'type':'string'
        }, 
        'last-name':{
            'type':'string'
        }, 
        'country':{
            'type':'string'
        }, 
        'first-name':{
            'type':'string'
        }
    
}
inventors = {
    'item_title': 'inventor',
#    'additional_lookup': {
#        'url': 'regex("[\w.+\-]")',
#        'field': 'first-name'
#    },
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    # most global settings can be overridden at resource level
    'resource_methods': ['GET', 'POST','DELETE'],

    'schema': inventor_schema
}

patents = {
    # 'title' tag used in item links. Defaults to the resource title minus
    # the final, plural 's' (works fine in most cases but not for 'people')
    'item_title': 'patent',

    # by default the standard item entry point is defined as
    # '/people/<ObjectId>'. We leave it untouched, and we also enable an
    # additional read-only entry point. This way consumers can also perform
    # GET requests at '/people/<lastname>'.
#    'additional_lookup': {
#       'url': 'regex("[\w.+\-]")',
#        'field': 'doc-number'
#    },

    # We choose to override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    # most global settings can be overridden at resource level
    'resource_methods': ['GET', 'POST','DELETE'],
    

    'schema': patent_schema
}

DOMAIN = {
    'patents':patents,
    'inventors':inventors
}