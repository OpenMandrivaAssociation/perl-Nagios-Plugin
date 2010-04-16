%define upstream_name    Nagios-Plugin
%define upstream_version 0.34

Name:       perl-%{upstream_name}
%if %mdkversion > 200900
Version:    %perl_convert_version %{upstream_version}
%else
Version:    %{upstream_version}
%endif
Release:    %mkrel 1
Summary:	A family of perl modules to streamline writing Nagios plugins
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Nagios/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:	perl(Class::Accessor)
BuildRequires:	perl(Config::Tiny)
BuildRequires:	perl(Math::Calc::Units)
BuildRequires:	perl(Params::Validate)
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Test::Simple)
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
These modules are meant for perl developers of plugins for Nagios
(http://nagiosplug.sourceforge.net). It is meant to simplify a lot of the
common functions required to do checking of a particular service.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
