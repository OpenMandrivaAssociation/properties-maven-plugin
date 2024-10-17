%{?_javapackages_macros:%_javapackages_macros}

%global namedreltag -alpha-2
%global namedversion %{version}%{?namedreltag}
Name:          properties-maven-plugin
Version:       1.0
Release:       0.9.alpha2.1
Summary:       Properties Maven Plugin
Group:		Development/Java
License:       ASL 2.0
URL:           https://mojo.codehaus.org/properties-maven-plugin/
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

# - not allowed in EVR
sed -i 's|<version>1.0-alpha-2</version>|<version>1.0_alpha_2</version>|' pom.xml

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
%doc LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE-2.0.txt

