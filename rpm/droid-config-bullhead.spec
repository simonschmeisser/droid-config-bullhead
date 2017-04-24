%define device bullhead
%define vendor lge
%define vendor_pretty LG
%define device_pretty Nexus 5x
%define dcd_path ./
%define pixel_ratio 2.0

# Community HW adaptations need this
%define community_adaptation 1

Provides: ofono-configs
Provides: sensord-configs

%include droid-configs-device/droid-configs.inc
