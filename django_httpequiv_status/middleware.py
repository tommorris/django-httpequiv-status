from bs4 import BeautifulSoup
import re

def parse_status_code_from_status_string(status_str):
    after_first_non_numeric_char = re.compile('[^\d].+')
    stripped_str = after_first_non_numeric_char.sub('', status_str)
    return int(stripped_str)

class HttpEquivStatusMiddleware(object):
    def process_response(self, request, response):
        if response.streaming:
            override_status = get_http_equiv(response.streaming_content)
        else:
            override_status = self.get_http_equiv(response.content)
        if override_status is not None:
            response.status_code = override_status
        return response

    def get_http_equiv(self, content):
        soup = BeautifulSoup(content)
        matching_tags = [x for x in soup.find_all("meta") if
                         x['http-equiv'] == "Status" and
                         len(x['content']) > 0]
        if len(matching_tags) > 0:
            status_str = matching_tags[0]['content']
            status = parse_status_code_from_status_string(status_str)
            return status
        return None