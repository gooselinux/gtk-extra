Name:		gtk+extra
Version:	2.1.1
Release:	13%{?dist}
Summary:	A library of gtk+ widgets
Summary(fr):	Une bibliothèque de widgets gtk+

Group:		System Environment/Libraries
License:	GPLv2+
URL:		http://gtkextra.sourceforge.net/
Source:		http://dl.sf.net/scigraphica/gtk+extra-%{version}.tar.gz
Patch:		%{name}-%{version}.g_free.diff
Patch1:		%{name}-%{version}-deleterow.patch
Patch2:		%{name}-%{version}-item.patch
Patch3:		%{name}-%{version}-gtk2.18.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	gtk2-devel

%description
A library of dynamically linked gtk+ widgets including:
GtkSheet, GtkPlot, and GtkIconList

%description -l fr
Une bibliothèque de widgets gtk+ liés dynamiquement incluant :
GtkSheet, GtkPlot et GtkIconList

%package devel
Summary:	A library of gtk+ widgets
Summary(fr):	Une bibliothèque de widgets gtk+
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk2-devel

%description devel
The %{name}-devel package includes the static libraries, header files,
and documentation for compiling programs that use gtk+extra widgets.

%description -l fr devel
Le paquetage %{name}-devel contient les bibliothèques statiques, les fichiers
d'en-têtes et la documentation nécessaires à la compilation des programmes
qui utilisent les widgets gtk+extra.

%prep
%setup -q
%{__chmod} a-x ChangeLog
%{__sed} -i 's/\r//' docs/{gtk*.ChangeLog,HELP,README,TODO,VERSION}
%{__sed} -i 's/\r//' docs/reference/*.html
%{__sed} -i 's/\r//' docs/tutorial/{*.html,gtksheet/*.{c,html}}

%patch -p0
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README
%{_libdir}/libgtkextra*.so.*

%files devel
%defattr(-,root,root,-)
%doc docs/{gtk*.ChangeLog,COPYING,HELP,README,TODO,VERSION}
%doc docs/reference/ docs/tutorial/
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*


%changelog
* Fri Jan 15 2010 Miloslav Trmač <mitr@redhat.com> - 2.1.1-13
- Fix crash with gtk2-2.18 (patch by rrankin AT ihug DOT com DOT au)
  Resolves: #546649

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 2.1.1-12.1
- Rebuilt for RHEL 6

* Sat Aug 01 2009 Roy Rankin <rrankin[AT]ihug[DOT]com[DOT]au> - 2.1.1-12
- Patch to compile with gtk2-2.17.5

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Dec  6 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> 2.1.1-9
  - Rebuild for pkgconfig

* Mon Apr 07 2008 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2.1.1-8
  - Patch to fix BZ #431150

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.1.1-7
  - Autorebuild for GCC 4.3

* Fri Oct 19 2007 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2.1.1-6
  - Update patch to fix BZ #339611

* Tue Aug 21 2007 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2.1.1-5
  - Licence tag clarification

* Thu May  3 2007 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2.1.1-4
  - Add patch to fix SF #1504169

* Fri Sep  1 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2.1.1-3
  - FE6 rebuild

* Mon Mar 13 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2.1.1-2
  - Rebuild for FE5

* Wed Oct 5 2005 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2.1.1-1
  - New version
  - Revert to the official package.

* Thu Sep 15 2005 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 1.1.0-3
  - BuildRequires is gtk2-devel, not gtk+-devel
  - Add Requires gtk2-devel for package devel
  - Exclude .la files
  - Add a lot of documentation
  - Move gtk*.ChangeLog in devel package
  - Convert DOS format end-of-line to Unix-like format
  - Contributions of Jose Pedro Oliveira <jpo[AT]di[DOT]uminho[DOT]pt>
    Thanks to him.

* Tue Sep 13 2005 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 1.1.0-2
  - Add french summary and description

* Mon Sep 12 2005 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 1.1.0-1
  - New version

* Fri Oct 29 2004 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 0:0.99.17-0.fdr.2
  - Add BuildRequires gtk+-devel

* Wed Oct 27 2004 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 0:0.99.17-0.fdr.1
  - Initial Fedora RPM
