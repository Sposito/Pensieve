
Visual Studio Code is a partially [[FOSS|Open Source]] text Electron based text edtior highly extensible developed by [[Microsoft]]. As any of its products it has no regard to user's privacy and it is loaded with telemetry. An alternative is its  community fork: VSCodium.

It is available for [[MacOS]], [[Windows]] and [[Linux]].
## Tips and Tricks
### Override Default Market Place on Codium
```bash
sudo flatpak override --env=VSCODE_GALLERY_SERVICE_URL=https://marketplace.visualstudio.com/_apis/public/gallery com.vscodium.codium
sudo flatpak override --env=VSCODE_GALLERY_ITEM_URL=https://marketplace.visualstudio.com/items com.vscodium.codium  
```
											\* use --user for local override

