# 
# WARNING: This version make error connection refused on Zope 2.7.0b3!
#
%include	/usr/lib/rpm/macros.python
%define 	zope_subname	ZWiki
Summary:	Zope product allows you to build wiki webs in zope
Summary(pl):	Produkt Zope umo¿liwiaj±cy budowanie stron WWW typu wiki
Name:		Zope-%{zope_subname}
%define		sub_ver rc2
Version:	0.25.0
Release:	1.%{sub_ver}.1
License:	GPL
Group:		Development/Tools
Source0:	http://zwiki.org/releases/%{zope_subname}-%{version}%{sub_ver}.tgz
# Source0-md5:	a1533c6d82c578a6cb19d9ca91d98dda
URL:		http://zwiki.org/FrontPage/
%pyrequires_eq	python-modules
Requires:	Zope
Requires(post,postun):	/usr/sbin/installzopeproduct
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Zope product allows you to build wiki webs in zope

%description -l pl
Produkt Zope umo¿liwiaj±cy budowanie stron WWW typu wiki

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
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/installzopeproduct -d %{zope_subname}
	if [ -f /var/lock/subsys/zope ]; then
		/etc/rc.d/init.d/zope restart >&2
	fi
fi

%files
%defattr(644,root,root,755)
%doc docs/*
%{_datadir}/%{name}
