# thing
"thing" python database using dicts


usage:

```
import thing
secret = "<secret here>"
tdb = thing.start("path/to/db.thing", secret)

tdb['demo'] = "Thing is awesome!"

thing.save(tdb, "path/to/db.thing", secret)
```

"secret" is a 32 byte string used to decrypt the file; it is optional but must be used every time after used to save it once.

Upon first use you will need to do:

```
import thing
secret = "<secret here>"
thing.save({}, "path/to/db.thing", secret)
```

how to install:

```
git clone https://github.com/ItsLukeJames/thing.git thing
cd thing
python setup.py install
```

https://pypi.python.org/pypi/thingdb
