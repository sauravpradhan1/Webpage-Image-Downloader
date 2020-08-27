import urllib.request


# Adding information about user agent
opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)


def downloadImage(imageUrl, filename):

    # calling urlretrieve function to get resource
    urllib.request.urlretrieve(imageUrl, filename)