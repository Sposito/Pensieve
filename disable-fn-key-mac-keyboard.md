For mac layout like keyboards, on [[linux]] you can run the following command in order to make Fkeys being the default keys instead of media keys.
```
echo 2 | sudo tee /sys/module/hid_apple/parameters/fnmode
```
