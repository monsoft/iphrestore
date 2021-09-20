# iPhone backup pictures extractor

This small script will extract pictures and videos from iPhone backup. Depends on which software has been used to do backup it, your backup location is:

* Windows: \Users\\[USERNAME]\AppData\Roaming\Apple Computer\MobileSync\Backup\\[ID]
* Linux: [your_choice_directory]\\[ID]

To run restore process, start script with options:
```
$ ./iphrestore.py backup_location directory_to_restore
```

I haven't tested this script under Windows but I assume that it should works as expected.