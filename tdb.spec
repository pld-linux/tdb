Summary:	TDB - Trivial Database
Summary(pl.UTF-8):	TDB - prosta baza danych
Name:		tdb
Version:	1.2.10
Release:	1
Epoch:		2
License:	LGPL v3+
Group:		Libraries
Source0:	http://samba.org/ftp/tdb/%{name}-%{version}.tar.gz
# Source0-md5:	cc28048309df19782b04359282e9f98b
URL:		http://tdb.samba.org/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
Obsoletes:	tdb-extras
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

%package -n python-tdb
Summary:	Python bindings for TDB
Summary(pl.UTF-8):	Pythonowy interfejs do TDB
Group:		Libraries/Python
Requires:	%{name} = %{epoch}:%{version}-%{release}
%pyrequires_eq  python-libs

%description -n python-tdb
Python bindings for TDB.

%description -n python-tdb -l pl.UTF-8
Pythonowy interfejs do TDB.

%prep
%setup -q

%build
# note: configure in fact is waf call
CC="%{__cc}" \
CFLAGS="%{rpmcflags}" \
PYTHONDIR=%{py_sitedir} \
./configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir}

%{__make} \
	V=1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%triggerpostun -p /sbin/postshell -- %{name} < 2:1.2.9-2
-rm -f %{_libdir}/libtdb.so.1
/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc docs/README
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

%files -n python-tdb
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/tdb.so
