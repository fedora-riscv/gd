Summary:        A graphics library for quick creation of PNG or JPEG images
Name:           gd
Version:        2.0.33
Release:        3
Group:          System Environment/Libraries
License:        BSD-style
URL:            http://www.boutell.com/gd/
Source0:        http://www.boutell.com/gd/http/%{name}-%{version}.tar.gz
Patch0:         gd-2.0.33-freetype.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  freetype-devel, fontconfig-devel, xorg-x11-devel
BuildRequires:  libjpeg-devel, libpng-devel, zlib-devel

%description
The gd graphics library allows your code to quickly draw images
complete with lines, arcs, text, multiple colors, cut and paste from
other images, and flood fills, and to write out the result as a PNG or
JPEG file. This is particularly useful in Web applications, where PNG
and JPEG are two of the formats accepted for inline images by most
browsers. Note that gd is not a paint program.


%package progs
Requires:       gd = %{version}-%{release}
Summary:        Utility programs that use libgd
Group:          Applications/Multimedia

%description progs
The gd-progs package includes utility programs supplied with gd, a
graphics library for creating PNG and JPEG images. If you install
these, you must also install gd.


%package devel
Summary:        The development libraries and header files for gd
Group:          Development/Libraries
Requires:       gd = %{version}-%{release}
Requires:       xorg-x11-devel, libjpeg-devel, freetype-devel, libpng-devel, zlib-devel

%description devel
The gd-devel package contains the development libraries and header
files for gd, a graphics library for creating PNG and JPEG graphics.


%prep
%setup -q
%patch0 -p1 -n .freetype

%build
%configure --disable-rpath
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT/%{_libdir}/libgd.la

%clean
rm -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc COPYING README-JPEG.TXT index.html entities.html
%{_libdir}/*.so.*

%files progs
%defattr(-,root,root,-)
%{_bindir}/*
%exclude %{_bindir}/gdlib-config

%files devel
%defattr(-,root,root,-)
%{_bindir}/gdlib-config
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a


%changelog
* Wed Sep 07 2005 Phil Knirsch <pknirsch@redhat.com> 2.0.33-3
- Fixed broken freetype-config --libs flags in configure (#165875)

* Sun Apr 17 2005 Warren Togami <wtogami@redhat.com> 2.0.33-2
- devel reqs (#155183 thias)

* Tue Mar 22 2005 Than Ngo <than@redhat.com> 2.0.33-1
- 2.0.33 #150717
- apply the patch from Jose Pedro Oliveira
  - Added the release macro to the subpackages requirements versioning
  - Handled the gdlib-config movement to gd-devel in a differment manner
  - Added fontconfig-devel to the build requirements
  - Added xorg-x11-devel to the build requirements (Xpm)
  - Removed explicit /sbin/ldconfig requirement (gd rpm)
  - Removed explicit perl requirement (gd-progs rpm)
  - Added several missing documentation files (including the license file)
  - Replaced %%makeinstall by make install DESTDIR=...

* Thu Mar 10 2005 Than Ngo <than@redhat.com> 2.0.32-3
- move gdlib-config in devel

* Wed Mar 02 2005 Phil Knirsch <pknirsch@redhat.com> 2.0.32-2
- bump release and rebuild with gcc 4

* Wed Nov 03 2004 Phil Knirsch <pknirsch@redhat.com> 2.0.32-1
- Update to 2.0.32 which includes all the security fixes

* Wed Oct 27 2004 Phil Knirsch <pknirsch@redhat.com> 2.0.28-2
- Fixed several buffer overflows for gdMalloc() calls

* Tue Jul 27 2004 Phil Knirsch <pknirsch@redhat.com> 2.0.28-1
- Update to 2.0.28

* Fri Jul 02 2004 Phil Knirsch <pknirsch@redhat.com> 2.0.27-1
- Updated to 2.0.27 due to:
  o Potential memory overruns in gdImageFilledPolygon. Thanks to John Ellson.
  o The sign of Y-axis values returned in the bounding box by gdImageStringFT
    was incorrect. Thanks to John Ellson and Riccardo Cohen.

* Wed Jun 30 2004 Phil Knirsch <pknirsch@redhat.com> 2.0.26-1
- Update to 2.0.26

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Apr 21 2004 Phil Knirsch <pknirsch@redhat.com> 2.0.21-3
- Disable rpath usage.

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Feb 02 2004 Phil Knirsch <pknirsch@redhat.com> 2.0.21-1
- Updated to 2.0.21

* Tue Aug 12 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 2.0.15

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue May 06 2003 Phil Knirsch <pknirsch@redhat.com> 2.0.12-1
- Update to 2.0.12

* Wed Jan 22 2003 Tim Powers <timp@redhat.com> 1.8.4-11
- rebuilt

* Wed Dec 11 2002 Tim Powers <timp@redhat.com> 1.8.4-10
- rebuild on all arches

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Jan 24 2002 Phil Knirsch <pknirsch@redhat.com>
- Specfile update to add URL for homepage (#54608)

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Oct 31 2001 Bernhard Rosenkraenzer <bero@redhat.com> 1.8.4-5
- Rebuild with current libpng

* Mon Aug 13 2001 Philipp Knirsch <pknirsch@redhat.de> 1.8.4-4
- Fixed a wrong double ownership of libgd.so (#51599).

* Fri Jul 20 2001 Bernhard Rosenkraenzer <bero@redhat.com> 1.8.4-3
- There's really no reason to link against both freetype 1.x and 2.x,
  especially when gd is configured to use just freetype 2.x. ;)

* Mon Jun 25 2001 Philipp Knirsch <pknirsch@redhat.de>
- Forgot to include the freetype library in the shared library linking. Fixed.

* Thu Jun 21 2001 Philipp Knirsch <pknirsch@redhat.de>
- Update to 1.8.4

* Tue Dec 19 2000 Philipp Knirsch <pknirsch@redhat.de>
- Updates the descriptions to get rid of al references to gif

* Tue Dec 12 2000 Philipp Knirsch <Philipp.Knirsch@redhat.de>
- Fixed bug #22001 where during installation the .so.1 and the so.1.8 links
  didn't get installed and therefore updates had problems.

* Wed Oct  4 2000 Nalin Dahyabhai <nalin@redhat.com>
- define HAVE_LIBTTF to actually enable ttf support (oops, #18299)
- remove explicit dependencies on libpng, libjpeg, et. al.
- add BuildPrereq: freetype-devel

* Wed Aug  2 2000 Matt Wilson <msw@redhat.com>
- rebuilt against new libpng

* Mon Jul 31 2000 Nalin Dahyabhai <nalin@redhat.com>
- add %%postun run of ldconfig (#14915)

* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Tue Jun 27 2000 Nalin Dahyabhai <nalin@redhat.com> 
- update to 1.8.3

* Sat Jun  4 2000 Nalin Dahyabhai <nalin@redhat.com> 
- rebuild in new environment

* Mon May 22 2000 Nalin Dahyabhai <nalin@redhat.com> 
- break out a -progs subpackage
- disable freetype support

* Fri May 19 2000 Nalin Dahyabhai <nalin@redhat.com> 
- update to latest version (1.8.2)
- disable xpm support

* Thu Feb 03 2000 Nalin Dahyabhai <nalin@redhat.com> 
- auto rebuild in the new build environment (release 6)

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 5)

* Thu Dec 17 1998 Cristian Gafton <gafton@redhat.com>
- buiuld for glibc 2.1

* Fri Sep 11 1998 Cristian Gafton <gafton@redhat.com>
- built for 5.2
