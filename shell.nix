with import <nixpkgs> { };
mkShell {
  NIX_LD_LIBRARY_PATH = lib.makeLibraryPath [
    glibc
    libGL
    stdenv.cc.cc
    xorg.libX11
    zlib
  ];
  NIX_LD = lib.fileContents "${stdenv.cc}/nix-support/dynamic-linker";
  shellHook = ''
    export LD_LIBRARY_PATH=$NIX_LD_LIBRARY_PATH
    # check if the venv is already created
    if [ ! -d .venv ]; then
      python3 -m venv .venv
      source .venv/bin/activate
      pip install --upgrade pip
      pip install -r requirements.txt
    fi
    source .venv/bin/activate
    trap "exit 0" EXIT
  '';
}
