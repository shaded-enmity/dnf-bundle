FROM fedora:22
MAINTAINER Pavel Odvody <podvody@redhat.com>

RUN dnf install -y automake cmake curl-devel check-devel\
                   dnf-plugins-core gcc git glib2-devel gpgme-devel\
                   libxml2-devel  make openssl-devel which xz\
 && dnf -y builddep rpm libsolv python3\
 && rm -rf /var/cache/dnf/*

RUN git clone https://github.com/rpm-software-management/rpm.git\
 && (cd rpm/\
  && ./autogen.sh --prefix=/usr --with-external-db --enable-python CPPFLAGS="-I/usr/include/nspr4 -I/usr/include/nss3"\
  && make)\
 && git clone https://github.com/openSUSE/libsolv.git\
 && (cd libsolv/ && mkdir build && cd build/\ 
  && cmake -DENABLE_LZMA_COMPRESSION=1 -DENABLE_COMPLEX_DEPS=1 -DUSE_VENDORDIRS=1 -DFEDORA=1 -DCMAKE_INSTALL_PREFIX=/usr ../\
  && make && make install)\
 && git clone https://github.com/rpm-software-management/hawkey.git\
  && (cd hawkey/ && mkdir build && cd build/\
  && cmake -DPYTHON_DESIRED="3" ../ && make)\
 && git clone https://github.com/rpm-software-management/librepo.git\
  && (cd librepo/ && mkdir build && cd build/\
  && cmake -DPYTHON_DESIRED="3" ../ && make librepo)\
 && git clone https://github.com/rpm-software-management/libcomps.git\
  && (cd libcomps/libcomps/\
  && cmake -DPYTHON_DESIRED="3" && make libcomps)\
 && git clone https://github.com/python/cpython.git\
  && (cd cpython/ && git checkout 3.4\
  && ./configure --enable-shared && make) 

CMD ["bash"]
