from flask import current_app as app
from flask_assets import Bundle

def compile_static_assets(assets: Bundle) -> Bundle:
    assets.auto_build = True
    assets.debug = False
    common_style_bundle = Bundle(
        "src/less/*.less",
        filters="less,cssmin",
        output="dist/css/style.css",
        extra={"rel": "stylesheet/less"},
    )
    home_style_bundle = Bundle(
        "home_blueprint/less/home.less",
        filters="less,cssmin",
        output="dist/css/home.css",
        extra={"rel": "stylesheet/less"},
    )
    assets.register("common_style_bundle", common_style_bundle)
    assets.register("home_style_bundle", home_style_bundle)
    if app.config['ENVIRONMENT'] == 'development':
        common_style_bundle.build()
        home_style_bundle.build()
    return assets