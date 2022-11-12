Name:		texlive-cursolatex
Version:	24139
Release:	1
Summary:	A LaTeX tutorial
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/portuguese/cursolatex
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cursolatex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cursolatex.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
The tutorial is presented as a set of slides (in Portuguese).

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/cursolatex/MiKTeX-Basic.png
%doc %{_texmfdistdir}/doc/latex/cursolatex/MiKTeX-Complete.png
%doc %{_texmfdistdir}/doc/latex/cursolatex/Musica.pdf
%doc %{_texmfdistdir}/doc/latex/cursolatex/README
%doc %{_texmfdistdir}/doc/latex/cursolatex/TeXShopPNG.png
%doc %{_texmfdistdir}/doc/latex/cursolatex/TeXworksPDF.pdf
%doc %{_texmfdistdir}/doc/latex/cursolatex/WinEdt.pdf
%doc %{_texmfdistdir}/doc/latex/cursolatex/cursolatex.nav
%doc %{_texmfdistdir}/doc/latex/cursolatex/cursolatex.pdf
%doc %{_texmfdistdir}/doc/latex/cursolatex/cursolatex.snm
%doc %{_texmfdistdir}/doc/latex/cursolatex/cursolatex.tex
%doc %{_texmfdistdir}/doc/latex/cursolatex/cursolatex.vrb
%doc %{_texmfdistdir}/doc/latex/cursolatex/emacs.pdf
%doc %{_texmfdistdir}/doc/latex/cursolatex/integral.pdf
%doc %{_texmfdistdir}/doc/latex/cursolatex/tabuleiro.pdf
%doc %{_texmfdistdir}/doc/latex/cursolatex/texmaker.pdf
%doc %{_texmfdistdir}/doc/latex/cursolatex/texniccenter.pdf
%doc %{_texmfdistdir}/doc/latex/cursolatex/texstudio.pdf
%doc %{_texmfdistdir}/doc/latex/cursolatex/tipografia.pdf
%doc %{_texmfdistdir}/doc/latex/cursolatex/ubuntu.pdf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
