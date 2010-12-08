%define version 0.3.5
%define release %mkrel 13
%define name wmwebcam
%define title WmWebcam 

Summary:    Watch your own webcam in a small dockapp window
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Toys
Source:		%{name}-%{version}.tar.bz2
Source1:    %{name}.16x16.png.bz2
Source2:    %{name}.32x32.png.bz2
Source3:    %{name}.48x48.png.bz2
URL:		http://fragment.stc.cx/?abd
BuildRequires:	libxdmcp-devel
BuildRequires:	libxau-devel
Buildrequires:	libxpm-devel
Buildrequires:	libjpeg-devel
Buildrequires:	libx11-devel
Buildrequires:	libxext-devel
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
This is for watching your webcam which has a video4linux driver in your
windowmakers dock..
This is actually just a edited version of vidcat (from w3cam's package)
Default jpeg output file is /tmp/wmwebcam.jpg and default quality is 100%,
change the default values if necessary from the source code.
Also remember to check the wmwebcam.pl and edit it

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q

%build
 
%make

%install
[ -d $RPM_BUILD_ROOT ] && rm -rf $RPM_BUILD_ROOT

install -m 755 -d $RPM_BUILD_ROOT%{_bindir}
install -m 755 {wmwebcam,wmwebcam.pl} $RPM_BUILD_ROOT%{_bindir}

install -m 755 -d $RPM_BUILD_ROOT%{_miconsdir}
install -m 755 -d $RPM_BUILD_ROOT%{_iconsdir}
install -m 755 -d $RPM_BUILD_ROOT%{_liconsdir}
bzcat %{SOURCE1} > $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
bzcat %{SOURCE2} > $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
bzcat %{SOURCE3} > $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png


mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop <<EOF
[Desktop Entry]
Name=%{title}
Comment=Watch your own webcam in a small dockapp window
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-Multimedia-Video;AudioVideo;TV;Tuner;
EOF


%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean
[ -z $RPM_BUILD_ROOT ] || {
    rm -rf $RPM_BUILD_ROOT
}

%files
%defattr (-,root,root)
%doc README Changelog COPYING
%{_bindir}/*
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop


