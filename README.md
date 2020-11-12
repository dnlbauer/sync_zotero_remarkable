## Transfer files from a Zotero collection to a folder on a reMarkable.

This uses the Zotero and reMarkable API to keep your reMarkable updated with a folder from Zotero. In short, it fetches a collection from zotero, uses CalDAV to download all corresponding .pdf and .epub files and finally uploads them to the reMarkable cloud. Finally, the zotero collection is cleared to prevent uploading the same file multiple times (so dont use it on your main library but create a separate fodler!)

#### Installation & Usage ####

Install via pip:
``` python
> pip install git+https://github.com/danijoo/sync_zotero_remarkable
```

On first run, you will be asked to provide login information to zotero, your associated caldav api and remarkable:
```bash
> sync_zotero_rm

zot_api_key: *******
zot_user_id: *******
zot_collection: unread_files
webdav_url: *******
webdav_user: *******
webdav_password: *******
rm_folder: Read me!
```

**Caution**: All login credentials are stored in clear text in your home
folder (`~/.zotero_remarkable.yaml`). So you probably do not want to use this
on publicly accessible devices.
If you later want to adjust the configuration, e.g. changing the Zotero collection or the folder on your reMarkable, simply change `~/.zotero_remarkable.yaml` accordingly.

And then:
```bash
Fetching collection from Zotero... Done.
Fetching item list... Done.
Items to sync: 1

#### Processing files ####

Kunzmann et al_2020_Substitution matrix based color schemes for sequence alignment visualization.pdf download, unzip, upload, done.

Removing uploaded items from zotero collection...Done.
Sync complete.


# let's see if it worked.
> rmapi            
ReMarkable Cloud API Shell
[/]>cd Read\ me!/
[/Read me!]>ls

[f]	Kunzmann et al_2020_Substitution matrix based color schemes for sequence alignment visualization
```





#### TODO
- Handle some the corner cases
- Option to not clear the folder

#### LICENSE
![do whatever you want](https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/WTFPL_badge.svg/220px-WTFPL_badge.svg.png)

Do whatever you want.

Inspired by ![Michael Mior's Zotero reMarkable sync (PHP)](https://github.com/michaelmior/zotero-remarkable)
