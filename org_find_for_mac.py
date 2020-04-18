'''
Simple script to get Company Name for provided mac-address
Usage: org_find_for_mac -k <api-key> -m <mac-address>
'''

import argparse
import requests
import re

def validate_mac(mac_addr):
    '''
    mac-address validation for the format xx;xx:xx:xx:xx:xx
    '''
    mac_pattern = r'(([\da-fA-F]{2}\:){5}[\da-fA-F]{2})'
    if not re.search(mac_pattern, mac_addr):
        return False
    return True
    
def org_name_fetch(api_key, mac_addr):
    '''
    api_key - user api-key
    mac_addr - mac address
    if valid mac:
        return statement with mac-address and its company_name
    else:
        return error message
    '''
        
    # use user api-key to get vendor details
    api_url = "https://api.macaddress.io/v1"
    parameters = {'apiKey':api_key, 'output':'json', 'search':mac_addr}
    get_req = ''
    try:
        get_req = requests.get(url = api_url, params = parameters)
    except Exception as e:
        return str(e)
    
    if not get_req.ok:
        return get_req.content
      
    json_content = get_req.json()
    company_name = ''
    if 'vendorDetails' in json_content:
        if 'companyName' in json_content['vendorDetails']:
            company_name = json_content['vendorDetails']['companyName']
    
    if not company_name:
        return "Company Name is not available in Vendor details"
    
    return "Company Name for mac {} is {}".format(mac_addr, company_name)

def main():
    '''
    Main script to get "auth api key" and "mac-address" 
    And find vendor name for that given mac-address
    '''

    try:
        arg_parser = argparse.ArgumentParser(description='Find the company name for a provided mac-address')
        arg_parser.add_argument('-k', '--key', metavar='key', type=str, required=True, help='auth api key')
        arg_parser.add_argument('-m', '--mac', metavar='mac', type=str, required=True, help='mac address')
        argument = arg_parser.parse_args()
        print(argument)
        
        if argument.key and argument.mac:
            if not validate_mac(argument.mac):
                print("Invalid mac-address, provide valid mac in format xx;xx:xx:xx:xx:xx")
            else:
                output = org_name_fetch(argument.key, argument.mac)
                print(output)
        else:    
            print("Required two arugments, 'auth api key' and 'mac-address'")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
    
