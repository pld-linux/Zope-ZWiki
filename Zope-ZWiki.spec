
%include	/usr/lib/rpm/macros.python
%define 	zope_subname	ZWiki
# %%define		sub_ver	rc1
Summary:	Zope product which allows you to build wiki webs in Zope
Summary(pl):	Produkt Zope umo¿liwiaj±cy budowanie stron WWW typu wiki
Name:		Zope-%{zope_subname}
Version:	0.27.1
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://zwiki.org/releases/%{zope_subname}-%{version}.tgz
# Source0-md5:	4a255182c6dd4ebcb2163cf64c33746e
URL:		http://zwiki.org/FrontPage/
Requires(post,postun):	/usr/sbin/installzopeproduct
%pyrequires_eq	python-modules
Requires:	Zope
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ZWiki is a Zope product which allows you to build wiki webs in Zope.

%description -l pl
ZWiki to produkt Zope umo¿liwiaj±cy budowanie stron WWW typu wiki.

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
