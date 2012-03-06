Name:		crosti
Summary:	Tool to create cross stitch scheme from custom image
Version:	1.6.0
Release:	2
License:	GPLv3+
Group:		Graphics
URL:		http://
Source0:	%{name}-%{version}-source.zip
Patch0:		crosti-1.6.0-mdv-homepath.patch
Patch1:		crosti-1.6.0-mdv-desktop.patch
BuildRequires:	libqt4-devel

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
%patch1 -p1

%build
pushd Repository/%{name}-%{version}
%qmake_qt4
%make
popd

%install
pushd Repository/%{name}-%{version}
make install INSTALL_ROOT=%{buildroot}
popd
#pushd crosti
#
#install -D -m 755 crosti %{buildroot}/%{_bindir}/%{name}
#install -d %{buildroot}/%{_datadir}/
#cp -rf system %{buildroot}/%{_datadir}/%{name}
#install -d %{buildroot}%{_docdir}/%{name}
#
#popd

%files
%doc crosti/readme.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
