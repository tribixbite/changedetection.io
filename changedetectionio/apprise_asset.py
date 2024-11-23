import apprise

# Create our AppriseAsset and populate it with some of our new values:
# https://github.com/caronc/apprise/wiki/Development_API#the-apprise-asset-object
asset = apprise.AppriseAsset(
   image_url_logo='https://raw.githubusercontent.com/tribixbite/changedetection.io/master/changedetectionio/static/images/avatar-256x256.png'
)

asset.app_id = "scry.shinyspells.com"
asset.app_desc = "Scry - website monitoring and change detection spells"
asset.app_url = "https://scry.shinyspells.com"
