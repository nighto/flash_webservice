# monta XML
from xml.etree.ElementTree import Element, SubElement, tostring

my_xml         = Element('consultaListaHawbArXML')
usuario_xml    = SubElement(my_xml, "usuario")
senha_xml      = SubElement(my_xml, "senha")
cliente_id_xml = SubElement(my_xml, "cliente_id")
numEncCli_xml  = SubElement(my_xml, "numEncCli")

usuario_xml.text    = "ddx.webservice"
senha_xml.text      = "123"
cliente_id_xml.text = "2600"
numEncCli_xml.text  = ""

# insere HAWBs
hawb_xml = SubElement(my_xml, "hawb")
hawb_xml.text = "JB392553598BR"

# faz a consulta
import requests
ENDPOINT = "http://jall3.no-ip.info:8080/FlashOnline/rest/hawb/getconsultalistaAR/"
request = tostring(my_xml, encoding="UTF-8")
#print request
headers = {'Content-Type': 'application/xml'}
r = requests.post(ENDPOINT, data=request, headers=headers)
print "request: ", request
print "status_code: ", r.status_code
print "headers: ", r.headers
print "text: ", r.text