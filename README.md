# thing2
"thing" python database using dicts [![Codacy Badge](https://api.codacy.com/project/badge/grade/83fa6dc499a54f2c9cf575c14eac6a07)] (https://www.codacy.com/app/me_64/thing) [![PyPI](https://img.shields.io/pypi/dm/thingdb.svg)](https://pypi.python.org/pypi/thingdb)


usage:

```
import thingdb
tdb = thingdb.thing("path/to/db")

tdb['demo'] = "Thing is awesome!"

tdb.sync()

#When finished with a DB

tdb.close()
```
installation:

```
sudo pip install thingdb
```

installation(dev):

```
sudo pip install git+https://github.com/dev-zz/thing
```

https://pypi.python.org/pypi/thingdb


[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/dev-zz/thing/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

