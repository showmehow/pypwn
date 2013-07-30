#!/usr/bin/env python

import postfile

host = "www.virustotal.com"
selector = "https://www.virustotal.com/vtapi/v2/file/scan"
fields = [("apikey","68f20b074f062331cbf1e31bb54e2fc42954bc04756f205d90582be4e94aaef6")]
file_to_send = open("test.php","rb").read()
files = [("file","test.php", file_to_send)]
json = postfile.post_multipart(host,selector, fields, files)
print json
