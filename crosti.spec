Name:		crosti
Summary:	Tool to create cross stitch scheme from custom image
Version:	1.7.0
Release:	1
License:	GPLv3+
Group:		Graphics
URL:		https://sites.google.com/site/crostiapp/
Source0:	%{name}-%{version}-source.zip
Source1:	crosti.xml
Patch0:		crosti-1.7.0-mdv-desktop.patch
BuildRequires:	pkgconfig(Qt3Support)

%description
This tool allows you to make your own unique cross stitch scheme from custom
image. You can resize and rotate image, reduce the number of colors, change
image palette, make cross stitch scheme, preview it, save and print. Cross
stitch scheme edition available: colors and icons changing, new color addition,
color fill, scheme pixel draw, lines and half-stitches.

Features

* Convert custom image to cross stitch scheme.
* Edit cross stitch scheme.
* Save and print the scheme that you created.
* Input images: BMP, GIF, ICO, JPEG, JPG, MNG, PBM, PGM, PNG, PPM, SVG, TIF,
  TIFF, XBM, XPM.
* Output cross stitch scheme: BMP, ICO, JPEG, JPG, PNG, PPM, TIF, TIFF, XBM,
  XPM, PDF, CST (crosti scheme text file).

%prep
%setup -q -n source
%patch0 -p1

%build
pushd Repository/%{name}-%{version}
%qmake_qt4
%make
popd

%install
pushd Repository/%{name}-%{version}
make install INSTALL_ROOT=%{buildroot}
popd

install -D -m 644 %{SOURCE1} %{buildroot}%{_datadir}/mime/packages/%{name}.xml

for size in 16 32
do
install -d %{buildroot}%{_iconsdir}/hicolor/${size}x${size}/apps/
mv %{buildroot}%{_datadir}/%{name}/system/image/crosti${size}.png \
	%{buildroot}%{_iconsdir}/hicolor/${size}x${size}/apps/%{name}.png
done

%files
%doc crosti/readme.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_iconsdir}/hicolor/*/apps/*


%changelog
* Sun Apr 08 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 1.7.0-1
+ Revision: 789888
- update to 1.7.0

* Tue Mar 06 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 1.6.0-3
+ Revision: 782423
- move icons to iconsdir

* Tue Mar 06 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 1.6.0-2
+ Revision: 782379
- fix desktop file
- use home directory instead /usr/share

* Fri Mar 02 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 1.6.0-1
+ Revision: 781742
- imported package crosti

