#
# TODO:
# - icon
#
Summary:	The fun, free snowballing computer game
Summary(pl.UTF-8):	Zabawna, darmowa gra komputerowa w śnieżki
Name:		snowballz
Version:	0.9.4
Release:	0.1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://joey101.net/snowballz/files/%{name}-%{version}.tar.gz
# Source0-md5:	064a4d1a9e2eeb2bf550c668610a9c4d
# Source 1:        %{name}.desktop
URL:		http://joey101.net/snowballz/
BuildRequires:	rpm-pythonprov
Requires:	python
Requires:	python-GooeyPy
Requires:	python-Numeric
Requires:	python-PIL
Requires:	python-PyOpenGL
Requires:	python-Rabbyt
Requires:	python-pygame
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Take command of your army of penguins as you blaze your path to
victory! March through snow laden forests to conquer new frontiers
and grow your small army. Ambush enemy lines with blasts of freezing
snowballs. But don't neglect your home, invaders are just over the
next snow drift! Gather fish for your cold penguins to munch on as
they warm up in your cozy igloo. It's a snowy world you don't want to
miss!

Snowballz is packed with adventure and fun yearning to be discovered.
Grab your free copy now and play by yourself or duel it out with your
friends. Well, what are you waiting for?

%description -l pl.UTF-8
Obejmij dowództwo nad armią pingwinów wypalając swoją drogę do
zwycięstwa! Maszeruj poprzez wypełnione śniegiem lasy aby podbić nowe
granice i powiększyć swoją małą armię. Wpędź linie przeciwnika w
zasadzkę wybuchów marznących kul śnieżnych. Ale nie lekceważ swojego
domu, najeźdźcy czyhają za następną zaspą! Gromadź ryby dla swoich
zziębniętych pingwinów, aby miały czym pożywić się ogrzewając w
przytulnym igloo. To jest śnieżny świat, którego nie chcesz utracić!

Snowballz jest grą przepełnioną przygodą i zabawą czekającą na
odkrycie. Pobierz darmową kopię i graj lub zmierz się z kolegami. Na
co jeszcze czekasz?

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/%{name},%{_bindir}}

cat <<'EOF' >$RPM_BUILD_ROOT%{_bindir}/snowballz.sh
#!/bin/sh
cd %{_datadir}/snowballz
exec python snowballz.pyc $@
EOF

cp -fr buildings $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -fr data	 $RPM_BUILD_ROOT%{_datadir}/%{name}
#cp -fr gooeypy   $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -fr maps	 $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -fr plugins	 $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -f *.py	 $RPM_BUILD_ROOT%{_datadir}/%{name}

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE README.txt
%attr(755,root,root) %{_bindir}/snowballz.sh
%{_datadir}/%{name}
#%{_desktopdir}/%{name}.desktop
#%{_pixmapsdir}/%{name}.png
