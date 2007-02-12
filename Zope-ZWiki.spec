%define 	zope_subname	ZWiki
# %%define		sub_ver	rc1
Summary:	Zope product which allows you to build wiki webs in Zope
Summary(pl.UTF-8):   Produkt Zope umożliwiający budowanie stron WWW typu wiki
Name:		Zope-%{zope_subname}
Version:	0.49.0
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://zwiki.org/releases/%{zope_subname}-%{version}.tgz
# Source0-md5:	ec7d61cbff03ad304c3d22bdb375df13
URL:		http://zwiki.org/FrontPage/
BuildRequires:	python
BuildRequires:	rpmbuild(macros) >= 1.268
Requires(post,postun):	/usr/sbin/installzopeproduct
Requires:	Zope
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ZWiki is a Zope product which allows you to build wiki webs in Zope.

%description -l pl.UTF-8
ZWiki to produkt Zope umożliwiający budowanie stron WWW typu wiki.

%prep
%setup -q -n %{zope_subname}

%build
mkdir docs
mv -f {CHANGES.txt,README.txt} docs

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -af * $RPM_BUILD_ROOT%{_datadir}/%{name}

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/docs

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/installzopeproduct %{_datadir}/%{name} %{zope_subname}
%service -q zope restart

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/installzopeproduct -d %{zope_subname}
	%service -q zope restart
fi

%files
%defattr(644,root,root,755)
%doc docs/*
%{_datadir}/%{name}
