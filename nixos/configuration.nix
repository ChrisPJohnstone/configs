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

  # User Agnostic Packages
  environment.systemPackages = with pkgs; [
    vim
    xclip
  ];

  # Enable Programs
  programs = {
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
      firefox
      git
      neovim
      pavucontrol
      tmux
    ];
  };
}
