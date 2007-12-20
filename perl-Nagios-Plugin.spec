%define real_name Nagios-Plugin

Summary:	A family of perl modules to streamline writing Nagios plugins
Name:		perl-%{real_name}
Version:	0.22
Release:	%mkrel 1
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	http://search.cpan.org/CPAN/authors/id/T/TO/TONVOON/%{real_name}-%{version}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	perl-Class-Accessor
BuildRequires:	perl-Config-Tiny
BuildRequires:	perl-Math-Calc-Units
BuildRequires:	perl-Params-Validate
BuildRequires:	perl-Test-Pod
BuildRequires:	perl-Test-Simple
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-root

%description
These modules are meant for perl developers of plugins for Nagios
(http://nagiosplug.sourceforge.net). It is meant to simplify a lot of the
common functions required to do checking of a particular service.

%prep

%setup -q -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}

%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Nagios/Plugin*
%{_mandir}/*/*
