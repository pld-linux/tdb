%define	snap	20080818
Summary:	TDB - Trivial Database
Summary(pl.UTF-8):	TDB - prosta baza danych
Name:		tdb
Version:	1.1.2
Release:	0.%{snap}.3
License:	GPL
Group:		Libraries
Source0:	%{name}-%{snap}.tar.bz2
# Source0-md5:	128dfb4865c2fcabf36d8cfbb1d20d06
URL:		http://tdb.samba.org/
BuildRequires:	gdbm-devel
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
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for TDB library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki TDB.

%package static
Summary:	Static TDB library
Summary(pl.UTF-8):	Statyczna biblioteka TDB
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static TDB library.

%description static -l pl.UTF-8
Statyczna biblioteka TDB.

%package -n python-tdb
Summary:	Python bindings for TDB
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
%pyrequires_eq  python-libs

%description -n python-tdb
Python bindings for TDB.

%prep
%setup -q -n %{name}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# it's a symlink
cp -a libtdb.so $RPM_BUILD_ROOT%{_libdir}

%py_comp $RPM_BUILD_ROOT
%py_ocomp $RPM_BUILD_ROOT
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc docs/README
%attr(755,root,root) %{_bindir}/tdbbackup
%attr(755,root,root) %{_bindir}/tdbdump
%attr(755,root,root) %{_bindir}/tdbtool
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/tdb.h
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files -n python-tdb
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/*.so
%{py_sitescriptdir}/*.py[co]
