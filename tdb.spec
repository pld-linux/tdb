Summary:	TDB - Trivial Database
Summary(pl):	TDB - prosta baza danych
Name:		tdb
Version:	1.0.6
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/tdb/%{name}-%{version}.tar.gz
# Source0-md5:	6b643fdeb48304010dcd5f675e458b58
Patch0:		%{name}-gcc33.patch
URL:		http://sourceforge.net/projects/tdb/
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TDB is a Trivial Database. In concept, it is very much like GDBM, and
BSD's DB except that it allows multiple simultaneous writers and uses
locking internally to keep writers from trampling on each other. TDB
is also extremely small.

%description -l pl
TDB to Trivial Database, czyli prosta baza danych. W za³o¿eniach jest
bardzo podobna do GDBM lub DB z BSD z wyj±tkiem tego, ¿e pozwala na
zapis wielu procesom jednocze¶nie i u¿ywa wewnêtrznie blokowania, aby
nie pozwoliæ pisz±cym na zadeptanie siê nawzajem. TDB jest ponadto
ekstremalnie ma³a.

%package devel
Summary:	Header files for TDB library
Summary(pl):	Pliki nag³ówkowe biblioteki TDB
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for TDB library.

%description devel -l pl
Pliki nag³ówkowe biblioteki TDB.

%package static
Summary:	Static TDB library
Summary(pl):	Statyczna biblioteka TDB
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static TDB library.

%description static -l pl
Statyczna biblioteka TDB.

%prep
%setup -q
%patch -p1

%build
cp -f /usr/share/automake/config.* .
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/tdb.h
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
