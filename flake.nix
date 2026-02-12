{
  description = "A very basic flake";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
    flake-utils = { url = "github:numtide/flake-utils"; };
  };

  outputs = { self, nixpkgs, flake-utils, }:

    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };

        elixir = pkgs.beam.packages.erlang.elixir;
        elixir-ls = pkgs.beam.packages.erlang.elixir-ls;

        locales = pkgs.glibcLocales;

        node = pkgs.nodejs_22;
        pnpm = pkgs.pnpm;
        playwright = pkgs.playwright-test;
        playwright-browser = pkgs.playwright-driver.browsers;

        # deno = pkgs.deno;
        python = pkgs.python313Full;
        pip = pkgs.python313Packages.pip;
        pytest = pkgs.python313Packages.pytest;

        venvShellHook = pkgs.python313Packages.venvShellHook;

        libx11 = pkgs.xorg.libX11;
        xrandr = pkgs.xorg.libXrandr;

      in {
        devShell = pkgs.mkShell {
          venvDir = ".venv";
          buildInputs = [
            playwright
            pkgs.playwright-driver.browsers

            libx11
            xrandr

            elixir
            locales
            elixir-ls
            python
            pip
            pytest
            venvShellHook
            pnpm
          ];
          shellHook = ''
            export PLAYWRIGHT_NODEJS_PATH="${node}/bin/node";
            export PLAYWRIGHT_LAUNCH_OPTIONS_EXECUTABLE_PATH="${pkgs.playwright-driver.browsers}/chromium-1091/chrome-linux/chrome";
            export PLAYWRIGHT_BROWSERS_PATH="${pkgs.playwright-driver.browsers}";

          '';

        };
      });

}
