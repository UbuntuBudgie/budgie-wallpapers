#Ubuntu Budgie Wallpapers
This repo holds the wallpapers for each Ubuntu Budgie release

##Default Wallpapers
Generally, each Ubuntu Budgie release brings a brand new set of wallpapers. However, there are a few "default" wallpapers that we ship on all releases:
```
Xplo_by_Hugo_Cliff.png
ubuntu_budgie_wallpaper1.jpg
```

##Quality Assurance
To minimize package size of the debian package and to provide best experience for our users, we follow these image optmization steps for each file:

- Convert image to JPG if in another format:
`mogrify -format jpg <imagefile>`

- Scale down image to match 4K (3840x2400) size: 
`mogrify -resize 3840x <image.jpg>`

- Remove all metadata except XMP and comments:
`jhead -autorot -de -di -du -c <image.jpg>`

- Losslessly optimize image:
`/opt/mozjpeg/bin/jpegtran -optimize -progressive -outfile 'Output.jpg' 'Input.jpg'`

After renaming the resulting image to `Image_Title_by_Artist` format, it is ready for inclusion.
