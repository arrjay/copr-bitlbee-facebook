%global _version 0

%global hash e9b15f94f02a0445dbd493244af5d47ec7faf80f
%global shorthash %(bash -c 'c=%{hash}; echo ${c:0:7}')
%global bbver %(rpm -q --queryformat='%{version}-%{release}' bitlbee-devel)

Name: bitlbee-facebook
Version: %{_version}.b_%{shorthash}
Release: 1
Summary: The Facebook protocol plugin for bitlbee. This plugin uses the Facebook Mobile API.
Requires: bitlbee = %{bbver}

BuildRequires: bitlbee-devel autoconf automake libtool json-glib-devel zlib-devel

License: GPLv2
URL: https://wiki.bitlbee.org/HowtoFacebookMQTT
Source0: https://github.com/jgeboski/%{name}/archive/${hash}.tar.gz#/%{name}-%{shorthash}.tar.gz

%description
As an alternative to the now broken XMPP service provided by
facebook, jgeboski (who also wrote bitlbee-steam) made a new plugin based
on the facebook messenger mobile client (which uses a protocol called MQTT)

It also happens to work much better than the XMPP service ever did, and
supports groupchats. 

%prep
%setup -qn %{name}-%{hash}

%build
./autogen.sh
make

%install
make DESTDIR=$RPM_BUILD_ROOT install

%files
%defattr(-,root,root,-)
%{_libdir}/bitlbee/facebook.la
%{_libdir}/bitlbee/facebook.so

%changelog
* Sun Feb  7 2016 RJ Bergeron <rbergero@gmail.com>
- require matching bitlbee version to what built it

* Sun Feb  7 2016 RJ Bergeron <rbergero@gmail.com>
- update to e9b15f94f02a0445dbd493244af5d47ec7faf80f

* Wed Jan 13 2016 RJ Bergeron <rbergero@gmail.com>
- update to ad7193f7f5eaf1164ecf6cbab1989f75d9f35fb9

* Wed Jan 13 2016 RJ Bergeron <rbergero@gmail.com>
- fix hardcoded library dir in spec

* Thu Sep 24 2015 RJ Bergeron <rbergero@gmail.com>
- initial packaging
