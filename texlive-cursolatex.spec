%global tl_name cursolatex
%global tl_revision 24139

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A LaTeX tutorial
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/portuguese/cursolatex
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cursolatex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cursolatex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The tutorial is presented as a set of slides (in Portuguese).

