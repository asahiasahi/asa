
from bs4 import BeautifulSoup
import lxml
html = """
<html>
<head>
</head>
<body>
<a href="https://google.com">google</a>
</body>
</html>
"""

soup = BeautifulSoup(html,"lxml")
print(soup.find("a")["href"])
