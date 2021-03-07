# Advanced Tello Programming in Python

## Computer Art

## Examples

### Style Transfer Example
`python tello_script_runner.py --display-video --tello-video-sim --handler style_transfer_user_script.py`


### Image Effects Example
`python tello_script_runner.py --display-video --tello-video-sim --handler image_effects_user_script.py`

## Tests

Change directory into the `tests` directory.

`python <test file name>`


## Tello Commands

`python tello_script_runner.py --display-video --handler style_transfer_user_script.py`


## Breaking Changes

### tello_script_runner 

* now will look to see if handler is returning a new image and if so, will use the returned image to display.  This means the handler function is expected to return an image OR return None

* 