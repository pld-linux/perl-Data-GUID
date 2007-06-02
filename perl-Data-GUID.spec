#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Data
%define		pnam	GUID
Summary:	Data::GUID - Perl extension for generating GUIDs
Summary(pl):	Data::GUID - rozszerzenie Perla do generowania GUID-ów
Name:		perl-Data-GUID
Version:	0.043
Release:	1
License:	distributable
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Data/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	130afa8c397bfec6ac09d1125d3e0405
URL:		http://search.cpan.org/dist/Data-GUID/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a framework for generating UUIDs (Universally
Unique Identifiers, also known as GUIDs (Globally Unique Identifiers).
A GUID is 128 bits long, and is guaranteed to be different from all
other UUIDs/GUIDs generated until 3400 A.D. GUIDs were originally used
in the Network Computing System (NCS) and later in the Open Software
Foundation's (OSF) Distributed Computing Environment. Currently many
different technologies rely on GUIDs to provide unique identity for
various software components.

%description -l pl
Modu³ Perla Data::GUID udostêpnia szkielet do generowania UUID-ów
(Universally Unique Identifiers - identyfikatorów unikalnych
powszechnie), znanych te¿ jako GUID-y (Globally Unique Identifiers -
identyfikatory unikalne globalnie). GUID-y s± 128-bitowe i
gwarantowana jest ich unikalno¶æ w¶ród wszyskich innych UUID-ów/
/GUID-ów wygenerowanych do roku 3400. GUID-y pierwotnie by³y u¿ywane w
Network Computing System (NCS), a pó¼niej w Rozproszonym ¦rodowisku
Obliczeniowym (Distributed Computing Environment) Fundacji Open
Software (OSF). Obecnie na zagwarantowanych przez GUID-y unikalnych
identyfikatorach dla ró¿nych sk³adników oprogramowania opartych jest
wiele ró¿nych technologii.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL </dev/null \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Data/GUID.pm
%{_mandir}/man3/*
