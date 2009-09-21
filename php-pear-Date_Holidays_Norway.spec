%define		_class		Date
%define		_subclass	Holidays
%define		_region		Norway
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}_%{_region}

Summary:	Driver based class to calculate holidays in %{_region}
Name:		php-pear-%{_pearname}
Version:	0.1.2
Release:	%mkrel 2
License:	PHP License
Group:		Development/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tar.bz2
URL:		http://pear.php.net/package/%{_pearname}/
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
Requires:	php-pear-Date_Holidays >= 0.21.1
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
%{_pearname} is the Date_Holidays driver for %{_region} region.

In PEAR status of this package is: %{_status}.

%prep
%setup -q -c

%install
rm -rf %{buildroot}

#TODO: ajouter les tests ?

install -d %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/Driver
install %{_pearname}-%{version}/%{_subclass}/Driver/*.php %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/Driver

install -d %{buildroot}%{_datadir}/pear/packages
install -m0644 package.xml %{buildroot}%{_datadir}/pear/packages/%{_pearname}.xml

%post
if [ "$1" = "1" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear install --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi
if [ "$1" = "2" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear upgrade -f --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi

%preun
if [ "$1" = 0 ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear uninstall --nodeps -r %{_pearname}
	fi
fi

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}/%{_subclass}/Driver/*.php
%{_datadir}/pear/packages/%{_pearname}.xml
