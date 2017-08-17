# Aristotle Themes

An Aristotle Extension to install and configure themes like bootstrap


## Installation

Install aristotle themes with pip, or add it to your requirements.txt

```
-e git+git://github.com/LogicalOutcomes/aristotle-themes@master#egg=aristotle-themes
```

Extend your `settings.py` file to include SASS support to django static precompiler:

```
STATIC_PRECOMPILER_COMPILERS = (
    ('static_precompiler.compilers.LESS', {"executable": "lesscpy"}),
    ('static_precompiler.compilers.libsass.SCSS', {
        "sourcemap_enabled": True,
        "precision": 8,
    })
)
```

Add Aristotle Themes to your `INSTALLED_APPS`:

```
INSTALLED_APPS = (
    'aristotle_themes',
    ...
```

Install theme (this will download required npm modules into app static folder)

```
./manage.py install_aristotle_themes
```

and collect statics:

```
./manage.py collectstatic
```

## Customization

On your project `static` folder add your `scss` files inside a `scss` folder. For example:

```
static/
    scss/
        myproject.scss
        _variables.scss
        _header.scss
```

And `myproject.scss` should looks like this:

```
// include bootstrap custom variables here
@import "_variables.scss";

// bootstrap main file, this file is provided by the aristotle_themes app
@import "_bootstrap.scss";

// Extra customization can go here
@import "_header.scss";
```

Finally add your main scss file to the Django settings file:

```
ARISTOTLE_SETTINGS.update({
    ...
    'THEMES_MAIN_SCSS': 'scss/myproject.scss',
    ...
```

## Extending

You might need to run collect statics when you add/modify files:

```
./manage.py collectstatic --noinput
```

## Builtin Themes:

### Themes

 * bootstrap-material-design (default)
 * more themes are coming...

To select a custom theme from our list you need to set the varialbe `THEMES_NAME` on your settings file under ARISTOTLE_SETTINGS. For example:

```
ARISTOTLE_SETTINGS.update({
    ...
    'SITE_FAVICON': 'http://www.example.com/favicon.ico',
    'THEMES_MAIN_SCSS': 'scss/aristotle_theme.scss',
    'THEMES_NAME': 'bootstrap-material-design',
    'THEMES_LIST': '[]',
    ...
```

you can also optionally include your theme list by setting variabe `THEMES_LIST` in your settings.py

The favicon can be set from Aristotle `SITE_FAVICON`


## Next steps:

 * Ability to import custom bootstrap themes
 * Builtin bootstrap themes selectable using the settings file
