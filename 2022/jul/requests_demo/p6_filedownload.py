import re
import requests
# image_url = "https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"
# r = requests.get(image_url)
# with open('python_logo.png','wb') as f:
#     f.write(r.content)

file_url = "http://codex.cs.yale.edu/avi/db-book/db4/slide-dir/ch1-2.pdf"
r = requests.get(file_url,stream=True)
with open('python.pdf','wb') as pdf:
    for chunk in r.iter_content(chunk_size=1024):
        if chunk:
            pdf.write(chunk)