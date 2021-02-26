Summary:	TDB - Trivial Database
Summary(pl.UTF-8):	TDB - prosta baza danych
Name:		tdb
Version:	1.4.3
Release:	2
Epoch:		2
License:	LGPL v3+
Group:		Libraries
Source0:	https://www.samba.org/ftp/tdb/%{name}-%{version}.tar.gz
# Source0-md5:	e638e8890f743624a754304b3f994f4d
URL:		https://tdb.samba.org/
BuildRequires:	libbsd-devel
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.507
Obsoletes:	tdb-extras
# tdb 1.4+ dropped python2 suport
Obsoletes:	python-tdb
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TDB is a Trivial Database. In concept, it is very much like GDBM, and
BSD's DB except that it allows multiple simultaneous writers and uses
locking internally to keep writers from trampling on each other. TDB
is also extremely small.

%description -l pl.UTF-8
TDB to Trivial Database, czyli prosta baza danych. W założeniach jest
bardzo podobna do GDBM lub DB z BSD z wyjątkiem tego, że pozwala na
zapis wielu procesom jednocześnie i używa wewnętrznie blokowania, aby
nie pozwolić piszącym na zadeptanie się nawzajem. TDB jest ponadto
ekstremalnie mała.

%package devel
Summary:	Header files for TDB library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki TDB
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	tdb-static

%description devel
Header files for TDB library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki TDB.

%package -n python3-tdb
Summary:	Python 3 bindings for TDB
Summary(pl.UTF-8):	Interfejs Pythona 3 do TDB
Group:		Libraries/Python
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	python3-libs >= 1:3.2

%description -n python3-tdb
Python 3 bindings for TDB.

%description -n python3-tdb -l pl.UTF-8
Interfejs Pythona 3 do TDB.

%prep
%setup -q

%build
export JOBS=1

CC="%{__cc}" \
CFLAGS="%{rpmcflags}" \
%{__python3} buildtools/bin/waf configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--disable-rpath

%{__make} \
	V=1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py3_comp $RPM_BUILD_ROOT%{py3_sitedir}
%py3_ocomp $RPM_BUILD_ROOT%{py3_sitedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%triggerpostun -p /sbin/postshell -- tdb < 2:1.2.9-2
-rm -f %{_libdir}/libtdb.so.1
/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc docs/{README,mutex.txt,tracing.txt}
%attr(755,root,root) %{_bindir}/tdbbackup
%attr(755,root,root) %{_bindir}/tdbdump
%attr(755,root,root) %{_bindir}/tdbrestore
%attr(755,root,root) %{_bindir}/tdbtool
%attr(755,root,root) %{_libdir}/libtdb.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtdb.so.1
%{_mandir}/man8/tdbbackup.8*
%{_mandir}/man8/tdbdump.8*
%{_mandir}/man8/tdbrestore.8*
%{_mandir}/man8/tdbtool.8*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtdb.so
%{_includedir}/tdb.h
%{_pkgconfigdir}/tdb.pc

%files -n python3-tdb
%defattr(644,root,root,755)
%attr(755,root,root) %{py3_sitedir}/tdb.cpython-*.so
%{py3_sitedir}/_tdb_text.py
%{py3_sitedir}/__pycache__/_tdb_text.cpython-*.py[co]
