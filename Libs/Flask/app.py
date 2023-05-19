from flask import Flask, render_template, request, jsonify
from flask_restful import Api, Resource
from random import randint
from abc import ABC, abstractmethod


app = Flask(__name__)
api = Api(app)

def log_ext(msg):
    ...

def check_post_data(post_data, function_name):...

class InterfaceRoute(ABC, Resource):    
    @abstractmethod
    def _method_post(self, post_data):
        return jsonify(
            {'message':'POST not allowed'}
        )

    @abstractmethod
    def _valitaditon_post(self, *args, **kwargs):
        ...
    
    @abstractmethod
    def _method_get(self, *args, **kwargs):
        return jsonify(
            {'message':'GET not allowed'}
        )

    @abstractmethod
    def _valitaditon_get(self, *args, **kwargs):
        ...
    
    def post(self):
        post_data = request.get_json()
        self._valitaditon_post()
        return jsonify(self._method_post(post_data))


class Add(InterfaceRoute):
    def _valitaditon_post(self, *args, **kwargs):
        return super()._valitaditon_post(*args, **kwargs)
    
    def _valitaditon_get(self, *args, **kwargs):
        return super()._valitaditon_get(*args, **kwargs)
    
    def _method_get(self, *args, **kwargs):
        return super()._method_get(*args, **kwargs)

    def _method_post(self, post_data):
        math = 'NotCalculated'

        try:            
            x = float(post_data.get('x'))
            y = float(post_data.get('y'))
            math = x + y
        except ValueError as e:
            # Formato de numero inválido
            status_code = 400
            log_ext("Erro nos inputs")
        except Exception as e:
            status_code = 405
            log_ext("Erro desconhecido")
        else:
            status_code = 200
        finally:
            ret_dict = {
                'message':math,
                'status_code':status_code
            }
        return ret_dict


class Subtract(InterfaceRoute):
    def _valitaditon_post(self, *args, **kwargs):
        return super()._valitaditon_post(*args, **kwargs)
    
    def _valitaditon_get(self, *args, **kwargs):
        return super()._valitaditon_get(*args, **kwargs)
    
    def _method_get(self, *args, **kwargs):
        return super()._method_get(*args, **kwargs)

    def _method_post(self, post_data):
        math = 'NotCalculated'

        try:            
            x = float(post_data.get('x'))
            y = float(post_data.get('y'))
            math = x + y
        except ValueError as e:
            # Formato de numero inválido
            status_code = 400
            log_ext("Erro nos inputs")
        except Exception as e:
            status_code = 405
            log_ext("Erro desconhecido")
        else:
            status_code = 200
        finally:
            ret_dict = {
                'message':math,
                'status_code':status_code
            }
        return ret_dict


class Divide(InterfaceRoute):
    def _valitaditon_post(self, *args, **kwargs):
        return super()._valitaditon_post(*args, **kwargs)
    
    def _valitaditon_get(self, *args, **kwargs):
        return super()._valitaditon_get(*args, **kwargs)
    
    def _method_get(self, *args, **kwargs):
        return super()._method_get(*args, **kwargs)

    def _method_post(self, post_data):
        math = 'NotCalculated'

        try:            
            x = float(post_data.get('x'))
            y = float(post_data.get('y'))
            math = x + y
        except ValueError as e:
            # Formato de numero inválido
            status_code = 400
            log_ext("Erro nos inputs")
        except Exception as e:
            status_code = 405
            log_ext("Erro desconhecido")
        else:
            status_code = 200
        finally:
            ret_dict = {
                'message':math,
                'status_code':status_code
            }
        return ret_dict
    

class Multipy(InterfaceRoute):
    def _valitaditon_post(self, *args, **kwargs):
        return super()._valitaditon_post(*args, **kwargs)
    
    def _valitaditon_get(self, *args, **kwargs):
        return super()._valitaditon_get(*args, **kwargs)
    
    def _method_get(self, *args, **kwargs):
        return super()._method_get(*args, **kwargs)

    def _method_post(self, post_data):
        math = 'NotCalculated'

        try:            
            x = float(post_data.get('x'))
            y = float(post_data.get('y'))
            math = x + y
        except ValueError as e:
            # Formato de numero inválido
            status_code = 400
            log_ext("Erro nos inputs")
        except Exception as e:
            status_code = 405
            log_ext("Erro desconhecido")
        else:
            status_code = 200
        finally:
            ret_dict = {
                'message':math,
                'status_code':status_code
            }
        return ret_dict


api.add_resource(Add,'/add')
api.add_resource(Subtract,'/subtract')
api.add_resource(Divide,'/division')
api.add_resource(Multipy,'/multiply')




#     def get(self): ...

# class Subtract(Resource):
#     def post(self): ...
#     def get(self): ...

# class Multiply(Resource):
#     def post(self): ...
#     def get(self): ...

# class Divide(Resource):
#     def post(self): ...
#     def get(self): ...

@app.route("/")
def home():
    return (
        "Hello Worldhhhhhhhhhhhhhhhhhh   scfsd cvdhhhhhhhsdasda dsd asdashdljkahs!!"
        + "afdsffsdf fsdfsdf "
    )


# @app.route("/add/<n1><n2>")
# def teste(n1, n2):
#     num = [randint(1, 99), 3, 4, 6, 22]
#     return render_template("teste.html", numero=num, nome_user=name)


if __name__ == "__main__":
    app.run()
