# IPython Saver

This is a tool that will save your IPython sessions for you.

Just launch this command, adding or not those optional arguments:
```bash
./start_ipython.sh -n <storing-directory> -s <script-to-import>
```
- storing-directory: directory where will be stored the session (common by default) 
- script-to-import: if you supply the path to a python script here, it will be played before the session starts

After your session ends, it will be stored in `gs://$GCP_PROJECT_IPYTHON/ipython/<storing-directory>`, and you can then freely reimport it another time.

You can fetch scripts from GCS by simply typing this command:
```bash
./fetch.sh
```

If you've renamed, added or deleted scripts from `ipython/` and want to update the bucket, use this command:
```bash
./push.sh
``` 