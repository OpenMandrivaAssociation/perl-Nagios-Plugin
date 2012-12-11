%define upstream_name    Nagios-Plugin
%define upstream_version 0.35

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2
Summary:	A family of perl modules to streamline writing Nagios plugins
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Nagios/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::Accessor)
BuildRequires:	perl(Config::Tiny)
BuildRequires:	perl(Math::Calc::Units)
BuildRequires:	perl(Params::Validate)
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Test::Simple)
BuildArch:	noarch

%description
These modules are meant for perl developers of plugins for Nagios
(http://nagiosplug.sourceforge.net). It is meant to simplify a lot of the
common functions required to do checking of a particular service.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Nagios
%{_mandir}/*/*


%changelog
* Mon Dec 06 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.350.0-1mdv2011.0
+ Revision: 612250
- update to new version 0.35

* Fri Apr 16 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.340.0-1mdv2011.0
+ Revision: 535531
- new version

* Thu Oct 22 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.330.0-2mdv2010.0
+ Revision: 458764
- ensure backportability

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.330.0-1mdv2010.0
+ Revision: 404044
- rebuild using %%perl_convert_version

* Sun Jun 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.33-1mdv2010.0
+ Revision: 383530
- update to new version 0.33

* Wed Mar 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.32-1mdv2009.1
+ Revision: 348534
- update to new version 0.32

* Tue Jan 06 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.31-1mdv2009.1
+ Revision: 325311
- update to new version 0.31

* Wed Dec 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.30-1mdv2009.1
+ Revision: 315203
- new version
- drop test patch, uneeded anymore

* Wed Dec 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.29-1mdv2009.1
+ Revision: 312497
- new version

* Sat Nov 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.28-1mdv2009.1
+ Revision: 305755
- update to new version 0.28

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.27-2mdv2009.0
+ Revision: 268620
- rebuild early 2009.0 package (before pixel changes)

* Wed Jun 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.27-1mdv2009.0
+ Revision: 217988
- update to new version 0.27

* Thu Dec 20 2007 Oden Eriksson <oeriksson@mandriva.com> 0.22-1mdv2008.1
+ Revision: 135705
- 0.22

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Oct 11 2007 Oden Eriksson <oeriksson@mandriva.com> 0.21-1mdv2008.1
+ Revision: 97100
- import perl-Nagios-Plugin


* Thu Oct 11 2007 Oden Eriksson <oeriksson@mandriva.com> 0.21-1mdv2008.1
- initial Mandriva package 
