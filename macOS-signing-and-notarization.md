<!-- TOC start (generated with https://github.com/derlin/bitdowntoc) -->
#### Table of contents

- [Signing and notarizing a single plugin file](#signing-and-notarizing-a-single-plugin-file)
- [Signing and notarizing SuperCollider](#signing-and-notarizing-supercollider)
- [Entitlement files](#entitlement-files)

<!-- TOC end -->

First, you’ll need a signing cert. With Apple binaries, this means using a Developer account to create a Developer ID, and creating a signing cert with Keychain.


## Signing and notarizing a single plugin file

To sign a single binary for a Plugin.scx file, you just need to sign the scx file itself, using the entitlements that come in the SuperCollider.app bundle. From Terminal, move into the SuperCollider directory (that contains SuperCollider.app), and use the command line below against your .scx binary. The last argument in the command is the path to your .scx file, and you’ll need to replace the signing identity with what you have stored in your keychain:

`codesign --deep --force --verify --verbose --timestamp --entitlements SuperCollider.app/Contents/entitlements.plist --sign “*** your signing ID ***” --options runtime ***path to your plugin***`

As an example, this would sign a plugin called MyUgen.scx on my Desktop

`codesign --deep --force --verify --verbose --timestamp --entitlements SuperCollider.app/Contents/entitlements.plist --sign "Developer ID Application: Joshua Parmenter" --options runtime ~/Desktop/MyUgen.scx`


## Signing and notarizing SuperCollider

The process for signing and notarizing SuperCollider is complicated by our usage of Qt binaries, interprocess communications and binary plugins. On a given SuperCollider binary .app bundle, the following commands are used to import entitlements, sign everything (ORDER MATTERS!), zip up the .app bundle, upload to Apple for notarization, stapling the notarization upon success, then finally rezipping the package and singing the .zip file at the end so the download won’t freak out your computer.

I’ll use my signing identity as the example below, but when I get to the notarization step I will remove my personal signing info (a user name and app specific password) for security. The notarization is asynchronous, and can take anywhere from a couple minutes (after upload) to a couple hours to complete.


```
cd path/to/SuperCollider

echo "Removing Finder cruft..."
xattr -cr SuperCollider.app

# add entitlements to SuperCollider folder, then mv to SuperCollider.app/Contents
# files are attached on this post, and show them as living on my Desktop

cp ~/Desktop/QtWebEngineProcess.entitlements SuperCollider.app/Contents/

cp ~/Desktop/entitlements.plist SuperCollider.app/Contents/

codesign --deep --force --verify --verbose --timestamp --entitlements SuperCollider.app/Contents/entitlements.plist  --sign "Developer ID Application: Joshua Parmenter" --options runtime SuperCollider.app

codesign --deep --force --verify --verbose --timestamp --sign "Developer ID Application: Joshua Parmenter" --options runtime SuperCollider.app/Contents/Frameworks/QtWebEngineCore.framework/Helpers/QtWebEngineProcess.app/Contents/MacOS/QtWebEngineProcess

codesign --deep --force --verify --verbose --timestamp --entitlements SuperCollider.app/Contents/entitlements.plist --sign "Developer ID Application: Joshua Parmenter" --options runtime SuperCollider.app/Contents/Resources/scsynth

codesign --deep --force --verify --verbose --timestamp --entitlements SuperCollider.app/Contents/entitlements.plist --sign "Developer ID Application: Joshua Parmenter" --options runtime SuperCollider.app/Contents/Resources/supernova

codesign --deep --force --verify --verbose --timestamp --entitlements SuperCollider.app/Contents/entitlements.plist --sign "Developer ID Application: Joshua Parmenter" --options runtime SuperCollider.app/Contents/Resources/plugins/*

## do the above in SC3Plugins … sign *.scx and */*.scx

codesign --deep --force --verify --verbose --timestamp --entitlements SuperCollider.app/Contents/entitlements.plist --sign "Developer ID Application: Joshua Parmenter" --options runtime SuperCollider.app/Contents/MacOS/SuperCollider

codesign --deep --force --verify --verbose --timestamp --sign "Developer ID Application: Joshua Parmenter" --entitlements SuperCollider.app/Contents/QtWebEngineProcess.entitlements --options runtime SuperCollider.app/Contents/Frameworks/QtWebEngineCore.framework/Helpers/QtWebEngineProcess.app


ditto -c -k --rsrc --keepParent SuperCollider.app SuperCollider.app.zip


xcrun altool --notarize-app -t osx -f SuperCollider.app.zip --primary-bundle-id net.sourceforge.supercollider -u YourAppleDevID -p YouAppleAppSpecificPassword

# Notarization-info comes from the above… it is a UUID passed back after the app
# is uploaded Apple will email you when notarization is completed - OR - take
# the UUID that comes back and check the status

xcrun altool --notarization-info TheUUID -u YourAppleDevID -p YouAppleAppSpecificPassword

# after it is accepted, staple your .app:

xcrun stapler staple SuperCollider.app

# remove the zip you created, and move one level up

rm SuperCollider.app.zip
cd ..

# Now, in Finder, compress the SuperCollider folder to
# SuperCollider.zip (or whatever you want to name it) then code sign the zip

codesign --deep --force --verify --verbose --timestamp --sign "Developer ID Application: Joshua Parmenter" SuperCollider.zip
```

## Entitlement files

Save this as QtWebEngineProcess.entitlements

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>com.apple.security.cs.disable-executable-page-protection</key>
    <true/>
</dict>
</plist>
```

Save this as entitlements.plist

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.security.cs.allow-unsigned-executable-memory</key>
	<true/>
	<key>com.apple.security.device.audio-input</key>
	<true/>
	<key>com.apple.security.cs.disable-library-validation</key>
	<true/>
	<key>com.apple.security.device.microphone</key>
	<true/>
</dict>
</plist>
```
