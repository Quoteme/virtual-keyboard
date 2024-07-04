let pkgs = import (builtins.getFlake "nixpkgs") { };
in
[
  pkgs.gcc.cc
  pkgs.glibc
  pkgs.zlib
  pkgs.libGL
  pkgs.xorg.libX11
]
