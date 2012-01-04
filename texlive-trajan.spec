# revision 15878
# category Package
# catalog-ctan /fonts/trajan
# catalog-date 2007-10-24 18:05:15 +0200
# catalog-license lppl
# catalog-version 1.1
Name:		texlive-trajan
Version:	1.1
Release:	2
Summary:	Fonts from the Trajan column in Rome
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/trajan
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/trajan.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/trajan.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/trajan.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Provides fonts (in both MetaFont and Adobe Type 1 format) based
on the capitals carved on the Trajan column in Rome in 114 AD,
together with macros to access the fonts. Many typographers
think these rank first among the Roman's artistic legacy. The
font is uppercase letters together with some punctuation and
analphabetics; no lowercase or digits.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/trajan/trjnr10.afm
%{_texmfdistdir}/fonts/afm/public/trajan/trjnsl10.afm
%{_texmfdistdir}/fonts/map/dvips/trajan/trajan.map
%{_texmfdistdir}/fonts/tfm/public/trajan/trjnr10.tfm
%{_texmfdistdir}/fonts/tfm/public/trajan/trjnsl10.tfm
%{_texmfdistdir}/fonts/type1/public/trajan/trjnr10.pfb
%{_texmfdistdir}/fonts/type1/public/trajan/trjnsl10.pfb
%{_texmfdistdir}/tex/latex/trajan/t1trjn.fd
%{_texmfdistdir}/tex/latex/trajan/trajan.sty
%doc %{_texmfdistdir}/doc/latex/trajan/README
%doc %{_texmfdistdir}/doc/latex/trajan/trajan.pdf
%doc %{_texmfdistdir}/doc/latex/trajan/trytrajan.pdf
%doc %{_texmfdistdir}/doc/latex/trajan/trytrajan.tex
#- source
%doc %{_texmfdistdir}/source/latex/trajan/trajan.dtx
%doc %{_texmfdistdir}/source/latex/trajan/trajan.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
