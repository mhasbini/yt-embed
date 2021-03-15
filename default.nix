let
  nixpkgs = import (builtins.fetchGit {
    name = "nixpkgs";
    url = "https://github.com/NixOS/nixpkgs-channels";
    rev = "4762fba469e2baa82f983b262e2c06ac2fdaae67";
  }) {};
 
  py3 = nixpkgs.python37.override {
    packageOverrides = self: super: with self; {
    };
  };

  install_packages = [
    (py3.buildEnv.override {
      ignoreCollisions = true;
      extraLibs = with py3.pkgs; [
            flask
            pillow
            gunicorn
            ipdb
            requests
      ];
    })
  ];


in
  nixpkgs.stdenv.mkDerivation {
    name = "yt-embed";
    buildInputs = install_packages;
  }
