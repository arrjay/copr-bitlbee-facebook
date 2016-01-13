%global _version 0

%global hash 635c9cef534f9b469e1adfca0b5f091789eaef1c
%global shorthash %(bash -c 'c=%{hash}; echo ${c:0:7}')

Name: bitlbee-facebook
Version: %{_version}.b_%{shorthash}
Release: 1
Summary: The Facebook protocol plugin for bitlbee. This plugin uses the Facebook Mobile API.

BuildRequires: bitlbee-devel autoconf automake libtool json-glib-devel zlib-devel

License: GPLv2
URL: https://wiki.bitlbee.org/HowtoFacebookMQTT
Source0: https://github.com/jgeboski/%{name}/archive/${hash}.tar.gz#/%{name}-%{shorthash}.tar.gz

%description
As an alternative to the now (mostly-)defunct XMPP service provided by
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
* Wed Jan 13 2016 RJ Bergeron <rbergero@gmail.com>
- fix hardcoded library dir in spec

* Thu Sep 24 2015 RJ Bergeron <rbergero@gmail.com>
- initial packaging
