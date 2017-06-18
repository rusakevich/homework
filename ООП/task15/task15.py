from abc import ABCMeta, abstractmethod
import pickle
import json
import os

class ParamHandler(metaclass=ABCMeta):   
    types = {}
    def __init__(self, source):
        self.source = source
        self.params = {}

    def add_param(self, key, value):
        self.params[key] = value

    def get_all_params(self):
        return self.params

    @abstractmethod
    def read(self):
        pass
    @abstractmethod
    def write(self):
        pass

    @classmethod    
    def add_type(cls, name, klass):        
        if not name:            
            raise ParamHandlerException('Type must have a name!')
        if not issubclass(klass, ParamHandler):            
            raise ParamHandlerException('Class "{}" is not ParamHandler!'.format(klass))
        cls.types[name] = klass
    @classmethod    
    def get_instance(cls, source, *args, **kwargs):        
        # Шаблон "Factory Method"
        _, ext = os.path.splitext(str(source).lower())        
        ext = ext.lstrip('.')        
        klass = cls.types.get(ext)
        if klass is None:            
            raise ParamHandlerException('Type "{}" not found!'.format(ext))
        return klass(source, *args, **kwargs)



    
class PickleParamHandler(ParamHandler):    
    def read(self):
        with open(self.source, 'r') as f:
            self.params = json.load(f)
            return self.params
    def write(self):       
        with open(self.source, 'w') as f:
            json.dump(self.params, f)




class JsonParamHandler(ParamHandler):    
    def read(self):
        with open(self.source, 'rb') as f:
            self.params = pickle.load(f)
            return self.params
    def write(self):       
        with open(self.source, 'wb') as f:
            pickle.dump(self.params, f)



ParamHandler.add_type('pickle', PickleParamHandler)    
config_pickle = ParamHandler.get_instance('C:/Users/rusak/Documents/Visual Studio 2017/Projects/homework/ООП/task15/users.pickle')
config_pickle.add_param('key1', 'pickle1') 
config_pickle.add_param('key2', 'pickle2') 
config_pickle.add_param('key3', 'pickle3') 
config_pickle.write()
print(config_pickle.read())


ParamHandler.add_type('json', PickleParamHandler)   
config_json = ParamHandler.get_instance('C:/Users/rusak/Documents/Visual Studio 2017/Projects/homework/ООП/task15/users.json')
config_json.add_param('key1', 'json1') 
config_json.add_param('key2', 'json2') 
config_json.add_param('key3', 'json3') 
config_json.write()
print(config_json.read())