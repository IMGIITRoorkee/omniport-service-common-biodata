import re
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


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
    

class SemicolonSeparatedURLValidator:
    def __init__(self):
        self.single_url_validator = UpdatedURLValidator()

    def __call__(self, value):
        if not value:
            return
        urls = [url.strip() for url in value.split(";") if url.strip()]
        for url in urls:
            self.single_url_validator(url)

class CommaSeparatedURLValidator:
    """
    Validates a comma-separated list of URLs using UpdatedURLValidator.
    """

    def __init__(self):
        self.single_url_validator = UpdatedURLValidator()

    def __call__(self, value):
        if not value:
            return
        urls = [url.strip() for url in value.split(",") if url.strip()]
        errors = []
        for url in urls:
            try:
                self.single_url_validator(url)
            except ValidationError as e:
                errors.append(f"'{url}': {e.messages[0]}")

        if errors:
            raise ValidationError("Invalid URL(s): " + "; ".join(errors))