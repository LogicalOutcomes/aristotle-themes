# Aristotle Themes

An Aristotle Extension to install and configure themes like bootstrap


## Installation

Install aristotle themes with pip, or add it to your requirements.txt

```
-e git+git://github.com/LogicalOutcomes/aristotle-themes@master#egg=aristotle-themes
libsass
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
