from snippets.helper import FooException
import requests


class RequestHelper:
    SUCCESS = 200
    CREATED = 201
    BAD_REQUEST = 400
    INTERNAL_SERVER_ERROR = 500
    SERVICE_UNAVAILABLE = 503

    url = None
    _type = None
    params = None
    request = None
    response = None

    def __init__(self, url, _type='post', params=[]):
        if not url:
            raise FooException("URL inválida")

        self.url = url
        self._type = _type
        self.params = params

        self.request = requests.session()

    def sendRequest(self):
        try:
            response = self.getRequest().request(self.getType(), self.getUrl(), self.getParams())
            self.setResponse(response)
        except Exception as e:
            self.setResponse(e.getResponse)

        bln = self.getResponse()

        if bln:
            return bln.status_code

        return bln

    def getBody(self, json=False):
        body = self.getResponse()

        if body:
            return body.json()

        return body

    def getAccessToken(self):
        body = self.getBody(True)
        return body.access_token

    def getCode(self):
        response = self.getResponse()
        return response.getStatusCode()

    def getResponse(self):
        return self.response

    def setResponse(self, response):
        self.response = response

        return self

    def getRequest(self):
        return self.request

    def setRequest(self, request):
        self.request = request

        return self

    def getParams(self):
        return self.params

    def setParams(self, params):
        self.params = params

        return self

    def getType(self):
        return self._type

    def setType(self, _type):
        self._type = _type

        return self

    def getUrl(self):
        return self.url

    def setUrl(self, url):
        self.url = url

        return self

    def verificarCodigo(self, code=200):
        return self.getCode() == code
