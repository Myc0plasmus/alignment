{ pkgs ? import <nixpkgs> {}}:
let
  fhs = pkgs.buildFHSUserEnv {
    name = "python env";

    targetPkgs = _: [
      pkgs.micromamba
    ];

    profile = ''
      eval "$(micromamba shell hook --shell=posix)"
      export MAMBA_ROOT_PREFIX=${builtins.getEnv "PWD"}/.mamba
	 	  
      micromamba create -q -n structural-bio-env
      micromamba activate structural-bio-env
	    micromamba install --yes -f env.yml -c conda-forge

      set +e
    '';
  };
in fhs.env


