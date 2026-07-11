%global tl_name trajan
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Fonts from the Trajan column in Rome
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/trajan
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/trajan.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/trajan.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/trajan.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Provides fonts (both as Metafont source and in Adobe Type 1 format)
based on the capitals carved on the Trajan column in Rome in 114 AD,
together with macros to access the fonts. Many typographers think these
rank first among the Roman's artistic legacy. The font is uppercase
letters together with some punctuation and analphabetics; no lowercase
or digits.

