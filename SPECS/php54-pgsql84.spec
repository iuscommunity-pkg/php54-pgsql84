%global php_base php54
%global php_ver 5.4.41
%global php_basever 5.4

Summary: A PostgreSQL 8.4 database module for PHP
Name: %{php_base}-pgsql84
Version: %{php_ver}
Release: 1.ius%{?dist}
Group: Development/Languages
License: PHP
URL: http://php.net
Source0: http://www.php.net/distributions/php-%{php_ver}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%if 0%{?fedora} >= 11 || 0%{?rhel} >= 6
BuildRequires: postgresql-devel >= 8.4
%else
BuildRequires: postgresql84-devel
%endif
BuildRequires: krb5-devel, openssl-devel
BuildRequires: %{php_base}-devel >= %{php_ver}
Requires: %{php_base}-pdo%{?_isa} >= %{version}

Conflicts: %{php_base}-pgsql
Conflicts: php-pgsql < %{php_basever}
Conflicts: php-pdo-pgsql < %{php_basever}
Provides: php-pgsql = %{version}-%{release}, php-pgsql%{?_isa} = %{version}-%{release}
Provides: php-pdo-pgsql = %{version}-%{release}
Provides: %{php_base}-pdo-pgsql = %{version}-%{release}
Provides: php_database, %{php_base}_database
Provides: php-pdo_pgsql, php-pdo_pgsql%{?_isa}
Provides: %{php_base}-pdo_pgsql, %{php_base}-pdo_pgsql%{?_isa}
Provides: config(php-pgsql) = %{version}-%{release}


%description 
The php-pgsql package includes a dynamic shared object (DSO) that can
be compiled in to the Apache Web server to add PostgreSQL database
support to PHP. PostgreSQL is an object-relational database management
system that supports almost all SQL constructs. PHP is an
HTML-embedded scripting language. If you need back-end support for
PostgreSQL, you should install this package in addition to the main
php package.


%prep
%setup -q -n php-%{php_ver}
cp -a ext/pgsql/README README.pgsql
cp -a ext/pgsql/CREDITS CREDITS.pgsql
cp -a ext/pdo_pgsql/CREDITS CREDITS.pdo_pgsql

%build
pushd ext/pgsql
phpize
%configure  --prefix=%{_prefix} \
            --disable-rpath \
            --with-pgsql=shared 

make %{?_smp_mflags}
popd

pushd ext/pdo_pgsql
phpize
%configure  --prefix=%{_prefix} \
            --disable-rpath \
            --enable-pdo=shared \
            --with-pdo-pgsql=shared,%{_prefix}

make %{?_smp_mflags}
popd


%install
rm -rf $RPM_BUILD_ROOT
%{__mkdir} -p   %{buildroot}%{_sysconfdir}/php.d \
                %{buildroot}%{_libdir}/php/modules
%{__install} ext/pgsql/modules/pgsql.so %{buildroot}%{_libdir}/php/modules/pgsql.so
%{__install} ext/pdo_pgsql/modules/pdo_pgsql.so %{buildroot}%{_libdir}/php/modules/pdo_pgsql.so

# the configs
cat >%{buildroot}%{_sysconfdir}/php.d/pgsql.ini <<EOF
; PostGreSQL 8.4 Module Configuration
extension=pgsql.so
EOF

cat >%{buildroot}%{_sysconfdir}/php.d/pdo_pgsql.ini <<EOF
; PostGreSQL 8.4 PDO Module Configuration
extension=pdo_pgsql.so
EOF


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc LICENSE README.pgsql CREDITS.pgsql CREDITS.pdo_pgsql
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/pgsql.ini
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/pdo_pgsql.ini
%{_libdir}/php/modules/pgsql.so
%{_libdir}/php/modules/pdo_pgsql.so

%changelog
* Fri May 15 2015 Ben Harper <ben.harper@rackspace.com> - 5.4.41-1.ius
- Latest upstream

* Thu Apr 16 2015 Ben Harper <ben.harper@rackspace.com> - 5.4.40-1.ius
- Latest upstream

* Fri Mar 20 2015 Carl George <carl.george@rackspace.com> - 5.4.39-1.ius
- Latest upstream

* Thu Feb 19 2015 Ben Harper <ben.harper@rackspace.com> - 5.4.38-1.ius
- Latest upstream

* Fri Jan 23 2015 Carl George <carl.george@rackspace.com> - 5.4.37-1.ius
- Add missing provides
- Remove redundant requirements
- Latest upstream

* Fri Dec 19 2014 Ben Harper <ben.harper@rackspace.com> - 5.4.36-1.ius
- Latest sources from upstream

* Fri Nov 14 2014 Ben Harper <ben.harper@rackspace.com> - 5.4.35-1.ius
- Latest sources from upstream

* Mon Oct 20 2014 Ben Harper <ben.harper@rackspace.com> - 5.4.34-1.ius
- Latest sources from upstream

* Fri Sep 19 2014 Ben Harper <ben.harper@rackspace.com> - 5.4.33-1.ius
- Latest sources from upstream

* Fri Aug 22 2014 Ben Harper <ben.harper@rackspace.com> - 5.4.32-1.ius
- Latest sources from upstream

* Fri Jul 25 2014 Carl George <carl.george@rackspace.com> - 5.4.31-1.ius
- Latest sources from upstream

* Fri Jun 27 2014 Carl George <carl.george@rackspace.com> - 5.4.30-1.ius
- Latest sources from upstream

* Fri May 30 2014 Carl George <carl.george@rackspace.com> - 5.4.29-1.ius
- Latest sources from upstream

* Fri May 02 2014 Carl George <carl.george@rackspace.com> - 5.4.28-1.ius
- Latest sources from upstream

* Fri Apr 04 2014 Ben Harper <ben.harper@rackspace.com> - 5.4.27-1.ius
- Latest sources from upstream

* Fri Mar 07 2014 Ben Harper <ben.harper@rackspace.com> - 5.4.26-1.ius
- Latest sources from upstream

* Fri Feb 07 2014 Ben Harper <ben.harper@rackspace.com> - 5.4.25-1.ius
- Latest sources from upstream

* Fri Jan 10 2014 Ben Harper <ben.harper@rackspace.com> - 5.4.24-1.ius
- Latest sources from upstream

* Fri Dec 13 2013 Ben Harper <ben.harper@rackspace.com> - 5.4.23-1.ius
- Latest sources from upstream

* Fri Nov 15 2013 Ben Harper <ben.harper@rackspace.com> - 5.4.22-1.ius
- Latest sources from upstream

* Fri Oct 18 2013 Ben Harper <ben.harper@rackspace.com> - 5.4.21-1.ius
- Latest sources from upstream

* Fri Sep 20 2013 Ben Harper <ben.harper@rackspace.com> - 5.4.20-1.ius
- Latest sources from upstream

* Fri Aug 23 2013 Ben Harper <ben.harper@rackspace.com> - 5.4.19-1.ius
- Latest sources from upstream

* Fri Aug 16 2013 Ben Harper <ben.harper@rackspace.com> - 5.4.18-1.ius
- Latest sources from upstream

* Mon Jul 08 2013 Ben Harper <ben.harper@rackspace.com> - 5.4.17-1.ius
- Rebulding for php 5.4.17

* Fri Jun 07 2013 Ben Harper <ben.harper@rackspace.com> - 5.4.16-1.ius
- Rebulding for php 5.4.16

* Thu May 09 2013 Ben Harper <ben.harper@rackspace.com> - 5.4.15-1.ius
- Rebulding for php 5.4.15

* Fri Apr 12 2013 Ben Harper <ben.harper@rackspace.com> - 5.4.14-1.ius
- Rebulding for php 5.4.14

* Fri Mar 15 2013 Ben Harper <ben.harper@rackspace.com> - 5.4.13-1.ius
- Rebulding for php 5.4.13

* Fri Feb 22 2013 Ben Harper <ben.harper@rackspace.com> - 5.4.12-1.ius
- Rebulding for php 5.4.12

* Thu Jan 17 2013 Ben Harper <ben.harper@rackspace.com> - 5.4.11-1.ius
- Rebulding for php 5.4.11

* Thu Dec 20 2012 Ben Harper <ben.harper@rackspace.com> - 5.4.10-1.ius
- Rebulding for php 5.4.10

* Mon Nov 26 2012 Ben Harper <ben.harper@rackspace.com> - 5.4.9-1.ius
-Rebulding for php 5.4.9

* Mon Oct 29 2012 Ben Harper <ben.harper@rackspace.com> - 5.4.8-1.ius
-Rebulding for php 5.4.8
   
* Tue Aug 21 2012 Jeffrey Ness <jeffrey.ness@rackspace.com> - 5.4.3-2.ius
- Rebuilding against php54-5.4.6-2.ius as it is now using bundled PCRE.

* Fri May 11 2012 Dustin Henry Offutt <dustin.offutt@rackspace.com> - 5.4.3-1.ius
- Rebuild for php 5.4.3
- Adjust Buildrequires for el6

* Fri Aug 19 2011 Jeffrey Ness <jeffrey.ness@rackspace.com> - 5.3.5-2.ius
- Rebuilding

* Wed Feb 02 2011 BJ Dierkes <wdierkes@rackspace.com> - 5.3.5-1.ius
- Rebuild for php 5.3.5
- BuildRequires php53u >= %%{php_ver}

* Fri Dec 17 2010 BJ Dierkes <wdierkes@rackspace.com> - 5.3.4-1.ius
- Renamed as php53u-pgsql84.  Resolves LP#691755
- Rebuild against php53u-5.3.4

* Mon Jul 26 2010 BJ Dierkes <wdierkes@rackspace.com> - 5.3.3-1.ius
- Latest php source from upstream.

* Tue Jun 15 2010 BJ Dierkes <wdierkes@rackspace.com> - 5.3.2-1.ius
- Initial spec build

