'''
Pattern to match any IPV4 Address:

'''
import re

ipv4_pattern = r'[]'

test_str = "123 456"

print(re.findall(ipv4_pattern, test_str))
