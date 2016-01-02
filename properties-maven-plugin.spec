%global namedreltag -alpha-2
%global namedversion %{version}%{?namedreltag}
Name:          properties-maven-plugin
Version:       1.0
Release:       0.9.alpha2%{?dist}
Summary:       Properties Maven Plugin
License:       ASL 2.0
URL:           http://mojo.codehaus.org/properties-maven-plugin/
# svn export http://svn.codehaus.org/mojo/tags/properties-maven-plugin-1.0-alpha-2/
# tar czf properties-maven-plugin-1.0-alpha-2-src-svn.tar.gz properties-maven-plugin-1.0-alpha-2
Source0:       %{name}-%{namedversion}-src-svn.tar.gz
Source1:       http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires: mvn(org.codehaus.mojo:mojo-parent:pom:)
BuildRequires: mvn(org.codehaus.plexus:plexus-utils)
BuildRequires: mvn(org.apache.maven:maven-core)
BuildRequires: mvn(org.apache.maven:maven-model)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)

# test deps (no test to run)
BuildRequires: mvn(junit:junit)

BuildRequires: maven-local
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-plugin-cobertura
BuildRequires: maven-plugin-plugin

BuildArch:     noarch

%description
The Properties Maven Plugin is here to make life a little easier when dealing
with properties. It provides goals to read and write properties from files.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

# use maven 3.x apis
sed -i "s|maven-project|maven-core|" pom.xml

cp -p %{SOURCE1} .
sed -i 's/\r//' LICENSE-2.0.txt

%mvn_file :%{name} %{name}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE-2.0.txt

%changelog
* Wed Feb 11 2015 gil cattaneo <puntogil@libero.it> 1.0-0.9.alpha2
- introduce license macro

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.8.alpha2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 1.0-0.7.alpha2
- Use Requires: java-headless rebuild (#1067528)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.6.alpha2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 03 2013 gil cattaneo <puntogil@libero.it> 1.0-0.5.alpha2
- switch to XMvn
- minor changes to adapt to current guideline

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.4.alpha2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.0-0.3.alpha2
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.2.alpha2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 04 2012 gil cattaneo <puntogil@libero.it> 1.0-0.1.alpha2
- initial rpm
