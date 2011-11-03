# revision 18159
# category Package
# catalog-ctan /macros/latex/contrib/tabto
# catalog-date 2010-05-23 19:54:42 +0200
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-tabto-ltx
Version:	1.0
Release:	1
Summary:	"Tab" to a measured position in the line
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tabto
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabto-ltx.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabto-ltx.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
\tabto{<length>} moves the typesetting position to <length>
from the left margin of the paragraph. If the typesetting
position is already further along, \tabto starts a new line;
the command \tabto* will move position backwards if necessary,
so that previous text may be overwritten. The command
\TabPositions may be used to define a set of tabbing positions,
after which the command \tab advances typesetting position to
the next defined 'tab stop'.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tabto-ltx/tabto.sty
%doc %{_texmfdistdir}/doc/latex/tabto-ltx/tabto-doc.pdf
%doc %{_texmfdistdir}/doc/latex/tabto-ltx/tabto-doc.tex
%doc %{_texmfdistdir}/doc/latex/tabto-ltx/tabto.txt
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
