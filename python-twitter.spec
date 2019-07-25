Summary:	Python bindings for Twitter
Name:		python-twitter
Version:	1.18.0
Release:	1
License:	ASL 2.0
Group:		Development/Python
Url:		http://code.google.com/p/python-twitter/
Source0:	https://files.pythonhosted.org/packages/8a/9d/cea0ec784ba05d56fbd8a56a674ca12d9b012487528ce91e0064b19224f7/twitter-1.18.0.tar.gz
BuildRequires:	python-setuptools
Requires:	python-simplejson

%description
This library provides a pure python interface for the Twitter API.

Twitter (http://twitter.com) provides a service that allows people to connect
via the web, IM, and SMS. Twitter exposes a web services API
(http://twitter.com/help/api) and this library is intended to make it even
easier for python programmers to use. 

%prep
%setup -qn twitter-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot} --install-purelib=%{py_platsitedir}
chmod a+r %{buildroot}%{py_platsitedir}/*/*

%files
%{_bindir}/twitter*
%{py_platsitedir}/*
