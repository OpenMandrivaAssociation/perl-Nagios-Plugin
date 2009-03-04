%define module Nagios-Plugin

Summary:	A family of perl modules to streamline writing Nagios plugins
Name:		perl-%{module}
Version:	0.32
Release:	%mkrel 1
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Nagios/%{module}-%{version}.tar.gz
BuildRequires:	perl(Class::Accessor)
BuildRequires:	perl(Config::Tiny)
BuildRequires:	perl(Math::Calc::Units)
BuildRequires:	perl(Params::Validate)
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Test::Simple)
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}

%description
These modules are meant for perl developers of plugins for Nagios
(http://nagiosplug.sourceforge.net). It is meant to simplify a lot of the
common functions required to do checking of a particular service.

%prep
%setup -q -n %{module}-%{version} 

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
%{perl_vendorlib}/Nagios
%{_mandir}/*/*
