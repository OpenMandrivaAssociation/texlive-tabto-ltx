%global tl_name tabto-ltx
%global tl_revision 78101

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.4
Release:	%{tl_revision}.1
Summary:	Tab to a measured position in the line
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tabto
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tabto-ltx.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tabto-ltx.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
\tabto{<length>} moves the typesetting position to <length> from the
left margin of the paragraph. If the typesetting position is already
further along, \tabto starts a new line; the command \tabto* will move
position backwards if necessary, so that previous text may be
overwritten. The command \TabPositions may be used to define a set of
tabbing positions, after which the command \tab advances typesetting
position to the next defined 'tab stop'.

