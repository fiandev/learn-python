import urllib2,random, json
fjson = open("file.json")
data = json.load(fjson)
urls = data["urls"]
i = 0
totalFile = len(urls)
for url in urls:
  i = i + 1
  file_name = str(random.randint(0,9999)) + ".jpg"
  u = urllib2.urlopen(url)
  f = open("result/"+file_name, 'wb')
  meta = u.info()
  file_size = int(meta.getheaders("Content-Length")[0])
  print "%s/%s Downloading: %s \nBytes: %s" % (i, totalFile, file_name, file_size)
  
  file_size_dl = 0
  block_sz = 1000000 * 5
  while True:
      buffer = u.read(block_sz)
      if not buffer:
          break
  
      file_size_dl += len(buffer)
      f.write(buffer)
      status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
      status = status + chr(8)*(len(status)+1)
      print status,"\n"
  f.close()