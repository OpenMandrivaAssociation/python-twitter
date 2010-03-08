%define name	python-twitter
%define version 0.6
%define release %mkrel 1

Summary:	Python bingings for Twitter
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://python-twitter.googlecode.com/files/%{name}-%{version}.tar.gz
License:	ASL 2.0
Group:		Development/Python
Url:		http://code.google.com/p/python-twitter/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	python-setuptools
Requires:	python-simplejson

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
