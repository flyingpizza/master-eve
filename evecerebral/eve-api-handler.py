'''
API based utility got eve
'''
import requests, json

class EveUtil(object):

    def __init__(self,cloudURL = 'esi.evetech.net',datasource='tranquility', route=''):

        self.route = 'system_kills'
        # self.route = 'system_jumps'
            
        try:
            if cloudURL:
                self.cloudURL = cloudURL
                self.datasource = datasource
                self.system_jump = 'https://' + self.cloudURL + '/latest/universe/{}/?datasource={}'.format(self.route,self.datasource)        
            else:
                print ('Provide a valid url') 

        except Exception as e:
            print('Provided URL is not valid {}'.format(e)) 

    def eve_system_jumps(self):
        """
        Function which returns json data 
        
        Returns:
            list -- contains a list of dictionaries which contains system_id and number of jumps 
        """
        
        headers = {'accept': 'application/json'}
        response = requests.get(self.system_jump,headers=headers,verify=False)
        system_info = json.loads(response._content)
        
        return system_info




if __name__ == '__main__':
    obj = EveUtil()
    x = obj.eve_system_jumps()
    print (x)