About CPython/Freeze
--------------------

Since the `Freeze` tool requires *object* files (*.o), we can't use the already present shared objects (*.so) and need to build
from scratch.

The challenge is that `./freeze.py` has some mythical files in its toolchain, the closest I got with `Setup`:

```
librepo._librepo /librepo/build/librepo/CMakeFiles/librepo.dir/repoconf.c.o /librepo/build/librepo/CMakeFiles/librepo.dir/gpg.c.o /librepo/build/librepo/CMakeFiles/librepo.dir/downloader.c.o /librepo/build/librepo/CMakeFiles/librepo.dir/mirrorlist.c.o /librepo/build/librepo/CMakeFiles/librepo.dir/metalink.c.o /librepo/build/librepo/CMakeFiles/librepo.dir/handle.c.o /librepo/build/librepo/CMakeFiles/librepo.dir/checksum.c.o /librepo/build/librepo/CMakeFiles/librepo.dir/util.c.o /librepo/build/librepo/CMakeFiles/librepo.dir/package_downloader.c.o /librepo/build/librepo/CMakeFiles/librepo.dir/repoutil_yum.c.o /librepo/build/librepo/CMakeFiles/librepo.dir/yum.c.o /librepo/build/librepo/CMakeFiles/librepo.dir/repomd.c.o /librepo/build/librepo/CMakeFiles/librepo.dir/lrmirrorlist.c.o /librepo/build/librepo/CMakeFiles/librepo.dir/fastestmirror.c.o /librepo/build/librepo/CMakeFiles/librepo.dir/xmlparser.c.o /librepo/build/librepo/CMakeFiles/librepo.dir/url_substitution.c.o /librepo/build/librepo/CMakeFiles/librepo.dir/result.c.o /librepo/build/librepo/CMakeFiles/librepo.dir/downloadtarget.c.o /librepo/build/librepo/CMakeFiles/librepo.dir/rcodes.c.o
```

Fails in GCC because it's trying to name a variable `librepo._librepo` and the dot obviously hurts it.
