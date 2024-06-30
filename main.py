import requests

GoogleURL = ''  # link to the google form

urlResponse = GoogleURL + '/formResponse'
urlReferer = GoogleURL + '/viewform'

for i in range(4):
    form_data = {'entry.839817015': 'Rarely or never',  #  we find the entries in html of options
                 'entry.951218388': 'Not important at all',  # if you want you can answer using list for multiplce choice questions
                 'entry.1214604849': 'Never', 
                 'entry.1119028097': 'Not really',
                 'entry.2082564747': "I'm not sure",
                }
    user_agent = {'Referer': urlReferer,
                  'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"  # this thing you should take from you browser
                 }
    r = requests.post(urlResponse, data=form_data, headers=user_agent)
