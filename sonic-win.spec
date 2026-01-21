%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
#define git 20240222
%define gitbranch Plasma/6.5
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

# (tpg) optimize it a bit
%global optflags %{optflags} -O3

Summary: An X11-only, lighter-weight fork of KWin
Name: sonic-win
Version: 6.5.5
Release: %{?git:0.%{git}.}1
URL: https://github.com/Sonic-DE/sonic-win
License: GPL
Group: System/Libraries
%if 0%{?git:1}
Source0:	%url/archive/%{gitbranch}/kwin-x11-%{gitbranchd}.tar.bz2#/kwin-%{git}.tar.bz2
%else
Source0: %url/archive/refs/tags/%{version}.tar.gz#/%name-%version.tar.gz
%endif
# Patch0: kwin-6.3.3-wayland-egl-is-wayland.patch
# (tpg) is it still needed ?
#Patch1: kwin-5.3.0-enable-minimizeall.patch

BuildRequires: appstream
BuildRequires: pkgconfig(egl)
BuildRequires: %{_lib}EGL_mesa-devel
BuildRequires: pkgconfig(epoxy)
BuildRequires: cmake(QAccessibilityClient6)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Concurrent)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Multimedia)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6QmlCore)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6QuickWidgets)
BuildRequires: cmake(Qt6Sensors)
BuildRequires: cmake(Qt6UiTools)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6UiPlugin)
BuildRequires: cmake(Qt6UiTools)
BuildRequires: cmake(Qt6Core5Compat)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6Service)
BuildRequires: cmake(KF6Svg)
BuildRequires: cmake(KNightTime)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(libinput)
BuildRequires: pkgconfig(libxcvt)
BuildRequires: pkgconfig(gbm)
BuildRequires: pkgconfig(udev)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(libcanberra)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-cursor)
BuildRequires: pkgconfig(wayland-egl)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-composite)
BuildRequires: pkgconfig(xcb-cursor)
BuildRequires: pkgconfig(xcb-damage)
BuildRequires: pkgconfig(xcb-glx)
BuildRequires: pkgconfig(xcb-icccm)
BuildRequires: pkgconfig(xcb-image)
BuildRequires: pkgconfig(xcb-keysyms)
BuildRequires: pkgconfig(xcb-randr)
BuildRequires: pkgconfig(xcb-render)
BuildRequires: pkgconfig(xcb-shape)
BuildRequires: pkgconfig(xcb-shm)
BuildRequires: pkgconfig(xcb-sync)
BuildRequires: pkgconfig(xcb-xfixes)
BuildRequires: pkgconfig(xcb-xtest)
BuildRequires: pkgconfig(xcb-event)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(xkbcommon-x11)
BuildRequires: pkgconfig(xi)
BuildRequires: pkgconfig(sm)
BuildRequires: pkgconfig(libcap)
BuildRequires: pkgconfig(libei-1.0)
BuildRequires: pkgconfig(libeis-1.0)
BuildRequires: cmake(ECM)
BuildRequires: cmake(PlasmaActivities)
BuildRequires: cmake(KF6Declarative)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6NewStuff)
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(Plasma) >= 5.90.0
BuildRequires: cmake(PlasmaQuick) >= 5.90.0
BuildRequires: cmake(Wayland) >= 5.90.0
BuildRequires: cmake(KDecoration3)
BuildRequires: cmake(KF6IdleTime)
BuildRequires: cmake(KF6GlobalAccel)
BuildRequires: cmake(KScreenLocker) > 5.27.50
BuildRequires: cmake(Breeze)
BuildRequires: cmake(KF6Kirigami2)
BuildRequires: cmake(KF6Runner)
BuildRequires: cmake(KF6GlobalAccel)
BuildRequires: cmake(KF6Auth)
BuildRequires: cmake(KGlobalAccelD)
BuildRequires: cmake(PlasmaWaylandProtocols)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(lcms2)
BuildRequires: pkgconfig(libpipewire-0.3)
BuildRequires: pkgconfig(libdisplay-info)
BuildRequires: cmake(KPipeWire) > 5.27.50
BuildRequires: cmake(KWayland)
BuildRequires: pkgconfig(vulkan)
BuildRequires: cmake(VulkanHeaders)
# FIXME Package QAccessibilityClient6 and BR it
BuildRequires: x11-server-xwayland
BuildRequires: hwdata
#BuildRequires: libhybris
Suggests:	kwin-aurorae
Requires: libplasma plasma-framework-common
#(tpg) this is needed for kcm_kwin_effects
Requires: glib-networking
# Obsolete packages that used to be split out solely for old policy reasons
%define effectmajor 1
%define effectname %mklibname kwin4_effect_builtins 1
Obsoletes: %{effectname} < %{EVRD}
BuildSystem: cmake
BuildOption: -DBUILD_QCH:BOOL=ON
BuildOption: -DBUILD_WITH_QT6:BOOL=ON
BuildOption: -DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
# Renamed 2025-05-01 after 6.0
# %rename plasma6-kwin
# %rename plasma6-kwin-x11
Provides: kwin-x11 = %{version}-%{release}
Conflicts: kwin-x11
Obsoletes: kwin-x11 < %{version}-%{release}

%description
sonic-win is an X11 window manager and a compositing manager. 
Its primary usage is in conjunction with a Desktop Shell 
(e.g. sonic-desktop). sonic-win is designed to stay out of the way; 
users should not notice that they use a window manager at all. 
Nevertheless sonic-win provides a steep learning curve for 
advanced features, which are available, if they do not conflict with 
the primary mission. sonic-win does not have a dedicated targeted 
user group, but follows the targeted user group of the Desktop Shell 
using sonic-win as it's window manager.

%package devel
Summary: Development files for the KDE Frameworks Win library
Group: Development/KDE and Qt
# Renamed 2025-05-01 after 6.0
# %rename plasma6-kwin-devel

%description devel
Development files for the KDE Frameworks Win library.

%files -f %{name}.lang
%{_bindir}/kwin_x11
%{_datadir}/kwin-x11
%{_userunitdir}/plasma-kwin_x11.service
%{_libdir}/kconf_update_bin/*
%{_libdir}/libexec/kwin-applywindowdecoration-x11
%{_libdir}/libexec/kwin_killer_helper_x11
%{_libdir}/libkcmkwincommon-x11.so*
%{_libdir}/libkwin-x11.so*
%{_qtdir}/plugins/kf6/packagestructure/kwin_*_x11.so
%{_qtdir}/plugins/kwin-x11
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_*_x11.so
%{_qtdir}/plugins/plasma/kcms/systemsettings_qwidgets/kcm_*_x11.so
%{_qtdir}/plugins/plasma/kcms/systemsettings_qwidgets/kwincompositing.so
%{_qtdir}/qml/org/kde/kwin_x11
%{_datadir}/applications/kcm_*_x11.desktop
%{_datadir}/applications/kwincompositing.desktop
%{_datadir}/applications/org.kde.kwin_x11.killer.desktop
%{_datadir}/dbus-1/interfaces/kwin_x11_org.kde.KWin.*.xml
%{_datadir}/dbus-1/interfaces/kwin_x11_org.kde.kwin.*.xml
%{_datadir}/dbus-1/interfaces/kwin_x11_org.kde.KWin.xml
%{_datadir}/icons/hicolor/*/apps/kwin-x11.*
%{_datadir}/kconf_update/kwin-x11.upd
%{_datadir}/knotifications6/kwin-x11.notifyrc
%{_datadir}/knsrcfiles/kwineffect-x11.knsrc
%{_datadir}/knsrcfiles/kwinscripts-x11.knsrc
%{_datadir}/knsrcfiles/kwinswitcher-x11.knsrc
%{_datadir}/knsrcfiles/window-decorations-x11.knsrc
%{_datadir}/krunner/dbusplugins/kwin-runner-windows-x11.desktop
%{_datadir}/qlogging-categories6/org_kde_kwin_x11.categories

%files devel
%{_includedir}/kwin-x11
%{_libdir}/cmake/KWinX11
%{_libdir}/cmake/KWinX11DBusInterface
