#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v21
# autospec commit: 5424026
#
Name     : R-Amelia
Version  : 1.8.3
Release  : 52
URL      : https://ftp.osuosl.org/pub/cran/src/contrib/Amelia_1.8.3.tar.gz
Source0  : https://ftp.osuosl.org/pub/cran/src/contrib/Amelia_1.8.3.tar.gz
Summary  : A Program for Missing Data
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-Amelia-lib = %{version}-%{release}
Requires: R-Rcpp
Requires: R-RcppArmadillo
Requires: R-rlang
BuildRequires : R-Rcpp
BuildRequires : R-RcppArmadillo
BuildRequires : R-rlang
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
(such as a survey), from a time series (like variables collected for
  each year in a country), or from a time-series-cross-sectional data
  set (such as collected by years for each of several countries).
  Amelia II implements our bootstrapping-based algorithm that gives
  essentially the same answers as the standard IP or EMis approaches,
  is usually considerably faster than existing approaches and can
  handle many more variables.  Unlike Amelia I and other statistically
  rigorous imputation software, it virtually never crashes (but please
  let us know if you find to the contrary!).  The program also
  generalizes existing approaches by allowing for trends in time series
  across observations within a cross-sectional unit, as well as priors
  that allow experts to incorporate beliefs they have about the values
  of missing cells in their data.  Amelia II also includes useful
  diagnostics of the fit of multiple imputation models.  The program
  works from the R command line or via a graphical user interface that
  does not require users to know R.

%package lib
Summary: lib components for the R-Amelia package.
Group: Libraries

%description lib
lib components for the R-Amelia package.


%prep
%setup -q -n Amelia
pushd ..
cp -a Amelia buildavx2
popd
pushd ..
cp -a Amelia buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1731636491

%install
export SOURCE_DATE_EPOCH=1731636491
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/Amelia/CITATION
/usr/lib64/R/library/Amelia/DESCRIPTION
/usr/lib64/R/library/Amelia/INDEX
/usr/lib64/R/library/Amelia/Meta/Rd.rds
/usr/lib64/R/library/Amelia/Meta/data.rds
/usr/lib64/R/library/Amelia/Meta/features.rds
/usr/lib64/R/library/Amelia/Meta/hsearch.rds
/usr/lib64/R/library/Amelia/Meta/links.rds
/usr/lib64/R/library/Amelia/Meta/nsInfo.rds
/usr/lib64/R/library/Amelia/Meta/package.rds
/usr/lib64/R/library/Amelia/Meta/vignette.rds
/usr/lib64/R/library/Amelia/NAMESPACE
/usr/lib64/R/library/Amelia/NEWS
/usr/lib64/R/library/Amelia/R/Amelia
/usr/lib64/R/library/Amelia/R/Amelia.rdb
/usr/lib64/R/library/Amelia/R/Amelia.rdx
/usr/lib64/R/library/Amelia/data/Rdata.rdb
/usr/lib64/R/library/Amelia/data/Rdata.rds
/usr/lib64/R/library/Amelia/data/Rdata.rdx
/usr/lib64/R/library/Amelia/doc/ameliaview.R
/usr/lib64/R/library/Amelia/doc/ameliaview.Rmd
/usr/lib64/R/library/Amelia/doc/ameliaview.html
/usr/lib64/R/library/Amelia/doc/diagnostics.R
/usr/lib64/R/library/Amelia/doc/diagnostics.Rmd
/usr/lib64/R/library/Amelia/doc/diagnostics.html
/usr/lib64/R/library/Amelia/doc/index.html
/usr/lib64/R/library/Amelia/doc/intro-mi.R
/usr/lib64/R/library/Amelia/doc/intro-mi.Rmd
/usr/lib64/R/library/Amelia/doc/intro-mi.html
/usr/lib64/R/library/Amelia/doc/using-amelia.R
/usr/lib64/R/library/Amelia/doc/using-amelia.Rmd
/usr/lib64/R/library/Amelia/doc/using-amelia.html
/usr/lib64/R/library/Amelia/gui/action_go.gif
/usr/lib64/R/library/Amelia/gui/action_save.gif
/usr/lib64/R/library/Amelia/gui/action_stop.gif
/usr/lib64/R/library/Amelia/gui/amelia.ico
/usr/lib64/R/library/Amelia/gui/arrow_down.gif
/usr/lib64/R/library/Amelia/gui/arrow_left.gif
/usr/lib64/R/library/Amelia/gui/arrow_up.gif
/usr/lib64/R/library/Amelia/gui/flag_red.gif
/usr/lib64/R/library/Amelia/gui/gallery19.gif
/usr/lib64/R/library/Amelia/gui/gallery19.jpg
/usr/lib64/R/library/Amelia/gui/histogram.gif
/usr/lib64/R/library/Amelia/gui/icon_accept.gif
/usr/lib64/R/library/Amelia/gui/icon_clock.gif
/usr/lib64/R/library/Amelia/gui/icon_user.gif
/usr/lib64/R/library/Amelia/gui/icon_world.gif
/usr/lib64/R/library/Amelia/gui/page-R.gif
/usr/lib64/R/library/Amelia/gui/page.gif
/usr/lib64/R/library/Amelia/gui/page_dta.gif
/usr/lib64/R/library/Amelia/gui/page_edit.gif
/usr/lib64/R/library/Amelia/gui/page_sas.gif
/usr/lib64/R/library/Amelia/gui/page_spss.gif
/usr/lib64/R/library/Amelia/gui/page_text.gif
/usr/lib64/R/library/Amelia/gui/page_up.gif
/usr/lib64/R/library/Amelia/gui/table.gif
/usr/lib64/R/library/Amelia/help/Amelia.rdb
/usr/lib64/R/library/Amelia/help/Amelia.rdx
/usr/lib64/R/library/Amelia/help/AnIndex
/usr/lib64/R/library/Amelia/help/aliases.rds
/usr/lib64/R/library/Amelia/help/paths.rds
/usr/lib64/R/library/Amelia/html/00Index.html
/usr/lib64/R/library/Amelia/html/R.css
/usr/lib64/R/library/Amelia/test/transform.R
/usr/lib64/R/library/Amelia/tests/bounds.R
/usr/lib64/R/library/Amelia/tests/moPrep-test.R
/usr/lib64/R/library/Amelia/tests/overimp.R

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/Amelia/libs/Amelia.so
/V4/usr/lib64/R/library/Amelia/libs/Amelia.so
/usr/lib64/R/library/Amelia/libs/Amelia.so
