{
  description = "A very basic flake";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
    flake-utils = {
      url = "github:numtide/flake-utils";
    };
  };

  outputs =
    {
      self,
      nixpkgs,
      flake-utils,
    }:

    flake-utils.lib.eachDefaultSystem (
      system:
      let
        pkgs = import nixpkgs { inherit system; };

        node = pkgs.nodejs_22;

        python = pkgs.python314Packages.python;
        pip = pkgs.python314Packages.pip;
        pytest = pkgs.python314Packages.pytest;
        venvShellHook = pkgs.python314Packages.venvShellHook;

      in
      {
        devShell = pkgs.mkShell {
          venvDir = ".venv";
          buildInputs = [
            python
            pip
            pytest
            venvShellHook
            # pnpm
          ];
          shellHook = ''
            export PLAYWRIGHT_NODEJS_PATH="${node}/bin/node";
            export PLAYWRIGHT_LAUNCH_OPTIONS_EXECUTABLE_PATH="${pkgs.playwright-driver.browsers}/chromium-1091/chrome-linux/chrome";
            export PLAYWRIGHT_BROWSERS_PATH="${pkgs.playwright-driver.browsers}";

          '';

        };
      }
    );

}
