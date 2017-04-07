Summary:       Scriptable database and system performance benchmark
Name:          sysbench
# Version will be replaced by packpack
Version:       x.y.z
Release:       1%{?dist}
License:       GPLv2+
Group:         Applications/System
Source0:       https://github.com/akopytov/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
URL:           https://github.com/akopytov/sysbench/

%if 0%{?el6}
BuildRequires: mysql-devel
%else
BuildRequires: mariadb-devel
%endif
BuildRequires: postgresql-devel
BuildRequires: make
BuildRequires: automake
BuildRequires: libtool
BuildRequires: pkgconfig
BuildRequires: libaio-devel
BuildRequires: vim-common
# Tests
BuildRequires: /usr/bin/cram

ExclusiveArch:  %{arm} %{ix86} x86_64 %{mips} aarch64


%description
sysbench is a modular, cross-platform and multi-threaded benchmark
tool for evaluating OS parameters that are important for a system
running a database under intensive load.

The idea of this benchmark suite is to quickly get an impression about
system performance without setting up complex database benchmarks or
even without installing a database at all. Current features allow to
test the following system parameters:
- file I/O performance
- scheduler performance
- memory allocation and transfer speed
- POSIX threads implementation performance
- database server performance (OLTP benchmark)

Primarily written for MySQL server benchmarking, sysbench will be
further extended to support multiple database backends, distributed
benchmarks and third-party plug-in modules.


%prep
%setup -q

%build
export CFLAGS="%{optflags}"
autoreconf -vif
%configure --with-mysql \
           --with-pgsql \

%make_build

%install
%make_install
rm -f %{buildroot}%{_docdir}/sysbench/manual.html

%check
make test

%files
%doc ChangeLog COPYING README.md
%license COPYING
%{_bindir}/*
%{_datadir}/%{name}


%changelog
* Thu Apr  6 2017 Alexey Kopytov <akopytov@gmail.com> - 1.0.5-1
- Reuse downstream Fedora spec with modifications (prefer bundled libraries)

* Mon Mar 13 2017 Xavier Bachelot <xavier@bachelot.org> 1.0.4-2
- Don't build aarch64 on el7.

* Mon Mar 13 2017 Xavier Bachelot <xavier@bachelot.org> 1.0.4-1
- Fix build for i686.
- Drop bundled cram.

* Wed Mar 08 2017 Xavier Bachelot <xavier@bachelot.org> 1.0.3-1
- Update to 1.0.3 (RHBZ#1424670).
- Restrict arches to the same ones as luajit.
- Add --with-gcc-arch=native to configure for %%{arm} and aarch64.
- Ignore test suite results for aarch64, it segfaults in koji.

* Sat Feb 25 2017 Xavier Bachelot <xavier@bachelot.org> 1.0.2-2
- Run test suite.

* Sat Feb 25 2017 Xavier Bachelot <xavier@bachelot.org> 1.0.2-1
- Update to 1.0.2 (RHBZ#1424670).

* Sun Feb 12 2017 Honza Horak <hhorak@redhat.com> - 1.0.0-1
- Update to the first proper release 1.0.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.12-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.12-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.12-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Sep 04 2014 Xavier Bachelot <xavier@bachelot.org> 0.4.12-12
- Modernize specfile.

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.12-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.12-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Sep 06 2011 Xavier Bachelot <xavier@bachelot.org> 0.4.12-5
- Add BR: libaio-devel (rhbz#735882).

* Wed Mar 23 2011 Dan Horák <dan@danny.cz> - 0.4.12-4
- rebuilt for mysql 5.5.10 (soname bump in libmysqlclient)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 24 2010 Xavier Bachelot <xavier@bachelot.org> 0.4.12-2
- Rebuild against new mysql.

* Wed Jul 07 2010 Xavier Bachelot <xavier@bachelot.org> 0.4.12-1
- Update to 0.4.12.

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 0.4.10-5
- rebuilt with new openssl

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Mar 18 2009 Xavier Bachelot <xavier@bachelot.org> 0.4.10-3
- License is GPLv2+, not GPLv2.

* Sat Mar 14 2009 Xavier Bachelot <xavier@bachelot.org> 0.4.10-2
- Make postgres support optional, the version in rhel4 is too old.
- Drop TODO and manual.html from %%doc, they are empty.

* Thu Mar 05 2009 Xavier Bachelot <xavier@bachelot.org> 0.4.10-1
- Adapt original spec file taken from PLD.
