from os import path
from lxml import objectify
import re

orgs = {}


def get_address(item):
    if hasattr(item, 'address'):
        address = {}
        if hasattr(item.address, 'thoroughfare'):
            address['thoroughfare'] = str(item.address.thoroughfare).replace(',', '')
            suite = re.findall('Suite ([0-9]+),?', str(item.address.thoroughfare), re.IGNORECASE)
            if len(suite) > 0:
                print(suite[0])
                address['suite'] = str(suite[0])
            level = re.findall('Level ([0-9]+),?', str(item.address.thoroughfare), re.IGNORECASE)
            if len(level) > 0:
                print(level[0])
                address['level'] = str(level[0])
            fn = re.findall(' ([0-9]+) ([A-Za-z]+) ([Street|St|Ave|Rd|Avenue|Road])', str(item.address.thoroughfare), re.IGNORECASE)
            if len(fn) > 0:
                print(fn[0])
                address['first_number'] = str(fn[0][0])
                address['street_name'] = str(fn[0][1])
        if hasattr(item.address, 'locality'):
            address['locality'] = item.address.locality
        if hasattr(item.address, 'administrative_area'):  # State
            address['administrative_area'] = item.address.administrative_area
        if hasattr(item.address, 'postal_code'):
            address['postal_code'] = item.address.postal_code
        orgs[item.unique_record_id] = address

        if address.get('first_number'):
            if address.get('level'):
                sql = '''SELECT * 
                      FROM gnaf.address_detail a 
                      INNER JOIN gnaf.street_locality s 
                      ON a.street_locality_pid = s.street_locality_pid 
                      WHERE a.number_first = {} 
                      AND s.street_name = '{}' 
                      AND a.postcode = '{}'
                      AND a.level_number = {};'''\
                    .format(
                    address['first_number'],
                    address['street_name'],
                    address['postcode'],
                    address['level']
                )
            else:
                sql = '''SELECT * 
                      FROM gnaf.address_detail a 
                      INNER JOIN gnaf.street_locality s 
                      ON a.street_locality_pid = s.street_locality_pid 
                      WHERE a.number_first = {} 
                      AND s.street_name = '{}' 
                      AND a.postcode = '{}';'''.format(
                    address['first_number'],
                    address['street_name'],
                    address['postcode']
                )

            print(sql)


def parse_items(export_file_name):
    this_dir = path.dirname(path.realpath(__file__))
    export_file_path = path.join(this_dir, 'data', export_file_name)
    items = objectify.parse(export_file_path).getroot().getchildren()
    for item in items:
        if str(item.unique_record_id).startswith('O') and hasattr(item, 'address'):
            print(item.unique_record_id)
            get_address(item)


if __name__ == '__main__':
    parse_items('export_2018-03-27.xml')

    with open('addresses.txt', 'w') as f:
        for k, v in sorted(orgs.items()):
            address_line = ''
            if v.get('thoroughfare'):
                address_line += v.get('thoroughfare')
            else:
                address_line += ','
            if v.get('locality'):
                address_line += ',' + v.get('locality')
            else:
                address_line += ','
            if v.get('administrative_area'):
                address_line += ',' + v.get('administrative_area')
            else:
                address_line += ','
            if v.get('postal_code'):
                address_line += ',' + str(v.get('postal_code'))
            else:
                address_line += ','
            if v.get('suite'):
                address_line += ',' + str(v.get('suite'))
            else:
                address_line += ','
            if v.get('level'):
                address_line += ',' + str(v.get('level'))
            else:
                address_line += ','
            if v.get('first_number'):
                address_line += ',' + str(v.get('first_number'))
            else:
                address_line += ','
            f.write(k + ',' + address_line + '\n')

    print(len(orgs))
