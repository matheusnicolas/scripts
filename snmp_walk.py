from easysnmp import Session
from easysnmp import snmp_get, snmp_set, snmp_walk 


VARIABLE = 'name'
IP_ADDRESS = '000.000.0.0:0000'
PUBLIC = 'public'

class Walk:
    
    def __init__(self, variable, hostname, community, version):
        self.variable = variable
        self.hostname = hostname
        self.community = community
        self.version = version
    
    def _walk(self):
        session = Session(hostname=self.hostname, community=self.community, version=self.version)
        system_items = session.bulkwalk(self.variable)
        for item in system_items:
            print ('{oid}.{oid_index} {snmp_type} = {value}').format(
              oid=item.oid,
              oid_index=item.oid_index,
              snmp_type=item.snmp_type,
              value=item.value
            )

if __name__ == '__main__':
    walk = Walk(VARIABLE, IP_ADDRESS, PUBLIC, 2)
    walk._walk()