{ config, pkgs, ... }:

{
  imports = [
    /etc/nixos/hardware-configuration.nix
  ];

  # Release Version
  system.stateVersion = "24.05";

  # Bootloader.
  boot.loader.systemd-boot.enable = true;
  boot.loader.efi.canTouchEfiVariables = true;

  # Networking
  networking = {
    hostName = "nixos";
    networkmanager.enable = true;
  };

  # Set your time zone.
  time.timeZone = "Europe/London";

  # Locale properties
  i18n = {
    defaultLocale = "en_GB.UTF-8";
    extraLocaleSettings = {
      LC_ADDRESS = "en_GB.UTF-8";
      LC_IDENTIFICATION = "en_GB.UTF-8";
      LC_MEASUREMENT = "en_GB.UTF-8";
      LC_MONETARY = "en_GB.UTF-8";
      LC_NAME = "en_GB.UTF-8";
      LC_NUMERIC = "en_GB.UTF-8";
      LC_PAPER = "en_GB.UTF-8";
      LC_TELEPHONE = "en_GB.UTF-8";
      LC_TIME = "en_GB.UTF-8";
    };
  };

  # Location Properties
  location = {
    provider = "manual";
    latitude = 55.8617;
    longitude = 4.2583;
  };

  # Enable non-free packages
  nixpkgs.config.allowUnfree = true;

  # Configure X11
  hardware.nvidia.package = config.boot.kernelPackages.nvidiaPackages.stable;
  services.xserver = {
    enable = true;
    videoDrivers = [ "nvidia" ];
    xkb = {
      layout = "us";
      variant = "";
    };
    displayManager = {
      startx.enable = true;
    };
    windowManager.i3 = {
      enable = true;
      extraPackages = with pkgs; [
        dmenu
        i3status
        i3lock
      ];
    };
  };

  # Sound
  hardware.pulseaudio = {
    enable = true;
    support32Bit = true;
  };

  # Blue Light Shield
  services.redshift = {
    enable = true;
    brightness = {
      day = "1";
      night = "0.8";
    };
    temperature = {
      day = 5500;
      night = 1500;
    };
  };

  # Enable cron
  services.cron.enable = true;

  # User Agnostic Packages
  environment.systemPackages = with pkgs; [
    firefox
    libreoffice
    vim
    xclip
  ];

  # Enable Programs
  programs = {
    steam.enable = true;
    zsh.enable = true;
  };

  # User Account
  users.users.christopher = {
    isNormalUser = true;
    shell = pkgs.zsh;
    description = "Christopher";
    extraGroups = [ "audio" "networkmanager" "wheel" ];
    packages = with pkgs; [
      alacritty
      fastfetch
      feh
      flameshot
      git
      imagemagick
      neovim
      pavucontrol
      pyright
      ripgrep
      tmux
    ];
  };
}
