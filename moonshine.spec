%define name moonshine
%define version 0.2
%define release %mkrel 5

Summary: Windows Media player based on Moonlight
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://abock.org/moonshine/releases/%{name}-%{version}.tar.bz2
Source1: npupp.h
License: MIT
Group: Video
Url: https://abock.org/moonshine/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: xulrunner-devel
BuildRequires: glib2-devel
BuildRequires: zip
Requires: moon >= 1.0

%description
Moonshine leverages the Windows Media capabilities from Silverlight,
provided by the Moonlight browser plugin on Linux, and the Firefox web
browser framework to enable the playback of embedded Windows Media
content on the web and local files on a user's desktop.

%package player
Summary: Standalone Windows Media player
Group: Video
Requires: xulrunner
Requires: %name = %version-%release

%description player
Moonshine leverages the Windows Media capabilities from Silverlight,
provided by the Moonlight browser plugin on Linux, and the Firefox web
browser framework to enable the playback of embedded Windows Media
content on the web and local files on a user's desktop.


%prep
%setup -q
cp %SOURCE1 plugin/

%build
%configure2_5x --with-browser-plugin-dir=%_libdir/mozilla/plugins --enable-xpi-build
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README AUTHORS NEWS
%_libdir/mozilla/plugins/libmoonshine-plugin.so
%_libdir/mozilla/plugins/libmoonshine-plugin.la

%files player
%defattr(-,root,root)
%doc README
%_bindir/%name
%_datadir/applications/%name.desktop
%_datadir/icons/hicolor/*/*/*
%_datadir/%name
