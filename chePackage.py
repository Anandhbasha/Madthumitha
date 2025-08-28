# import cherrypy

# class Helloworld:
#     @cherrypy.expose
#     def index(self):
#         return "Hello Working"

# if __name__=='__main__':
#     cherrypy.quickstart(Helloworld())

import cherrypy

class studAPI:
    @cherrypy.expose
    def index(self):
        return "Welcome to home"
    @cherrypy.expose
    def get_stud(self,id):
        return f'Details of Students with id :{id}'

if __name__=='__main__':
    cherrypy.quickstart(studAPI())
