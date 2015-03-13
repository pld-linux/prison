%define		qtver		4.7.3
Summary:	Prison - a barcode api to produce QRCode barcodes and DataMatrix barcodes
Name:		prison
Version:	1.0
Release:	3
License:	GPL v2
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/stable/prison/1.0/src/%{name}-%{version}.tar.gz
# Source0-md5:	8baac61506e37a31482a0df4a5d02cd2
URL:		http://projects.kde.org/prison
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.0
BuildRequires:	qrencode-devel
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.293
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qt-based barcode abstraction layer/library and provides uniform access
to generation of barcodes with data.

%package devel
Summary:	Header files for Prison
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files needed to build Prison client libraries and applications.

%description devel -l pl.UTF-8
Pliki nagłówkowe do tworzenia bibliotek klienckich i aplikacji
używających Prison.

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libprison.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libprison.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libprison.so
%{_libdir}/cmake/Prison
%{_includedir}/prison
