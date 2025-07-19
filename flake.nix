{
  description = "Toughts in zettel markdown format";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };
  
  devShell = pkgs.mkShell {
    buildInputs = with pkgs; [
      python3
      code-cursor
    ];
    
    shellHook = ''

    '';
  };
}
