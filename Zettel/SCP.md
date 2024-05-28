SCP, or secure copy, is a program that trasnfers archives in between networked machines throughout [[SSH]] tunneling.

### Usage:
- Pulling from remote:
```
scp username@remote:/file/to/send /where/to/put
```
- Pushing to remote:
```
scp /file/to/send username@remote:/where/to/put
```
- From remote to another remote:
```
scp username@remote_1:/file/to/send username@remote_2:/where/to/put
```
---
### Flags:
`-3`    Copies between two remote hosts are transferred through the local host.  Without this option the data is copied directly between the two remote hosts.  Note that this option disables the progress meter and selects batch mode for the second host, since scp cannot ask for passwords or passphrases for both hosts.

`-4`    Forces scp to use IPv4 addresses only.

`-6`    Forces scp to use IPv6 addresses only.

`-A`    Allows forwarding of ssh-agent(1) to the remote system.  The default is not to forward an authentication agent.

`-B`    Selects batch mode (prevents asking for passwords or passphrases).

`-C`    Compression enable.  Passes the -C flag to ssh(1) to enable compression.

`-c`    cipher: Selects the cipher to use for encrypting the data transfer.  This option is directly passed to ssh(1).

`-F`    ssh_config: Specifies an alternative per-user configuration file for ssh.  This option is directly passed to ssh(1).

`-i`    identity_file: Selects the file from which the identity (private key) for public key authentication is read.  This option is directly passed to ssh(1).

`-J`    destination: Connect to the target host by first making an scp connection to the jump host described by destination and then establishing a TCP forwarding to the ultimate destination from there.  Multiple jump hops may be specified separated by comma characters.  This is a shortcut to specify a ProxyJump configuration directive. This option is directly passed to ssh(1).

`-l`    limit: Limits the used bandwidth, specified in Kbit/s.

`-P`    port: Specifies the port to connect to on the remote host.  Note that this option is written with a capital ‘P’, because -p is already reserved for preserving the times and modes of the file.

`-p`    Preserves modification times, access times, and modes from the original file.

`-q`     Quiet mode: disables the progress meter as well as warning and diagnostic messages from ssh(1).

`-r`    Recursively copy entire directories.  Note that scp follows symbolic links encountered in the tree traversal.

`-S`    program: Name of program to use for the encrypted connection.  The program must understand ssh(1) options.

`-T`    Disable strict filename checking.  By default when copying files from a remote host to a local directory scp checks that the received filenames match those requested on the command-line to prevent the remote end from sending unexpected or unwanted files.  Because of differences in how various operating systems and shells interpret filename wildcards, these checks may cause wanted files to be rejected.  This option disables these checks at the expense of fully trusting that the server will not send unexpected filenames.

`source: man page for scp`

---