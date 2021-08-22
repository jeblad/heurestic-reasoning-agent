# Internationalization and localization

Generate new pot-file

```bash
xgettext -D . --output=pyhera.pot -L Python pyhera.py
```

or

```bash
xgettext --files-from=locales/POTFILES.in --language Python --output locales/pyhera.pot
```

Use poedit to open a file for editing, and then import the new pot-file.