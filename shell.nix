{ pkgs ? import <nixpkgs> {}}:
let
  fhs = pkgs.buildFHSUserEnv {
    name = "python env";

    targetPkgs = _: [
      pkgs.micromamba
    ];

    profile = ''
      set -e
      echo 1
      echo 2
      eval "$(micromamba shell hook --shell=posix)"
      export MAMBA_ROOT_PREFIX=${builtins.getEnv "PWD"}/.mamba
      echo 3
      micromamba create -n structural-bio-env
      echo $MAMBA_ROOT_PREFIX
      micromamba activate structural-bio-env
	    micromamba install --yes -f env.yml -c conda-forge

      set +e
    '';
  };
in fhs.env


