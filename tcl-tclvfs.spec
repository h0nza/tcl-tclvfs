%{!?tcl_version: %global tcl_version %(echo 'puts $tcl_version' | tclsh)}
%{!?tcl_sitearch: %global tcl_sitearch %{_libdir}/tcl%{tcl_version}}
%global realname tclvfs

Name:		tcl-%{realname}
Version:	20080503
Release:	18%{?dist}
Summary:	Tcl extension for Virtual Filesystem support
Group:		System Environment/Libraries
License:	MIT
URL:		http://sourceforge.net/projects/tclvfs
Source0:	http://downloads.sourceforge.net/%{realname}/%{realname}-%{version}.tar.gz
Patch0:		tclvfs-20080503-tcl86.patch
Provides:	tcl-vfs = %{version}-%{release}
Provides:	%{realname} = %{version}-%{release}
BuildRequires:	tcl-devel >= 8.6, tk-devel
Requires:	tcl(abi) = 8.6, tcl-trf

%description
The TclVfs project aims to provide an extension to the Tcl language which 
allows Virtual Filesystems to be built using Tcl scripts only. It is also a 
repository of such Tcl-implemented filesystems (metakit, zip, ftp, tar, 
http, webdav, namespace, url)

%prep
%setup -q -n %{realname}-%{version}
%patch0 -p1 -b .tcl86

%build
%configure
sed -i 's|/generic:|\$(srcdir)/generic:|g' Makefile
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
install -d %{buildroot}%{tcl_sitearch}
mv %{buildroot}%{_libdir}/vfs1.3 %{buildroot}%{tcl_sitearch}/vfs1.3
chmod +x %{buildroot}%{tcl_sitearch}/vfs1.3/template/fishvfs.tcl

%files
%doc Readme.txt DESCRIPTION.txt ChangeLog
%license license.terms
%{tcl_sitearch}/vfs1.3/
%{_mandir}/mann/vfs*

%changelog
* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20080503-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20080503-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20080503-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Tom Callaway <spot@fedoraproject.org> - 20080503-15
- modernize spec file

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080503-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080503-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jun 10 2014 Tom Callaway <spot@fedoraproject.org> - 20080503-12
- fix build against tcl 8.6

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080503-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 20080503-10
- Rebuilt for https://fedoraproject.org/wiki/Changes/f21tcl86

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080503-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080503-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080503-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080503-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080503-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080503-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Mar 18 2009 Tom "spot" Callaway <tcallawa@redhat.com> 20080503-3
- add Requires: tcl-trf

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080503-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jun 26 2008 Tom "spot" Callaway <tcallawa@redhat.com> 20080503-1
- initial package for Fedora
