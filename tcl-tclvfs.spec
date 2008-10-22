%{!?tcl_version: %define tcl_version %(echo 'puts $tcl_version' | tclsh)}
%{!?tcl_sitearch: %define tcl_sitearch %{_libdir}/tcl%{tcl_version}}
%define realname tclvfs

Name:		tcl-%{realname}
Version:	20080503
Release:	1%{?dist}
Summary:	Tcl extension for Virtual Filesystem support
Group:		System Environment/Libraries
License:	MIT
URL:		http://sourceforge.net/projects/tclvfs
Source0:	http://downloads.sourceforge.net/%{realname}/%{realname}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
Provides:	tcl-vfs = %{version}-%{release}
Provides:	%{realname} = %{version}-%{release}
BuildRequires:	tcl-devel, tk-devel
Requires:	tcl(abi) = 8.5

%description
The TclVfs project aims to provide an extension to the Tcl language which 
allows Virtual Filesystems to be built using Tcl scripts only. It is also a 
repository of such Tcl-implemented filesystems (metakit, zip, ftp, tar, 
http, webdav, namespace, url)

%prep
%setup -q -n %{realname}-%{version}

%build
%configure
sed -i 's|/generic:|\$(srcdir)/generic:|g' Makefile
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
install -d %{buildroot}%{tcl_sitearch}
mv %{buildroot}%{_libdir}/vfs1.3 %{buildroot}%{tcl_sitearch}/vfs1.3
chmod +x %{buildroot}%{tcl_sitearch}/vfs1.3/template/fishvfs.tcl

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc Readme.txt DESCRIPTION.txt license.terms ChangeLog
%{tcl_sitearch}/vfs1.3/
%{_mandir}/mann/vfs*

%changelog
* Thu Jun 26 2008 Tom "spot" Callaway <tcallawa@redhat.com> 20080503-1
- initial package for Fedora
