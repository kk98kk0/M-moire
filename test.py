from flask import Flask
from flask_restful import Api, Resource, reqparse
import json

app = Flask(__name__)
api = Api(app)
results = [{
    "target":[],
    "data":[]
}]
data = []
class Hello(Resource):
    
    def post(self, hello):

        result=[{'type': 'ScanInfo', 'arguments': '/home/fiacre/Python-Project/dnsrecon-master/dnsrecon.py', 'date': '2019-05-29 14:17:48.616911'}, 
        {'type': 'A', 'name': 'email.zonetransfer.me', 'address': '74.125.206.26'}, {'type': 'A', 'name': 'home.zonetransfer.me', 'address': '127.0.0.1'}, 
        {'type': 'A', 'name': 'office.zonetransfer.me', 'address': '4.23.39.254'}, {'type': 'A', 'name': 'owa.zonetransfer.me', 'address': '207.46.197.32'}, 
        {'type': 'CNAME', 'name': 'testing.zonetransfer.me', 'target': 'www.zonetransfer.me'}, {'type': 'A', 'name': 'www.zonetransfer.me', 'address': '5.196.105.14'}, 
        {'type': 'A', 'name': 'vpn.zonetransfer.me', 'address': '174.36.59.154'}, {'type': 'CNAME', 'name': 'staging.zonetransfer.me', 'target': 'www.sydneyoperahouse.com'}, 
        {'type': 'CNAME', 'name': 'www.sydneyoperahouse.com', 'target': 'd3gdbrxsb9xhmf.cloudfront.net'}, {'type': 'A', 'name': 'd3gdbrxsb9xhmf.cloudfront.net', 'address': '13.32.123.180'}, {'type': 'A', 'name': 'd3gdbrxsb9xhmf.cloudfront.net', 'address': '13.32.123.135'}, 
        {'type': 'A', 'name': 'd3gdbrxsb9xhmf.cloudfront.net', 'address': '13.32.123.30'}, {'type': 'A', 'name': 'd3gdbrxsb9xhmf.cloudfront.net', 'address': '13.32.123.196'}, 
        {'type': 'CNAME', 'name': 'staging.zonetransfer.me', 'target': 'www.sydneyoperahouse.com'}, {'type': 'CNAME', 'name': 'www.sydneyoperahouse.com', 'target': 'd3gdbrxsb9xhmf.cloudfront.net'}, 
        {'type': 'AAAA', 'name': 'd3gdbrxsb9xhmf.cloudfront.net', 'address': '2600:9000:211b:f000:3:59a3:1dc0:93a1'}, {'type': 'AAAA', 'name': 'd3gdbrxsb9xhmf.cloudfront.net', 'address': '2600:9000:211b:f800:3:59a3:1dc0:93a1'}, 
        {'type': 'AAAA', 'name': 'd3gdbrxsb9xhmf.cloudfront.net', 'address': '2600:9000:211b:a00:3:59a3:1dc0:93a1'}, 
        {'type': 'AAAA', 'name': 'd3gdbrxsb9xhmf.cloudfront.net', 'address': '2600:9000:211b:2800:3:59a3:1dc0:93a1'}, {'type': 'AAAA', 'name': 'd3gdbrxsb9xhmf.cloudfront.net', 'address': '2600:9000:211b:2a00:3:59a3:1dc0:93a1'}, 
        {'type': 'AAAA', 'name': 'd3gdbrxsb9xhmf.cloudfront.net', 'address': '2600:9000:211b:5000:3:59a3:1dc0:93a1'}, {'type': 'AAAA', 'name': 'd3gdbrxsb9xhmf.cloudfront.net', 'address': '2600:9000:211b:6a00:3:59a3:1dc0:93a1'}, 
        {'type': 'AAAA', 'name': 'd3gdbrxsb9xhmf.cloudfront.net', 'address': '2600:9000:211b:c000:3:59a3:1dc0:93a1'}, {'type': 'A', 'name': 'www.zonetransfer.me', 'address': '5.196.105.14'}, 
        {'type': 'info', 'zone_transfer': 'success', 'ns_server': '34.225.33.2'}, {'zone_server': '34.225.33.2', 'type': 'SOA', 'mname': 'nsztm1.digi.ninja', 'address': '81.4.108.41'}, {'zone_server': '34.225.33.2', 'type': 'NS', 'target': 'nsztm1.digi.ninja', 'address': '81.4.108.41'}, 
        {'zone_server': '34.225.33.2', 'type': 'NS', 'target': 'nsztm2.digi.ninja', 'address': '34.225.33.2'}, {'zone_server': '34.225.33.2', 'type': 'NS', 'target': 'intns1.zonetransfer.me', 'address': '81.4.108.41'}, 
        {'zone_server': '34.225.33.2', 'type': 'NS', 'target': 'intns2.zonetransfer.me', 'address': '167.88.42.94'}, 
        {'type': 'info', 'zone_transfer': 'failed', 'ns_server': '34.225.33.2'}, {'type': 'info', 'zone_transfer': 'success', 'ns_server': '81.4.108.41'}, 
        {'zone_server': '81.4.108.41', 'type': 'SOA', 'mname': 'nsztm1.digi.ninja', 'address': '81.4.108.41'}, {'zone_server': '81.4.108.41', 'type': 'NS', 'target': 'nsztm1.digi.ninja', 'address': '81.4.108.41'}, 
        {'zone_server': '81.4.108.41', 'type': 'NS', 'target': 'nsztm2.digi.ninja', 'address': '34.225.33.2'}, {'zone_server': '81.4.108.41', 'type': 'NS', 'target': 'intns1.zonetransfer.me', 'address': '81.4.108.41'}, 
        {'zone_server': '81.4.108.41', 'type': 'NS', 'target': 'intns2.zonetransfer.me', 'address': '167.88.42.94'}, {'type': 'info', 'zone_transfer': 'failed', 'ns_server': '81.4.108.41'}, 
        {'type': 'info', 'zone_transfer': 'success', 'ns_server': '34.225.33.2'}, {'zone_server': '34.225.33.2', 'type': 'SOA', 'mname': 'nsztm1.digi.ninja', 'address': '81.4.108.41'}, 
        {'zone_server': '34.225.33.2', 'type': 'NS', 'target': 'nsztm1.digi.ninja', 'address': '81.4.108.41'}, {'zone_server': '34.225.33.2', 'type': 'NS', 'target': 'nsztm2.digi.ninja', 'address': '34.225.33.2'}, 
        {'zone_server': '34.225.33.2', 'type': 'NS', 'target': 'intns1.zonetransfer.me', 'address': '81.4.108.41'}, {'zone_server': '34.225.33.2', 'type': 'NS', 'target': 'intns2.zonetransfer.me', 'address': '167.88.42.94'}, 
        {'type': 'info', 'zone_transfer': 'failed', 'ns_server': '34.225.33.2'}, {'type': 'info', 'zone_transfer': 'success', 'ns_server': '81.4.108.41'}, {'zone_server': '81.4.108.41', 'type': 'SOA', 'mname': 'nsztm1.digi.ninja', 'address': '81.4.108.41'}, 
        {'zone_server': '81.4.108.41', 'type': 'NS', 'target': 'nsztm1.digi.ninja', 'address': '81.4.108.41'}, {'zone_server': '81.4.108.41', 'type': 'NS', 'target': 'nsztm2.digi.ninja', 'address': '34.225.33.2'}, 
        {'zone_server': '81.4.108.41', 'type': 'NS', 'target': 'intns1.zonetransfer.me', 'address': '81.4.108.41'}, {'zone_server': '81.4.108.41', 'type': 'NS', 'target': 'intns2.zonetransfer.me', 'address': '167.88.42.94'}, 
        {'type': 'info', 'zone_transfer': 'failed', 'ns_server': '81.4.108.41'}, {'type': 'SOA', 'mname': 'nsztm1.digi.ninja', 'address': '81.4.108.41'}, 
        {'type': 'NS', 'target': 'nsztm2.digi.ninja', 'address': '34.225.33.2', 'recursive': 'True', 'Version': b'9.11.3-1ubuntu1.7-Ubuntu'}, {'type': 'NS', 'target': 'nsztm1.digi.ninja', 'address': '81.4.108.41', 'recursive': 'True', 'Version': b'9.10.3-P4-Debian'}, 
        {'type': 'MX', 'exchange': 'ASPMX5.GOOGLEMAIL.COM', 'address': '74.125.199.27'}, 
        {'type': 'MX', 'exchange': 'ASPMX4.GOOGLEMAIL.COM', 'address': '64.233.188.27'}, {'type': 'MX', 'exchange': 'ASPMX2.GOOGLEMAIL.COM', 'address': '108.177.14.27'}, 
        {'type': 'MX', 'exchange': 'ASPMX3.GOOGLEMAIL.COM', 'address': '74.125.200.27'}, {'type': 'MX', 'exchange': 'ALT2.ASPMX.L.GOOGLE.COM', 'address': '74.125.200.26'}, 
        {'type': 'MX', 'exchange': 'ALT1.ASPMX.L.GOOGLE.COM', 'address': '108.177.14.26'}, {'type': 'MX', 'exchange': 'ASPMX.L.GOOGLE.COM', 'address': '74.125.71.26'}, 
        {'type': 'MX', 'exchange': 'ASPMX5.GOOGLEMAIL.COM', 'address': '2607:f8b0:400e:c02::1b'}, {'type': 'MX', 'exchange': 'ASPMX4.GOOGLEMAIL.COM', 'address': '2404:6800:4008:c06::1b'}, 
        {'type': 'MX', 'exchange': 'ASPMX2.GOOGLEMAIL.COM', 'address': '2a00:1450:4010:c0f::1b'}, {'type': 'MX', 'exchange': 'ASPMX3.GOOGLEMAIL.COM', 'address': '2404:6800:4003:c00::1b'}, {'type': 'MX', 'exchange': 'ALT2.ASPMX.L.GOOGLE.COM', 'address': '2404:6800:4003:c00::1a'}, 
        {'type': 'MX', 'exchange': 'ALT1.ASPMX.L.GOOGLE.COM', 'address': '2a00:1450:4010:c0f::1b'}, {'type': 'MX', 'exchange': 'ASPMX.L.GOOGLE.COM', 'address': '2a00:1450:400c:c08::1a'}, 
        {'type': 'A', 'name': 'zonetransfer.me', 'address': '5.196.105.14'}, {'type': 'SRV', 'name': '_sip._tcp.zonetransfer.me', 'target': 'www.zonetransfer.me', 'address': '5.196.105.14', 'port': '5060'}, 
        {'type': 'A', 'name': 'www.zonetransfer.me', 'address': '5.196.105.14'}, {'type': 'A', 'name': 'zonetransfer.me', 'address': '5.196.105.14'}, {'type': 'A', 'name': 'email.zonetransfer.me', 'address': '74.125.206.26'}, 
        {'type': 'A', 'name': 'home.zonetransfer.me', 'address': '127.0.0.1'}, {'type': 'A', 'name': 'office.zonetransfer.me', 'address': '4.23.39.254'}, {'type': 'A', 'name': 'owa.zonetransfer.me', 'address': '207.46.197.32'}, 
        {'type': 'CNAME', 'name': 'testing.zonetransfer.me', 'target': 'www.zonetransfer.me'}, {'type': 'A', 'name': 'www.zonetransfer.me', 'address': '5.196.105.14'}, {'type': 'CNAME', 'name': 'staging.zonetransfer.me', 'target': 'www.sydneyoperahouse.com'}, {'type': 'CNAME', 'name': 'www.sydneyoperahouse.com', 'target': 'd3gdbrxsb9xhmf.cloudfront.net'}, 
        {'type': 'A', 'name': 'd3gdbrxsb9xhmf.cloudfront.net', 'address': '13.32.123.180'}, {'type': 'A', 'name': 'd3gdbrxsb9xhmf.cloudfront.net', 'address': '13.32.123.196'}, 
        {'type': 'A', 'name': 'd3gdbrxsb9xhmf.cloudfront.net', 'address': '13.32.123.30'}, {'type': 'A', 'name': 'd3gdbrxsb9xhmf.cloudfront.net', 'address': '13.32.123.135'}, 
        {'type': 'CNAME', 'name': 'staging.zonetransfer.me', 'target': 'www.sydneyoperahouse.com'}, {'type': 'CNAME', 'name': 'www.sydneyoperahouse.com', 'target': 'd3gdbrxsb9xhmf.cloudfront.net'}, 
        {'type': 'AAAA', 'name': 'd3gdbrxsb9xhmf.cloudfront.net', 'address': '2600:9000:211b:da00:3:59a3:1dc0:93a1'}, {'type': 'AAAA', 'name': 'd3gdbrxsb9xhmf.cloudfront.net', 'address': '2600:9000:211b:e000:3:59a3:1dc0:93a1'}, 
        {'type': 'AAAA', 'name': 'd3gdbrxsb9xhmf.cloudfront.net', 'address': '2600:9000:211b:f800:3:59a3:1dc0:93a1'}, {'type': 'AAAA', 'name': 'd3gdbrxsb9xhmf.cloudfront.net', 'address': '2600:9000:211b:200:3:59a3:1dc0:93a1'}, 
        {'type': 'AAAA', 'name': 'd3gdbrxsb9xhmf.cloudfront.net', 'address': '2600:9000:211b:2c00:3:59a3:1dc0:93a1'}, {'type': 'AAAA', 'name': 'd3gdbrxsb9xhmf.cloudfront.net', 'address': '2600:9000:211b:3000:3:59a3:1dc0:93a1'}, 
        {'type': 'AAAA', 'name': 'd3gdbrxsb9xhmf.cloudfront.net', 'address': '2600:9000:211b:7200:3:59a3:1dc0:93a1'}, {'type': 'AAAA', 'name': 'd3gdbrxsb9xhmf.cloudfront.net', 'address': '2600:9000:211b:c200:3:59a3:1dc0:93a1'}, 
        {'type': 'A', 'name': 'vpn.zonetransfer.me', 'address': '174.36.59.154'}, {'type': 'A', 'name': 'www.zonetransfer.me', 'address': '5.196.105.14'}, {'type': 'SRV', 'name': '_sip._tcp.zonetransfer.me', 'target': 'www.zonetransfer.me', 'address': '5.196.105.14', 'port': '5060'}, 
        {'type': 'A', 'name': 'zonetransfer.net', 'address': '165.160.15.20'}, {'type': 'A', 'name': 'zonetransfer.net', 'address': '165.160.13.20'}, {'type': 'A', 'name': 'zonetransfer.info', 'address': '165.160.15.20'}, {'type': 'A', 'name': 'zonetransfer.info', 'address': '165.160.13.20'}, 
        {'type': 'A', 'name': 'zonetransfer.com', 'address': '67.227.156.96'}, {'type': 'A', 'name': 'zonetransfer.fm', 'address': '198.74.54.240'}, {'type': 'A', 'name': 'zonetransfer.me', 'address': '5.196.105.14'}, {'type': 'A', 'name': 'zonetransfer.la', 'address': '173.230.141.80'}, {'type': 'A', 'name': 'zonetransfer.ph', 'address': '45.79.222.138'}, {'type': 'A', 'name': 'zonetransfer.vg', 'address': '88.198.29.97'}, 
        {'type': 'A', 'name': 'zonetransfer.ws', 'address': '64.70.19.203'}, {'type': 'A', 'name': 'www.zonetransfer.me', 'address': '5.196.105.14'}, 
        {'type': 'A', 'name': 'zonetransfer.me', 'address': '5.196.105.14'}]
        #print(result)
        #x = ['Some strings.', 1, 2, 3, 'More strings!']
        #y = [i.decode('UTF-8') if isinstance(i, basestring) else i for i in x]
        #results = []
        for mydict in result:
            mydict = {k: v.decode("utf-8") if isinstance(v, bytes) else v for k,v in mydict.items()}
            data.append(mydict)
        results.append({"target": hello, "data": data})
        return {"target": hello, "data": data}, 201
        #b"9.11.3-1ubuntu1.7-Ubuntu".decode("utf-8")
        #mydict = {k: v.decode("utf-8") if isinstance(v, bytes) else v for k,v in mydict.items()}
    
    def get(self, hello):
        #print(results.keys())
        for result in results:
            #print(result.keys()) 
            if(hello == result["target"]):
                return result, 200
        return "User not found", 404

api.add_resource(Hello, "/user/<string:hello>")

app.run(debug=True)