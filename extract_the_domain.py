def domain_name(url):
    result = []
    itemstoremove = ["www"]
    if url.find("://")!=-1:
        url = url[url.find("://")+3:]
    if url.find("/")!=-1:
        url = url[:url.find("/")]
    result = url.split(".")
    for x in result:
        if x in itemstoremove:
            result.remove(x)

    return result[0]

print(domain_name("http://google.com"))
print(domain_name("http://google.co.jp"))
print(domain_name("www.xakep.ru"))
print(domain_name("https://youtube.com"))
print(domain_name("http://www.mercadolibre.com/laporongasuelta/culos"))