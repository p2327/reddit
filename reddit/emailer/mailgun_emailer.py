import os
import configparser
import requests
from requests.exceptions import HTTPError


def send_email(html: str) -> None:
    """
    Take an HTML templates and send email using Mailgun API.
    """
    # Set API params
    config = configparser.ConfigParser()
    config.read(os.path.join(
        os.path.abspath(os.path.dirname(__file__)), 'settings.cfg')
        )
    key = config.get('Mailgun', 'api')
    domain = config.get('Mailgun', 'domain')

    # Set requests params
    request_url = 'https://api.mailgun.net/v3/sandbox5e559bf297f8421bace259e0f7021069.mailgun.org/messages'.format(domain)
    payload = {
        'from': 'mailgun@sandbox5e559bf297f8421bace259e0f7021069.mailgun.org',
        'to': 'pquadro@gmail.com',
        'subject': 'Top posts this week',
        'html': html,
    }

    try:
        r = requests.post(request_url, auth=('api', key), data=payload)
        r.raise_for_status()
        print('Success!')
    except HTTPError as e:
        print(f'Error {e.response.status_code}')