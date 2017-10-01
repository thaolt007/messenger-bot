test messenger bot on pythonanywhere use flask

Cau hinh file wsgi

<pre><code>import sys
path = '/home/boycq9x/messenger-bot'
if path not in sys.path:
   sys.path.append(path)

from bot import app as application</code></pre>
