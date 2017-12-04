from ..schemautils import *

def write_schema(schema):
    print('## SCHEMA')
    print('')
    print('from marshmallow import Schema, fields, pprint, post_load')
    print('')
    
    for c in schema.classes:
        cn = c.name
        parent = c.is_a
        if parent is None:
            parent = 'Schema'
        else:
            parent = get_schema_class_name(parent)
        print('class {}({}):'.format(get_schema_class_name(cn), parent))

        slots = c.slots
        if not slots:
            slots = []
        for f in slots:
            slotname = None
            if isinstance(f,str):
                slotname = f
            elif isinstance(f,dict):
                # TODO
                slotname = f['name']
            else:
                slotname = f.name
            pyslotname = get_slot_name(slotname)
            print('    {n} = fields.{type}()'.format(n=pyslotname, type='Str'))
        print('')
        print('    @post_load')
        print('    def make_object(self, data):')
        print('        {}(**data)'.format(get_class_name(cn)))
        print('')
        
    
