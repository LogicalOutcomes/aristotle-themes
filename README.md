# Aristotle Themes

An Aristotle Extension to install and configure themes like bootstrap


## Installation

Install aristotle themes with pip, or add it to your requirements.txt

```
-e git+git://github.com/LogicalOutcomes/aristotle-themes@master#egg=aristotle-themes
libsass
django-npm
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

Include `aristotle_themes.finders.NpmFinder` to `STATICFILES_FINDERS` in your setting file. Example:

```
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'aristotle_themes.finders.NpmFinder',
]
```


Add Aristotle Themes to your `INSTALLED_APPS`:

```
INSTALLED_APPS = (
    'aristotle_themes',
    ...
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
ARISTOTLE_THEMES_SCSS = 'scss/myproject.scss'
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

To select a custom theme from our list you need to set the varialbe `ARISTOTLE_THEMES_NAME` on your settings file. For example:

```
ARISTOTLE_THEMES_NAME = 'bootstrap-material-design'
```

## Next steps:

 * Ability to import custom bootstrap themes
 * Builtin bootstrap themes selectable using the settings file
