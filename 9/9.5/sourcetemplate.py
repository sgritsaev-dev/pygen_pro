def sourcetemplate(url):
    def requests(**kwargs):
        counter = 0
        for key, value in sorted(kwargs.items()):
            nonlocal url
            if counter == 0:
                url += '?'
                counter += 1
            elif counter > 0:
                url += '&'
            req = str(key) + '=' + str(value)
            url += req
        return url
    return requests


# TEST_4:
url = 'https://all_for_comfort_life.com'
load = sourcetemplate(url)
print(load(smartphone='iPhone', notebook='huawei', sale=True))
