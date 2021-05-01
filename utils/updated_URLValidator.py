import re
from django.core.validators import URLValidator


class UpdatedURLValidator(URLValidator):
    """
    This class adds _ (underscore) to the existing RegEx for URLValidator
    """

    hostname_re = URLValidator.hostname_re.replace(
        '0-9]', '0-9_]').replace('0-9-]', '0-9-_]')
    domain_re = URLValidator.domain_re.replace('0-9-]', '0-9-_]')
    host_re = '(' + hostname_re + domain_re + \
        URLValidator.tld_re + '|localhost)'

    regex = re.compile(
        r'^(?:[a-z0-9.+-]*)://'  # scheme
        r'(?:[^\s:@/]+(?::[^\s:@/]*)?@)?'  # user:pass authentication
        r'(?:' + URLValidator.ipv4_re + '|' + \
        URLValidator.ipv6_re + '|' + host_re + ')'
        r'(?::\d{2,5})?'  # port
        r'(?:[/?#][^\s]*)?'  # resource path
        r'\Z', re.IGNORECASE)
