import httplib2
import json

def mk_record(ty, name, values, ttl=1800):
    r = {}
    r['rrset_type'] = ty
    r['rrset_ttl'] = ttl
    r['rrset_name'] = name
    r['rrset_values'] = values
    return r

class Domain:
    def __init__(self, domain):
        self.name = domain
        self.records = {}

    def check_name(self, name):
        if(not name in self.records):
            self.records[name] = {}

    def a(self, name, value):
        self.check_name(name)
        if('a' in self.records[name]):
            raise Exception("record of type A already defined for name " + name)
        self.records[name]['a'] = value

    def aaaa(self, name, value):
        self.check_name(name)
        if('aaaa' in self.records[name]):
            raise Exception("record of type AAAA already defined for name " + name)
        self.records[name]['aaaa'] = value
    
    def cname(self, name, value):
        self.check_name(name)
        if('cname' in self.records[name]):
            raise Exception("record of type CNAME already defined for name " + name)
        self.records[name]['cname'] = value

    def mx(self, name, domain):
        self.check_name(name)
        if(not 'mx' in self.records[name]):
            self.records[name]['mx'] = []
        self.records[name]['mx'].append(domain)

    def spf(self, name, value):
        self.check_name(name)
        if(not 'spf' in self.records[name]):
            self.records[name]['spf'] = ""
        self.records[name]['spf'] += " " + value
    
    def txt(self, name, value):
        self.check_name(name)
        if(not 'txt' in self.records[name]):
            self.records[name]['txt'] = []
        self.records[name]['txt'].append("\"" + value + "\"")

    def subdomain(self, domain):
        if(domain.name in self.records):
            raise Exception("sub domain " + domain.name + "." + self.name + " already defined")
        self.records[domain.name] = {}
        for name in domain.records:
            if(name == "@"):
                new_name = domain.name
            else:
                new_name = name + "." + domain.name
            self.records[new_name] = domain.records[name]

    def body(self):
        items = []
        for name in self.records:
            r = self.records[name]
            if('a' in r):
                items.append(mk_record("A", name, [r['a']]))
            if('aaaa' in r):
                items.append(mk_record("AAAA", name, [r['aaaa']]))
            if('cname' in r):
                items.append(mk_record("CNAME", name, [r['cname']]))
            if('mx' in r):
                values = []
                p = 0
                for domain in r['mx']:
                    p += 10
                    values.append(str(p) + " " + domain)
                items.append(mk_record("MX", name, values))
            if('txt' in r or 'spf' in r):
                values = []
                if('txt' in r):
                    values += r['txt']
                if('spf' in r):
                    values.append("\"v=spf1" + r['spf'] + " ~all\"")
                items.append(mk_record("TXT", name, values))
        return json.dumps({'items': items}).encode()

    def push(self):
      key = open("/data/pnm/secrets/gandi/key.txt", "r").read()
      api_url = "https://api.gandi.net/v5/livedns"
      url = api_url + "/domains/" + self.name + "/records"
      headers = {
          'Authorization': "Apikey " + key,
          'Content-Type': 'application/json',
           }
      h = httplib2.Http(".cache")
      (resp, content) = h.request(url, "PUT", headers=headers, body=self.body())
      return content
