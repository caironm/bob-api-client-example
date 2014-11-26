from suds.sax.element import Element
from suds.plugin import MessagePlugin

import suds
import logging

logging.basicConfig(level=logging.INFO)

logging.getLogger('suds.client').setLevel(logging.INFO)

class BobPlugin(MessagePlugin):
    def marshalled(self, context):
        # import ipdb; ipdb.set_trace()

        context.envelope.nsprefixes.pop('ns0')
        context.envelope.nsprefixes.pop('ns1')
        context.envelope.nsprefixes.pop('xsi')
        context.envelope.nsprefixes.pop('SOAP-ENV')

        context.envelope.nsprefixes['soapenv'] = 'http://schemas.xmlsoap.org/soap/envelope/'
        context.envelope.nsprefixes['tem'] = 'http://tempuri.org/'

        context.envelope.prefix = 'soapenv'

        header = context.envelope.getChild('Header')
        header.prefix = 'soapenv'

        body = context.envelope.getChild('Body')
        body.prefix = 'soapenv'

        m = body.getChild('CreaTestVocacionalProspectoIntermedio')
        m.prefix = 'tem'

        for item in m:
            item.prefix = 'tem'

        # ipdb.set_trace()

        # for item in context.envelope.children:
        #     print item

# import ipdb; ipdb.set_trace()

client = suds.client.Client(
    "http://crm.upn.edu.pe:8091/CrearTestVocacionalProspectoIntermedio.asmx?wsdl",
    plugins=[BobPlugin()])

# ssnns = ('tem', 'http://tempuri.org/')
# ssn = Element('CreaTestVocacionalProspectoIntermedio', ns=ssnns)

# client.set_options(soapheaders=ssn)
try:
    resp = client.service.CreaTestVocacionalProspectoIntermedio(
        PortafolioID="20674274",
        MMDate="22/11/2014",
        Cluster1="",
        Cluster2="",
        ResultURL="http://localhost",
        Telefono="",
        Ocupaciones1_Cluster1="",
        Ocupaciones2_Cluster1="",
        Ocupaciones3_Cluster1="",
        Ocupaciones4_Cluster1="",
        Ocupaciones5_Cluster1="",
        Ocupaciones6_Cluster1="",
        Ocupaciones7_Cluster1="",
        Ocupaciones8_Cluster1="",
        Ocupaciones9_Cluster1="",
        Ocupaciones10_Cluster1="",
        Aptitudes1_Cluster1="",
        Aptitudes2_Cluster1="",
        Aptitudes3_Cluster1="",
        Aptitudes4_Cluster1="",
        Aptitudes5_Cluster1="",
        Aptitudes6_Cluster1="",
        Aptitudes7_Cluster1="",
        Aptitudes8_Cluster1="",
        Aptitudes9_Cluster1="",
        Aptitudes10_Cluster1="",
        Ocupaciones1_Cluster2="",
        Ocupaciones2_Cluster2="",
        Ocupaciones3_Cluster2="",
        Ocupaciones4_Cluster2="",
        Ocupaciones5_Cluster2="",
        Ocupaciones6_Cluster2="",
        Ocupaciones7_Cluster2="",
        Ocupaciones8_Cluster2="",
        Ocupaciones9_Cluster2="",
        Ocupaciones10_Cluster2="",
        Aptitudes1_Cluster2="",
        Aptitudes2_Cluster2="",
        Aptitudes3_Cluster2="",
        Aptitudes4_Cluster2="",
        Aptitudes5_Cluster2="",
        Aptitudes6_Cluster2="",
        Aptitudes7_Cluster2="",
        Aptitudes8_Cluster2="",
        Aptitudes9_Cluster2="",
        Aptitudes10_Cluster2="",
        TerminosCC="1"
    )

    print(resp)

except suds.WebFault, e:
    stacktrace = ""
    message = ""

    if isinstance(e.fault.detail.ExceptionDetail.StackTrace, str):
        stacktrace = e.fault.detail.ExceptionDetail.StackTrace.encode('utf-8')
    else:
        stacktrace = unicode(e.fault.detail.ExceptionDetail.StackTrace)

    if isinstance(e.message, str):
        message = e.message.encode('utf-8')
    else:
        message = unicode(e.message)

    print "ERROR"
    print message
    print stacktrace
