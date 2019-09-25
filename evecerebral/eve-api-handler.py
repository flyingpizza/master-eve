'''
API based utility got eve
'''
import requests, json

class EveUtil(object):

    def __init__(self,cloudURL = 'esi.evetech.net',datasource='tranquility'):

        try:
            if cloudURL:
                self.cloudURL = cloudURL
                self.datasource = datasource
            else:
                print ('Provide a valid url') 

        except Exception as e:
            print('Provided URL is not valid {}'.format(e)) 

    def eve_system_jumps(self):
        system_jumpURL = 'https://' + self.cloudURL + '/latest/universe/system_jumps/?datasource={}'.format(self.datasource)
        headers = {'accept': 'application/json'}
        response = requests.get(system_jumpURL,headers=headers,verify=False)
        return response     

    def eve_system_info(self, parameter_list):
        pass



if __name__ == '__main__':
