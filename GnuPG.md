#### _
GnuPG or gpg (GNU Privacy Guard) is the [[GNU]] implementation of PGP it tacks the [[IETF]] RFC 4880 specification of OpenPGP.

It is a hybrid encryption software because it offers [[symmetric-key cryptography]] (faster) and public-key cryptography for secure key exchange.

## Cheat sheet

### Install

``` bash 
# Debian or Ubuntu
sudo apt install gnupg2

#nix
nix-shell -p gnupg
```

``` nix
environment.systemPackages = [
    pkgs.gnupg
];
```

### Create 