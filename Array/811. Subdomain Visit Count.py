from typing import *
from collections import defaultdict

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        # split the domain name and its count from string to list
        domains = [ domain.split() for domain in cpdomains]
        result = defaultdict(int)

        # iterate over all domain given in input
        for count, url in domains:
            count = int(count)

            # split all the given url
            url_parts = url.split('.')

            # if at least 1 domain then add in total
            if len(url_parts) >= 1:
                result['.'.join(url_parts[-1:])] += count
            
            # if at least 2 domain then add combination in total
            if len(url_parts) >= 2:
                result['.'.join(url_parts[-2:])] += count

            # if at least 3 domain then add full url in total
            if len(url_parts) >= 3:
                result['.'.join(url_parts)] += count
        
        return [ f"{count} {url}" for url, count in result.items()]


if __name__ == "__main__":
    s = Solution()

    inp = ["9001 discuss.leetcode.com"]
    print(s.subdomainVisits(inp))

    inp = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
    print(s.subdomainVisits(inp))
