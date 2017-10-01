test messenger bot trên pythonanywhere với flask

Cấu hình file wsgi

<pre><code>
import sys
path = '/home/boycq9x/messenger-bot'
if path not in sys.path:
   sys.path.append(path)

from bot import app as application</code></pre>
