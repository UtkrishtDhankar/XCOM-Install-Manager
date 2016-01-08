# XCOM-Install-Manager
XCOM Install Manager allows you to have multiple installs of XCOM without them interfering. For example, you can have a Long War 1.0 install, a Long War Beta 14 install and a vanilla install, and XCOM Install Manager will help you to simply switch between the three installations.

## Installation
XCOM Install Manager needs no installation. Your download should include a file called `xcom_install_manager.py`. Put this file inside your XCOM Enemy Unkown installation folder (the one which includes the folder `XEW`).

To use XCOM Install Manager, you'll need Python 2.7, which is available on all platforms XCOM Enemy Within is available for.

## Usage
First off, you need to make multiple copies of the `XEW` folder inside your XCOM Enemy Unknown install folder. To do this, go to the folder where the game is installed (this can be done through Steam). The number of copies is up to you, depending on the number of seperate 'installs' you want to keep. Rename each copy something like, `XEW - Long War` or `XEW - Vanilla`. You can leave a single folder named as `XEW` (this is your default installation).

Once you're done with that, you're all set. Run the script included (`xcom_install_manager.py`), and it'll sort through the folders, and scan them. It might ask you for a name for the default folder (the one named `XEW`).

Once the script is done scanning the folders, whenever you want to change the installation you want to play, just fire up the script again and it'll give you a list of your installs. Type in the number of the install you want to play, and press enter. The script will exit. When you launch the game through Steam, the version you selected will be the one you launch.
