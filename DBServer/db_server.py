
import falcon
from math import sqrt
from wsgiref.simple_server import make_server


class Calc():
    def on_get(self, req, resp):
        qs = req.params
        resp.body = "Waiting for input\n"
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        chunk = req.stream.read(4096)
        values = chunk.split(b'&')
        a = int(values[0].split(b'=')[1])
        b = int(values[1].split(b'=')[1])
        c = int(values[2].split(b'=')[1])
        resp.body = self.calc_x(a,b,c)
        resp.status = falcon.HTTP_200

    def calc_determinant(self,a, b, c):
        return b*b - 4*a*c
        
    def calc_x(self,a,b,c):
        determinant = self.calc_determinant(a,b,c)
        if determinant > 0:
            x1 = (-b + sqrt(determinant)) / (2*a)
            x2 = (-b - sqrt(determinant)) / (2*a)
            return "Roots are real and different.\nx1 = {}\nx2 = {}".format(x1,x2)
        elif determinant == 0:
            x1 = (-b + sqrt(determinant)) / (2*a)
            return "Roots are real and same.\nx1 = x2 = {}".format(x1)
        else:
            realPart = -b/(2*a)
            imaginaryPart =sqrt(-determinant)/(2*a)
            return "Roots are complex and different.\nx1 = {0}+{1}i\nx2 = {0}-{1}i\n".format(realPart,imaginaryPart)


api = falcon.API()
r = Calc()
api.add_route('/',r)

ser = make_server('', 8080, api)
ser.serve_forever()
