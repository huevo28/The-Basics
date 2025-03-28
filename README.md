# Description
This is a repository for my smaller projects. I've lost so many tools over the years that have been helpful. This repository serves to preserve my newer tools.

## meta-strip.py
This tool removes metadata from your image files. The syntax for this tool is through the CLI. You will need to type the images' names into the CLI. You will be prompted afterwards for a directory location. The images' output will have a generic name, "no-metadata" followed by a number and current image's file extension.
### Example Usage of CLI
    python3 meta-strip.py Example-Image.jpg Example-Image-2.jpg [...]
  
The easiest way to select several images instead of typing them is to place them into a directory and use the "*" to select everything.

    python3 meta-strip.py /home/user/Documents/Strip-These-Pictures/*

Or like this.
    
    python3 meta-strip.py ~/Pictures/These-Pictures/*.png ~/Documents/And-These-Pictures/*.jpg


