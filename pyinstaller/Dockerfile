FROM fedora:22
MAINTAINER Pavel Odvody <podvody@redhat.com>

ENV PYI_COM='e2ad398556f0d7bec5bb5d266a0a558a46e116a5'
ENV LANG=en_US.utf8

RUN dnf install -y git python-pip which\
 && rm -rf /var/cache/dnf/*\
 && useradd pyinstaller\
 && git clone https://github.com/pyinstaller/pyinstaller\
  && (cd pyinstaller\
  && git checkout ${PYI_COM}) && chown -R pyinstaller:pyinstaller /pyinstaller\
 && (su pyinstaller -c "cd pyinstaller/ && python pyinstaller.py -F $(which dnf)")\
 && rpm -ev python-setuptools python-pip python-libs python-hawkey python-six pygpgme python-dnf python pyliblzma python-libcomps python-iniparse python-librepo rpm-python dnf dnf-yum\
 && cp /pyinstaller/dnf/dist/dnf /usr/bin/udnf\
 && rm -rf /pyinstaller

ENTRYPOINT ["/usr/bin/udnf"]
