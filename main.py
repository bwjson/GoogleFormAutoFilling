import requests

GoogleURL = 'https://docs.google.com/forms/d/e/1FAIpQLSdNKvNpWc3r95v0nUABmwOM9ZIaKj9HvYd8pXPMak6211V3SQ'

urlResponse = GoogleURL + '/formResponse'
urlReferer = GoogleURL + '/viewform'

for i in range(4):
    form_data = {'entry.839817015': 'Rarely or never',  # A few times a week Rarely or never Multiple times a day
                 'entry.471614409': 'Facebook', # Telegram, Facebook, Other
                 'entry.951218388': 'Not important at all', # Very important Somewhat important Not very important Not important at all
                 'entry.1214604849': 'Never', # Yes, often Sometimes Rarely Never
                 'entry.1776221472': 'Never', # Frequently Occasionally Rarely Never
                 'entry.1119028097': 'Not really',# Yes, completely To some extent Not really Not at all
                 'entry.2082564747': "I'm not sure",# Positively Neutral Negatively I'm not sure
                }
    user_agent = {'Referer': urlReferer,
                  'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
                 }
    r = requests.post(urlResponse, data=form_data, headers=user_agent)
