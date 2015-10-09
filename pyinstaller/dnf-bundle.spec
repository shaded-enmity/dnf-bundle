Name:		dnf-bundle
Version:	1.1.2
Release:	4%{?dist}
Summary:	Self-contained DNF executable bundle

License:	MIT
URL:		https://github.com/shaded-enmity/%{name}
Source0:	TBD

BuildRequires:	TBD
Requires:	TBD

%description


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
%make_install


%files
%doc



%changelog

