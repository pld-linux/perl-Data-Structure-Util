#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Data
%define	pnam	Structure-Util
Summary:	Data::Structure::Util - Change nature of data within a structure
Summary(pl):	Data::Structure::Util - Zmiana natury danych wewn±trz struktury
Name:		perl-%{pdir}-%{pnam}
Version:	0.11
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3cbec998cd7c55b1244b3f782569b552
URL:		http://search.cpan.org/dist/Data-Structure-Util/
%if %{with tests}
BuildRequires:	perl-Clone
BuildRequires:	perl-File-Find-Rule
BuildRequires:	perl-Test-Pod
%endif
BuildRequires:	perl-Module-Build >= 0.02
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Data::Structure::Util is a toolbox to manipulate data inside a data
structure. It can parse an entire tree and perform the operation
requested on each appropriate element. It can transform to UTF-8 any
string within a data structure. I can attempt to transform any UTF-8
string back to default encoding either. It can remove the blessing on
any reference. It can collect all the objects or detect if there is a
circular reference.

It is written in C for decent speed.

%description -l pl
Data::Structure::Util to zestaw narzêdzi do obróbki danych wewn±trz
struktur danych. Mo¿e analizowaæ ca³e drzewo i wykonywaæ ¿±dane
operacje na ka¿dym w³a¶ciwym elemencie. Mo¿e przekszta³caæ na UTF-8
dowolny ³añcuch wewn±trz struktury danych, a tak¿e próbowaæ
przekszta³ciæ dowolny ³añcuch z UTF-8 z powrotem do domy¶lnego
kodowania.  Mo¿e usuwaæ b³ogos³awieñstwo z dowolnej referencji. Mo¿e
zbieraæ wszystkie obiekty lub wykrywaæ czy s± zapêtlone referencje.

Jest napisany w C w celu zapewnienia przyzwoitej szybko¶ci.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PERL_INSTALL_ROOT=$RPM_BUILD_ROOT 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%{perl_vendorarch}/Data/Structure/Util.pm
%{_mandir}/man3/*
