import jsonpickle as jsonpickle


class Persistencia() :

    def guardar_json(cls,pregunta) :
        text_open=open("files/" + '.json',mode = 'w')
        json_pre=jsonpickle.encode(pregunta)
        text_open.write(json_pre)
        text_open.close()

    @classmethod
    def cargar_json(cls,file_name) :
        text_open=open("files/" + file_name,mode = 'r')
        json_pre=text_open.readline()
        pregunta=jsonpickle.decode(json_pre)
        text_open.close()
        return pregunta
