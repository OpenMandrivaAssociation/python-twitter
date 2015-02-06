%define name	python-twitter
%define version 0.6
%define release 2

Summary:	Python bindings for Twitter
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	ASL 2.0
Group:		Development/Python
Url:		http://code.google.com/p/python-twitter/
Source0:	http://python-twitter.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRequires:	python-setuptools
Requires:	python-simplejson
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This library provides a pure python interface for the Twitter API.

Twitter (http://twitter.com) provides a service that allows people to connect
via the web, IM, and SMS. Twitter exposes a web services API
(http://twitter.com/help/api) and this library is intended to make it even
easier for python programmers to use. 

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot} --install-purelib=%{py_platsitedir}
chmod a+r %{buildroot}%{py_platsitedir}/*/*

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{py_platsitedir}/*


%changelog
* Sat Jun 25 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.6-1mdv2011.0
+ Revision: 687047
- revert to original project, this one is not the same

* Mon Nov 22 2010 Funda Wang <fwang@mandriva.org> 1.4.2-2mdv2011.0
+ Revision: 599635
- rebuild for py2.7

* Sun Sep 12 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.4.2-1mdv2011.0
+ Revision: 577779
- new version

* Mon Mar 08 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.6-1mdv2010.1
+ Revision: 515900
- update to 0.6

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.5-3mdv2010.0
+ Revision: 442524
- rebuild

* Mon Feb 16 2009 Colin Guthrie <cguthrie@mandriva.org> 0.5-2mdv2009.1
+ Revision: 341123
- Fix permissions

* Mon Feb 16 2009 Colin Guthrie <cguthrie@mandriva.org> 0.5-1mdv2009.1
+ Revision: 341121
- imported package python-twitter


