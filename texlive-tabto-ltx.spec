Name:		texlive-tabto-ltx
Version:	54080
Release:	2
Summary:	"Tab" to a measured position in the line
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tabto
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabto-ltx.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabto-ltx.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
\tabto{<length>} moves the typesetting position to <length>
from the left margin of the paragraph. If the typesetting
position is already further along, \tabto starts a new line;
the command \tabto* will move position backwards if necessary,
so that previous text may be overwritten. The command
\TabPositions may be used to define a set of tabbing positions,
after which the command \tab advances typesetting position to
the next defined 'tab stop'.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tabto-ltx
%doc %{_texmfdistdir}/doc/latex/tabto-ltx

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
