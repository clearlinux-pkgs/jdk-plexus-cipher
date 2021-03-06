#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jdk-plexus-cipher
Version  : 1.7
Release  : 2
URL      : https://github.com/sonatype/plexus-cipher/archive/plexus-cipher-1.7.tar.gz
Source0  : https://github.com/sonatype/plexus-cipher/archive/plexus-cipher-1.7.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: jdk-plexus-cipher-data
BuildRequires : apache-maven
BuildRequires : apache-maven2
BuildRequires : javapackages-tools
BuildRequires : jdk-aether
BuildRequires : jdk-aopalliance
BuildRequires : jdk-atinject
BuildRequires : jdk-cdi-api
BuildRequires : jdk-commons-cli
BuildRequires : jdk-commons-codec
BuildRequires : jdk-commons-collections
BuildRequires : jdk-commons-compress
BuildRequires : jdk-commons-io
BuildRequires : jdk-commons-lang
BuildRequires : jdk-commons-lang3
BuildRequires : jdk-commons-logging
BuildRequires : jdk-doxia
BuildRequires : jdk-doxia-sitetools
BuildRequires : jdk-forge-parent
BuildRequires : jdk-glassfish-el-api
BuildRequires : jdk-glassfish-interceptor-api
BuildRequires : jdk-guava
BuildRequires : jdk-guice
BuildRequires : jdk-httpcomponents-client
BuildRequires : jdk-httpcomponents-core
BuildRequires : jdk-jsoup
BuildRequires : jdk-jsr-305
BuildRequires : jdk-jvnet-parent
BuildRequires : jdk-log4j
BuildRequires : jdk-maven-archiver
BuildRequires : jdk-maven-common-artifact-filters
BuildRequires : jdk-maven-compiler-plugin
BuildRequires : jdk-maven-filtering
BuildRequires : jdk-maven-invoker
BuildRequires : jdk-maven-jar-plugin
BuildRequires : jdk-maven-javadoc-plugin
BuildRequires : jdk-maven-plugin-tools
BuildRequires : jdk-maven-reporting-api
BuildRequires : jdk-maven-resources-plugin
BuildRequires : jdk-maven-shared-incremental
BuildRequires : jdk-maven-shared-utils
BuildRequires : jdk-objectweb-asm
BuildRequires : jdk-plexus-archiver
BuildRequires : jdk-plexus-build-api
BuildRequires : jdk-plexus-cipher
BuildRequires : jdk-plexus-classworlds
BuildRequires : jdk-plexus-compiler
BuildRequires : jdk-plexus-containers
BuildRequires : jdk-plexus-i18n
BuildRequires : jdk-plexus-interactivity
BuildRequires : jdk-plexus-interpolation
BuildRequires : jdk-plexus-io
BuildRequires : jdk-plexus-sec-dispatcher
BuildRequires : jdk-plexus-utils
BuildRequires : jdk-plexus-velocity
BuildRequires : jdk-sisu
BuildRequires : jdk-sisu-mojos
BuildRequires : jdk-slf4j
BuildRequires : jdk-snappy-java
BuildRequires : jdk-spice-parent
BuildRequires : jdk-surefire
BuildRequires : jdk-velocity
BuildRequires : jdk-wagon
BuildRequires : jdk-xbean
BuildRequires : jdk-xmlunit
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six
BuildRequires : xmvn

%description
No detailed description available

%package data
Summary: data components for the jdk-plexus-cipher package.
Group: Data

%description data
data components for the jdk-plexus-cipher package.


%prep
%setup -q -n plexus-cipher-plexus-cipher-1.7

python3 /usr/share/java-utils/pom_editor.py pom_xpath_replace  pom:project/pom:version "<version>1.7</version>"
python3 /usr/share/java-utils/pom_editor.py pom_remove_dep org.sonatype.sisu:sisu-inject-bean
python3 /usr/share/java-utils/pom_editor.py pom_add_dep        javax.inject:javax.inject:1:provided
python3 /usr/share/java-utils/pom_editor.py pom_add_dep        javax.enterprise:cdi-api:1.0:provided
python3 /usr/share/java-utils/mvn_file.py : plexus/plexus-cipher

%build
python3 /usr/share/java-utils/mvn_build.py -f

%install
xmvn-install  -R .xmvn-reactor -n plexus-cipher -d %{buildroot}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/plexus/plexus-cipher.jar
/usr/share/maven-metadata/plexus-cipher.xml
/usr/share/maven-poms/plexus/plexus-cipher.pom
