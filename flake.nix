{
  description = "A very basic flake";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
    flake-utils = { url = "github:numtide/flake-utils"; };
  };

  outputs = { self, nixpkgs, flake-utils }:

    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };

        elixir = pkgs.beam.packages.erlang.elixir;
        elixir-ls = pkgs.beam.packages.erlang.elixir-ls;

        locales = pkgs.glibcLocales;
        inotify-tools = pkgs.inotify-tools;
        libnotify = pkgs.libnotify;

        deno = pkgs.deno;
        python = pkgs.python313Full;
        pip = pkgs.python313Packages.pip;
        pytest = pkgs.python313Packages.pytest;

        venvShellHook = pkgs.python313Packages.venvShellHook;

      in {
        devShell = pkgs.mkShell {
          venvDir = ".venv";
          buildInputs = [
            elixir
            locales
            elixir-ls
            inotify-tools
            libnotify
            deno
            python
            pip
            pytest
            venvShellHook
          ];
        };
      });

}
